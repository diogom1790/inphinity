# -*- coding: utf-8 -*-
"""
Created on Wen Jan 31 14:56:05 2018

@author: Diogo
"""

from files_treatment_new.generic_fasta_file import _generic_fasta_file

from objects_new.Proteins_new import *

class Fasta_protein_RAST(_generic_fasta_file):
    """
    Class specified in the treatment of the fasta proteic RAST format file of fasta. Remember that its a heritage of the class generic_fasta_file that its used to read the data from a file

    """

    def __init__(self, path_file):
        """
        Constructor of the class fasta protein class, this one contain all methods for the treatment of fasta protein of RAST platform. After the parameters initialisation, the datails loaded

        :param path_file: Complete path with file name

        :type path_file: string - required
        """
        _generic_fasta_file.__init__(self, path_file)
        self.read_fasta_file()

    def create_list_proteins(self):
        """
        This method create a list of proteins based on the fasta data

        :return: list of proteins
        :rtype: list(Protein)
        """
        list_proteins = []
        for key, value in self.dict_fasta_data.items():
            protein_obj = Protein(id_accession = value.id, sequence_prot = str(value.seq))
            list_proteins.append(protein_obj)
        return list_proteins
