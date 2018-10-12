# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 09:44:05 2018

@author: Diogo
"""

from files_treatment_new.generic_fasta_file import _generic_fasta_file
from objects_new.WholeDNA_new import * 


class Fasta_whole_genome_NCBI (_generic_fasta_file):
    """
    Class specified in the treatment of the fasta whole genome format file of fasta. Remember that its a heritage of the class generic_fasta_file that its used to read the data from a file
    """


    def __init__(self, path_file):
        """
        Constructor of the class fasta protein class, this one contain all methods for the treatment of fasta protein - proteic sequence of NCBI platform. After the parameters initialisation, the datails loaded

        :param path_file: Complete path with file name

        :type path_file: string - required
        """
        _generic_fasta_file.__init__(self, path_file)
        self.read_fasta_file()

    def get_whole_genome(self):

        print(len(self.dict_fasta_data))
        assert len(self.dict_fasta_data) == 1
        acc_value = list(self.dict_fasta_data)[0]
        value = self.dict_fasta_data[acc_value]
        description = value.description
        sequence_wg =  str(value.seq)

        whole_dna_obj = WholeDNA(id_wholeDNA = -1, head = description, head_id = acc_value, sequence = sequence_wg)

        return whole_dna_obj