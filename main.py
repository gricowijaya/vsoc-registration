import os
from src import auth, checkhealth, list_agent
from dotenv import load_dotenv

load_dotenv()


WAZUH_USERNAME=os.getenv("WAZUH_USERNAME")
WAZUH_PASSWORD=os.getenv("WAZUH_PASSWORD")


def main():
    try: 
        print("Processing authentication ...")
        token = auth(WAZUH_USERNAME, WAZUH_PASSWORD)
        if not token:
            print("Authentication failed")
            exit(1)
        print("Successfully Authenticated")

        print("Processing List of Agents ...")
        health = checkhealth(token)
        if not health:
            print("No health information found") 
            exit(1)

        print("Processing List of Wazuh Agents ...")
        agents = list_agent(token)
        if agents == None:
            print("No agents found")
            exit(1)

    except Exception as e:
        print(e)
        exit(1)
    

if __name__ == "__main__":
    main()
