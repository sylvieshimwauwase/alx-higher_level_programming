#!/bin/bash
# Script that makes a request and causes server to respond with message
curl -sL -X PUT -H -d "user_id=98" 0.0.0.0:500/catch_me
