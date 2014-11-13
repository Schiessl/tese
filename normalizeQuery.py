#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division # floating numbers
from nltk import word_tokenize
#import datetime
import tokenizePT

#time1 =datetime.datetime.now()
##############################################################################
def normalizeQuery(query):
    '''(str) -> list

    Returns a list of normalized words
    >>> normalizeQuery('testando')
    ['testar']
    >>> normalizeQuery('informação digitada')
    ['informa\xc3\xa7\xc3\xa3o', 'digitar']
    '''
    normalizedQuery = [word for word in tokenizePT.lemmatizeWords_custom((word_tokenize(query))) 
    if word not in tokenizePT.stpWords_custom()]
    return normalizedQuery

##############################################################################

if __name__ == '__main__':
    text = '''Onde encontrar recursos sobre preservação digital e a difícil tarefa
    do profissional da informação'''
    #print tokenizePT.regex_tokenize(text)
    tokensNoStpWords = [w for w in word_tokenize(text) if w not in tokenizePT.stpWords_custom() and not w.isdigit()]
    
    #print 'Tokens: ', nltk.word_tokenize(text)
    #print 'Tokens without stopwords: ', tokensNoStpWords
    #print 'Tokens lemmatized: ', tokenizePT.lemmatizeWords_custom(text.split())
    #print [word for word in tokenizePT.lemmatizeWords_custom((nltk.word_tokenize(text)))
    #if word not in tokenizePT.stpWords_custom()]
    print 'Tokens normalized: ', normalizeQuery(text)
##############################################################################
#    print("\nEnd of process in %s" % (datetime.datetime.now() - time1))
#import doctest
#doctest.testmod()