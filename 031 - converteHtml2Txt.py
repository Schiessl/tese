#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This program reads directories and subdirs search for html files
to convert to plain text. All you need need is to entry the top dir
and then execute the program. Every html file is converted to txt file
and saved in the same directory.
"""
from __future__ import division
from urllib import urlopen
from bs4 import BeautifulSoup
import os
import datetime

time1 =datetime.datetime.now()
##############################################################################
#url = '/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/Gerop/SAS_crawler/Basileia_III/file2.html'

def htmlToTxt(dirPath,nameFile):
    '''Converting a html file into a plain text file and 
    writing it with '.txt' extension in the same directory
    '''
    print 'Converting '+ nameFile
    #extractin text from html file
    html = urlopen(os.path.join(dirPath,nameFile))
    rawTxt = BeautifulSoup(html).get_text()
    #writing text file
    to_file = open(os.path.join(dirPath,nameFile) + '.txt','w')
    print>>to_file, rawTxt.strip()
    to_file.close()

    return rawTxt
##############################################################################
# The top argument for walk
# Entry the top directory path.
topDir = "/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/Gerop/SAS_crawler/"
topDir = "/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/test/"

# The extension to search for
extension = '.html'
 
for dirPath, dirNames, nameFiles in os.walk(topDir):
    for nameFile in nameFiles:
        if nameFile.lower().endswith(extension):
            print(os.path.join(dirPath, nameFile))
            print htmlToTxt(dirPath,nameFile)
            
##############################################################################
print("\nEnd of process in %s" % (datetime.datetime.now() - time1))