#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Printing a deduplicated list with the order preserved
"""
import datetime
time1 =datetime.datetime.now()

def dedup(seq):
    '''(list) -> lst
    Return a list with no duplication and with the order preserved
    >>> dedup([1,2,2,2,3,4,3,6,6,5])
    [1, 2, 3, 4, 6, 5]
    >>> dedup(['b', 'B','b','a','c'])
    ['b', 'B', 'a', 'c']
    '''
   # order preserving
    checked = []
    for e in seq:
        if e not in checked:
            checked.append(e)
    return checked

if __name__ == '__main__':
    lst = ([1,2,2,2,3,4,3,6,6,5])
    print lst
    print dedup(lst)
        
    print("\nEnd of process in %s" % (datetime.datetime.now() - time1))