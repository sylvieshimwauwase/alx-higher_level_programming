#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_sorted = sorted(a_dictionary.keys())

    for key  in key_sorted:
        v = a_dictionary[key]
        print(f'{key} : {v}')
