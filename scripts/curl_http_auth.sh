#!/bin/bash

user=$1
password=$2
url=$3
port=$4

echo "Trying this $user, $password, https://$url:$port/secruity/user/authenticate?raw=true"

TOKEN=$(curl -u $user:$password -k -X POST "https://$url:$port/security/user/authenticate?raw=true")

echo $TOKEN

curl -k -X GET "https://$url:$port/" -H  "Authorization: Bearer $TOKEN"
