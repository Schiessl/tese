#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Examples of reading text data and performing clustering K-means for 
portuguese language
"""
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import PlaintextCorpusReader

####### Lembrar que o .DS_store dá problema - para removê-lo 'rm -f .DS_Store'
path = '/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/AlterTxt/testTxt/'
#path = "/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/test/"
#path = '/Users/marceloschiessl/RDF_text_project/corpus/dadosPT'
localFile = 'CollectionGloss.txt'

# creating stopwords file
stopwords = nltk.corpus.stopwords.words('portuguese')
#stpw = list([',',  '.', ':', 'é','também',')','(', "''", ';','-','é',
#    'ser','–','%','mn','cr','http'])
#
#import codecs
#outputFile = codecs.open("stopWordBr.txt", "wb")
##, "utf-16-le")
#for w in stpw:
#    outputFile.write(w)
#    outputFile.write('\n')
#    print w
#print
#outputFile.close()

#outputFile.writelines(stpw)
#
#for p in stpw:
#    stopwords.append(p)
#f = open('stopListBr.txt','rU').read()
f = open('stopWordsBr.txt','rU').read()
#.decode('utf-16-le')#little endian
stp = list(f.split())
for p in stp:
    stopwords.append(p)
#    print p
print

#stopwords.append(stp)
#print f, type(f)
#print stopwords
#print '*************************'
#f = open(path+localFile,'rU')
#print 'f: ', type(f)
#
#ex = f.read().decode('utf-16-le')#little endian
#print 'ex: ', type(ex)
#
#wrd = ex.split()
#print 'wrd: ', type(wrd)
#
#print 'wrd: ', len(ex), len(wrd)
#print wrd[1000:1050]
#
##fd = nltk.FreqDist(w.lower() for w in wordlists.words() if w not in stopwords)
#fd = nltk.FreqDist(w.lower() for w in wrd)
#for word in list(fd.keys())[:10]:
##    print(word, fd[word])
#    print word, fd[word]

####### Using NLTK to preprocess the text file   
# reading text file
raw = open(path+localFile,'rU').read().decode('utf-16-le')
#print 'raw: ', type(raw)
###################################################################
###### Replacing words, collocations or just correcting them
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
'Ativo Permanente':'Ativo_Permanente'
}
 
# bind the returned text of the method to a variable txt
txt = replace_all(raw, reps)
#print txt   
###################################################################

tokens = word_tokenize(txt)
#tokenizer = RegexpTokenizer(r'\w+')#transform words like também into tambe, which is wrong
#tokens = tokenizer.tokenize(raw)
#print 'tokens: ', type(tokens)

text = nltk.Text(tokens) #transform to Text for using many more functions
print '\nCollocations: ', text.collocations()
#print '\nBigrams: ', [bg for bg in nltk.bigrams(text)][:5]
#print '\nTrigrams: ', [tg for tg in nltk.trigrams(text)][:5]

#print '\n',[w for w in text if w.isalpha() ][:20]#only characteres 

words = [w.lower() for w in tokens]
#print 'words: ', type(words) 
#print words[1000:1050]

vocab = sorted(set(words))
#print 'vocab: ', (vocab)

from nltk.stem import SnowballStemmer
pt_SnowBall_stemmer = SnowballStemmer('portuguese')
pt_RSLPS_stemmer = nltk.stem.RSLPStemmer()
print 'Snowball: ',pt_stemmer.stem('valores mobiliários')
print 'RSLPS: ', pt_RSLPS_stemmer.stem('valores mobiliários')

#wd = (stemmer.stem(w.lower()) for w in words if w not in stopwords)
#print type(wd)

# Getting word frequency
#fd = nltk.FreqDist(w for w in words if w not in stopwords)
#print "\n****** The most common words ******"
#for word in fd.most_common()[:50]:
#    print word[0], word[1]
print
#print type(stopwords), type(f), type(stp), type(words)
#print fd.plot(50,cumulative=True)

#for w in fd.hapaxes()[:5]:#words that happen only once
#    print w
#print fd.tabulate(10)#showing the 10th most frequent words

#print "\n****** Using Regex to tokenize ******"
#text = '''Família-Empresa S.A. dispõe de $12.400 milhões para concorrência. A 
#âncora, desse negócio, é conhecida no coração do Órgão responsável. '''
pattern = r'''(?x)    # set flag to allow verbose regexps
     ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
   | \w+(-\w+)*        # words with optional internal hyphens
   | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
   | \.\.\.            # ellipsis
   | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
   '''
#result = nltk.regexp_tokenize(text, pattern,flags=re.UNICODE) 
#for w in result:
#    print w
#print result

#for w in text.split(): print w #it fails with punctuation
#f.close()
##### Changind file encoding, but it seems not working ############
#with open(path+localFile, 'rb') as source_file:
#  with open(path+localFile+'utf8', 'w+b') as dest_file:
#    contents = source_file.read()
#    dest_file.write(contents.decode('utf-16').encode('utf-8'))
###################################################################
#wordlists = PlaintextCorpusReader(path, '.*', encoding='utf-16-le')#equal to 'latin-'
#wordlists = PlaintextCorpusReader(path, '.*')
#print wordlists.fileids()
#
