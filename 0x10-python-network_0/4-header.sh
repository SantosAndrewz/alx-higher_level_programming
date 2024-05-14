#!/bin/bash
# script takess in a URL, sends it a GET request, displays body's response
curl -sX GET "$1" -H "X-School-User_Id: 98"
