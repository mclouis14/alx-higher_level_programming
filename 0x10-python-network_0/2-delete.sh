#!/bin/bash
# Sends a DELETE request to the URL passed as first argument and displays the body of response.
curl -sX DELETE "$1"
