#!/bin/bash
# script takes in a URL, sends it a JSON POST request and displays the body of the response.
curl "$1" -s -H "Content-Type: application/json" -d "$(cat "$2")"
