#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Extracting the list of terms and its variants
"""
import csv
import datetime
from deduplication import dedup
from submittingQueryToSolr import connectSolr

time1 =datetime.datetime.now()

# reading source
###############################################################################
# only alter variables here
#inputCsv ='sourceToLemon.csv'
inputCsv ='test_sourceToLemon.csv'

def inputVocab(input_file):
    '''Reads a csv file and generates a vocabulary to desambiguate query
    '''
    with open(input_file, 'rb') as csvfile:
        f = csv.reader(csvfile, delimiter=',', quotechar='|')
#        i = 0
        vocab = []
        for w in (f):
            if w[0].strip() == '@':
                lst =[]
#                i += 1
                lexicalEntry = w[1].strip()
                lst.append(lexicalEntry)
    #            print i, 'Term :', lexicalEntry
#                j = 1
            else:
                otherForm = w[1].strip()
                lst.append(otherForm)
    #            print str(i)+'.'+str(j),'Variant :', otherForm
#                j += 1
            vocab.append(dedup(lst))
    return (vocab)
#print inputVocab('test_sourceToLemon.csv')
###############################################################################
def buildQuery(query, boost):
    '''Builds a query with the weight to boost the term which is the ontology
    vocabulary, otherwise it returns only the term to a standard search
    '''
    for line in dedup(inputVocab(inputCsv)):
        domainVocab = dedup(line)
        if query in domainVocab:
#            print domainVocab
            boostedQuery = ''
            for i,w in enumerate(domainVocab):
                boostedQuery = boostedQuery + ' ' + '"' + w + '"' + 'ˆ' + str(boost)
        else:
            boostedQuery = query
    return boostedQuery

#print buildQuery('ameaça',4).strip()

#############################################################################
# Automatic procedure to read a list of terms from an ontology e submit them
# to a Solr instance.
manualQuery = ["produto", "mercadoria", "artigo", "objecto posto à venda", 
               "fazenda", "bem", "produção", "utensílio", "artefato", "fruto",
               "produtos"]
#manualQuery = ['ameaça', 'risco', 'perigo']
for i,w in enumerate(manualQuery):
#        print w
        fullWordQuery ='"' + w + '"' 
        wordQuery = w
        print fullWordQuery
        print "Semantic search - ", " term: ", wordQuery, "|| Docs found : ", connectSolr(buildQuery(wordQuery,4)).total_results
        print "Syntactic search - ", " term: ", wordQuery, "|| Docs found : ", connectSolr(fullWordQuery).total_results
        print

#############################################################################
# Automatic procedure to read a list of terms from an ontology e submit them
# to a Solr instance.
#def automaticQuery(inputFile):
#    '''Reads a ontology vocabulary and submit the terms into a Solr instance
#    '''
#    for i,line in enumerate(dedup(inputVocab(inputFile))):
#    #    print  i,line
#        for w in dedup(line):
#    #        print w
#            fullWordQuery ='"' + w + '"' 
#            wordQuery = w
#            print fullWordQuery
#    #        print buildQuery(wordQuery,4)
#            print buildQuery(wordQuery,4)
#            print "Semantic search - ", " term: ", wordQuery, "|| Docs found : ", connectSolr(buildQuery(wordQuery,4)).total_results
#            print "Syntactic search - ", " term: ", wordQuery, "|| Docs found : ", connectSolr(fullWordQuery).total_results
#            print
#    return
#print automaticQuery('test_sourceToLemon.csv')

#############################################################################
print("\nEnd of process in %s" % (datetime.datetime.now() - time1))