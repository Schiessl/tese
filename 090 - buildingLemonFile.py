#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Printing the output file in ttl (turtle) - lemon standard
"""
import csv
import datetime
time1 =datetime.datetime.now()

prefix = '''
@base <http://www.example.org/lexico> .
@prefix lemon: <http://lemon-model.net/lemon#> .
@prefix :<http://www.exemplo.org/> .
@prefix ontology:<http://www.semanticweb.org/ontologies/2014/8/risk_management#> .
@prefix lexinfo: <http://www.lexinfo.net/ontology/2.0/lexinfo#> . 
'''
#description = '''
#:meuLexico a lemon:Lexico;
#  lemon:language "pt" ;
#  lemon:LexicalEntry :risco,  :perigo .
#'''
def lexEntry(termCanonic, termOnto):
    description = '''
:riscoFinanceiro a lemon:Lexicon;
  lemon:language "pt" ;
  lemon:entry :'''+termCanonic.replace(' ', '_')+''' .
'''
    lexicalEntry = '''
:'''+termCanonic.replace(' ', '_')+''' a lemon:LexicalEntry ;
    lexinfo:partOfSpeech lexinfo:noun ;
    lemon:canonicalForm [ lemon:writtenRep "'''+termCanonic+'''"@pt ] ;
    lemon:sense [ lemon:reference ontology:'''+termOnto.replace(' ', '_')+''' ] .
    '''

    return description + lexicalEntry
# :perigo a lemon:EntradaLexical ;
#   lemon:canonicalForm [ lemon:writtenRep "perigo"@pt ] ;
#   lemon:otherForm [ lemon:writtenRep "perigos"@pt ] ;
#   lemon:sense [ lemon:referencia ontology:risco ] .

#print prefix  
#print lexEntry('produto','produtos','produto')
#print lexEntry('mercadoria','mercadorias','produto')
##print lexEntry('bem','bens','produto')
##print lexEntry('fruto','frutos','produto')
#print lexEntry('risco','riscos','risco')
#print lexEntry('perigo','perigos','risco')
#

# reading source and printing to file
###############################################################################
###############################################################################
# only alter variables here
input_file = 'sourceToLemon.csv'
output_file = 'lemonFileResult.ttl'
######## Atenção: lembrar de tratar os duplicados na fonte ###############
#Printing results and creating txt file
to_file = open(output_file, 'w') #opening the file to write
print prefix  
print>>to_file,prefix  

with open(input_file, 'rb') as csvfile:
    f = csv.reader(csvfile, delimiter=',', quotechar='|')
    for i,w in enumerate(f):
        if w[0].strip() == '@':
            lexicalEntry = w[1].strip()
#            print i, 'lexicalEntry :', lexicalEntry
            print lexEntry(lexicalEntry,lexicalEntry)
            print>>to_file, lexEntry(lexicalEntry,lexicalEntry)
        else:
            otherForm = w[1].strip()
#            print w[0], 'otherForm :', otherForm
            print lexEntry(otherForm,lexicalEntry)
            print>>to_file, lexEntry(otherForm,lexicalEntry)

to_file.close() #closing the file

print("\nEnd of process in %s" % (datetime.datetime.now() - time1))