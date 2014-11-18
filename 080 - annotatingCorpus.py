#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Extracting the list of terms and its variants
"""
import csv
import datetime
from deduplication import dedup

time1 =datetime.datetime.now()

# reading source
###############################################################################
# only alter variables here
input_file = 'sourceToLemon.csv'

with open(input_file, 'rb') as csvfile:
    f = csv.reader(csvfile, delimiter=',', quotechar='|')
    i = 0
    vocab = []
    for w in (f):
        if w[0].strip() == '@':
            lst =[]
            i += 1
            lexicalEntry = w[1].strip()
            lst.append(lexicalEntry)
#            print i, 'Term :', lexicalEntry
            j = 1
        else:
            otherForm = w[1].strip()
            lst.append(otherForm)
#            print str(i)+'.'+str(j),'Variant :', otherForm
            j += 1
        vocab.append(lst)

# print list with no duplication
for i, w in enumerate(dedup(vocab)):
    print dedup(w)
    for t in dedup(w):
        print i,t
        
        
print("\nEnd of process in %s" % (datetime.datetime.now() - time1))