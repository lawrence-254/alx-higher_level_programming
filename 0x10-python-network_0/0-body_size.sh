#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL,
#and displays the size of the body of the response

#message=$(curl -s -o /dev/null -w "%{size_download}" "$1");
#echo $message
#curl -sI "$1" | grep 'Content-Length' | cut -d' ' -f2
url="$1"
response=$(curl -s "$url")
size=$(echo -n "$response" | wc -c)
echo $size
