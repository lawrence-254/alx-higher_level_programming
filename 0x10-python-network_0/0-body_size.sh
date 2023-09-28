#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL
curl -s -o "$1" | wc -c
