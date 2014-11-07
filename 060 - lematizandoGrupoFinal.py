#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Reading two files, one with current words from texts and a dictionary with
term, parent, and category. Parent has the canonical form and category has the
syntactical function of the terms.
It is also possible to correct words manually to a preferred entry by using the
second function.
"""
import datetime

time1 =datetime.datetime.now()

###############################################################################
###############################################################################
# only alter variables here
path = '/Users/marceloschiessl/RDF_text_project/corpus/dic_sas_pt/'
typeVar = 'stpwFinalGroup' 
input_file1 = 'stpwFinalGroup.txt'
input_file2 = 'dicflexunitbr.txt'#{dicionario.txt dicflexunitbr.txt }
output_file = 'std_'+typeVar+'.txt'
########## Atenção: lembrar de tratar os duplicados na fonte #################

def compareWords(f1, f2):
    '''Comparing words from the chosen cluster and the dictionary to normalize 
    words to their lemmas, like plurals to singular, verbs to inflected forms.
    A text file is created with the new contents.
    '''
    #Printing results and creating txt file

    to_file = open(output_file, 'w') #opening the file to write
    with open(f1, "rU")as f1, open(path+f2, "rU") as f2:
        # creating file into dict improves performance
        words_dict = {k:v for k, v, _ in (line.split(',') for line in f2)} 
        for i,word in enumerate(f1):
            word = word.rstrip()
            if word in words_dict:
    #            print i, word, words_dict[word]
                print>>to_file, words_dict[word]
            else:
                print>>to_file, word
                
    to_file.close() #closing the file
    return

#compareWords(input_file1, input_file2)

# fixing detected strage words to a regular form
def replaceTerm(oldWord, newWord, fileToEdit):
    '''Fixing words which were wrongly transformed by the comparedWords() 
    function.
    '''
    f = open(fileToEdit, "rU")
    filedata = f.read()
    f.close()
    
    #for w in filedata:
    newdata = filedata.replace(oldWord, newWord)
    
    f = open(fileToEdit,'w')
    f.write(newdata)
    f.close()
    return
    
# type pair of words to change into the file
termToReplace = [('receitar','receita'),
                 ('garantir','garantia'),
                 ('empresar','empresa'),
                 ('taxar','taxa'),
                 ('mercar','mercado'),
                 ('resultar','resultado'),
                 ('valorar','valor'),
                 ('despesar','despesa'),
                 ('contar','conta'),
                 ('reservar','reserva')]

for i,t in enumerate(termToReplace): #loop to call the function to replace
    replaceTerm(t[0],t[1], output_file)
    print i, t[0], t[1]

print("\nEnd of process in %s" % (datetime.datetime.now() - time1))