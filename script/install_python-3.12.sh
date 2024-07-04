#!/bin/bash

sudo apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev pkg-config

cd /tmp
wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tar.xz

if [ $? -ne 0 ]; then
	echo "Failed to download Python-3.12.0.tar.xz"
	exit 1
fi

wait
tar -xf Python-3.12.0.tar.xz

if [ $? -ne 0 ]; then
	echo "Failed to extract Python-3.12.0.tar.xz"
	exit 1
fi

cd Python-3.12.0
./configure --enable-optimizations
make -j $(nproc)

if [ $? -ne 0 ]; then
	echo "Failed to make Python-3.12.0"
	exit 1
fi

sudo make altinstall

if [ $? -ne 0 ]; then
	echo "Failed to install Python-3.12.0"
	exit 1
fi

sudo ln -sf /usr/local/bin/python3.12 /usr/local/bin/python

if [ $? -ne 0 ]; then
	echo "Failed to create symlink for Python-3.12.0"
	exit 1
fi

wait

sudo python3.12 -m pip install virtualenv

if [ $? -ne 0 ]; then
	echo "Failed to install virtualenv"
	exit 1
fi

echo "Python 3.12 and virtualenv installation completed."