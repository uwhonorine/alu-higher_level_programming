#!/bin/bash
# Sends a POST request with the variables email and subject
curl -s -X POST --data-urlencode 'email=test@gmail.com' --data-urlencode 'subject=I will always be here for PLD' "$1"
