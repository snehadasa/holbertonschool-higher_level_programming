#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers."""


def find_peak_high(arr, l, h, n):
    """ Find a peak"""
    m = l + (h - l)//2
    m = int(m)

    if (m == 0 or arr[m - 1] <= arr[m]) and\
       (m == (n - 1) or arr[m + 1] <= arr[m]):
        return arr[m]
    elif (m > 0 and arr[m - 1] > arr[m]):
        return find_peak_high(arr, l, (m - 1), n)
    else:
        return find_peak_high(arr, (m + 1), h, n)


def find_peak(list_of_integers):
    """To find peak"""
    if list_of_integers is None:
        return None
    return find_peak_high(list_of_integers, 0, (len(list_of_integers) - 1),
                          len(list_of_integers))
