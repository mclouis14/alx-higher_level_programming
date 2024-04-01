#!/bin/bash
# Sends a JSON POST request to a URL passed as first argument and displays body of the response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
