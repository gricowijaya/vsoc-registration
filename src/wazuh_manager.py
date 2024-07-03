import requests
import os
import json
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from dotenv import load_dotenv

load_dotenv()


WAZUH_MANAGER_URL=os.getenv('WAZUH_MANAGER_URL')
WAZUH_MANAGER_PORT=os.getenv('WAZUH_MANAGER_PORT')


def auth(username, password):
    try:
        url = (f"{WAZUH_MANAGER_URL}:{WAZUH_MANAGER_PORT}/security/user/authenticate")
        response = requests.post(url, auth=(username, password), verify=False)
        response_json = response.json()
        token = response_json['data']['token']
        return token
    except HTTPError as http_err:
        print (f'HTTP error occurred: {http_err}')
        return f'HTTP error occurred: {http_err}'
    except ConnectionError as conn_err:
        print (f'Connection error occurred: {conn_err}')
        return f'Connection error occurred: {conn_err}'
    except Timeout as time_err:
        print (f'Timeout error occurred: {time_err}')
        return f'Timeout error occurred: {time_err}'
    except RequestException as req_err:
        print (f'Request error occurred: {req_err}')
        return f'Request error occurred: {req_err}'
    except Exception as e:
        print(e)
        return e


def checkhealth(token):
    try: 
        url = (f"{WAZUH_MANAGER_URL}:{WAZUH_MANAGER_PORT}")
        headers = { "Atuhorization": f"Bearer {token}"}
        response = requests.post(url, headers=headers, verify=False)
        response.raise_for_status()

        try:
            response_json = response.json()
            return response_json
        except json.JSONDecodeError:
            return "Invalid JSON Response from API"
    except requests.exceptions.RequestException as e:
        print(e)
        return e


def get_agent_key(agent_name, token):
    try: 
        url = f"{WAZUH_MANAGER_URL}:{WAZUH_MANAGER_PORT}/agents?pretty=true"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        payload = {
            "name": agent_name
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
        
        if response.status_code == 200:
            response_data = response.json()
            if response_data.get("error") == 0:
                agent_id = response_data["data"]["id"]
                agent_key = response_data["data"]["key"]
                return agent_id, agent_key
            else:
                raise Exception(f"API returned an error: {response_data.get('error')}")
        else:
            raise Exception(f"Request failed with status code: {response.status_code}")
    except HTTPError as http_err:
        print (f'HTTP error occurred: {http_err}')
        return f'HTTP error occurred: {http_err}'
    except ConnectionError as conn_err:
        print (f'Connection error occurred: {conn_err}')
        return f'Connection error occurred: {conn_err}'
    except Timeout as time_err:
        print (f'Timeout error occurred: {time_err}')
        return f'Timeout error occurred: {time_err}'
    except RequestException as req_err:
        print (f'Request error occurred: {req_err}')
        return f'Request error occurred: {req_err}'
    except Exception as e:
        print(e)
        return e