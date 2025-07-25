#!/bin/bash
# This script makes a request to catch the server and get "You got me!" response
curl -s -X GET "0.0.0.0:5000/catch_me" -H "X-School: 98"
