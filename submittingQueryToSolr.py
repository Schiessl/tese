#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Submits a query into a Solr instance and get the results
'''
from __future__ import division # floating numbers
import datetime
from mysolr import Solr

time1 = datetime.datetime.now()

##############################################################################
def connectSolr(q, core='pdfsTest', numRows=10000, whereStart=0):
    '''(str),(str),(int),(int) -> <class 'mysolr.response.SolrResponse'>
    Returns an object which contains several outputs from an specific query
    submitted to a Solr instance.
    >>> connectSolr('caixa')
    <SolrResponse status=200>
    >>> connectSolr("'basileia~' AND 'CAIXA'")
    <SolrResponse status=200>  
    '''
    solrConn = Solr('''http://localhost:8983/solr/''' + core + '''/''')
    response = solrConn.search(q=q , rows=numRows, start=whereStart) # limited rows
#    response = solrConn.search(**q) # limited rows
    return response

##############################################################################
if __name__ == '__main__':
    query ='"risco crédito"~1 AND "bancária"' #combining terms and logical connectors
    query ='facto~ AND superv*' #combining fuzzy and wildcards
#    query ='te?t?*' #single wildcard
    query = "(basileia~  'risco operacional'ˆ4) AND banc~" #grouping '()' and boosting terms 'ˆ'
#    query = {'q' : '*:basileia~&fl=*,score', 'debugQuery' : 'true', 'facet.field' : ['risco', 'caixa']}
    query = "basileia~&fl=*,score"
    
    for j, docs in enumerate(connectSolr(query,'pdfsTest',1000,0).documents):
        for doc in (docs['content']):
            print ' \n'+ str(j) + ' - ' + doc.strip()
        print
    
    #example of query with score, sort, and debug to visualize how Solr calculates document relevance
    #http://localhost:8983/solr/pdfsTest/select?q=basileia~&sort=score+desc&fl=*%2Cscore&wt=python&indent=true&debugQuery=true       
    #http://wiki.apache.org/solr/SolrRelevancyFAQ#How_can_I_see_the_relevancy_scores_for_search_results
    print "Docs found - ", connectSolr(query).total_results
    print "Query time - ", connectSolr(query).qtime
    print "Solr message - ", connectSolr(query).extract_errmessage
    print "Solr status - ", connectSolr(query).solr_status
    print "More like this - ", connectSolr(query).mlt
    print "Url - ", connectSolr(query).url
    print "Headers - ", connectSolr(query).headers
    print "Stats - ", connectSolr(query).stats
    print "Type response Solr - ", type(connectSolr(query)) 

    print("\nEnd of process in %s" % (datetime.datetime.now() - time1))

##criação dos arquivos de teste de conexão com o Solr
#f = open('glossTest.txt', 'rU').readlines()
#for i, line in enumerate(f):
#    fw = open('''/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/test/gloss/gloss''' + str(i) + '''.txt''','w')
#    print>>fw, line
#    fw.close()