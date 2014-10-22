#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Reading a text file, extracting words and
finding synonyms, definition, examples and POS
from Open Multilingual Wordnet via NLTK. '''

from __future__ import division
import nltk
from nltk.corpus import wordnet as wn
import datetime

time1 =datetime.datetime.now()

tokenizer = nltk.data.load('tokenizers/punkt/portuguese.pickle')

###############################################################################
###############################################################################
# only alter variables here
#typeVar = 'test' #{Class, DatatypeProperty, ObjectProperty}
#input_file1 = 'test_outClassProperty.txt'
typeVar = 'ObjectProperty' #{Class, DatatypeProperty, ObjectProperty}
input_file1 = 'out'+typeVar+'.txt'
output_file = 'compared'+typeVar+'_wn_synset.txt'
###############################################################################
###############################################################################

#fp = open(input_file1).read()
words = list(open(input_file1).readlines())

#tokenizing input text into sentences and into words

#words = [w.lower() for w in nltk.wordpunct_tokenize(fp.decode("utf8"))]

to_file = open(output_file, 'w') #opening the file to write
for i,term in enumerate(words):
    print '---------------------------------------'
    print i, 'Term to analyze: ', term 
    print '---------------------------------------'
    print>>to_file, '---------------------------------------'
    print>>to_file, 'Term to analyze: ', term 
    print>>to_file, '---------------------------------------'
    syns = wn.synsets(term.lower().strip())

    for j,s in enumerate(syns):
        print j, "Synsets = ", s, s.lemma_names('por') 
        print>>to_file, "Synsets = ", s, s.lemma_names('por') 
        for l in s.lemmas():
            print l.name()
            print>>to_file, l.name()
        print 'Definition: ', s.definition()
        print 'Example: ', s.examples()
        print 'POS: ', s.pos(),'\n'
        print>>to_file, 'Definition: ', s.definition()
        print>>to_file, 'Example: ', s.examples()
        print>>to_file, 'POS: ', s.pos(),'\n'

to_file.close() #closing the file
            
print("\nEnd of process in %s" % (datetime.datetime.now() - time1))