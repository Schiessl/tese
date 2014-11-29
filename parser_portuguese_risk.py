# -*- coding: utf-8 -*-
from __future__ import division, print_function

# Floresta Portuguese Corpus
import nltk
from nltk.corpus import floresta
from nltk.corpus import mac_morpho
import datetime

time1 =datetime.datetime.now()

### Grammatical categories (tags) used in the Floresta project ###
'''http://www.linguateca.pt/floresta/BibliaFlorestal/anexo1.html'''
###############################################################################

def performance(cfd, wordlist):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt, 
                                         backoff=nltk.DefaultTagger('H+n')) 
    return baseline_tagger.evaluate(nltk.corpus.floresta.tagged_sents())
    
def display():
    import pylab
    words_by_freq = list(nltk.FreqDist(nltk.corpus.floresta.words())) 
    cfd = nltk.ConditionalFreqDist(nltk.corpus.floresta.tagged_words())
    sizes = 2 ** pylab.arange(15)
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size') 
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()
#display() # show the graph

# simplifying the tag from floresta corpus 
# examples - http://www.nltk.org/howto/portuguese_en.html
def simplify_tag(t):
    '''Returns the simplyfied tag of floresta corpus, for example 
    'h+n' -> 'n'
    '''
    if "+" in t:
        return t[t.index("+")+1:]
    else:
        return t

def corpusChoose(corpus, corpusName):
    '''Returns tagged sentences from the selected corpus
    '''
    time0 =datetime.datetime.now()
    print('\n'+ corpusName + ' corpus selected')
    tagged_sents = corpus.tagged_sents()
    sents = corpus.sents()
    print("\nCorpus selected in %s" % (datetime.datetime.now() - time0))
    return tagged_sents, sents
    
def splitTrainTestModel(sizeTrain, corpus, corpusName):
    time0 =datetime.datetime.now()
    tagged_sents , sents = corpusChoose(corpus, corpusName)
    size = int(len(tagged_sents) * sizeTrain)
    print('Training set: ', size, round(size/int(len(tagged_sents))*100,0),'%')
    print('Testing set: ', int(len(tagged_sents)) - size, round((int(len(tagged_sents)) - size)/int(len(tagged_sents))*100,0),'%')
    train_sents = tagged_sents[:size]
    test_sents = tagged_sents[size:]
    print("\nCorpus splitted in %s" % (datetime.datetime.now() - time0))
    return train_sents, test_sents, corpus

def evaluateModel(train_sents, test_sents, corpus, ngramModel):
    '''Returns a text parsed according to the model
    '''
    time0 =datetime.datetime.now()
#    train_sents, test_sents, corpus = modelProp
    if ngramModel not in ['unigram', 'bigram', 'trigram', 'default']:
        return 'You should type unigram, bigram, trigram or default to run'
    elif  ngramModel == 'unigram':
        print('\nPerforming ' + ngramModel + ' tagging...\n')
        t0 = nltk.DefaultTagger('H+n')
        taggedModel = nltk.UnigramTagger(train_sents, backoff=t0)
        print('Taggers performance - '+ngramModel+': ', 
              taggedModel.evaluate(test_sents),'\n')
        print("\n" + ngramModel + " tagging performed  in %s" % (datetime.datetime.now() - time0))
        return taggedModel
    elif ngramModel == 'bigram':
        print('\nPerforming ' + ngramModel + ' tagging...\n')
        t0 = nltk.DefaultTagger('H+n')
        t1 = nltk.BigramTagger(train_sents, backoff=t0)
        taggedModel = nltk.BigramTagger(train_sents, backoff=t1) 
        print('Taggers performance - '+ngramModel+': ', 
              taggedModel.evaluate(test_sents),'\n')
        print("\n" + ngramModel + " tagging performed  in %s" % (datetime.datetime.now() - time0))
        return taggedModel
    elif ngramModel == 'trigram':
        print('\nPerforming ' + ngramModel + ' tagging...\n')
        t0 = nltk.DefaultTagger('H+n')
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        t2 = nltk.BigramTagger(train_sents, backoff=t1) 
        taggedModel = nltk.TrigramTagger(train_sents, backoff=t2) 
        print('Taggers performance - '+ngramModel+': ', 
              taggedModel.evaluate(test_sents),'\n')
        print("\n" + ngramModel + " tagging performed  in %s" % (datetime.datetime.now() - time0))
        return taggedModel
    else:
        print('\nPerforming ' + 'Default' + ' tagging...\n')
        taggedModel = nltk.DefaultTagger('H+n')
        print('Taggers performance - '+ ngramModel + ': ',
              taggedModel.evaluate(test_sents),'\n')
        print("\n" + ngramModel + " tagging performed  in %s" % (datetime.datetime.now() - time0))
        return taggedModel

#############################################################################
if __name__ == '__main__':

    ngramModelType = 'trigram' # choose one of these 'default, unigram, bigram or trigram'
    propSplit = 0.9 # define the train corpus size
    corpusName = 'Floresta'  # choose one of these 'floresta' or 'mac_morpho'
    corpus = floresta  # choose one of these 'floresta' or 'mac_morpho'

    # text to be tagged
    text = '''Agora que nós treinamos um rotulador em algum
    dado de treinamento, temos que ter o cuidado de não testá-lo no mesmo dado,
    como fizemos no exemplo anterior. Um etiquetador que simplesmente memorizou
    os dados de treinamento e não tentou construir um modelo generalizado, 
    obteria scores perfeitos, mas seria inútil para etiquetar novos textos.'''
    text = '''João não gosta de limão,nem de mortadela com pão. Ele prefere
    um bom vinho e uma boa música.'''
    words = nltk.word_tokenize(text)

#    twords = evaluateModel2(
#                        splitTrainTestModel(propSplit, corpus, corpusName),
#                        ngramModelType, words)

    train_sents, test_sents, corpus = splitTrainTestModel(propSplit, corpus, corpusName)
    tModel = evaluateModel(train_sents, test_sents, corpus, ngramModelType)
    twords = tModel.tag(words)    

#    for raw_text in risco.fileids()[1:20]:
#        print('...Analising ' + raw_text)
#        words = word_tokenize(risco.raw(raw_text))
#        twords = tModel.tag(words)
#        twords = [(w, simplify_tag(t)) for (w,t) in twords]
#        print(' '.join(word + '[' + tag  + ']' for (word, tag) in twords))
    
    twords = [(w, simplify_tag(t)) for (w,t) in twords] #nice printing when using floresta corpus
    print('\n' + ' '.join(word + '[' + tag  + ']' for (word, tag) in twords))

    print("\nEnd of process in %s" % (datetime.datetime.now() - time1))