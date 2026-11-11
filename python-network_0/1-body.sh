#!/bin/bash
# Displays the body of the response from a URL (redirects followed), only for a 200 status code
response=$(curl -sL -w '\n%{http_code}' "$1"); if [ "${response##*$'\n'}" = "200" ]; then printf '%s' "${response%$'\n'*}"; fi
