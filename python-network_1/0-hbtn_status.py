#!/usr/bin/python3
"""Fetches the status of a given URL using urllib."""
import urllib.request
def fetch_status(url):
    """Fetches and prints the status of the given URL."""
    with urllib.request.urlopen(url) as response:
        body = response.read()
        
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
if __name__ == "__main__":
    # Fetching the status from the specified URL
    fetch_status("https://intranet.hbtn.io/status")
    # Uncomment the line below to fetch from the alternative URL
    # fetch_status("http://0.0.0.0:5050/status")
