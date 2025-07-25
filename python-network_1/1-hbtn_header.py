#!/usr/bin/python3
import urllib.request

def fetch_page_content():
    try:
        with urllib.request.urlopen('https://alu-higher_level_programming.holberton.co/status') as response:
            body = response.read()
            print("Body response:")
            print(f"    - type: {type(body)}")
            print(f"    - content: {body}")
            print(f"    - utf8 content: {body.decode('utf-8')}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_page_content()
