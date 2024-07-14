from flask import Flask, request, jsonify
from openapiutils import  get_function_details, create_function_call, generate_open_api_services, remove_openapi_files, clean_url, generate_hash
import requests
import os
from dotenv import load_dotenv
import chromadb

load_dotenv()

app = Flask(__name__)

def delete_agent_or_chatflow(type: str, doc_id: str):
  chroma_client = chromadb.PersistentClient(path="agenticprotocol/vectordb")
  collection = chroma_client.get_or_create_collection(name="marketplace")
  collection.delete(ids=[str(doc_id)])
  return jsonify({'doc_id': doc_id,'Success': f'{type} has been deleted'}), 204
  # else:
  #   return jsonify({'doc_id': doc_id,'Error': f'{type} not found'}), 404

def create_agent_or_chatflow(type: str):
  if not request.is_json:
     return jsonify({'error': 'Request body must be JSON'}), 400
  else:
    name = request.json['name'].strip()
    description = request.json['description']  #e.g. Fetches weather data from the Open-Meteo API for the given latitude and longitude.
    query_type = request.json['query_type'] #e.g. str
    query_description = request.json['query_description'] #e.g. The name of the city.
    return_type = request.json['return_type'] #e.g. str
    return_description = request.json['return_description'] #e.g. The weather forecast.
    marketplace_id = request.json['marketplace_id']

    chroma_client = chromadb.PersistentClient(path="agenticprotocol/vectordb")
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
    doc_id = str(generate_hash(function_doc))
    doc_metadata = {"function_name": function_name, "marketplace_id": marketplace_id, "doc_id": doc_id, "type": type}

    collection = chroma_client.get_or_create_collection(name="marketplace")
    collection.add(
        documents=[function_doc],
        metadatas=[doc_metadata],
        ids=[doc_id]
    )

    return jsonify({'doc_id': doc_id,'Success': f'{type} has been created'}), 200

@app.route('/api/v1/agent', methods=['POST'])
def create_agent():
  return create_agent_or_chatflow("agent")
   
@app.route('/api/v1/chatflow', methods=['POST'])
def create_chatflow():
  return create_agent_or_chatflow("chatflow")

@app.route('/api/v1/agent/<doc_id>', methods=['DELETE'])
def delete_agent(doc_id: str):
  return delete_agent_or_chatflow("agent", doc_id)

@app.route('/api/v1/chatflow/<doc_id>', methods=['DELETE'])
def delete_chatflow(doc_id: str):
  return delete_agent_or_chatflow("chatflow", doc_id)

def chat_completion(user_query: str, chatId: str):
  # Forward a user query to a LLM  to Galadriel network
  json_body = {"question":user_query, "chatId": chatId }
  llm_url = os.getenv("GALADRIEL_URL")
  response = requests.post(llm_url, json = json_body)
  return jsonify(response)
  # if(response.status_code == 200):
  #   return response.text
  # else:
  #    return response.status_code

@app.route('/api/v1/useService', methods=['POST'])
def useService():
  if not request.is_json:
     return jsonify({'error': 'Request body must be JSON'}), 400
  
  user_query = request.json['question']
  chatId = request.json['chatId']
  function_details = get_function_details(user_query)
  function_call = create_function_call(user_query, function_details["documents"])
  if "no_op" in function_call:
      print(function_call)
      response = chat_completion(user_query, chatId)
      return response
  else :
      # check if the parameters are valid
      marketplace_id = function_details["metadatas"][0][0]["marketplace_id"]
      marketplace_url = f"{os.getenv("MARKETPLACE_URL")}/{marketplace_id}/"

      json_body = {"question":user_query, "chatId": chatId }
      print(json_body)
      response = requests.post(marketplace_url, json = json_body)

      # # call the function
      # openapi_url = function_details["metadatas"][0][0]["openapi_uri"]
      # service_url = function_details["metadatas"][0][0]["end_point"]
      # import_statement = function_details["metadatas"][0][0]["import_statement"]

      # output_dir = generate_hash(clean_url(openapi_url))
      # generate_open_api_services(openapi_url, service_url, output_dir)

      # exec(import_statement)
      # result = eval(function_call)

      # from threading import Thread
      # # Create a thread object with the worker function and data
      # thread = Thread(target=remove_openapi_files, args=(output_dir,))
      # thread.start()  
      # return jsonify(result)


     
if __name__ == '__main__':
  app.run(debug=True)
