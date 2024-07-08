#!/bin/bash

WAZUH_AGENT_KEY=$1

if [ -z "$WAZUH_AGENT_KEY" ]; then
    echo "Please provide Wazuh Agent Key" 1>&2
    exit 1
fi

if [ ! -f /var/ossec/bin/manage_agents ]; then
    echo "Wazuh agent is not installed." 1>&2
    exit 1
fi

/var/ossec/bin/manage_agents -i $WAZUH_AGENT_KEY

if [ $? -ne 0 ]; then
    echo "Failed to add Wazuh agent." 1>&2
    exit 1
fi

exit 0 