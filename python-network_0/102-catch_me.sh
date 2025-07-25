#!/bin/bash
# Comprehensive attempt to catch the endpoint
curl -s -X PUT -L -H "User-Agent: Secret-Agent" -H "X-Catch-Me: true" -d "secret=catch_me" 0.0.0.0:5000/catch_me
