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

    def __init__(self, path_file, identification_key):
        """
        Constructor of the class fasta protein class, this one contain all methods for the treatment of fasta protein - nucleic sequence of NCBI platform. After the parameters initialisation, the details loaded

        :param path_file: Complete path with file name
        :param identification_key: Key used to obtain the different proteins in the fasta files

        :type path_file: string - required
        :type identification_key: string - required
        """
        _generic_fasta_file.__init__(self, path_file)
        self.read_fasta_file()
        self.identification_key = identification_key



    def get_list_nucleotid_name(self):
        """
        This method return a list of the key_designation in the fasta file

        :param key_designation: Key used to obtain the information in the fasta file

        :type key_designation: string - required

        :return: list of id proteins
        :rtype: list(string)
        """
        list_id = []
        for key, value in self.dict_fasta_data.items():
            dict_elements = self.split_header_by_square_brackets(value.description)

            list_id.append(dict_elements[self.identification_key])
        return list_id


    def get_nucleotid_sequence_by_key(self, protein_id):
        """
        This method return the nucleotid sequence based on the protein_id (ACC)

        :return: nucleotid sequence
        :rtype: string
        """
        for key, value in self.dict_fasta_data.items():
            dict_elements = self.split_header_by_square_brackets(value.description)
            if dict_elements[self.identification_key] == protein_id:
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
            if dict_elements[self.identification_key ] == protein_id:
                location = dict_elements['location']
                print(location)
                search_loc = re.findall('\d+' ,location)
                print(search_loc)
                
                start_location = search_loc[0]
                end_location = search_loc[1]
                return start_location, end_location
        return [0,0]
