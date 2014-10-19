#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" There are some pieces of codes examples to cover the most common needs when dealing with querying data
from semantic web. It shows how to query local and remote data by using rdflib package, which has a specific
notation, and more traditional sparql notation by using SPARQLWrapper package. 
"""
from __future__ import division # floating numbers
import os, rdflib
from rdflib.graph import Graph

# change the current working directory in order to use functions
# called functions must be in the same folder
os.chdir('/Users/marceloschiessl/RDF_text_project/corpus') 
    
# ############ Loading local document ###########
source = '/Users/marceloschiessl/ontologies/sioc/ns.owl'
g = Graph()
fileParsed = g.parse(source)
# #########################################
# 
# ### reading local files saved onto /Users/marceloschiessl/RDF_text_project/sparql
# # g.parse("dbpedia_3.9.owl") # latest version up to this date 08aug2014
# 
# print g.serialize(format="turtle") # print graph in turtle format
# # print g.serialize(format="application/rdf+xml") # print graph in rdf/xml format
# 
# #total number of triples
# query = """
# SELECT (COUNT(*) AS ?number) { ?s ?p ?o  }
# """
# qres = g.query(query)
# for i,(row) in enumerate(qres):
#     print  "%s triplas" % row
# 
#### Calculating simple statistics from an ontology. 
#### Extracted from https://code.google.com/p/void-impl/wiki/SPARQLQueriesForStatistics
 
#total number of distinct classes
query = """
SELECT distinct ?o 
WHERE 
{ 
    ?s rdf:type ?o 
}
"""
# Atention:this second version match to the SIOC ontology description in http://www.w3.org/wiki/Good_Ontologies; it has 
# a local copy in /Users/marceloschiessl/ontologies/sioc/ns.owl
query = """
SELECT DISTINCT ?o 
{
   ?o rdf:type owl:Class .
}
ORDER BY ?o
"""
# SELECT (COUNT(DISTINCT ?o) AS ?number) { ?s rdf:type ?o } ORDER BY ?o
qres = g.query(query)
for i,(row) in enumerate(qres):
    print  i,"%s" % row
#     print  i,"%s distinct classes" % row
  
# # #total number of distinct predicates
# query = """
# SELECT (COUNT(DISTINCT ?p) AS ?number) { ?s ?p ?o }
# """
# # SELECT (COUNT(DISTINCT ?p) AS ?number) { ?s ?p ?o }
# qres = g.query(query)
# for i,(row) in enumerate(qres):
#     print  "%s distinct properties" % row

### examples of how to count using sparql
# ex069_ttl = """
# @prefix ab: <http://learningsparql.com/ns/addressbook#> .
# @prefix d: <http://learningsparql.com/ns/data#> . 
# 
# #People
# d:i0432 ab:firstName    "Richard" ; 
#         ab:lastName     "Mutt" ; 
#         ab:email        "richard49@hotmail.com" .
# d:i9771 ab:firstName    "Cindy" ;
#         ab:lastName     "Marshall" ; 
#         ab:email        "cindym@gmail.com" .
# d:i8301 ab:firstName    "Craig" ;
#         ab:lastName     "Ellis" ; 
#         ab:email        "c.ellis@usairwaysgroup.com" .
# 
# # Courses
# d:course34 ab:courseTitle "Modeling Data with OWL" . 
# d:course71 ab:courseTitle "Enhancing Websites with RDFa" . 
# d:course59 ab:courseTitle "Using SPARQL with non-RDF Data" . 
# d:course85 ab:courseTitle "Updating Data with SPARQL" .
# 
# # Who's taking which courses
# d:i8301 ab:takingCourse d:course59 . 
# d:i9771 ab:takingCourse d:course34 . 
# d:i0432 ab:takingCourse d:course85 . 
# d:i0432 ab:takingCourse d:course59 . 
# d:i9771 ab:takingCourse d:course59 .
# """

# g.parse(data=ex069_ttl, format="turtle") 
# 
# query = """SELECT ?p WHERE{?s ?p ?o}"""
# query = """SELECT DISTINCT ?p WHERE{?s ?p ?o}"""
# query = """SELECT DISTINCT ?first ?last WHERE{?s ab:takingCourse ?class ; ab:firstName ?first ; ab:lastName ?last .}"""
# qres = g.query(query)
# for i,(row) in enumerate(qres):
#     print  i,"%s %s" % row
# #     print  i,"%s distinct classes" % row
