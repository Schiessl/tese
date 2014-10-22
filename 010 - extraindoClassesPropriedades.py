#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Extracting labels of classes, datatype and object properties 
from a local ontology (owl).
Creating a txt file with classes and properties extracted. 
"""
from __future__ import division # floating numbers
import os, rdflib
import rdflib

# change the current working directory in order to use functions
# called functions must be in the same folder
os.chdir('/Users/marceloschiessl/RDF_text_project/corpus') 
    
############# Loading local document ###########
input_file = 'risk_management_pt.owl'
input_path = 'financial_risk/'
source = input_path + input_file #don't change this line

g = rdflib.Graph()
fileParsed = g.parse(source) #reading graph
print '======================================================='
print("O grafo tem %s declarações." % len(g))
print '======================================================='

def querySparql(varToQuery):
    '''It receives a variable which represents a part of the triple (subject, property, object) that
    one wants to extract the label in Portuguese. Therefore, every function is timed to track its performance 
    '''
    query = '''
            SELECT DISTINCT ?type ?label
            {
               ?type a owl:'''+varToQuery+''' .
               ?type rdfs:label ?label .
               filter(langMatches(lang(?label),"pt"))
            }
            '''
    result_set = g.query(query)
    print
    print '======================================================='
    if varToQuery == 'Class':
        print ' Classes em português '
        wFile = "/Users/marceloschiessl/RDF_text_project/tese/outClass.txt" #defining file to write
    elif varToQuery == 'DatatypeProperty':
        print ' Propriedades de dados em português '
        wFile = "/Users/marceloschiessl/RDF_text_project/tese/outDatatypeProperty.txt" #defining file to write
    else:
        print ' Propriedades de objetos em português '
        wFile = "/Users/marceloschiessl/RDF_text_project/tese/outObjectProperty.txt" #defining file to write
    print '======================================================='

    to_file = open(wFile, 'w') #opening file to write

    for i,stmt in enumerate(result_set):
#         print i,stmt[0],stmt[1]
        print i,stmt[1]
        print>>to_file, stmt[1] #creating file content
    to_file.close() #closing the file
    return 

##### This part tests the function execution time. Change the number parameter to test the number of time you want
if __name__ == '__main__':
    import timeit
    print(timeit.timeit("querySparql('Class')", setup="from __main__ import querySparql", number=1))
    print(timeit.timeit("querySparql('ObjectProperty')", setup="from __main__ import querySparql", number=1))
    print(timeit.timeit("querySparql('DatatypeProperty')", setup="from __main__ import querySparql", number=1))
