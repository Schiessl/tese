#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Extracting the list of terms and its variants
"""
import datetime
import nltk
from nltk import word_tokenize
import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

time1 =datetime.datetime.now()

f = '''INVESTIMENTO RELEVANTE É aquele que comparado ao porte de faturamento 
da empresa, sua estrutura de capitais, situação econômico-financeira, bem como 
sua posição no mercado, apresenta significância nos seus negócios, 
sob a ótica do risco de crédito;'''
#text = nltk.Text(f)
words = nltk.word_tokenize(f)

### ATENTION: if we have some tmp files like .DS_STORE in Mac OSX, we must remove it ###

# Reading corpus
corpusdir = '/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/test/glossAnnotated/' # Directory of corpus.
#corpusdir = '/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/test/test1/' # Directory of corpus.   
risco = PlaintextCorpusReader(corpusdir, '.*')
risco.fileids()

#raw_text = risco.raw('gloss533.txt')
#print raw_text[0:]

# Some statistics

print 'Number of term: ', len(risco.words())
print 'Number of unique terms: ', len(set(risco.words()))

fd = nltk.FreqDist(risco.words())
print fd.freq('bem')
print fd['bem']

# presenting ngrams of the term
target_word = 'bem'
fd = nltk.FreqDist(ng
              for ng in nltk.ngrams(risco.words(), 6)
              if target_word in ng)
for hit in fd:
    print(' '.join(hit))

txt = nltk.Text(risco.words())
print "\n### See words in a context ###"
print txt.concordance('bem')

print "\n### Find words with a similar text distribution ###"
print txt.similar('bem')

print "\n### Statistically significant collocations in a text ###"
print txt.collocations()

fd1 = nltk.FreqDist(txt)
print fd1
#print risco.concordance('bem')    
    
#############################################################################
print("\nEnd of process in %s" % (datetime.datetime.now() - time1))