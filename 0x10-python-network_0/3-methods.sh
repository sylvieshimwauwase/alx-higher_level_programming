#!/bin/bash
# script that takes URL and displays all HTTP method
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
