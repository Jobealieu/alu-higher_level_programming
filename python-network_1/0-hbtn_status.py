#!/usr/bin/python3
"""
0-hbtn_status.py

Fetches https://alu-intranet.hbtn.io/status using urllib
and displays the body response in a formatted way.
"""

import urllib.request

def main():
    url = "https://alu-intranet.hbtn.io/status"
    # Using with statement to open the URL and get the response object
    with urllib.request.urlopen(url) as response:
        body = response.read()

    # Printing outputs as per requirement
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))

if __name__ == "__main__":
    main()
