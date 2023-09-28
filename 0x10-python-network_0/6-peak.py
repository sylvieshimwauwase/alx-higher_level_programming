#!/usr/bin/python3
# function to find a peak in alist of unsorted integers

def find_peak(list_of_int):
    """
    Find a peak in a lis of unsorted integers
    Args:
    list_of_int: A list of unsorted integers
    """
    if not list_of_int:
        return None

    size = len(list_of_int)

    if size == 1:
        return list_of_int[0]
    elif size == 2:
        return max(list_of_int)

    mid = int(size / 2)

    maxp = list_of_int[mid]

    if maxp >= list_of_int[mid - 1] and maxp >= list_of_int[mid + 1]:
        return maxp

    elif maxp < list_of_int[mid - 1]:
        return find_maxp(list_of_int[:mid])
    else:
        return find_maxp(list_of_int[mid + 1:])
