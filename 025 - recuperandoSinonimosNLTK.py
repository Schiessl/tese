#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Retrieving synonyms from the Open Multilingual Wordnet using NLTK package.
It uses label of classes and properties extracted from the financial risk management ontology
in portuguese. It reads a file containing words and search for synonyms.
Reference:http://www.nltk.org/howto/wordnet.html 
"""
import os, nltk, sys
from nltk.corpus import wordnet as wn
### Words ###
# print sorted(wn.langs()) # languages available
# print len(wn.all_lemma_names(pos='n', lang='por'))# counting noun lemmas available in a language
# print wn.synset('risk.n.01').lemma_names('por')# listing lemmas in the desired language 
# print sorted(wn.synset('dog.n.01').lemmas('por'))
# print wn.synsets(b'cão'.decode('utf-8'),lang='por')# list synsets when the input is in utf-8
# print wn.lemma(b'dog.n.01.c\xc3\xa3o'.decode('utf-8'), lang='por')

### Extracting all synsets
print '******* all synsets ********'
term = 'banco'
lang = 'por'
for synset in wn.synsets(term.decode('utf-8'), lang='por'):
    print '@en --> %s \t\t @pt --> %s' % (synset.lemma_names(), synset.lemma_names(lang))
    for t in synset.lemma_names(lang):
        print t # this is how to extract letters like ã, ç

print
print '******* all hyponyms ********'
term_syn = wn.synset('bank.n.03')
types_term_syn = term_syn.hyponyms()
print types_term_syn
print types_term_syn[0]

print
print

for i,syn in enumerate(types_term_syn):
#     print 1, syn
    for lem in syn.lemmas():
        print '@en --> %s \t\t @pt --> %s' % (lem.name(), syn.lemma_names(lang))
        