import json
import yaml
from urllib.request import urlretrieve
import ast
import inspect
import re
import hashlib
import re
import os
import importlib
import chromadb
from chromadb.config import DEFAULT_TENANT, DEFAULT_DATABASE, Settings
import shutil
import subprocess
from utils import query_raven
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from flask import jsonify

chromadb_host = os.getenv("CHROMADB_HOST")
chromadb_port = int(os.getenv("CHROMADB_PORT"))
openai_key = os.getenv("OPENAI_KEY")
os.environ["OPENAI_API_KEY"] = openai_key


def get_completion(request_json):
    # Initialize the OpenAI LLM with your API key
    """
    Responds to a user query with a helpful answer using OpenAI.

    Args:
        request_json: A JSON object with keys "question", "chatId", and "sessionId".

    Returns:
        A JSON object with keys "text", "question", "chatId", "chatMessageId", and "sessionId".
    """
    llm = ChatOpenAI(model="gpt-4o")
    # Define a prompt template
    prompt_template = PromptTemplate(
        input_variables=["user_input"],
        template="You are a helpful assistant. Answer the following question: {user_input}"
    )

    # Create an LLMChain with the LLM and the prompt template
    chain = LLMChain(llm=llm, prompt=prompt_template)
    response = chain.run(user_input=request_json.get("question"))
    return jsonify({ 'text': response, 'question': request_json.get("question"), 'chatId': request_json.get("chatId"), 'chatMessageId': 'a9a1701c-615a-462b-b1bc-86d765cb6ec7', 'sessionId': request_json.get("chatId") })


def verify_function_call(function_definition, user_query):
    """
    Verifies if the function call is correct for the user query.

    Args:
    function_call (str): The function call as a string
    user_query (str): The user's query

    Returns:
    bool: True if the function call is correct for the user query, False otherwise
    """

    # Initialize the OpenAI API
    llm = ChatOpenAI(model="gpt-4o")

    # Define the prompt template
    prompt_template = PromptTemplate(
        input_variables=["function_call", "user_query"],
        template="""
        Given the following function call and user query, return "Yes" if the function call is correct for the user query, and "No" if it is incorrect.
        
        Function Call: {function_call}
        User Query: {user_query}
        """
    )

    # Generate the prompt
    prompt = prompt_template.format(function_call=function_definition, user_query=user_query).replace("\n", "")

    # Get the response from the OpenAI API
    response = llm.invoke(prompt)

    # Check the response and return the boolean value
    return response.content.strip().lower() == "yes"

def generate_open_api_services(openapi_url: str, service_url: str, output_dir: str):
    download_openapi_spec(openapi_url, service_url, output_dir)
    # Construct the command using string formatting
    command = f"openapi-python-generator {output_dir}//openapi.json {output_dir}/"  # !openapi-python-generator openapi.json ./api_specification_main/
    subprocess.run(command.split(), check=True)

def remove_openapi_files(output_dir: str):
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

def get_function_details(user_query: str):
    chroma_client = chromadb.HttpClient(host=chromadb_host, port=chromadb_port, ssl=False, headers=None, tenant=DEFAULT_TENANT, database=DEFAULT_DATABASE,settings=Settings(allow_reset=True, anonymized_telemetry=False))
    # chroma_client = chromadb.PersistentClient(path="vectordb")
    collection = chroma_client.get_or_create_collection(name="marketplace")
    num_of_results = os.getenv("NUM_OF_RESULTS")
    results = collection.query(
                query_texts=[user_query], 
                n_results=int(num_of_results), # how many results to return
                include=["documents", "metadatas"])
    return results

def create_function_call(user_query: str, documents: list) -> (str, str):
    function_definition = ""
    prompt = f'''
    Function:
    no_op():
    """
    Default OOD
    """
    '''
    
    for items in documents:
      for item in items:
          function_definition += str(item) + "\n"

    prompt = prompt + function_definition + f'''User Query: {user_query}<human_end>'''
    print(prompt)
    call = query_raven(prompt)
    return (call, function_definition)

