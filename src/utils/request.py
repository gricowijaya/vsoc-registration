import json 
import requests
import urllib3
from .exception import exception_handler

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

@exception_handler
def get_response(request_method, url, headers, verify=False, body=None):
	if body is None:
		body = {}

	# for logging body, must deleted soon
	print("13: get_response.py, body:", body)

	request_result = getattr(requests, request_method.lower())(url, headers=headers, verify=verify, data=body)
	
	print("18: get_response.py, request_result:", request_result)

	print("20: get_response.py, json.loads(request_result.content.decode()):", json.loads(request_result.content.decode()))

	if request_result.status_code == 200:
		return json.loads(request_result.content.decode())
	else:
		raise Exception(f"Request failed with status code: {request_result.status_code}")
