#!/bin/bash
# Script that catches the server response
curl -s -X PUT -H "X-Custom-Header: catch" 0.0.0.0:5000/catch_me
