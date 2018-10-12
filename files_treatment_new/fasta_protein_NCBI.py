# -*- coding: utf-8 -*-
"""
Created on Wen Fev 22 17:49:05 2018

@author: Diogo
"""

from files_treatment_new.generic_fasta_file import _generic_fasta_file

from objects_new.Proteins_new import *
import re

class Fasta_protein_NCBI (_generic_fasta_file):
    """
    Class specified in the treatment of the fasta protein nucleotids sequence NCBI format file of fasta. Remember that its a heritage of the class generic_fasta_file that its used to read the data from a file

    """

    def __init__(self, path_file):
        """
        Constructor of the class fasta protein class, this one contain all methods for the treatment of fasta protein - proteic sequence of NCBI platform. After the parameters initialisation, the datails loaded

        :param path_file: Complete path with file name

        :type path_file: string - required
        """
        _generic_fasta_file.__init__(self, path_file)
        self.read_fasta_file()


    def get_list_protein_name(self):
        """
        This method return a list of the proteins_id in the fasta file

        :return: list of id proteins
        :rtype: list(string)
        """
        list_id = []
        for key, value in self.dict_fasta_data.items():
            dict_elements = self.split_header_by_square_brackets(value.description)
            list_id.append(dict_elements['protein_id'])
        return list_id

    def get_protein_sequence_prot_id(self, protein_id):
        """
        This method return the protein sequence based on the protein_id (ACC)

        :return: protein sequence
        :rtype: string
        """
        for key, value in self.dict_fasta_data.items():
            dict_elements = self.split_header_by_square_brackets(value.description)
            if dict_elements['protein_id'] == protein_id:
                return str(value.seq)
        return ''

    def get_list_of_proteins(self):
        """
        This method return a list of proteins found in the fasta file

        :return:list of proteins
        :rtype: List(Protein_new)
        """
        listOfProteins = []
        acc_prot = ''
        description = ''
        values_p = [-1,-1]
        for key, value in self.dict_fasta_data.items():
            dict_elements = self.split_header_by_square_brackets(value.description)
            if 'protein_id' in dict_elements:
                acc_prot = dict_elements['protein_id'] 
            if 'protein' in dict_elements:
                description = dict_elements['protein'] 
            if 'location' in dict_elements:
                string_position = dict_elements['location'] 
                positions_values = re.findall(r'-?([0-9]*)', string_position)
                values_p = [i for i in positions_values if len(i) >0]
            protein_obj = Protein(id_accession=acc_prot, designation = description, start_point = int(values_p[0]), end_point = int(values_p[1]), sequence_prot = str(value.seq))
            listOfProteins.append(protein_obj)

        return listOfProteins

