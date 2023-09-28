#!/bin/bash
# Script that takes URL sends a POST request
curl -s -x POST -d "email=test@gmail.com&subject=I will alwaays be here for PLD" "$1"
