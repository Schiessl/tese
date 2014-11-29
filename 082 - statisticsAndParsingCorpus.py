#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Extracting the list of terms and its variants
"""
import datetime
import nltk
from nltk import word_tokenize
import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.corpus import floresta,mac_morpho
from parser_portuguese_risk import evaluateModel, splitTrainTestModel, simplify_tag
time1 =datetime.datetime.now()

###############################################################################
### ATENTION: if we have some tmp files like .DS_STORE in Mac OSX, we must remove it ###

# Reading corpus
corpusdir = '/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/test/glossAnnotated/' # Directory of corpus.
#corpusdir = '/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/test/test1/' # Directory of corpus.   
risco = PlaintextCorpusReader(corpusdir, '.*')
risco.fileids()

raw_text = risco.raw('gloss533.txt')
#print raw_text[0:]

# Some statistics

print 'Number of term: ', len(risco.words())
print 'Number of unique terms: ', len(set(risco.words()))

fd = nltk.FreqDist(risco.words())
print fd.freq('bem')
print fd['bem']

# presenting ngrams of the term
target_word = 'bem como'
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

#text = '''Hipoteca é um tipo de garantia real, acessório de uma dívida, que incide 
#sobre bens imóveis. Neste caso, o bem hipotecado permanece em poder do 
#devedor.'''
#
text = '''O homem viu a criança de binóculos'''
words = word_tokenize(text)

ngramModelType = 'trigram' # choose one of these 'default, unigram, bigram or trigram'
propSplit = 0.9 # define the train corpus size
corpusName = 'Floresta'  # choose one of these 'floresta' or 'mac_morpho'
corpus = floresta  # choose one of these 'floresta' or 'mac_morpho'

train_sents, test_sents, corpus = splitTrainTestModel(propSplit, corpus, corpusName)
tModel = evaluateModel(train_sents, test_sents, corpus, ngramModelType)
twords = tModel.tag(words)    

#for raw_text in risco.fileids()[0:]:
##    print('...Analising ' + raw_text)
#    words = word_tokenize(risco.raw(raw_text))
#    twords = tModel.tag(words)
#    twords = [(w, simplify_tag(t)) for (w,t) in twords]
#    print('\n' + ' '.join(word + '[' + tag  + ']' for (word, tag) in twords))

twords = tModel.tag(words)
twords = [(w, simplify_tag(t)) for (w,t) in twords]
print('\n' + ' '.join(word + '[' + tag  + ']' for (word, tag) in twords))

#############################################################################
print("\nEnd of process in %s" % (datetime.datetime.now() - time1))