#!/bin/bash
# Takes a URL as argument, sends GET request to the URL and displays body of the response.
curl -s "$1" -H "X-School-User-Id: 98"
