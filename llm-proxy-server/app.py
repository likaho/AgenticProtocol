from flask import Flask, request, jsonify
from function_calling_utils import  get_function_details, create_function_call, generate_hash, verify_function_call, get_completion
import requests
import os
import sys
import json
from dotenv import load_dotenv
from flask_cors import CORS
import chromadb
from chromadb.config import DEFAULT_TENANT, DEFAULT_DATABASE, Settings
import certifi
import logging

load_dotenv()

app = Flask(__name__)
CORS(app)
chromadb_host = os.getenv("CHROMADB_HOST")
chromadb_port = int(os.getenv("CHROMADB_PORT"))
log_format = "%(asctime)s::%(levelname)s::%(lineno)d::%(message)s"
logging.basicConfig(level=logging.INFO, stream=sys.stdout, format=log_format)
logger = logging.getLogger("app")


def delete_agent_or_chatflow(type: str, id: str):
  chroma_client = chromadb.HttpClient(host=chromadb_host, port=chromadb_port, ssl=False, headers=None, tenant=DEFAULT_TENANT, database=DEFAULT_DATABASE,settings=Settings(allow_reset=True, anonymized_telemetry=False))
  # chroma_client = chromadb.PersistentClient(path="vectordb")
  collection = chroma_client.get_or_create_collection(name="marketplace")
  results = collection.get(ids=[id])
  if len(results["ids"]) > 0:
    collection.delete(ids=[id])
    return jsonify({'id': id,'Success': f'{type} has been deleted'}), 204
  else:
    return jsonify({'id': id,'Error': f'{type} not found'}), 404

def create_agent_or_chatflow(type: str):
  if not request.is_json:
     return jsonify({'error': 'Request body must be JSON'}), 400
  else:
    name = request.json['name'].strip().replace(" ", "_")
    description = request.json['description']  #e.g. Fetches weather data from the Open-Meteo API for the given latitude and longitude.
    query_type = request.json['query_type'] #e.g. str
    query_description = request.json['query_description'] #e.g. The name of the city.
    return_type = request.json['return_type'] #e.g. str
    return_description = request.json['return_description'] #e.g. The weather forecast.
    flow_id = request.json['id']
    chroma_client = chromadb.HttpClient(host=chromadb_host, port=chromadb_port, ssl=False, headers=None, tenant=DEFAULT_TENANT, database=DEFAULT_DATABASE,settings=Settings(allow_reset=True, anonymized_telemetry=False))
    # chroma_client = chromadb.PersistentClient(path="vectordb")
    function_name = f"def {name}(query):"
    function_doc = \
    f'''
    Function:
    {function_name}
        """
        {description}

        Args:
        query ({query_type}): {query_description}

        Returns:
        {return_type}: {return_description}
        """
    '''
    hash = str(generate_hash(function_doc))
    doc_metadata = {"function_name": function_name, "hash": hash, "type": type}

    collection = chroma_client.get_or_create_collection(name="marketplace")
    collection.upsert(
        ids=[flow_id],
        documents=[function_doc],
        metadatas=[doc_metadata]
    )

    return jsonify({'id': flow_id,'Success': f'{type} has been created'}), 200

@app.route('/api/v1/agent', methods=['POST'])
def create_agent():
  return create_agent_or_chatflow("agent")
   
@app.route('/api/v1/chatflow', methods=['POST'])
def create_chatflow():
  return create_agent_or_chatflow("chatflow")

@app.route('/api/v1/agent/<id>', methods=['DELETE'])
def delete_agent(id: str):
  return delete_agent_or_chatflow("agent", id)

@app.route('/api/v1/chatflow/<id>', methods=['DELETE'])
def delete_chatflow(id: str):
  return delete_agent_or_chatflow("chatflow", id)

def chat_completion(user_query: str, chat_id: str):
  # Forward a user query to a LLM  to Galadriel network
  json_body = {"question":user_query, "chatId": chat_id }
  llm_url = os.getenv("GALADRIEL_URL")
  response = requests.post(llm_url, json = json_body, verify=certifi.where())
  return response.json()
  # response = get_completion(json_body)
  # return response

@app.route('/api/v1/prediction/123', methods=['POST'])
def use_service():
  if not request.is_json:
     return jsonify({'error': 'Request body must be JSON'}), 400
  
  user_query = request.json['question']
  chat_id = request.json['chatId']
  function_details = get_function_details(user_query)
  function_call, function_definition = create_function_call(user_query, function_details["documents"])
  logger.info(f"function_definition: {function_definition}")
  #Check if function_call construction is valid based on the user query 
  valid_function_call = False if "no_op" in function_call else verify_function_call(function_definition, user_query)

  if "no_op" in function_call or "default" in function_call or valid_function_call == False:
      logger.info("no_op")
      logger.info(f"user_query: {user_query}")
      logger.info(f"chatId: {chat_id}")
      response = chat_completion(user_query, chat_id)
      logger.info(f"response: {response}")
      return response
  else :
      # check if the parameters are valid
      logger.info(f"function_call: {function_call}")
      flow_id = function_details["ids"][0][0]
      marketplace_url = os.getenv("MARKETPLACE_URL") + "/" + flow_id + "/"
      logger.info(f"marketplace_url: {marketplace_url}")
      payload = json.dumps({"question":user_query, "chatId": str(chat_id)})
      logger.info(f"payload: {payload}")
      response = requests.post(marketplace_url, data=payload, verify=certifi.where(), headers={'Content-Type': 'application/json'})
      return response.json()

@app.route('/api/v1/heartbeat', methods=['GET'])
def heartbeat():
    return jsonify(status='healthy'), 200


if __name__ == '__main__':
  # log_full_path = "./app.log"

  # if os.path.exists(log_full_path) == True:
  #     open(log_full_path, "w").close()

  logger.info("Start")

  app.run(host='0.0.0.0', port=5000)