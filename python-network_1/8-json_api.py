#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    # Get the letter from command line argument, or set to empty string
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    # Prepare the data to send
    data = {'q': q}

    # Send POST request
    try:
        response = requests.post('http://0.0.0.0:5000/search_user', data=data)

        # Try to parse JSON response
        try:
            json_response = response.json()

            # Check if JSON is empty or None
            if (json_response and 'id' in json_response and
                    'name' in json_response):
                print("[{}] {}".format(json_response['id'],
                                       json_response['name']))
            else:
                print("No result")

        except ValueError:
            # JSON is invalid
            print("Not a valid JSON")

    except requests.RequestException:
        print("Request failed")
