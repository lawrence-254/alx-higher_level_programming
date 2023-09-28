#!/bin/bash
#sends DELETE request to URL passed as first argument
curl -X DELETE -s "$1"
