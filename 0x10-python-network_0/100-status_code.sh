#!/bin/bash
# script takes in a URL, sends it a request and displays only the response's status code.
curl "$1" -s -o /dev/null -w "%{http_code}"
