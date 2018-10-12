# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:24:17 2017

@author: Stage
"""


from SQL_obj_old.Bacterium_sql_old import Bacterium_sql_old
from Bio import SeqIO
from objects_new.Proteins_new import Protein
from objects_new.WholeDNA_new import WholeDNA

from files_treatment.fasta_proteins import *
from files_treatment.fasta_whole_genome import *

from files_treatment.csv_files import *

import re
import numpy as np

class Bacteria_old(object):
    def __init__(self, bacterium_id = -1, species = "", strain = "", GI = -1, 
               nb_proteins = -1, whole_genome = "", prot_dna_cod_seq = "", prot_seq = ""):
        self.bacterium_id = bacterium_id
        self.species = species
        self.strain = strain
        self.GI = GI
        self.nb_proteins = nb_proteins

        
        self.proteins_fasta_gen = None
        self.proteins_DNA_fasta_gen = None
        self.dna_whole_genome = None
        
        self.proteins_list = None
        self.whole_genom_obj = None
        
        self.number_prots_counted_nucleo = 0
        self.number_prots_counted_aa = 0

    def get_all_Bacteria(self):
        listOfBacteria = []
        sqlObj = Bacterium_sql_old()
        results = sqlObj.select_all_bacteria_all_attributes()
        for element in results:
            listOfBacteria.append(Bacteria_old(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7]))
        return listOfBacteria
    
    def complete_bacteria_from_old_DB(self):
        self.get_whole_dna_old_db()
        self.get_proteins_old_db()
        self.get_dna_old_db()
        self.get_qty_prots_old_db()
        
        self.complete_proteins_list()
        self.complete_whole_gen()
    
    def complete_proteins_list(self):
        prot_fasta_obj = proteins_fasta(self.proteins_fasta_gen, self.proteins_DNA_fasta_gen)
        self.proteins_list = prot_fasta_obj.parse_fasta_format()
        
    def complete_whole_gen(self):
        whole_dna_obj = whole_genome_fasta(self.dna_whole_genome)
        self.whole_genom_obj = whole_dna_obj.get_whole_sequence()
        
        
    def get_qty_prots_old_db(self):
        sqlObj = Bacterium_sql_old()
        self.nb_proteins = sqlObj.get_proteins_qty_prot_by_GI(self.GI)
        
    def get_proteins_old_db(self):
        sqlObj = Bacterium_sql_old()
        prot_seq = sqlObj.get_proteins_sequences_by_GI(self.GI)
        
        self.number_prots_counted_aa = prot_seq[0].count('>')
        
        self.write_temp_file(prot_seq[0])
        #fasta_dict = SeqIO.index('/tmp/temp_fasta.fasta', "fasta")
        fasta_dict = SeqIO.to_dict(SeqIO.parse('/tmp/temp_fasta.fasta', "fasta"))
        self.proteins_fasta_gen = fasta_dict
        
        

    def get_dna_old_db(self):
        sqlObj = Bacterium_sql_old()
        prot_dna_cod_seq = sqlObj.get_proteins_dna_sequences_by_GI(self.GI)
        
        self.number_prots_counted_nucleo = prot_dna_cod_seq[0].count('>')
        
        self.write_temp_file(prot_dna_cod_seq[0])
        #fasta_dict = SeqIO.index('/tmp/temp_fasta.fasta', "fasta")
        fasta_dict = SeqIO.to_dict(SeqIO.parse('/tmp/temp_fasta.fasta', "fasta"))
        self.proteins_DNA_fasta_gen = fasta_dict
        
        

    def get_whole_dna_old_db(self):
        sqlObj = Bacterium_sql_old()
        whole_dna_seq = sqlObj.select_whole_genemo_by_GI(self.GI)
        self.write_temp_file(whole_dna_seq[0])
        self.dna_whole_genome = SeqIO.to_dict(SeqIO.parse('/tmp/temp_fasta.fasta', "fasta"))
    
    
    
    def write_temp_file(self, content):
        path_file = '/tmp/temp_fasta.fasta'
        with open(path_file, "w") as out:
            out.write(content)
        out.close()
        
    def write_csv_list_prots(self):
        csv_file_obj = CSV_file((str(self.species) + "_" + str(self.strain) + ".csv") , self.proteins_list)
        csv_file_obj.create_CSV_form_list_obj_fields()
        
    
    
    