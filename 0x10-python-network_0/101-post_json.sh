#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument
curl -s -X POST -d -H "Content-Type: application/json" "$1" "$(cat "$2")"
