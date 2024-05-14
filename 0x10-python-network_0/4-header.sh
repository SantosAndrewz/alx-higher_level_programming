#!/bin/bash
# script takess in a URL, sends it a GET request, displays body's response
curl -sX "$1" GET -H "X-School-User_Id: 98"
