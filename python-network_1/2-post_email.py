#!/usr/bin/python3
"""Script that sends a POST request with an email parameter"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Prepare the data to be sent in the POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    
    # Create the request with POST data
    with urllib.request.urlopen(url, data=data) as response:
        # Read and decode the response body
        body = response.read().decode('utf-8')
        print(body)
