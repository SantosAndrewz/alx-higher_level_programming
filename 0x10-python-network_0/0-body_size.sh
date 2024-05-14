#!/bin/bash
# Script taking in the URL, sending it a request and displaying its body-size
curl -s "$1" | wc -c
