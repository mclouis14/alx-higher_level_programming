#!/bin/bash
# Script takes a URL, sends a POST request to the passed URL and displays body of the response.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
