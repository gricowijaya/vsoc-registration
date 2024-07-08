#!/bin/bash

if [ ! -f /etc/debian_version ]; then
    if ! lsb_release -a 2>/dev/null | grep -iq "Debian\|Ubuntu"; then
        echo "This script is intended for Debian-based systems only."
        exit 1
    fi
fi

curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | gpg --no-default-keyring --keyring gnupg-ring:/usr/share/keyrings/wazuh.gpg --import && chmod 644 /usr/share/keyrings/wazuh.gpg;
if [ $? -ne 0 ]; then
    echo "Failed to import Wazuh GPG key."
    exit 1
fi

echo "deb [signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | tee -a /etc/apt/sources.list.d/wazuh.list;
if [ $? -ne 0 ]; then
    echo "Failed to add Wazuh repository."
    exit 1
fi

wait 
sudo apt-get update;
if [ $? -ne 0 ]; then
    echo "Failed to update package list."
    exit 1
fi
sudo apt-get install wazuh-agent -y;
if [ $? -ne 0 ]; then
    echo "Failed to install Wazuh agent."
    exit 1
fi

echo "Wazuh agent installation completed."


sed -i "s/^deb/#deb/" /etc/apt/sources.list.d/wazuh.list
if [ $? -ne 0 ]; then
    echo "Failed to comment out Wazuh repository."
    exit 1
fi

sudo apt-get update
if [ $? -ne 0 ]; then
    echo "Failed to update package list. for disable  wazuh agent"
    exit 1
fi

echo "Package wazuh agent update disabled."