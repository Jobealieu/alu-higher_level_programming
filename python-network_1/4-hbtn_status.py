#!/usr/bin/python3
"""Script that fetches https://alu-intranet.hbtn.io/status using requests"""


if __name__ == "__main__":
    import requests
    
    response = requests.get("https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
