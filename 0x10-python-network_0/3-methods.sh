#!/bin/bash
# This script takes a URL and displays all HTTP methods the server will accept
curl -sI -X OPTIONS "$1" | grep -i Allow | awk '{gsub(",", ""); for(i=2;i<=NF;++i)print $i}'
