# -*- coding: utf-8 -*-
"""
Created on Tur Jan 11 15:34:27 2018

@author: Diogo
"""

from Bio import SeqIO

import re

class _generic_fasta_file(object):
    """
    This class treat the fasta files in general. Just load the data based on the file location

    """

    def __init__(self, path_file):
        """
        Constructor of the class fasta top class, the data are loaded into dict_fasta_data variable. The classe only manipulate the data with the bioPython

        :param path_file: Complete path with file name

        :type path_file: string - required
        """
        self.path_file = path_file
        self.dict_fasta_data = None

    def read_fasta_file(self):
        """
        method use to load the data into its dict_fasta_data
        """
        self.dict_fasta_data = SeqIO.to_dict(SeqIO.parse(self.path_file, "fasta"))

    def split_header_by_square_brackets(self, description):
        """
        This method splie the description line of the fasta file. This line needs to have the folloe structur [qqq=eee]

        :param description: string which contains the description

        :return: dictionary with all the tags
        :rtype: dictionary 
        """
        matchObj = re.findall( r'\[(.*?)\]', description)
        dict_elements = {}
        for element in matchObj:
            try:
                values = element.split('=')
                dict_elements[values[0]] = values[1]
            except IndexError:
                dict_elements[values[0]] = 'No information'
        return dict_elements

    def __str__(self):
        """
        Overwrite of the str method
        """
        message = "File name: {0}, number of fasta entries {1:d}".format(self.path_file, len(self.dict_fasta_data))
        return message