def create_function_names_docs_import_statements(output_dir: str)->(list,list, list):
    """
    Collects function documentation from files within a directory and its subdirectories.

    Args:
        output_dir (str): The base directory containing service files.

    Returns:
        list: A list of function documentation strings.
    """
    print("Creating function docs")
    function_docs = []
    import_statements = []
    directory = output_dir + "/services"
    file_names = os.listdir(directory)
    for file_name in file_names:
        if file_name != "__init__.py":   
            function_names = get_function_names_from_file(f"{directory}/{file_name}")
            for function_name in function_names:
                module_name = output_dir + ".services." + file_name[:file_name.rfind(".")]
                import_statement = "from "+module_name+" import " + function_name
                import_statements.append(import_statement)
                # exec(import_statement)
                module = importlib.import_module(module_name)
                if module:
                    function = getattr(module, function_name)
                    function_doc = create_function_doc(function)
                    function_docs.append(function_doc)

    return function_names, function_docs, import_statements


def generate_hash(data):
  """
  Generates a hash string suitable for use as a directory name.

  Args:
      data (str or bytes): The data to be hashed.

  Returns:
      str: The hashed string with characters safe for directory names.
  """
  # Hash the data using SHA-256
  hashed_data = hashlib.sha256(data.encode()).hexdigest()

  # Remove characters not allowed in directory names (Windows and Linux)
  allowed_chars = re.compile(r"[a-zA-Z0-9_-]")
  sanitized_hash = "".join(char for char in hashed_data if allowed_chars.match(char))

  # Truncate to a reasonable length to avoid overly long directory names
  max_length = 64  # Adjust this value as needed
  truncated_hash = sanitized_hash[:max_length]

  return truncated_hash


def clean_url(url):
    # Remove protocol (http, https, etc.)
    url = re.sub(r'^https?://', '', url)
    
    # Remove slashes and dots
    url = re.sub(r'[\\/\\.]', '', url)
    
    return url

def create_function_doc(function):
    signature = inspect.signature(function)
    docstring = \
    '''
    Requires the latitude and longitude.
    Set current_weather to True to get the weather.
    Set hourly or daily based on preference.
    '''

    function_doc = \
    f'''
    Function:
    {function.__name__}{signature}
    """{docstring}"""'''
    return function_doc

def get_function_names_from_file(filename):
    """
    This function parses a Python file using ast and extracts function names.

    Args:
        filename: The name of the Python file.

    Returns:
        A list of function names from the file.
    """
    with open(filename) as f:
        code = f.read()

    tree = ast.parse(code)
    function_names = []

    def find_functions(node):
        if isinstance(node, ast.FunctionDef):
            function_names.append(node.name)
        for child in ast.iter_child_nodes(node):
            find_functions(child)

    find_functions(tree)
    return function_names

def download_openapi_spec(openapi_url, service_url, output_dir):
  """
  Downloads an OpenAPI spec from the given URL, performs modifications, and saves as JSON.

  Args:
      openapi_url (str): The URL of the OpenAPI spec to download.
      output_json_file (str, optional): The filename to save the modified OpenAPI spec in JSON format.
          Defaults to "openapi.json".

  Raises:
      ValueError: If the OpenAPI URL is not provided.
      IOError: If there's an error downloading or saving the file.
  """
  if not os.path.exists(output_dir):
    os.mkdir(output_dir)
  output_json_file = output_dir + "\\openapi.json"
  if not openapi_url:
      raise ValueError("Please provide a valid OpenAPI URL")

  try:
      # Download the OpenAPI spec
      urlretrieve(openapi_url, output_dir + "\\openapi.yml")

      # Read the content of the file
      with open(output_dir + "\\openapi.yml", "r") as file:
          file_content = file.read()

      # Modify content (replace int and float types with number)
      file_content = file_content.replace("int\n", "number\n")
      file_content = file_content.replace("float\n", "number\n")

      # Parse the content as YAML
      data = yaml.safe_load(file_content)

      # Add servers entry (optional, modify if your OpenAPI spec requires a different structure)
      data["servers"] = [{"url": service_url}]

      # Convert to JSON and save
      with open(output_json_file, "w") as file:
          json.dump(data, file, indent=4)  # Add indentation for readability (optional)

      print(f"Downloaded and modified OpenAPI spec saved to: {output_json_file}")

  except (ValueError, IOError) as e:
      print(f"Error: {e}")