#!/usr/bin/python3
def lookup(obj):
    """function to return list of available attributes"""

    attr = dir(obj)
    return attr

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
