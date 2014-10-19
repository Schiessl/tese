#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Reading a text file, extracting words and
finding synonyms, definition, examples and POS
from Open Multilingual Wordnet via NLTK. '''

from __future__ import division
import nltk
from nltk.corpus import wordnet as wn

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("outClassProperty.txt")
data = fp.read()

#tokenizing input text into sentences and into words

words = [w.lower() for w in nltk.wordpunct_tokenize(data.decode("utf8"))]   # other lines in your code are just excessive

for term in words:
    print '---------------------------------------'
    print 'Term to analyze: ', term 
    print '---------------------------------------'
    syns = wn.synsets(term)

    for s in syns:
        print "Synsets = ", s, s.lemma_names('por') 
        for l in s.lemmas():
            print l.name()
        print 'Definition: ', s.definition()
        print 'Example: ', s.examples()
        print 'POS: ', s.pos(),'\n'
        