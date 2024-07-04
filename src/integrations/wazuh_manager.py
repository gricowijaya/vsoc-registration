import os
import json
import urllib3
from base64 import b64encode
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from dotenv import load_dotenv
from ..utils import get_response, exception_handler

load_dotenv()


WAZUH_MANAGER_URL=os.getenv('WAZUH_MANAGER_URL')
WAZUH_MANAGER_PORT=os.getenv('WAZUH_MANAGER_PORT')


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@exception_handler
def auth(username, password):
    path = "/security/user/authenticate"
    url = (f"{WAZUH_MANAGER_URL}:{WAZUH_MANAGER_PORT}{path}")
    basic_auth = f"{username}:{password}".encode()
    headers = { 
                'Authorization': f'Basic {b64encode(basic_auth).decode()}', 
                'Content-Type': 'application/json'
                }
    token = get_response("POST", url, headers)["data"]["token"]
    return token


@exception_handler
def checkhealth(token):
    url = (f"{WAZUH_MANAGER_URL}:{WAZUH_MANAGER_PORT}")
    headers = { "Authorization": f"Bearer {token}"}
    response = get_response("GET", url, headers)
    return response


@exception_handler
def list_agent(token):
    url = f"{WAZUH_MANAGER_URL}:{WAZUH_MANAGER_PORT}/agents?pretty=true"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = get_response("GET", url, headers)
    return response


@exception_handler
def get_agent_key(agent_name, token):
    url = f"{WAZUH_MANAGER_URL}:{WAZUH_MANAGER_PORT}/agents?pretty=true"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "name": agent_name
    }

    response = get_response("POST", url, headers, body=json.dumps(payload))
    agent_id = response["data"]["id"]
    agent_key = response["data"]["key"]

    return agent_id, agent_key
