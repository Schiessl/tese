#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 13:19:27 2014

@author: marceloschiessl

Validating whether a term exist in a corpus (bag of words). Besides, just tuning
the limit value, one can get a list of similar terms based on distance metric 
String Matching which is a normalized Levenshtein.
 """
from __future__ import unicode_literals, division
import datetime, traceback, sys
from nltk.metrics import edit_distance

time1 =datetime.datetime.now()

###############################################################################
###############################################################################
# only alter variables here
typeVar = 'synsets' #{Class, DatatypeProperty, ObjectProperty}
input_file1 = 'synsetsToCompare.txt'
#typeVar = 'Class' #{Class, DatatypeProperty, ObjectProperty}
#input_file1 = 'out'+typeVar+'.txt'
input_file2 = 'stpwFinalGroup.txt'
output_file = 'compared'+typeVar+'.txt'
limit = .9
###############################################################################
###############################################################################
#reading files and eliminating duplicated record
#d1 = list(set(open(input_file1,'rU').readlines()))
inpList1 = (open(input_file1,'rU').readlines())
d1 = []
#removing duplicates, but maintaining the order
[d1.append(item.strip()) for item in inpList1 
    if item.strip() not in d1 and len(item.strip()) > 0]
    
inpList2 = (open(input_file2,'rU').readlines())
d2 = []
#removing duplicates, but maintaining the order
[d2.append(item.strip()) for item in inpList2 
    if item.strip() not in d2 and len(item.strip()) > 0]

###############################################################################
def string_matching(label1, label2): #by Maedchen and Staab
    """ (string, string) -> float
    
Return the coefficient of similarity between two sequence of strings based on
the Levenshtein distance (edit distance). It equates 1 for exact match and
0 to no similarity.
>>> string_matching('power','power')
1.0
>>> string_matching('power','abba')
0.0
"""
    sm = float(
        min(len(label1),len(label2)) - 
        edit_distance(label1, label2)
        ) / min(len(label1),len(label2)
        )    
    try:
        if sm < 0:
            return 0.0
        else:
            return sm
    except:
        print "Error found:"
        traceback.print_exc(file=sys.stdout)
        return 0

###############################################################################
def compWords(limit):
    """ (float) -> list
    
    Return a list of two term to be compared, and the value of the similarity
    between them.
    >>> compWords(0.75)
    0 (Ameaça ; ameaça) = 1.0
    >>> compWords(0.75)
    4 (Fornecedor ; fornecedores) = 0.818
    """
    t0=datetime.datetime.now()
    ordList=[]
    deduplic=[]
    print 'Calculating similarities...'
    for i,w1 in enumerate(d1):
        ordTup=(w1.strip(),'not found', 0)              
        for j,w2 in enumerate(d2):
            sm = string_matching(w1.lower().replace(' ', ''), 
                                 w2.lower().replace(' ', ''))
            if sm >= limit:
                ordTup=(w1.strip(),w2.strip(),round(sm,3))              
                ordList.append(ordTup)
                continue
        ordList.append(ordTup)

    [deduplic.append(item) for item in ordList if item not in deduplic]# deduplication, but maintaining the order
#    sortList = sorted(set(ordList), key=lambda e: (e[0],e[2]*-1))#sorting by w1 and sm (descending)
    print "done in %s" % (datetime.datetime.now() - t0),'\n'
#    return sortList
    return deduplic

###############################################################################
#Printing results and creating txt file
to_file = open(output_file, 'w') #opening the file to write
for i,t in enumerate(compWords(limit)):
        print i,'({v1} ; {v2}) = {v3}'.format(v1=t[0], #print to screen
                                            v2=t[1], 
                                            v3=t[2])
        print>>to_file, t[0], ',', t[1], ',', t[2] #printing to file

to_file.close() #closing the file

print("\nEnd of process in %s" % (datetime.datetime.now() - time1))

#import doctest
#doctest.testmod()     