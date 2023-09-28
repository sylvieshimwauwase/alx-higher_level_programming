#!/usr/bin/python3
# function to find a peak in alist of unsorted integers

def find_peak(list_of_integers):
    """
    Find a peak in a lis of unsorted integers
    Args:
    list_of_int: A list of unsorted integers
    """
    if not list_of_int:
        return None

    l, r = 0, len(list_of_int) - 1

    while l < r:
        mid = (l + r) // 2

        if list_of_int[mid] >= list_of_int[mid + 1] and list_of_int[mid] >= list_of_int[mid - 1]:
            return list_of_int[mid]

        if list_of_int[mid] < list_of_int[mid + 1]:
            l = mid + 1
        else:
            r = mid -1

    return max(list_of_int[l], list_of_int[r])
