#!/bin/bash
# Sends a GET request with the header X-HolbertonSchool-User-Id: 98 (redirects followed)
curl -sL -H 'X-HolbertonSchool-User-Id: 98' "$1"
