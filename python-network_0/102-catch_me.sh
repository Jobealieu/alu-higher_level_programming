#!/bin/bash
# Try with a specific catch header
curl -s -X POST -H "X-School: Holberton" -d "name=catch_me" 0.0.0.0:5000/catch_me
