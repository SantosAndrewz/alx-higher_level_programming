#!/bin/bash
# script takes in a URL, sends it a POST request and displays its body of response.
curl "$1" -sX POST -d "email=test@gmail.com&subject=will always be here for PLD"
