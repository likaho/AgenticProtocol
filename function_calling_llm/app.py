from flask import Flask, request, jsonify
from openapiutils import  get_function_details, create_function_call, generate_open_api_services, remove_openapi_files, clean_url, generate_hash


app = Flask(__name__)

@app.route('/usetool', methods=['POST'])
def useTool():
  if not request.is_json:
     return jsonify({'error': 'Request body must be JSON'}), 400
  
  user_query = request.json['user_query']
  function_details = get_function_details(user_query)
  function_call = create_function_call(user_query, function_details["documents"])
  if function_call.startswith("no_op("):
      # forward to a LLM 
      return ("no_op")
  else :
      # check if the parameters are valid
      # call the function
      # print(function_details["documents"] )
      # print((function_details["metadatas"][0][0]["function_name"]) )
      openapi_url = function_details["metadatas"][0][0]["openapi_uri"]
      service_url = function_details["metadatas"][0][0]["end_point"]
      import_statement = function_details["metadatas"][0][0]["import_statement"]

      output_dir = generate_hash(clean_url(openapi_url))
      generate_open_api_services(openapi_url, service_url, output_dir)

      exec(import_statement)
      result = eval(function_call)

      from threading import Thread
      # Create a thread object with the worker function and data
      thread = Thread(target=remove_openapi_files, args=(output_dir,))
      thread.start()  
      return jsonify(result)


     
if __name__ == '__main__':
  app.run(debug=True)
