#!/usr/bin/env python
# -*- coding:  latin-1 -*-
""" Spliting text in portuguese (enconding 'latin-1') using regex. 
DON'T FORGET TO CHANGE THE SECOND LINE coding: latin-1
"""
import nltk
import re

text = open('smallText_pt.txt','rU').read().decode('utf-8')
#text = '''Fam�lia-Empresa S.A. disp�e de $12.400 milh�es para concorr�ncia. A 
#�ncora, desse neg�cio, � conhecida no cora��o do �rg�o respons�vel. '''
#text = 'Bancos situados em Bras�lia'

print "\n****** Using Regex to tokenize ******"
pattern = r'''(?x)    # set flag to allow verbose regexps
     ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
    | \w+(-\w+)*        # words with optional internal hyphens
    | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
    | \.\.\.            # ellipsis
    | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
    '''
result = nltk.regexp_tokenize(text, pattern, flags=re.UNICODE) 
for w in result:
    print w.decode('latin-1')
    print w #when reading text from a file

print result