#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            uppercase_str += chr(ord(c) - (ord('a') - ord('A')))
        else:
            uppercase_str += c
    print(f"{uppercase_str}\n")
   