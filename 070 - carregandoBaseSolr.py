#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Read files from directories and subdirs and post them to a Solr instance.
"""
from __future__ import print_function, division
import os
import datetime

time1 =datetime.datetime.now()
##############################################################################
def postSolr(path,fileInput,solrCore):
    '''(string,string,string) --> None
    
    Post files to a Solr instance
    '''
    print('\n** Searching path: ', path)
    os.chdir(path)
    print('**** Posting file: ', fileInput)
    os.popen("curl -X POST 'http://localhost:8983/solr/"+solrCore+"/update/extract?extractFormat=text&literal.id=doc1&commit=true' -F 'myfile=@"+fileInput+"'")
    return 

##############################################################################
# Change the top dir path and file extension to start searching
# Change the Solr core 
topDir = "/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/tese/internos_caixa"
extension = '.pdf' # The file extension to search for
solrCore = 'pdfsTest' 
i=0
for dirPath, dirNames, nameFiles in os.walk(topDir):
    for nameFile in nameFiles:
        if nameFile.lower().endswith(extension):
            print('\n'+str(i)+' Files: ',os.path.join(dirPath, nameFile))
            postSolr(dirPath,nameFile,solrCore)
            i += 1

##############################################################################
print("\nEnd of process in %s" % (datetime.datetime.now() - time1))