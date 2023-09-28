#!/bin/bash
# script to take URL and display the size of the body
curl -sI "$1" | awk '/content-length/{print $2}'
