#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Extracting the list of terms and its variants
"""
from __future__ import division, print_function
import datetime
import nltk
from nltk.corpus import wordnet as wn
from collections import defaultdict

time1 =datetime.datetime.now()

###############################################################################
#print(wn.synsets('motorcar')) # get possibles synsets
#print(wn.synset('car.n.01').lemma_names()) #get a collections of lemma names
#print(wn.synset('car.n.01').definition()) #get definition 
#print(wn.synset('car.n.01').examples()) #get example of a synset
#print(wn.synset('car.n.01').lemmas()) #get all the lemas for a given synset
#print(wn.lemma('car.n.01.automobile')) #lookup to a particular lemma
#print(wn.lemma('car.n.01.automobile').synset())#get the synset corresponding to a lemma
#print(wn.lemma('car.n.01.automobile').name()) #get the name of the lemma
#print()
# for ambiguous word, get all synsets
#print(wn.synsets('car'))

#for synset in wn.synsets('car'):
#    print(synset.lemma_names())

#print(wn.synsets('dog', pos=wn.VERB))
#print(wn.synset('dog.n.01').definition())
#print(wn.synset('dog.n.01').examples()[0])
#print(wn.synset('dog.n.01').lemmas())
#print([str(lemma.name()) for lemma in wn.synset('dog.n.01').lemmas()])
#print(wn.lemma('dog.n.01.dog').synset())
#
#
#
#
# 
#print(sorted(wn.synset('dog.n.01').lemmas('por'))) # Lemma in portuguese

#print(wn.synsets('article'))


#wordSynset = 'article'
#wordSynset_n = wn.synsets(wordSynset, 'n') #store only 'noun' - 'a','v','r'
#synsetToCompare = 'product.n.04'

#def synset_property(wordSynset, synsetToCompare):
#    for i,synset in enumerate(wn.synsets(wordSynset)):
#        print('Meaning:' + str(i), synset)
#        print('Lemma names: ',synset.lemma_names())
#        print('Definition: ',synset.definition())
#        print('Examples: ',synset.examples())
#        print('Lemmas: ',synset.lemmas())
#        print('Hyponyms: ', synset.hyponyms())
#        print('Hypernyms: ', synset.hypernyms())
#        print('Root Hypernyms: ', synset.root_hypernyms())
#        for n in range(len(synset.hypernym_paths())):
#            print('Path:' + str(n),[synset.name() for synset in synset.hypernym_paths()[n]])
#        print('Lowest common hypernym between "' + wordSynset + '" and "' + synsetToCompare + '": ',
#              synset.lowest_common_hypernyms(wn.synset(synsetToCompare)))
#        print('Common hypernym between "' + wordSynset + '" and "' + synsetToCompare + '": ',
#              synset.common_hypernyms(wn.synset(synsetToCompare)))
#        print('Part meronyms: ', synset.part_meronyms())
#        print('Substance meronyms: ', synset.substance_meronyms())
#        print('Member holonyms: ', synset.member_holonyms())
#        print('Entailments: ', synset.entailments())
#        for n in range(len(synset.lemmas())):
#            print('Antonyms: ', synset.lemmas()[n].antonyms())
#        print()
#term = 'artigo'
def synset_property(wordSynset, synsetToCompare):
    for i,synset in enumerate(wn.synsets(wordSynset.decode('utf-8'), lang='por')):
#        if i<1:
            print('a) Meaning:' + str(i), synset)
            print('a.1) Meaning:' + str(i), synset.lemmas('por'))
            print('b) Lemma names: ',synset.lemma_names('por'))
            print('c) Definition: ',synset.definition())
            print('d) Examples: ',synset.examples())
            print('e) Lemmas: ',synset.lemmas())
            print('f) Hyponyms: ', synset.hyponyms())
#            for h in synset.hyponyms():
#                print(h, '(@EN) --', h.lemma_names('por'), '(@PT)')
            print('f.1) Hyponyms @pt: ', 
                  [pt.lemma_names('por') for pt in synset.hyponyms()])
            print('g) Hypernyms: ', synset.hypernyms())
#            for h in synset.hypernyms():
#                print(h, '(@EN) --', h.lemma_names('por'), '(@PT)')
            print('g.1) Hypernyms @pt: ', 
                  [pt.lemma_names('por') for pt in synset.hypernyms()])
            print('h) Root Hypernyms: ', synset.root_hypernyms())
            print('h.1) Root Hypernyms @pt: ', 
                  [pt.lemma_names('por') for pt in synset.root_hypernyms()])
            print('j) Lowest common hypernym between "' + str(synset.lemma_names('por')) +
            '" and "' + str(wn.synset(synsetToCompare).lemma_names('por')) + '": ',
                  synset.lowest_common_hypernyms(wn.synset(synsetToCompare)))
            print('j.1) Lowest common hypernym between "' + str(synset.lemma_names('por')) + '" and "' + synsetToCompare + '": @pt',
                  [pt.lemma_names('por') for pt in synset.lowest_common_hypernyms(wn.synset(synsetToCompare))])
            print('h) Common hypernym between "' + str(synset.lemma_names('por')) +
            '" and "' + str(wn.synset(synsetToCompare).lemma_names('por')) + '": ',
                  synset.common_hypernyms(wn.synset(synsetToCompare)))
            print('h.1) Common hypernym between "' + str(synset.lemma_names('por')) +
            '" and "' + str(wn.synset(synsetToCompare).lemma_names('por')) + '": @pt',
                  [pt.lemma_names('por') for pt in synset.common_hypernyms(wn.synset(synsetToCompare))])
            print('l) Similarity between "' + str(synset.lemma_names('por')) +
            '" and "' + str(wn.synset(synsetToCompare).lemma_names('por')) + '": ',
                  synset.path_similarity(wn.synset(synsetToCompare)))
            for n in range(len(synset.hypernym_paths())):
                print('i) Path:' + str(n),
                      [synset.name() for synset in synset.hypernym_paths()[n]])
                print('i.1) Path:' + str(n) + ' @pt',
                      [synset.lemma_names('por') for synset in synset.hypernym_paths()[n]])
            for n in range(len(wn.synset(synsetToCompare).hypernym_paths())):
                print('#) Path:' + str(n),
                      [synset.name() for synset in wn.synset(synsetToCompare).hypernym_paths()[n]])
                print('#.1) Path:' + str(n) + ' @pt',
                      [synset.lemma_names('por') for synset in wn.synset(synsetToCompare).hypernym_paths()[n]])
#            print('Part meronyms: ', synset.part_meronyms())
#            print('Substance meronyms: ', synset.substance_meronyms())
#            print('Member holonyms: ', synset.member_holonyms())
#            print('Entailments: ', synset.entailments())
#            for n in range(len(synset.lemmas())):
#                print('Antonyms: ', synset.lemmas()[n].antonyms())
            print()
    return
# print('Similarity between "' + wordSynset + '" and "' + synsetToCompare + '": ',synset.path_similarity(wn.synset(synsetToCompare)))
#wn.synset('dog.n.01').path_similarity(cat)

print(synset_property('crime', 'fraud.n.01'))

# nltk.app.wordnet() starts the default browser to explore the WordNet hierarchy

def wn_pos_dist():
    """Count the Synsets in each WordNet POS category."""
    # One-dimensional count dict with 0 as the default value:
    cats = defaultdict(int)
    # The counting loop:
    for synset in wn.all_synsets():
        cats[synset.pos()] += 1
    # Print the results to the screen:
    for tag, count in cats.items():
         print(tag, count)
    # Total number (sum of the above):
    print('Total', sum(cats.values()))
#print(wn_pos_dist())    


def synset_method_values(synset):
    """
    For a given synset, get all the (method_name, value) pairs
    for that synset. Returns the list of such pairs.
    """
    name_value_pairs = []
    # All the available synset methods:
#    method_names = ['hypernyms()', 'instance_hypernyms()', 'hyponyms()', 'instance_hyponyms()'] 
    method_names = ['hypernyms', 'instance_hypernyms', 'hyponyms', 'instance_hyponyms', 
                    'member_holonyms', 'substance_holonyms', 'part_holonyms', 
                    'member_meronyms', 'substance_meronyms', 'part_meronyms', 
                    'attributes', 'entailments', 'causes', 'also_sees', 'verb_groups',
                    'similar_tos']
    for method_name in method_names:
        # Get the method's value for this synset based on its string name.
#        method = getattr(synset, method_name+'()')
        method = getattr(synset, method_name)
#        print(method)
        vals = method()
#        print(vals)
        name_value_pairs.append((method_name, vals))
#        print(name_value_pairs)
    return name_value_pairs    
#tree = wn.synsets('article', 'n')[0]
#for key, val in synset_method_values(tree):
#    print(key, val)

def synset_methods():
    """
    Iterates through all of the synsets in WordNet.  For each,
    iterate through all the Synset methods, creating a mapping
 
    method_name --> pos --> count
 
    where pos is a WordNet pos and count is the number of Synsets that 
    have non-empty values for method_name.
    """
    # Two-dimensional count dict with 0 as the default value final value:
    d = defaultdict(lambda : defaultdict(int))
    # Iterate through all the synsets using wn.all_synsets():
    for synset in wn.all_synsets():
        for method_name, vals in synset_method_values(synset):
            if vals: # If vals is nonempty:
                d[method_name][synset.pos()] += 1
    return d
#for d in synset_methods():
#    print(d)

#############################################################################
print("\nEnd of process in %s" % (datetime.datetime.now() - time1))