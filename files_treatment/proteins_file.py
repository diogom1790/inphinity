# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:34:22 2017

@author: Stage
"""

from objects_old.Bacteria_old import *
from files_treatment.download_files import Download_file
from Bio import SeqIO
from objects_new.Proteins_new import Protein
import re

class Proteins_genome(object):
    def __init__(self, id_bact):
        self.id_bact = id_bact
        self.file_fasta_protein_seq = None
        self.file_fasta_nucleic_seq = None
        self.list_proteins = []
        
    def getFasta_seq_all_proteins(self):
        dict_url_values = {}
        dict_url_values["db"] = "Nucleotide"
        dict_url_values["id"] = self.id_bact
        dict_url_values["rettype"] = "fasta_cds_aa"
        dict_url_values["retmode"] = "text"
        objFildD = Download_file("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi", dict_url_values)
        self.file_fasta_protein_seq = objFildD.request_fasta_file()
        
    def getFasta_seq_proteins_DNA(self):
        dict_url_values = {}
        dict_url_values["db"] = "Nucleotide"
        dict_url_values["id"] = self.id_bact
        dict_url_values["rettype"] = "fasta_cds_na"
        dict_url_values["retmode"] = "text"
        objFildD = Download_file("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi", dict_url_values)
        self.file_fasta_nucleic_seq = objFildD.request_fasta_file()
        
    def getFasta_proteic_DNA(self):
        self.getFasta_seq_all_proteins()
        self.getFasta_seq_proteins_DNA()
        print("je suis diogo 2")
        print(len(self.file_fasta_protein_seq))
        print("je suis diogo")
        print(type(self.file_fasta_protein_seq))
        #print(self.file_fasta_protein_seq)
        list_keys = []
        list_proteins = []
        for key, value in self.file_fasta_protein_seq.items():
            list_keys.append(key)
            DNA_string_key = self.get_DNA_description(key)
        
        
            id_protein = -1
            id_prot_DB_online = self.get_protein_id(self.file_fasta_protein_seq[key].description)
            designation = self.get_protein_description(self.file_fasta_protein_seq[key].description)
            sequence_prot = self.file_fasta_protein_seq[key].seq
            sequence_DNA = self.file_fasta_nucleic_seq[DNA_string_key].seq
            start_point, end_point = self.get_protein_location(self.file_fasta_protein_seq[key].description)
        
            protein_obj = Protein(id_protein, id_prot_DB_online, designation, sequence_prot, 
                                  sequence_DNA, start_point, end_point)
            print(start_point)
            print(end_point)
            
            list_proteins.append(protein_obj)
        print(len(list_proteins))
        print("finiinininininiiiiii")
        return list_proteins
        
        
        
    def get_protein_id(self, string):
        try:
            protein = re.search('protein_id=[a-zA-Z0-9\.]+', string)
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
            print("--------------")
            print(location_start)
            print(location_end)
            print("--------------")
        except AttributeError:
            return 0, 0
        return location_start, location_end
    
    def get_protein_description(self, string):
        print(string)
        try:
            prot_description = re.search('protein=[\(\)\-\&\%A-Za-z0-9\s]+', string)
            prot_desc_match = prot_description.group(0)
            prot_desc_vec = prot_desc_match.split('=')
            prot_description = prot_desc_vec[1]
            return prot_description
        except AttributeError:
            return "protein=error"
    
    def get_DNA_description(self, string):
        print(string)
        dna_description = string.replace("_prot_", "_cds_")
        print(dna_description)
        return dna_description
        
        
        