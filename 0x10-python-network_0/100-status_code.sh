#!/bin/bash
# Script that sends a request to URL Passed as an argument
curl -s -o /dev/null -w "%{http_code}" "$1"
