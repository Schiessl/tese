# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 11:06:40 2014
Transform pdf files into txt files in the same folder
@author: marceloschiessl
"""
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import datetime

time1 =datetime.datetime.now()

def convert_pdf_to_txt(path, outtype='txt'):
    t0 = datetime.datetime.now()
    print("\n Converting %s ..." % path)
    outfile = path[:-3] + outtype
    rsrcmgr = PDFResourceManager()
    codec = 'utf-8'
    laparams = LAParams()
    if outfile:
        outfp = file(outfile, 'w')
    else:
        outfp = sys.stdout
    device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    outfp.close()
    print("\n %s converted in %s" % (path, (datetime.datetime.now() - t0)))
    return
#convert_pdf_to_txt('/Users/marceloschiessl/RDF_text_project/corpus/temp/CR741001.pdf')

import os
os.chdir("/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/test")
path = "/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/test"
#pathOut = "/Users/marceloschiessl/RDF_text_project/corpus/WikiRisk/test"
files = os.listdir(path)
for f in files:
    if f != '.DS_Store':
        convert_pdf_to_txt(f)

print("\n End of process in %s" % (datetime.datetime.now() - time1))
