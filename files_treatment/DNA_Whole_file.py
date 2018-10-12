# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 10:30:15 2017

@author: Stage
"""

from objects_old.Bacteria_old import *
from files_treatment.download_files import Download_file
from Bio import SeqIO
from objects_new.WholeDNA_new import *

class DNA_Whole_genome(object):
    def __init__(self, id_bact):
        self.id_bact = id_bact
        self.file_fasta = None
        self.obj_Whole_Genome = WholeDNA()
        
    def get_whole_sequence(self):
        self.getFasta_seq_whole_genome()
        key_whole_gen = ""
        for element in self.file_fasta:
            key_whole_gen = element
        self.obj_Whole_Genome.head = self.file_fasta[key_whole_gen].description
        self.obj_Whole_Genome.sequence = self.file_fasta[key_whole_gen].seq
        self.obj_Whole_Genome.head_id = key_whole_gen.split('.')[0]
        
        
        
    def getFasta_seq_whole_genome(self):  
        dict_url_values = {}
        dict_url_values["db"] = "Nucleotide"
        dict_url_values["id"] = self.id_bact
        dict_url_values["rettype"] = "fasta"
        dict_url_values["retmode"] = "text"
        objFildD = Download_file("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi", dict_url_values)
        self.file_fasta = objFildD.request_fasta_file()
        
  
        
        