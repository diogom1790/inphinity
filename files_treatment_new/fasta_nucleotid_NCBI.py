# -*- coding: utf-8 -*-
"""
Created on Wen Fev 22 17:49:05 2018

@author: Diogo
"""
import re
from files_treatment_new.generic_fasta_file import _generic_fasta_file

from objects_new.Proteins_new import *


class Fasta_nucleotid_NCBI (_generic_fasta_file):
    """
    Class specified in the treatment of the fasta protein nucleotids sequence NCBI format file of fasta. Remember that its a heritage of the class generic_fasta_file that its used to read the data from a file

    """

    def __init__(self, path_file):
        """
        Constructor of the class fasta protein class, this one contain all methods for the treatment of fasta protein - nucleic sequence of NCBI platform. After the parameters initialisation, the datails loaded

        :param path_file: Complete path with file name

        :type path_file: string - required
        """
        _generic_fasta_file.__init__(self, path_file)
        self.read_fasta_file()


    def get_list_nucleotid_name(self):
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

    def get_nucleotid_sequence_prot_id(self, protein_id):
        """
        This method return the nucleotid sequence based on the protein_id (ACC)

        :return: nucleotid sequence
        :rtype: string
        """
        for key, value in self.dict_fasta_data.items():
            dict_elements = self.split_header_by_square_brackets(value.description)
            if dict_elements['protein_id'] == protein_id:
                return str(value.seq)
        return ''

    def get_location_by_prot_id(self, protein_id):
        """
        This method return the start and end location of the protein in the genome based on its id

        :return: start and end position
        :rtype: array[int, int]
        """
        for key, value in self.dict_fasta_data.items():
            dict_elements = self.split_header_by_square_brackets(value.description)
            if dict_elements['protein_id'] == protein_id:
                location = dict_elements['location']
                print(location)
                search_loc = re.findall('\d+' ,location)
                print(search_loc)
                
                start_location = search_loc[0]
                end_location = search_loc[1]
                return start_location, end_location
        return [0,0]
