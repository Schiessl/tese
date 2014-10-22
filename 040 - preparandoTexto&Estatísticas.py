#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Examples of reading text data and performing clustering K-means for 
portuguese language
"""
from __future__ import unicode_literals, division
import nltk, re, datetime
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer

time1 =datetime.datetime.now()

####### Lembrar que o .DS_store dá problema - para removê-lo 'rm -f .DS_Store'
path = '/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/AlterTxt/testTxt/'
localFile = 'CollectionGloss.txt'
raw = open(path+localFile,'rU').read().decode('utf-16-le')#reading file

# creating stopwords file
stopwords = nltk.corpus.stopwords.words('portuguese')

f = open('stopWordsBr.txt','rU').read()
stp = list(f.split())
for p in stp:
    stopwords.append(p)
print

####### Using NLTK to preprocess the text file   
### reading raw text file ###
# Getting word frequency
#fd = nltk.FreqDist(w for w in words if w not in stopwords)
#print "\n****** The most common words ******"
#for word in fd.most_common()[:50]:
#    print word[0], word[1]
#print
#print type(stopwords), type(f), type(stp), type(words)
#print fd.plot(50,cumulative=True)

#for w in fd.hapaxes()[:5]:#words that happen only once
#    print w
#print fd.tabulate(10)#showing the 10th most frequent words
def freq(text, numWords):
    fd = nltk.FreqDist(w for w in text)
    print 'Total number of terms (tokens): ', fd.N()
    print 'Total number of unique terms (Vocabulary): ',len(set(text))
    print "\n****** The most common terms ******"
    for word in fd.most_common()[:numWords]:
        print word[0], word[1]
    print
    return fd

def printResult(tokens, header):
    t0 = datetime.datetime.now()
    #Printing statistics of the corpus
    print '\n', header
    print("Calculating statistics from the corpus...\n")
    print freq(tokens,5)
    print "done in %s" % (datetime.datetime.now() - t0),'\n'
    return
    

rawTokens = word_tokenize(raw)#tokenizing text raw text

print printResult(rawTokens, 10*'*' + ' Statistics without preprocessing text ' + 10*'*')
##Printing statistics of the corpus
#print 10*'*' + ' Statistics without preprocessing text ' + 10*'*'
#print("Calculating statistics from the corpus...\n")
#t0 = datetime.datetime.now()
#
#print 'Terms: ', len(rawTokens)
#print 'Vocabulary: ', len(rawVocab)
#print 'The most common terms \n', freq(rawTokens,10)
#
#print "\ndone in %s" % (datetime.datetime.now() - t0),'\n'

####################################################################
####### Replacing words, collocations or just correcting them
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text
# put the collocations to be replaced 
reps = {
'Banco Central do Brasil':'Banco_Central_do_Brasil', 
'instituições financeiras':'instituições_financeiras',
'valores mobiliários':'valores_mobiliários',
'Tesouro Nacional':'Tesouro_Nacional',
'renda fixa':'renda_fixa',
'Patrimônio Líquido':'Patrimônio_Líquido',
'Sistema Financeiro':'Sistema_Financeiro',
'moeda estrangeira':'moeda_estrangeira',
'saldo devedor':'saldo_devedor',
'cheque especial':'cheque_especial',
'pessoas físicas':'pessoas_físicas',
'pessoa física':'pessoa_física',
'Banco Central':'Banco_Central',
'Sistema_Financeiro Nacional':'Sistema_Financeiro_Nacional',
'títulos públicos':'títulos_públicos',
'São Paulo':'São_Paulo',
'bancos centrais':'bancos_centrais',
'risco operacional':'risco_operacional',
'arrendamento mercantil':'arrendamento_mercantil',
'instituição financeira':'instituição_financeira',
'títulos_públicos federais':'títulos_públicos_federais',
'bancos comerciais':'bancos_comerciais',
'instituição financeira':'instituição_financeira',
'Setor Público':'Setor_Público',
'sociedade anônima':'sociedade_anônima',
'Valores Mobiliários':'Valores_Mobiliários',
'tarifa bancária':'tarifa_bancária',
'instrumentos financeiros':'instrumentos_financeiros',
'salários mínimos':'salários_mínimos',
'Sistema_Financeiro Nacional':'Sistema_Financeiro_Nacional',
'mercado financeiro':'mercado_financeiro',
'Ativo Permanente':'Ativo_Permanente',
'VALUE AT RISK':'Value_at_Risk',
'Value at Risk':'Value_at_Risk'
}
# bind the returned text of the method to a variable txt
#txt = replace_all(raw, reps)
##print txt   
#text = nltk.Text(rawTokens) #transform to Text for using many more functions
##print '\nCollocations: ', text.collocations()
##print '\nBigrams: ', [bg for bg in nltk.bigrams(text)][:5]
##print '\nTrigrams: ', [tg for tg in nltk.trigrams(text)][:5]
##print '\n',[w for w in text if w.isalpha() ][:20]#only characteres 

####################################################################
txt = replace_all(raw, reps)
cTokens = word_tokenize(txt)#tokenizing preprocessed text
print printResult(cTokens, 10*'*' + ' Statistics without collocations in the text ' + 10*'*')

####################################################################
lTokens = [w.lower() for w in cTokens]#lower case to every token
print printResult(lTokens, 10*'*' + ' Statistics with lower case ' + 10*'*')

####################################################################
stpWords = [w for w in lTokens if w not in stopwords and not w.isdigit()]
print printResult(stpWords, 10*'*' + ' Statistics without stopwords ' + 10*'*')

# printing file which represents the best collection of words   
#with open("stpwFinalGroup.txt", "w") as myfile:
#    for w in stpWords:
##        print w
#        myfile.write(w)
#        myfile.write('\n')

###################################################################
pt_SnowBall_stemmer = nltk.stem.SnowballStemmer('portuguese')
stpWordsStemm = [pt_SnowBall_stemmer.stem(w) for w in stpWords]
print printResult(stpWordsStemm, 10*'*' + ' Statistics with Snowball stemmer ' + 10*'*')

####################################################################
pt_RSLPS_stemmer = nltk.stem.RSLPStemmer()
stpWordsStemm = [pt_RSLPS_stemmer.stem(w) for w in stpWords]
print printResult(stpWordsStemm, 10*'*' + ' Statistics with RSLPS stemmer ' + 10*'*')

####################################################################

print("\nEnd of process in %s" % (datetime.datetime.now() - time1))
