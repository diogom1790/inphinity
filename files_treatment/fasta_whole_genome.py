# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:46:16 2017

@author: Stage
"""

from objects_new.WholeDNA_new import *

class Fasta_whole_genome(object):
    
    def __init__(self, fasta_content_wg):
        self.fasta_content_wg = fasta_content_wg
        self.whole_gen = None
        
    def get_whole_sequence(self):  
        whole_dna_obj = WholeDNA()
        key_whole_gen = None
        for element in self.fasta_content_wg:
            key_whole_gen = element
        whole_dna_obj.head = self.fasta_content_wg[key_whole_gen].description
        whole_dna_obj.sequence = self.fasta_content_wg[key_whole_gen].seq
        whole_dna_obj.head_id = key_whole_gen.split('.')[0]
        
        return whole_dna_obj
    
        
