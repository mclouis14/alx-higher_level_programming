#!/bin/bash
# Script takes a URL as argument, sends GET request to the URL and displays body of the response.
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
