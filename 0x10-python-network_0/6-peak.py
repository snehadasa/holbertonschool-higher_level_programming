#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers."""


def find_peak_high(arr, l, h):
    """ Find a peak"""
    m = l + (h - l)//2

    print("low " + str(l) + " high " + str(h))
    if (l == h):
        return arr[l]
    if ((h - l) == 1):
        return max(arr[l], arr[h])

    if (arr[m] > arr[m-1] and arr[m] > arr[m+1]):
        return arr[m]
    elif (arr[m] <  arr[m + 1]):
        return find_peak_high(arr, m + 1, h)
    else:
        return find_peak_high(arr, l, m - 1)


def find_peak(list_of_integers):
    """To find peak"""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    return find_peak_high(list_of_integers, 0, (len(list_of_integers) - 1))
