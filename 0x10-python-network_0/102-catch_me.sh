#!/bin/bash
# script makes a request to 0.0.0.0:5000/catch_me, causes server respond with a message.
curl "0.0.0.0:5000/catch_me" -sL -X PUT -d "user_id=98" -H "origin: HolbertonSchool"
