import os
from src import wazuh_manager
from dotenv import load_dotenv

load_dotenv()


WAZUH_USERNAME=os.getenv("WAZUH_USERNAME")
WAZUH_PASSWORD=os.getenv("WAZUH_PASSWORD")


def main():
    try: 
        print("processing the authentication ...")
        token = wazuh_manager.auth(WAZUH_USERNAME, WAZUH_PASSWORD)
        if token == None:
            return "Authentication failed"
        print(token)

        agents = wazuh_manager.list_agent(token)
        if agents == None:
            return "No agents found"
        print(agents)

        health = wazuh_manager.checkhealth(token)
        if health == None:
            return "No health information found"
        print(health)

        return health
    except Exception as e:
        print(e)
        return e
    

if __name__ == "__main__":
    main()
