#!/usr/bin/env python
# -*- coding: latin-1 -*-
# -*- coding: utf-8 -*-
from __future__ import division # floating numbers
import re, os, nltk
import datetime
from nltk.tokenize import sent_tokenize, word_tokenize

#time1 =datetime.datetime.now()

##############################################################################
def regex_tokenize(text):
    '''(text) -> list

    Return list of words from a text.
    >>> regex_tokenize('bancos situados em Brasília')
    ['bancos', 'situados', 'em', 'Bras\xc3', 'lia']
    >>> regex_tokenize('Isto é um teste difícil')
    ['Isto', '\xc3', 'um', 'teste', 'dif\xc3', 'cil']
    '''
#    print "\n****** Using Regex to tokenize ******"
    pattern = r'''(?x)    # set flag to allow verbose regexps
        ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
        | \w+(-\w+)*        # words with optional internal hyphens
        | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
        | \.\.\.            # ellipsis
        | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
        '''
    words = nltk.regexp_tokenize(text, pattern, flags=re.UNICODE)    
    return words 

##############################################################################
def stpWords_custom():
    # creating stopwords file
    stopwords = nltk.corpus.stopwords.words('portuguese')
    f = open('stopWordsBr.txt','rU').read()
    stp = list(f.split())
    for p in stp:
        stopwords.append(p)
    return stopwords

##############################################################################
def lemmatizeWords_custom(f1):
    '''(list) -> list
    Comparing words from the chosen cluster and the dictionary to normalize 
    words to their lemmas, like plurals to singular, verbs to inflected forms.
    A text file is created with the new contents.
    '''
    path = '/Users/marceloschiessl/RDF_text_project/corpus/dic_sas_pt/'
    input_file = 'dicflexunitbr.txt'#{dicionario.txt dicflexunitbr.txt }
    #Printing results and creating txt file
#    with open(f1, "rU")as f1, open(path+f2, "rU") as f2:
    lemmatizedText = []
    with open(path+input_file, "rU") as f2:
        # creating file into dict improves performance
        words_dict = {k:v for k, v, _ in (line.split(',') for line in f2)} 
        for i,word in enumerate(f1):
            word = word.rstrip().lower()
            if word in words_dict:
#                print i, word, words_dict[word]
                lemmatizedText.append(words_dict[word])
            else:
#                print i, word
                lemmatizedText.append(word)
    return lemmatizedText

##############################################################################

if __name__ == '__main__':
#    for word in regex_tokenize(text):
#        print word.decode('latin-1')
#    print regex_tokenize(text)
    print nltk.word_tokenize('Bancos situados em Brasília')
#    print stopwords
    print lemmatizeWords_custom('Bancos situados em Brasília'.split())
    print [word for word in lemmatizeWords_custom((nltk.word_tokenize('Bancos situados em Brasília')))
    if word not in stpWords_custom()]

##############################################################################
#print("\nEnd of process in %s" % (datetime.datetime.now() - time1))
#import doctest
#doctest.testmod()