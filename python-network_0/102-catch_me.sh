#!/bin/bash
# This script makes a request to the server to catch a message
curl -s -X PUT -H "Origin: 0.0.0.0" 0.0.0.0:5000/catch_me_2
