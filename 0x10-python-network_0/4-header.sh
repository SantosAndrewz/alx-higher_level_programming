#!/bin/bash
# script takess in a URL, sends it a GET request, displays body's response
curl "$1" -sX GET -H "X-School-User-Id: 98"
