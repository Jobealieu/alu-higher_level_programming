#!/bin/bash
# This script sends a GET request to a URL with a custom header X-HolbertonSchool-User-Id
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
