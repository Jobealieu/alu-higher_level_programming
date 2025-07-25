#!/bin/bash
# Script to catch the server response
curl -s -X PUT -H "X-Custom-Header: gotcha" -d "catch=me" 0.0.0.0:5000/catch_me
