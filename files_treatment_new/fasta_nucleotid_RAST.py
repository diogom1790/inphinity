# -*- coding: utf-8 -*-
"""
Created on Wen Jan 31 15:20:17 2018

@author: Diogo
"""

from files_treatment_new.generic_fasta_file import _generic_fasta_file

from objects_new.Proteins_new import *

class Fasta_nucleotid_RAST (_generic_fasta_file):
    """
    Class specified in the treatment of the fasta protein nucleotids sequence RAST format file of fasta. Remember that its a heritage of the class generic_fasta_file that its used to read the data from a file

    """

    def __init__(self, path_file):
        """
        Constructor of the class fasta protein class, this one contain all methods for the treatment of fasta protein - nucleic sequence of RAST platform. After the parameters initialisation, the datails loaded

        :param path_file: Complete path with file name

        :type path_file: string - required
        """
        _generic_fasta_file.__init__(self, path_file)
        self.read_fasta_file()

    def complete_list_proteins(self, list_protein):
        """
        This method add the dna sequence into the proteins based on these acession number

        :param list_protein:list of the proteins

        :type list_protein: list(protein)

        :return: list of proteins
        :rtype: list(Protein)
        """
        aux_id_position_prot = 0
        for protein in list_protein:
            list_protein[aux_id_position_prot].sequence_dna = str(self.dict_fasta_data[protein.id_accession].seq)
            aux_id_position_prot += 1
        return list_protein
