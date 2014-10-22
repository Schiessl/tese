#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Retrieving synonyms from Wiktionary - Dbnary.
It uses label of classes and properties extracted from the financial risk management ontology
in portuguese. It reads a file containing words and search for synonyms,
pos and definitions.
"""
from __future__ import division
import datetime, nltk
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import cross_validation
import sklearn.datasets

time1 = datetime.datetime.now()

######## Reading text files
rootPath =r"/Users/marceloschiessl/RDF_text_project/corpus/20news-18828/"
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']

twenty_train = sklearn.datasets.load_files(rootPath, description='train', categories=categories, shuffle=True, random_state=42, encoding=None)
 
print twenty_train.target_names #print the list of the folders
print len(twenty_train.data), len(twenty_train.filenames) #both .data or .filenames can be used
print("\n".join(twenty_train.data[0].split("\n")[:3]))# printing the first lines of the first loaded file
print(twenty_train.target_names[twenty_train.target[0]])# printing the target name of the first loaded file
 
print twenty_train.target[:10] # printing the index folder of the document
for t in twenty_train.target[:10]:  # printing the name folder of the document
    print(twenty_train.target_names[t])

######## Transforming text into vector
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer(decode_error='ignore') #tokenizing
X_train_counts = count_vect.fit_transform(twenty_train.data) #creating a Dictionary of feature indices
print '\n Counting files and features \n', X_train_counts.shape #quantity of files and features
  
print '\n', count_vect.vocabulary_.get(u'algorithm') # printing frequency of a specific word
 
######## tf-idf representation
from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
print '\n Term frequency (tf): \n', X_train_tf.shape
 
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print '\n Term frequency - inverse document frequency (tf-idf): \n', X_train_tfidf.shape






# groups = ['comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.ma c.hardware', 'comp.windows.x', 'sci.space']
# # groups = ['comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware']
# txtData = sklearn.datasets.load_files(rootPath, categories=groups, encoding=None )
# print len(txtData.filenames)

# def splitTrainTestModel(percTrain, corpus):
#     size = int(len(corpus))
#     sizeTrain = round(percTrain*int(len(corpus)),0)
#     sizeTest = size - sizeTrain
#     print 'Corpus: ', size
# 
#     print 'Training set: ', sizeTrain, round(sizeTrain/size*100),'%'
#     print 'Testing set: ', sizeTest, round(sizeTest/size*100), '%'
#     train_set = corpus[:sizeTrain]
#     test_set = corpus[sizeTest:]
#     ### Creating physical file
# #     print>>to_file, test_set   #creating physical file
#     return train_set, test_set, corpus
# # splitTrainTestModel(.60, txtData.filenames)
# 
# english_stemmer = nltk.stem.SnowballStemmer('english')
# class StemmedTfidfVectorizer(TfidfVectorizer):
#     def build_analyzer(self):
#         analyzer = super(TfidfVectorizer, self).build_analyzer()
#         return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))
# 
# vectorizer = StemmedTfidfVectorizer(min_df=1, max_df=0.5, stop_words='english', decode_error='ignore')
# 
# # vectorized = vectorizer.fit_transform(dataset.data)   
# vectorized = vectorizer.fit_transform(txtData.filenames)   
# num_samples, num_features = vectorized.shape
# print("#samples: %d, #features: %d" % (num_samples, num_features))
# 
# num_clusters = 3
# from sklearn.cluster import KMeans
# km = KMeans(n_clusters=num_clusters, init='random', n_init=1,verbose=1)
# km.fit(vectorized)
# print 'labels: ', km.labels_
# print km.labels_.shape
# print 'centroids: ', km.cluster_centers_



time2 = datetime.datetime.now()
print
print time2 - time1

# from sklearn.decomposition import PCA
# from sklearn.cluster import KMeans
# from sklearn.datasets import load_iris
# import pylab as pl
# 
# tt = vectorizer.fit_transform(txtData.filenames).toarray()
# 
# # iris = load_iris()
# # pca = PCA(n_components=2).fit(iris.data)
# pca = PCA(n_components=2).fit(tt)
# # # pca_2d = pca.transform(iris.data)
# pca_2d = pca.transform(tt)
# pl.figure('Reference Plot')
# pl.scatter(pca_2d[:, 0], pca_2d[:, 1], c=tt)
# kmeans = KMeans(n_clusters=3, random_state=111)
# kmeans.fit(tt)
# pl.figure('K-means with 3 clusters')
# pl.scatter(pca_2d[:, 0], pca_2d[:, 1], c=kmeans.labels_)
# pl.show()