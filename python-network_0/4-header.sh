#!/bin/bash
# Sends a GET request with the user id header (value 98), redirects followed
curl -sL -H 'X-HolbertonSchool-User-Id: 98' -H 'X-School-User-Id: 98' "$1"
