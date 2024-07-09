#!/usr/bin/env python3
import os
from src import *
from dotenv import load_dotenv


load_dotenv()


WAZUH_USERNAME=os.getenv("WAZUH_USERNAME")
WAZUH_PASSWORD=os.getenv("WAZUH_PASSWORD")
SOCKET_IP=os.getenv("SOCKET_IP")
SOCKET_PORT=os.getenv("SOCKET_PORT")


def main():
    try: 
        print("Processing authentication ...")
        token = auth(WAZUH_USERNAME, WAZUH_PASSWORD)
        if not token:
            print("Authentication failed")
            exit(1)
        print("Successfully Authenticated")

        print("Processing List of Agents ...")
        health = get_checkhealth(token)
        if not health:
            print("No health information found") 
            exit(1)

        print("Processing List of Wazuh Agents ...")
        agents = get_list_agent(token)
        if agents == None:
            print("No agents found")
            exit(1)

        print("Processing Summary of Agents OS ...")
        agents_os = get_summary_agents_os(token)
        if agents_os == None:
            print("No agents os found")
            exit(1)
        
        print("Processing Summary of Agents Status ...")
        agents_status = get_summary_agents_status(token)
        if agents_status == None:
            print("No agents status found")
            exit(1)

        # new_agent = get_agent_ip_hostname(SOCKET_IP, SOCKET_PORT)

        # print("Registering your server to Wazuh Manager ...")
        # agent_registration = set_register_agent(new_agent["hostname"], new_agent["ip"], token)
        # if agent_registration == None:
        #    print("No agents status found")
        #    exit(1)

        # print("Fetching your server agents Key ...")
        # agents_key = get_agent_key(agent_registration["data"]["id"], token)
        # if agents_key == None:
        #     print("No agents key found")
        #     exit(1)

        # config = set_config(agent_registration["data"]["ip"], SOCKET_IP, SOCKET_PORT)
        # if config == None:
        #     raise Exception("No config File returned")

        # register_agent = set_agent_key(agents_key["data"]["affected_items"][0]["key"])
        # if register_agent == None:
        #     raise Exception("No agent is registered")
        
        groups_list = get_groups_list(token)
        if groups_list == None:
            raise Exception("No agent is registered")

    except Exception as e:
        print(e)
        exit(1)
    

if __name__ == "__main__":
    main()
