#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This program reads directories and subdirs search for html files
to convert to plain text. All you need need is to entry the top dir
and then execute the program. Every html file is converted to txt file
and saved in the same directory.
"""
from __future__ import print_function, division
import pysolr
#from mysolr import Solr
import os
import datetime

time1 =datetime.datetime.now()
##############################################################################
# Lots of example on how to use pysolr
#https://code.google.com/p/pysolr/source/browse/trunk/pysolr.py

#solr = pysolr.Solr('http://localhost:8983/solr/simple/')
#solr = pysolr.Solr('http://localhost:8983/solr/pdfs/')
solr = pysolr.Solr('http://localhost:8983/solr/pdfsTest/')

#solr.add([
#    {
#        "id": 1,
#        "title": "A test document",
#    },
#    {
#        "id": 2,
#        "title": "The Banana: Tasty or Dangerous?",
#    },
#])

# You can optimize the index when it gets fragmented, for better speed.
#solr.optimize()

# Later, searching is easy. In the simple case, just a plain Lucene-style
# query is fine.
results = solr.search('*:*')
#results = solr.search('bananas')

# The ``Results`` object stores total results found, by default the top
# ten most relevant results and any additional data like
# facets/highlighting/spelling/etc.
#print("Saw {0} result(s).".format(len(results)))
#
## Just loop over it to access the results.
#for result in results:
##    print("The title is '{0}'.".format(result['uid']))
#    print("The resiçt is :", result)

# For a more advanced query, say involving highlighting, you can pass
# additional options to Solr.
results = solr.search('banco', **{
    'hl': 'true',
    'hl.fragsize': 30,
})

print("Saw {0} result(s).".format(len(results)))

# Just loop over it to access the results.
for i,result in enumerate(results):
##    print(result)
    print(str(i)+" The title is '{0}'.".format(result['uid'])) #for PDFS core
#    print("The title is '{0}'.".format(result['title'])) #for simple core

# You can also perform More Like This searches, if your Solr is configured
# correctly.
#similar = solr.more_like_this(q='id:2', mltfl='text')#not working

# Finally, you can delete either individual documents...
#solr.delete(id=1)

# ...or all documents.
#print ('\nDeletion response:\n', solr.delete(q='*:*'))

##############################################################################
print("\nEnd of process in %s" % (datetime.datetime.now() - time1))