#!/usr/bin/python3
"""
0-hbtn_status.py

Fetches status from a URL using urllib and displays the body response.

You can switch URL in the main() function between:
- http://0.0.0.0:5050/status  (local)
- https://intranet.hbtn.io/status (remote)
"""

import urllib.request


def fetch_status(url):
    """Fetches URL content and returns the bytes body."""
    with urllib.request.urlopen(url) as response:
        return response.read()


def print_response(body):
    """Prints the formatted output."""
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))


def main():
    # Default URL - change here if needed
    url = "http://0.0.0.0:5050/status"
    body = fetch_status(url)
    print_response(body)


def example_correct_output_remote():
    """Example output when fetching https://intranet.hbtn.io/status"""

    # Simulated output for demo purposes:
    print("Body response:")
    print("\t- type: <class 'bytes'>")
    print("\t- content: b'{\"status\":\"OK\"}'")
    print("\t- utf8 content: {\"status\":\"OK\"}")


if __name__ == "__main__":
    main()
    # Uncomment below line to see the example correct output for remote URL:
    # example_correct_output_remote()
