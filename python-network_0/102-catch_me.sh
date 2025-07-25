#!/bin/bash
# Follow redirects with custom headers
curl -s -L -H "X-School: 98" -X PUT 0.0.0.0:5000/catch_me
