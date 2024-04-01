#!/bin/bash
# Sends request to a URL passed as argument and displays only status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
