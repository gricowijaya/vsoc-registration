# What is the purpose of this repository?

We want to integrate Wazuh with bot system for registering agent, but this should be done securely to avoid agent registration abuse.

1. Create user in our database
2. Create user in Wazuh. (Sync with our system)
3. Assign the IP address of the User Server.
4. Assign the IP address to Wazuh manager.
5. Sync the Wazuh manager user account with our system.
6. Possible scenario is to create the middleware for packaging system between our agent and Wazuh.

## Installing the Project (in UNIX/Linux)


### Requirements 
- [Python 3.12](https://www.python.org/downloads/release/python-3120/?ref=upstract.com) installed on your system. 
	- This project also provides the installation script for `wazuh-agent` binary, `python-3.12` binary at the `scripts/` directory.
- [make](https://www.gnu.org/software/make/) installed on your system.

### Development Installation Steps

1. Use virtual environment

```
make venv
```

2. Activate virtual environment

```
source venv/bin/activate
```

3. Install Requirements

```
make install
```

4. Run the main script

```
make main
```

## Reference

- [Wazuh API Reference](https://documentation.wazuh.com/current/user-manual/api/reference.html)
- [Wazuh Agent Deployment in Linux](https://documentation.wazuh.com/current/installation-guide/wazuh-agent/wazuh-agent-package-linux.html)
- [Wazuh Agent Deployment in Windows](https://documentation.wazuh.com/current/installation-guide/wazuh-agent/wazuh-agent-package-windows.html)
- [Wazuh Secure Agent Identity Verification with SSL](https://documentation.wazuh.com/current/user-manual/agent/agent-enrollment/security-options/agent-identity-verification.html)
- [Wazuh agent enrollment using password](https://documentation.wazuh.com/current/user-manual/agent/agent-enrollment/security-options/using-password-authentication.html)
- [Using Wazuh API in python](https://documentation.wazuh.com/current/user-manual/api/getting-started.html#python)