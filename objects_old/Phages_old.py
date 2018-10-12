# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:50:55 2017

@author: Stage
"""


import sys
sys.path.insert(0, './SQL_obj_old')
from Phage_sql_old import *
from Bio import SeqIO

from objects_new.Proteins_new import Protein
from objects_new.WholeDNA_new import WholeDNA

from files_treatment.fasta_proteins import *
from files_treatment.fasta_whole_genome import *

class Phage_old(object):
    
    def __init__(self, phage_id = -1, name = "", GI = -1, nb_proteins = -1, 
                 whole_genome = "", dna_code_sequence = "", prot_sequence = ""):
        self.phage_id = phage_id
        self.name = name
        self.GI = GI
        self.nb_proteins = nb_proteins
        self.whole_genome = whole_genome
        self.dna_code_sequence = dna_code_sequence
        self.prot_sequence = prot_sequence
        
        self.number_prots_counted_aa = 0
        self.number_prots_counted_nucleo = 0
        
        
        self.proteins_list = None
        self.whole_genom_obj = None
        
    def get_all_phages(self):
        listOfPhages = []
        sqlObj = Phage_sql_old()
        results = sqlObj.select_all_phages_all_attributes()
        for element in results:
            listOfPhages.append(Phage_old(element[0], element[1], element[2], element[3], element[4], element[5], element[6]))
        return listOfPhages
    
    
    def complete_phage_from_old_DB(self):
        self.get_whole_dna_old_db()
        self.get_proteins_old_db()
        self.get_dna_old_db()
        
        self.get_qty_prots_old_db()
        
        self.complete_proteins_list()
        self.complete_whole_gen()
        

        
    def complete_proteins_list(self):
        prot_fasta_obj = proteins_fasta(self.prot_sequence, self.dna_code_sequence)
        self.proteins_list = prot_fasta_obj.parse_fasta_format()
        
    def complete_whole_gen(self):
        print(self.whole_genome)
        whole_dna_obj = whole_genome_fasta(self.whole_genome)
        self.whole_genom_obj = whole_dna_obj.get_whole_sequence()
     
        
    def get_qty_prots_old_db(self):
        sqlObj = Phage_sql_old()
        self.nb_proteins = sqlObj.get_proteins_qty_prot_by_ID(self.phage_id)
        
        
    def get_whole_dna_old_db(self):
        sqlObj = Phage_sql_old()
        whole_dna_seq = sqlObj.select_whole_genemo_by_ID(self.phage_id)
        whole_dna_seq_value = '>' + whole_dna_seq[0]
        self.write_temp_file(whole_dna_seq_value)
        self.whole_genome = SeqIO.to_dict(SeqIO.parse('/tmp/temp_fasta.fasta', "fasta"))  
     
    def get_proteins_old_db(self):
        sqlObj = Phage_sql_old()
        prot_seq = sqlObj.get_proteins_sequences_by_ID(self.phage_id)
        
        self.number_prots_counted_aa = prot_seq[0].count('>')
        
        self.write_temp_file(prot_seq[0])
        fasta_dict = SeqIO.to_dict(SeqIO.parse('/tmp/temp_fasta.fasta', "fasta"))
        self.prot_sequence = fasta_dict
        
    def get_dna_old_db(self):
        sqlObj = Phage_sql_old()        
        prot_dna_cod_seq = sqlObj.get_proteins_dna_sequences_by_ID(self.phage_id)
        
        self.number_prots_counted_nucleo = prot_dna_cod_seq[0].count('>')
        
        self.write_temp_file(prot_dna_cod_seq[0])
        #fasta_dict = SeqIO.index('/tmp/temp_fasta.fasta', "fasta")
        fasta_dict = SeqIO.to_dict(SeqIO.parse('/tmp/temp_fasta.fasta', "fasta"))
        self.dna_code_sequence = fasta_dict

    def write_temp_file(self, content):
        path_file = '/tmp/temp_fasta.fasta'
        with open(path_file, "w") as out:
            out.write(content)
        out.close()        