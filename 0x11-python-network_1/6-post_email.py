#!/usr/bin/python3
"""
Script takes in a URL and email address, sends a POST request to the passed URL
with email as parameter and finally displays body of the response.
"""
import requests
from sys import argv

if __name__ == '__main__':
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
