# -*- coding: utf-8 -*-
"""
Created on Tur Jan 11 11:51:13 2018

@author: Diogo
"""
from files_treatment_new.generic_gen_bank_files import _generic_genbank_file

class Genbank_proteic_NCBI(_generic_genbank_file):
    """
    Class specified in the treatment of the gen_bank NCBI format file of genbank. Remember that its a heritage of the class _generic_gen_bank_files that its used to read the data from a file

    """

    def __init__(self, path_file):
        """
        Constructor of the class gen_bank class, this one contain all methods for the treatment of excel files fasta contigs of RAST platform. After the parameters initialisation, the datais loaded

        :param path_file: Complete path with file name

        :type path_file: string - required
        """
        _generic_genbank_file.__init__(self, path_file)
        self.read_gen_bank()



    def get_number_of_contigs(self):
        """
        Return the quantity of contigs in the genbank file

        :return: quantity of contigs
        :rtype: int
        """
        qty_contigs = len(list(self.data_gen_bank.keys()))
        return qty_contigs

    def get_accession_number(self):
        first_key = list(self.data_gen_bank.keys())[0]
        acc_number = self.data_gen_bank[first_key].id
        return acc_number

    def get_contig_of_the_phage(self):
        first_key = list(self.data_gen_bank.keys())[0]
        contig_sequence = self.data_gen_bank[first_key].seq
        return contig_sequence


