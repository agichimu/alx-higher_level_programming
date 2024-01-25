#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a file and displays the body of the response
if [ -f "$2" ]; then
    curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
else
    echo "Not a valid JSON"
fi
