#!/usr/bin/python3
def safe_print_integer(value):
    try:
        f_value = "{:d}".format(value)
        print(f_value)
        return True
    except (ValueError, TypeError):
        return False
