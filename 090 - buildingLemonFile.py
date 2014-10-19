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
  lemon:lingua "pt" ;
  lemon:entrada :risco,  :perigo, :ameaça .
'''
def lexEntry(termCanonic, termVariant, termOnto):
    lexicalEntry = '''
:risco a lemon:EntradaLexical ;
  lemon:formaCanonica [ lemon:RepEscrita "'''+termCanonic+'''"@pt ] ;
  lemon:outraForma [ lemon:RepEscrita "'''+termVariant+'''"@pt ] ;
  lemon:sentido [ lemon:referencia ontology:"'''+termOnto+'''" ] .
    '''
    return lexicalEntry
# :perigo a lemon:EntradaLexical ;
#   lemon:formaCanonica [ lemon:RepEscrita "perigo"@pt ] ;
#   lemon:outraForma [ lemon:RepEscrita "perigos"@pt ] ;
#   lemon:sentido [ lemon:referencia ontology:risco ] .

print prefix + description 
print lexEntry('risco','riscos','risco')
print lexEntry('perigo','perigos','risco')
print lexEntry('ameaça','ameaças','risco')
