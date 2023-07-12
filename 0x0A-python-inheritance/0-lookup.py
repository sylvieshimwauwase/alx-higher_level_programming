#!/usr/bin/python3
def lookup(obj):
    """function to return list of available attributes"""

    attr = dir(obj)
    return attr

my_list = [1, 2, 3]
result = lookup(my_list)
print(result)
