#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Reads a text file and search for a string in the file content.
"""
from __future__ import print_function, division
import datetime

time1 =datetime.datetime.now()
##############################################################################
def get_file(pathFile):
    '''(file) --> (string)
    Returns the content of a file
    '''
    f = open(pathFile,'rU').read()
    return f
#print (get_file('/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/AlterTxt/Gerop/SAS_crawler/Basileia_III/txt/file34.txt'))

def findString(strToSearch, f):
    '''(string)-->(none)
    Finds a string in a text and returns the position where it begins
    '''
    #first loop
    findStr = f.strip().lower().find(strToSearch.strip().lower())
    if findStr == -1:
        print ('\nString not found!')
    else:
        #untill the EOF
        count = 0
        while (findStr) != -1:
            findStr = f.find(strToSearch,findStr+1)
            count += 1
            if findStr == -1:
                break
            else:
                print (str(count) + ' - String "' + strToSearch + '"' + ' found in position ' + str(findStr))
    return strToSearch, findStr, count

strValue, position, count = findString('Patrimônio', get_file('/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/AlterTxt/Gerop/SAS_crawler/Basileia_III/txt/file34.txt'))

##############################################################################
print("\nEnd of process in %s" % (datetime.datetime.now() - time1))