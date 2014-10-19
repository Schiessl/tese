#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Examples of reading texts files and classifying them
"""
from __future__ import division
import datetime
import sklearn.datasets

time1 = datetime.datetime.now()

######## Reading text files
rootPath =r"/Users/marceloschiessl/RDF_text_project/corpus/20news-18828/"
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']

#twenty_train = sklearn.datasets.load_files(rootPath, description='train', categories=categories, shuffle=True, random_state=42, encoding=None)
twenty_train = sklearn.datasets.load_files(rootPath, description='train', categories=categories, shuffle=True, random_state=42, encoding='Latin-1')
 
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

######## Training a classifier
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target) # naive bayes for word counts

docs_new = ['God is love', 'OpenGL on the GPU is fast'] # docs to be classified
#Using the same transformations for the new docs
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
    print('\n %r => %s' % (doc, twenty_train.target_names[category]))

######## Building a pipeline to make easier the classification process
from sklearn.pipeline import Pipeline
text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB()),])

text_clf = text_clf.fit(twenty_train.data, twenty_train.target) #not working

######## Evaluation
import numpy as np
#twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)
#twenty_test = sklearn.datasets.load_files(rootPath, description='test', categories=categories, shuffle=True, random_state=42, encoding=None)
twenty_test = sklearn.datasets.load_files(rootPath, description='test', categories=categories, shuffle=True, random_state=77, encoding='Latin-1')

docs_test = twenty_test.data
###### This following group replace the next line 'predicted = text_clf.predict(docs_test)'
#X_test_counts = count_vect.transform(docs_test)
#X_test_tfidf = tfidf_transformer.transform(X_test_counts)
#predicted = clf.predict(X_test_tfidf)
##########################################
predicted = text_clf.predict(docs_test) # it worked only changing the encoding to 'Latin-1'

print '\n', np.mean(predicted == twenty_test.target) 

from sklearn import metrics
print(metrics.classification_report(twenty_test.target, predicted,target_names=twenty_test.target_names))

print metrics.confusion_matrix(twenty_test.target, predicted)

####### Parameter tuning using grid search
from sklearn.grid_search import GridSearchCV
#We try out all classifiers on either words or bigrams, with or without idf, and with a penalty parameter of either 0.01 or 0.001 for the linear SVM
parameters = {'vect__ngram_range': [(1, 1), (1, 2)],'tfidf__use_idf': (True, False),'clf__alpha': (1e-2, 1e-3),}
#this parameter a value of -1, grid search will detect how many cores are installed and uses them all
gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)

gs_clf = gs_clf.fit(twenty_train.data[:400], twenty_train.target[:400])#just working with a smaller subset to speed up tests

print '\n', twenty_train.target_names[gs_clf.predict(['God is love'])],'\n' #finding best classification

best_parameters, score, _ = max(gs_clf.grid_scores_, key=lambda x: x[1]) #finding best parameters automatically

for param_name in sorted(parameters.keys()):
    print("%s: %r" % (param_name, best_parameters[param_name]))