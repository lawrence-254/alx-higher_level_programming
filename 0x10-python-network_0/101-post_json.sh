#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument
curl -s -d -X POST -H "Content-Type: application/json" -d "$(cat "$2")"
