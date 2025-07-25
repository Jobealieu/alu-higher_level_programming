#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -L -w "%{http_code}" -o /tmp/body "$1" | grep -q "200" && cat /tmp/body
