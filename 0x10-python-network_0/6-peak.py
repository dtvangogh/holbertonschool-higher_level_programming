#!/usr/bin/python3
# find the peak


def find_peak(list_of_integers):
    """find the peak of list of unsorted integers"""
    if list_of_integers is None or list_of_integers == []:
        return None
    if list_of_integers:
    	peak = max(list_of_integers)
    return(peak)
