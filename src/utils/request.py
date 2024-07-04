import json 
import requests
import urllib3
from .exception import exception_handler

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

@exception_handler
def get_response(request_method: str, url: str, headers: object, verify=False, body=None):
	if body is None:
		body = {}

	# for logging body, must deleted soon
	request_result = getattr(requests, request_method.lower())(url, headers=headers, verify=verify, data=body)
	
	if request_result.status_code == 200:
		return json.loads(request_result.content.decode())
	else:
		raise Exception(f"Request failed with status code: {request_result.status_code}, message: {request_result.content.decode()}")
