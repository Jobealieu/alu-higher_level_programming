#!/bin/bash
# Script that takes a URL and displays the size of the response body in bytes
curl -sI "$1" | grep -i content-length | cut -d' ' -f2 | tr -d '\r'
