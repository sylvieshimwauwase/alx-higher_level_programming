#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            uppercase_str += chr(ord(i) - 32)
        else:
            uppercase_str += i
    print(uppercase_str)
   