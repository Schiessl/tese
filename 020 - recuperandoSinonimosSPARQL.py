#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Retrieving synonyms from the portuguese lexical ontology - similar to Wordnet.
It uses label of classes and properties extracted from the financial risk management ontology
in portuguese. It reads a file containing words and search for synonyms.
"""
from __future__ import division
import datetime, nltk
from nltk.corpus import wordnet as wn
from SPARQLWrapper import SPARQLWrapper, JSON, XML

## Querying Fuseki server
## Attention: Server must be started manually to the query works 
time1 = datetime.datetime.now()

sparql = SPARQLWrapper("http://localhost:3030/ds/query") #endpoint SPARQL
############# setting parameters to build the query ###########
''' this query returns the synsets related to the 
string value of the term variable, and the definition '''
term = 'risco'
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
    for var in result_set["head"]["vars"] :
        if var in result:#to test whether all variables exists or not
            print result[var]["value"],": ",
    print
time2 = datetime.datetime.now()
print time2 - time1