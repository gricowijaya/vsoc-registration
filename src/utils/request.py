import json 
import requests
import urllib3
import os
from dotenv import load_dotenv
from .exception import exception_handler

load_dotenv()


WAZUH_MANAGER_URL=os.getenv('WAZUH_MANAGER_URL')
WAZUH_MANAGER_PORT=os.getenv('WAZUH_MANAGER_PORT')


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

@exception_handler
def get_response(request_method: str, path: str, headers: object, verify=False, body=None):
	url = (f"{WAZUH_MANAGER_URL}:{WAZUH_MANAGER_PORT}{path}")
	if body is None:
		body = {}

	request_result = getattr(requests, request_method.lower())(url, headers=headers, verify=verify, data=body)
	
	if request_result.status_code == 200:
		return json.loads(request_result.content.decode())
	elif request_result.status_code != 200:
		return json.loads(request_result.content.decode())
	else:
		raise Exception(f"Request failed with status code: {request_result.status_code}, message: {request_result.content.decode()}")
