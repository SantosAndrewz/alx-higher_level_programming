#!/bin/bash
# script makes a request to 0.0.0.0:5000/catch_me, causes server respond with a message.
curl -s 0.0.0.0:5000/catch_me -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchool"
