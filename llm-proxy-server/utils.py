import inspect
import os
from dotenv import load_dotenv

# Specify the LLM Endpoint
# Now, let's prompt Raven!
load_dotenv()
API_URL = os.getenv("FUNCTION_CALLING_URL")
headers = {
        "Content-Type": "application/json"
}

# pipeline = pipeline(
#     "text-generation",
#     model="Nexusflow/NexusRaven-V2-13B",
#     torch_dtype="auto",
#     device_map="auto",
# )

def raven_post(payload):
	"""
	Sends a payload to a TGI endpoint.
	"""
	import requests
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def query_raven(prompt):
	"""
	This function sends a request to the TGI endpoint to get Raven's function call.
	This will not generate Raven's justification and reasoning for the call, to save on latency.
	"""
     
	# prompt = prompt.format(query="What's the weather like in Seattle right now?")

	# result = pipeline(prompt, max_new_tokens=2048, return_full_text=False, do_sample=False, temperature=0.001)[0]["generated_text"]
	# return result	 

	import requests
	output = raven_post({
		"inputs": prompt,
		"parameters" : {"temperature" : 0.001, "stop" : ["<bot_end>"], "do_sample" : False, "max_new_tokens" : 2048, "return_full_text" : False}})
	call = output[0]["generated_text"].replace("Call:", "").strip()
	return call

def clean_docstring(docstring):
    if docstring is not None:
        # Remove leading and trailing whitespace
        docstring = docstring.strip()
    return docstring

def construct_prompt(raven_msg, functions):
    full_prompt = ""
    for function in functions:
        signature = inspect.signature(function)
        docstring = function.__doc__
        prompt = f'''Function:\n{function.__name__}{signature}\n"""{clean_docstring(docstring)}"""'''
        full_prompt += prompt + "\n\n"
    full_prompt += f'''User Query: {raven_msg}<human_end>'''
    return full_prompt