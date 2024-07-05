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


def create_function_docs_and_import_statements(output_dir: str)->(list, list):
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
    directory = f"{output_dir}/services"
    file_names = os.listdir(directory)
    for file_name in file_names:
        if file_name != "__init__.py":   
            function_names = get_function_names_from_file(f"{directory}/{file_name}")
            for function_name in function_names:
                module_name = f"{output_dir}.services.{file_name[:file_name.rfind(".")]}"
                import_statement = (f"from {module_name} import {function_name}")
                import_statements.append(import_statement)
                # exec(import_statement)
                module = importlib.import_module(module_name)
                if module:
                    function = getattr(module, function_name)
                    function_doc = create_function_doc(function)
                    function_docs.append(function_doc)

    return function_docs, import_statements


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

def download_openapi_spec(openapi_url, service_url):
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
  output_json_file="openapi.json"
  if not openapi_url:
      raise ValueError("Please provide a valid OpenAPI URL")

  try:
      # Download the OpenAPI spec
      urlretrieve(openapi_url, "openapi.yml")

      # Read the content of the file
      with open("openapi.yml", "r") as file:
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