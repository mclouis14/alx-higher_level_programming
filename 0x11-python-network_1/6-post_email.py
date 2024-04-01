#!/usr/bin/python3
"""
Script takes in a URL and email address, sends a POST request to the passed URL
with email as parameter and finally displays body of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
