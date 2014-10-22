#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Printing the output file in RDF - lemon standard
"""
prefix = '''
@base <http://www.example.org/lexico> .
@prefix lemon: <http://lemon-model.net/lemon#> .
@prefix :<http://www.exemplo.org/> .
@prefix ontology:<http://www.exemplo.org/ontology#> .
'''
description = '''
:meuLexico a lemon:Lexico;
  lemon:language "pt" ;
  lemon:entrada :risco,  :perigo, :ameaça .
'''
def lexEntry(termCanonic, termVariant, termOnto):
    lexicalEntry = '''
:risco a lemon:LexicalEntry ;
  lemon:canonicalForm [ lemon:writtenRep "'''+termCanonic+'''"@pt ] ;
  lemon:otherForm [ lemon:writtenRep "'''+termVariant+'''"@pt ] ;
  lemon:sense [ lemon:referencia ontology:"'''+termOnto+'''" ] .
    '''
    return lexicalEntry
# :perigo a lemon:EntradaLexical ;
#   lemon:canonicalForm [ lemon:writtenRep "perigo"@pt ] ;
#   lemon:otherForm [ lemon:writtenRep "perigos"@pt ] ;
#   lemon:sense [ lemon:referencia ontology:risco ] .

print prefix + description 
print lexEntry('risco','riscos','risco')
print lexEntry('perigo','perigos','risco')
print lexEntry('ameaça','ameaças','risco')

'''Exemplo do site http://lemon-model.net/lexica/uby/ow_eng/OW_eng_LexicalEntry_14548.ttl

@base <http://lemon-model.net/lexica/uby/ow_eng/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix lemon: <../../../lemon#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix lexinfo2: <http://www.lexinfo.net/ontology/2.0/lexinfo#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix lexinfo: <http://lexinfo.net/ontology/2.0/lexinfo#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix uby: <http://purl.org/olia/ubyCat.owl#> .
@prefix ubywn: <../wn/> .
@prefix ubyfn: <../fn/> .
@prefix ubyvn: <../vn/> .
@prefix ubyow_eng: <> .
@prefix ubyow_deu: <../ow_deu/> .
@prefix ubywktDE: <../wktDE/> .

<>
    dcterms:license <http://creativecommons.org/licenses/by-sa/3.0/> ;
    dcterms:source <http://www.omegawiki.org> .

ubyow_eng:OW_eng_LexicalEntry_14548
    lemon:canonicalForm <OW_eng_LexicalEntry_14548#CanonicalForm> ;
    lemon:sense ubyow_eng:OW_eng_Sense_16190 ;
    a lemon:LexicalEntry .

<OW_eng_LexicalEntry_14548#CanonicalForm>
    lemon:writtenRep "risk"@eng ;
    a lemon:Form .'''