#!/usr/bin/python3
"""
0-hbtn_status.py

Fetches https://intranet.hbtn.io/status using urllib
and displays the body response in a formatted way.
"""

import urllib.request


def fetch_status(url):
    """Fetch and return response body bytes from the URL."""
    with urllib.request.urlopen(url) as response:
        return response.read()


def print_response(body):
    """Print formatted body response."""
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))


def main():
    url = "https://intranet.hbtn.io/status"
    body = fetch_status(url)
    print_response(body)


if __name__ == "__main__":
    main()
