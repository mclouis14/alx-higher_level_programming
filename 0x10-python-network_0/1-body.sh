#!/bin/bash
# Takes URL, sends GET request to the URL and displays body of response for 200 status code.
curl -sL "$1"
