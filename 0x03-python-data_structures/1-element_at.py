#!/usr/bin/python3
def element_at(this_list, idx):
    if idx < 0:
        return None
    if idx >= len(this_list):
        return None
    else:
        return this_list[idx]
