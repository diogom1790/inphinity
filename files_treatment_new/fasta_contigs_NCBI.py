# -*- coding: utf-8 -*-
"""
Created on Tur Jan 11 15:39:15 2018

@author: Diogo
"""

from files_treatment_new.generic_fasta_file import _generic_fasta_file

from objects_new.Contigs_new import *
import numpy as np

class FastaContigsNCBI(_generic_fasta_file):
    """
    Class specified in the treatment of the fasta RAST format file of fasta. Remember that its a heritage of the class generic_fasta_file that its used to read the data from a file

    """

    def __init__(self, path_file):
        """
        Constructor of the class fasta contigs class, this one contain all methods for the treatment of fasta contigs of RAST platform. After the parameters initialisation, the datails loaded

        :param path_file: Complete path with file name

        :type path_file: string - required
        """
        _generic_fasta_file.__init__(self, path_file)
        self.read_fasta_file()


    def get_contig_seq_by_id(self, contig_id):
        """
        Get the nucleic sequence of a contig given its id
        
        :param contig_id: form used to request the download of genbank file to the  server

        :type contig_id: string - required

        :return: sequence nucleic in string format
        :rtype: string

        """
        sequence_nuc = str(self.dict_fasta_data[contig_id].seq)
        return sequence_nuc

    def get_qty_of_contigs(self):
        """
        Get the quantity of contigs in the fasta file
        
        :return: quantity of contigs
        :rtype: int

        """
        qty_contigs = len(self.dict_fasta_data)
        return qty_contigs

    def create_contigs_from_file(self):
        """
        This method create a list of contigs based on the fasta data

        :return: list of contigs
        :rtype: list(Contigs)
        """
        list_of_contigs = []
        for key, value in self.dict_fasta_data.items():
            contig_obj = Contig(head = value.description, sequence = str(value.seq))
            list_of_contigs.append(contig_obj)
        return list_of_contigs

    def get_list_contigs_id(self):
        """
        Return a list of the contigs ids in the fasta file (usualy used to comprare with those in the EXCEL file)

        :return: array of contigs
        :rtype: array(Contigs)
        """
        list_of_contigs_ids = np.empty([0], dtype=np.str)
        for key, value in self.dict_fasta_data.items():
            list_of_contigs_ids = np.append(list_of_contigs_ids, [value.description])
        return list_of_contigs_ids

