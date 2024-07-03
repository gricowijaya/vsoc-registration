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
        health = wazuh_manager.checkhealth(token)

        print(health)
        return health
    except Exception as e:
        print(e)
        return e
    


if __name__ == "__main__":
    main()
