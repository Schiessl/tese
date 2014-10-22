#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Retrieving synonyms from the OpenWN - portuguese lexical ontology - similar to Wordnet.
The input is label of classes and properties extracted from the financial risk management ontology
in portuguese. It reads a file containing words and search for synonyms and definitions.
/Users/marceloschiessl/RDF_text_project/corpus/openWordnet-PT-master/openWordnet-PT.rdf
"""
from __future__ import division
import datetime, nltk, re
from SPARQLWrapper import SPARQLWrapper, JSON, XML

time1 = datetime.datetime.now()
## Querying Fuseki server
## Attention: Server must be started, and the data updated
## manually to the query works 

sparql = SPARQLWrapper("http://localhost:3030/ds/query") #endpoint SPARQL
############# setting parameters to build the query ###########
''' this query returns the synsets related to the 
string value of the term variable, and the definition '''

print '*'*50
print 'Defitions from OpenWN-PT '  
print '*'*50

def sparqlQuery(term):
    print '-'*50
    print 'Term to analyze: ', term 
    print '-'*50
    print>>to_file, '-'*50
    print>>to_file, 'Term to analyze: ', term 
    print>>to_file, '-'*50

    selection = '?label ?synonym ?gloss' 
    # condition = '''?s ?p ?o .
    # FILTER (regex(?o, "garantia","i"))'''
    condition = '''?input_word a :WordSense .
      ?input_word rdfs:label ?input_label .
      FILTER (?input_label = "''' + term + '''")
      ?synset :containsWordSense ?input_word .
      ?synset :containsWordSense ?synonym .
      ?synonym rdfs:label ?label .
     
      ?input_word :word ?word .
      ?word :lexicalForm "''' + term +'''"@pt .
      OPTIONAL{?synset :gloss ?gloss .}'''
    distinct  = ' DISTINCT '
    limit     = ' LIMIT 30 '
    ###############################################################
    pref  = '''
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX owl: <http://www.w3.org/2002/07/owl#>
                PREFIX : <http://arademaker.github.com/wn30/schema/>
                PREFIX instbr:<http://arademaker.github.com/wn30-br/instances/>
                PREFIX inst:<http://arademaker.github.com/wn30/instances/>
            '''
    query = '''SELECT ''' + distinct + selection + '''  
                WHERE{''' + condition + '''}''' + limit + '''
            '''
    sparql.setQuery(pref + query)
    sparql.setReturnFormat(JSON) #fuseki output only XML and JSON
    result_set = sparql.query().convert()
     
    if result_set == {u'head': {u'vars': [u'synonym', u'label', u'gloss']}, u'results': {u'bindings': []}}:
        print "ATTENTION: No data to query. Upload some data"
     
    # print result_set
    for i,result in enumerate(result_set["results"]["bindings"]) :
        print i,
        print>>to_file, i,
        for var in result_set["head"]["vars"] :
            if var in result:#to test whether all variables exists or not
                t = re.sub(r'\bhttp?://[^- ]+\-[^- ]+\-', '', str(result[var]["value"])) # extracting the url from the result
                print t, ':',
                print>>to_file, t, ':',
        print
        print>>to_file, ''
    return
# sparqlQuery('risco')


# Reading txt files and calling SPARQL query
###############################################################################
###############################################################################
# only alter variables here
#typeVar = 'test' #{Class, DatatypeProperty, ObjectProperty}
#input_file1 = 'test_outClassProperty.txt'
typeVar = 'Class' #{Class, DatatypeProperty, ObjectProperty}
input_file1 = 'out'+typeVar+'.txt'
output_file = 'compared'+typeVar+'_OpenWNPT_synset.txt'
###############################################################################
###############################################################################
to_file = open(output_file, 'w') #opening the file to write

f = open(input_file1,r'U')
for line in f:
    term =line.strip() # remove the newline character (/n)
    sparqlQuery(term.lower())
#     print term

to_file.close() #closing the file

print("\nEnd of process in %s" % (datetime.datetime.now() - time1))