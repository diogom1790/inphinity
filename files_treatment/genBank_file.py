# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 10:35:05 2017

@author: Stage
"""

from Bio import GenBank

class gen_bank_parsing_file(object):
    
    def __init__(self, gene_bank_file):
        self.gene_bank_file = gene_bank_file
        self.whole_gen = None
        self.GI = None
        self.Acc = None
        
    def parse_genebank_file(self):
        with open(self.gene_bank_file, "rU") as input_handle:
            for record in GenBank.parse(input_handle):
                #print("Name:  %s, %i" % (record.name, len(record.features)))
                print(record.features)
                print(record.accession)
                print("----")
                print(record.gi)
                print("----")
                self.Acc = record.accession[0]
                
                if self.GI is None or len(self.GI) == 0:
                    self.GI = "NA"
                if self.Acc is None or len(self.Acc) == 0:
                    self.Acc = "NA"