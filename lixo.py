#!/usr/bin/env python
# -*- coding:  latin-1 -*-
""" Examples of spliting text in portuguese (enconding 'latin-1') using regex. 
"""
import nltk
import re

print "\n****** Using Regex to tokenize ******"
text = '''Família-Empresa S.A. dispõe de $12.400 milhões para concorrência. A 
âncora, desse negócio, é conhecida no coração do Órgão responsável. '''
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
print result
