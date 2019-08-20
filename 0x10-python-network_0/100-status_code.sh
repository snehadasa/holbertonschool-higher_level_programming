#!/bin/bash
#Bash script that sends a request to a URL  and displays only the status code
curl -s --head --write-out '%{http_code}' "$1" -o /dev/null
