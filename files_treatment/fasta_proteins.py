# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:36:37 2017

@author: Stage
"""

from objects_new.Proteins_new import *
import re

class proteins_fasta(object):
    
    def __init__(self, fasta_content_aa, fasta_content_dna):
        self.fasta_content_aa = fasta_content_aa
        self.fasta_content_dna = fasta_content_dna
        
        
    def parse_fasta_format(self):
        list_keys = []
        list_proteins = []
        errors = 0
        for key, value in self.fasta_content_aa.items():
            list_keys.append(key)
            DNA_string_key = self.get_DNA_description(key)
            
            
            id_protein = -1
            print(key)
            id_prot_DB_online = self.get_protein_id(self.fasta_content_aa[key].description)
            designation = self.get_protein_description(self.fasta_content_aa[key].description)
            sequence_prot = self.fasta_content_aa[key].seq
            try:
                sequence_DNA = self.fasta_content_dna[DNA_string_key].seq
            except KeyError:
                print("KEY ERROR")
                errors += 1
                sequence_DNA = "--"
            start_point, end_point = self.get_protein_location(self.fasta_content_aa[key].description)
            
            protein_obj = Protein(id_protein, id_prot_DB_online, designation, str(sequence_prot), 
                                  str(sequence_DNA), start_point, end_point)
            
            list_proteins.append(protein_obj)
        print("Nb d erreures: " + str(errors))
        return list_proteins
            
        
    def get_protein_id(self, string):
        try:
            protein = re.search('protein_id=[_a-zA-Z0-9\._]+', string)
            protein_match = protein.group(0)
            protein_vec = protein_match.split('=')
            protein_id = protein_vec[1].split('.')
            return protein_id[0]
        except AttributeError:
            return -1

    
    def get_protein_location(self, string):
        try:
            location = re.search('location=[0-9\.]+', string)
            location_match = location.group(0)
            location_vec = location_match.split('=')
            location_se = location_vec[1].split('..')
            location_start = location_se[0]
            location_end = location_se[1]
        except AttributeError:
            return 0, 0
        return location_start, location_end
    
    def get_protein_description(self, string):
        try:
            prot_description = re.search('protein=[\(\)\-\&\%A-Za-z0-9\s]+', string)
            prot_desc_match = prot_description.group(0)
            prot_desc_vec = prot_desc_match.split('=')
            prot_description = prot_desc_vec[1]
            return prot_description
        except AttributeError:
            return "protein=error"
    
    def get_DNA_description(self, string):
        dna_description = string.replace("_prot_", "_cds_")
        return dna_description
    
