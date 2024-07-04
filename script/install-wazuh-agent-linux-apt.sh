#!/bin/bash

if [ ! -f /etc/debian_version ]; then
    if ! lsb_release -a 2>/dev/null | grep -iq "Debian\|Ubuntu"; then
        echo "This script is intended for Debian-based systems only."
        exit 1
    fi
fi

curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | gpg --no-default-keyring --keyring gnupg-ring:/usr/share/keyrings/wazuh.gpg --import && chmod 644 /usr/share/keyrings/wazuh.gpg;
echo "deb [signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | tee -a /etc/apt/sources.list.d/wazuh.list;
wait 
sudo apt-get update;
sudo apt-get install wazuh-agent -y;

echo "Wazuh agent installation completed."


sed -i "s/^deb/#deb/" /etc/apt/sources.list.d/wazuh.list
sudo apt-get update

echo "Package wazuh agent update disabled."

# Dependencies for compiling Python
sudo apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev pkg-config

cd /tmp
wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tar.xz
wait
tar -xf Python-3.12.0.tar.xz
cd Python-3.12.0
./configure --enable-optimizations
make -j $(nproc)
sudo make altinstall

sudo ln -sf /usr/local/bin/python3.12 /usr/local/bin/python

wait

sudo python3.12 -m pip install virtualenv

echo "Python 3.12 and virtualenv installation completed."