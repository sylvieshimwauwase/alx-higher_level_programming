#!/usr/bin/python3
def magic_calculation(a, b):
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            res += (a ** b) / i
        except:
            res = b + a
            break
    return res
