#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Examples of reading text data and performing clustering K-means
"""
from __future__ import print_function

#import sklearn
import nltk, sklearn, string, os, collections
from nltk.stem.porter import PorterStemmer
from sklearn.datasets import load_files
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
#from sklearn.pipeline import Pipeline
#from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
from sklearn import metrics
from sklearn.cluster import KMeans, MiniBatchKMeans

import logging
from optparse import OptionParser
import sys, datetime
from time import time

time1 =datetime.datetime.now()
############################################################################
# Display progress logs on stdout
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
# parse commandline arguments
op = OptionParser()
op.add_option("--lsa",
              dest="n_components", type="int",
              help="Preprocess documents with latent semantic analysis.")
op.add_option("--no-minibatch",
              action="store_false", dest="minibatch", default=True,
              help="Use ordinary k-means algorithm (in batch mode).")
op.add_option("--no-idf",
              action="store_false", dest="use_idf", default=True,
              help="Disable Inverse Document Frequency feature weighting.")
op.add_option("--use-hashing",
              action="store_true", default=False,
              help="Use a hashing feature vectorizer")
op.add_option("--n-features", type=int, default=10000,
              help="Maximum number of features (dimensions)"
                   " to extract from text.")
op.add_option("--verbose",
              action="store_true", dest="verbose", default=False,
              help="Print progress reports inside k-means algorithm.")

print(__doc__)
op.print_help()

(opts, args) = op.parse_args()
if len(args) > 0:
    op.error("this script takes no arguments.")
    sys.exit(1)
###########################################################################
# Preprocessing text with NLTK package
token_dict = {}
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

###########################################################################
# Loading and preprocessing text data
# Uncomment the following to do the analysis on all the categories
#categories = None

print("\n Loading text dataset:")
t0 = datetime.datetime.now()

path = '/Users/marceloschiessl/RDF_text_project/corpus/txt/'
#path = '/Users/marceloschiessl/RDF_text_project/corpus/20news-18828'
j = 1
for subdir, dirs, files in (os.walk(path)):
    for i,f in enumerate(files):
        if f != '.DS_Store':
                file_path = subdir + os.path.sep + f
                file_to_read = open(file_path, 'r')
                text = file_to_read.read()
                lowers = text.lower()
                no_punctuation = lowers.translate(None, string.punctuation)
                token_dict[f] = no_punctuation
    j = j + i

print("\n %s files loaded in %s" % (j, (datetime.datetime.now() - t0)))
###########################################################################
#**************
#**************
true_k = 20 # *
#**************
#**************

#english_stemmer = nltk.stem.SnowballStemmer('english')
#class StemmedTfidfVectorizer(TfidfVectorizer):
#    def build_analyzer(self):
#        analyzer = super(TfidfVectorizer, self).build_analyzer()
#        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

#vectorizer = StemmedTfidfVectorizer(min_df=1, max_df=0.5, stop_words='english', decode_error='ignore')

print("Extracting features from the training dataset using a sparse vectorizer")
t0 = datetime.datetime.now()
if opts.use_hashing:
    if opts.use_idf:
        print("\n Hashing version")
        # Perform an IDF normalization on the output of HashingVectorizer
        hasher = HashingVectorizer(tokenizer=tokenize, encoding='latin-1', 
                                   n_features=opts.n_features,
                                   stop_words='english', non_negative=True,
                                   norm=None, binary=False)
        vectorizer = make_pipeline(hasher, TfidfTransformer())
    else:
        print("\n Hashing version normalized")
        vectorizer = HashingVectorizer(tokenizer=tokenize, encoding='latin-1', 
                                       n_features=opts.n_features,
                                       stop_words='english',
                                       non_negative=False, norm='l2',
                                       binary=False)
else:
    print("\n Performing stemming and tokenization...")
    vectorizer = TfidfVectorizer(tokenizer=tokenize, encoding='latin-1', 
                                 max_df=0.5, max_features=opts.n_features,
                                 min_df=2, stop_words='english',
                                 use_idf=opts.use_idf)

#this can take some time
X = vectorizer.fit_transform(token_dict.values())

print("done in %s" % (datetime.datetime.now() - t0))
print("n_samples: %d, n_features: %d" % X.shape)
print()

if opts.n_components:
    print("Performing dimensionality reduction using LSA")
    t0 = datetime.datetime.now()

    # Vectorizer results are normalized, which makes KMeans behave as
    # spherical k-means for better results. Since LSA/SVD results are
    # not normalized, we have to redo the normalization.
    svd = TruncatedSVD(opts.n_components)
    lsa = make_pipeline(svd, Normalizer(copy=False))

    X = lsa.fit_transform(X)

    print("\n done in %s" % (datetime.datetime.now() - t0))

    explained_variance = svd.explained_variance_ratio_.sum()
    print("Explained variance of the SVD step: {}%".format(
        int(explained_variance * 100)))

    print()

###############################################################################
# Do the actual clustering

if opts.minibatch:
    km = MiniBatchKMeans(n_clusters=true_k, init='k-means++', n_init=1,
                         init_size=1000, batch_size=1000, verbose=opts.verbose)
else:
    km = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1, verbose=opts.verbose)

print("Clustering sparse data with %s" % km)
t0 = datetime.datetime.now()

km.fit(X)
print("done in %s" % (datetime.datetime.now() - t0))
print()

#print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels, km.labels_))
#print("Completeness: %0.3f" % metrics.completeness_score(labels, km.labels_))
#print("V-measure: %0.3f" % metrics.v_measure_score(labels, km.labels_))
#print("Adjusted Rand-Index: %.3f"
#      % metrics.adjusted_rand_score(labels, km.labels_))
#print("Silhouette Coefficient: %0.3f"
#      % metrics.silhouette_score(X, labels, sample_size=1000))
print("Silhouette Coefficient: %0.3f \n"
      % metrics.silhouette_score(X, km.labels_ , sample_size=10000))
#
#print()

if not (opts.n_components or opts.use_hashing):
    print("Top terms per cluster:")
    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    id_cluster = collections.defaultdict(list)

    for i in range(true_k):
        print("Cluster %d:" % i, end='')
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind], end='')
        print()

    for idx, lbl in enumerate(km.labels_):
        id_cluster[lbl].append(idx)
    print("\nDocs per cluster:")
    for k,v in id_cluster.items():
        print ('Cluster %d:' % k, v)
        
#    print("\nList of documents in the corpus:")
#    j = 0
#    for k,v in (token_dict.items()):
#        print (j,path+k)
#        j += 1        

print("\n done in %s" % (datetime.datetime.now() - t0))

###################################################################

#### Graphics examples
#from matplotlib import pyplot
#import numpy as np
#
#labels = km.labels_
#centroids = km.cluster_centers_
#
#for i in range(true_k):
#    # select only data observations with cluster label == i
#    ds = X[np.where(labels==i)]
#    # plot the data observations
#    pyplot.plot(ds[:,0],ds[:,1],'o')
#    # plot the centroids
#    lines = pyplot.plot(centroids[i,0],centroids[i,1],'kx')
#    # make the centroid x's bigger
#    pyplot.setp(lines,ms=15.0)
#    pyplot.setp(lines,mew=2.0)
#pyplot.show()
#
#from sklearn.decomposition import PCA
#import pylab as pl
# 
#tt = vectorizer.fit_transform(dataset.data[:2000]).toarray()
#pca = PCA(n_components=2).fit(tt)
#pca_2d = pca.transform(tt)
#pl.figure('Reference Plot')
#pl.scatter(pca_2d[:, 0], pca_2d[:, 1], c=tt)
#pl.scatter(pca_2d[:, 0], pca_2d[:, 1], c=tt)
#pl.figure('K-means with 4 clusters')
#pl.scatter(pca_2d[:, 0], pca_2d[:, 1], c=km.labels_)
#pl.show()

#print("\n End of processing in %s" % (datetime.datetime.now() - time1))
##print (token_dict[f]), '*'*50
#print (type(token_dict))
#print (len(token_dict))
#for k,v in token_dict.items():
#    print ('#'*20)
#    print (k, '====>', v)
print("\n End of process in %s" % (datetime.datetime.now() - time1))
