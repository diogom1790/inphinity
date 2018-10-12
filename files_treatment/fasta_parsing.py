# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:30:40 2017

@author: Stage
"""
from Bio import SeqIO


class Fasta_parsing(object):
    def __init__(self, path_file):
        self.path_file = path_file
        
    def parse_fasta(self):
        dict_fasta_data = {}
        with open(self.path_file, "rU") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                print(record)
                dict_fasta_data[record.id] = record.seq
        return dict_fasta_data
    
    
    def parse_fasta_all_informations(self):
        dict_fasta_data = {}
        with open(self.path_file, "rU") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                dict_fasta_data[record.id] = record
        return dict_fasta_data