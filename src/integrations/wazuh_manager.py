import os
import json
import urllib3
from base64 import b64encode
from dotenv import load_dotenv
from ..utils import get_response, exception_handler, beautify_json

load_dotenv()


WAZUH_MANAGER_URL=os.getenv('WAZUH_MANAGER_URL')
WAZUH_MANAGER_PORT=os.getenv('WAZUH_MANAGER_PORT')


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@exception_handler
@beautify_json
def auth(username: str, password: str):
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
@beautify_json
def get_checkhealth(token: str):
    url = (f"{WAZUH_MANAGER_URL}:{WAZUH_MANAGER_PORT}")
    headers = { "Authorization": f"Bearer {token}" }
    response = get_response("GET", url, headers)
    return response


@exception_handler
@beautify_json
def get_list_agent(token: str):
    url = f"{WAZUH_MANAGER_URL}:{WAZUH_MANAGER_PORT}/agents?pretty=true"
    headers = { "Authorization": f"Bearer {token}" }
    response = get_response("GET", url, headers)
    return response


@exception_handler
@beautify_json
def get_summary_agents_os(token: str):
    url = f"{WAZUH_MANAGER_URL}:{WAZUH_MANAGER_PORT}/agents/summary/os?pretty=true"
    headers = { "Authorization": f"Bearer {token}" }
    response = get_response("GET", url, headers)
    return response


@exception_handler
@beautify_json
def get_summary_agents_status(token: str):
    url = f"{WAZUH_MANAGER_URL}:{WAZUH_MANAGER_PORT}/agents/summary/status?pretty=true"
    headers = { "Authorization": f"Bearer {token}" }
    response = get_response("GET", url, headers)
    return response

@exception_handler
@beautify_json
def get_agent_key(agent_name: str, token: str):
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
