# -*- coding: utf-8 -*-
"""
Created on Tur Jan 12 09:44:14 2018

@author: Diogo
"""

from Bio import SeqIO
import fileinput
from shutil import copyfile
import os

class _generic_genbank_file(object):
    """
    This class treat the genbank files in general. Just load the data based on the file location
    """

    def __init__(self, path_file):
        """
        Constructor of the class genbank top class, the data are loaded into data_gen_bank variable. The classe only manipulate the data with the bioPython

        :param path_file: Complete path with file name

        :type path_file: string - required
        """
        self.path_file = path_file
        self.data_gen_bank = None

    def read_write_gen_bank(self):
        """
        This method create a backup and update the file path with this one correcting the ACCESSION number
        """
        count_id = 0
        new_file_name = self.path_file + '.bak'
        copyfile(self.path_file, new_file_name)
        lines_file = []

        with open(self.path_file) as file:
            for line in file:
                if line.find('ACCESSION   unknown') != -1:
                    line = line.replace('ACCESSION   unknown', 'ACCESSION   unknown' + str(count_id))
                    count_id += 1
                lines_file.append(line)

        with open(new_file_name, 'w') as file:
            for value_line in lines_file:
                file.write(value_line)

# GARY
        #with open(new_file_name) as file_to_write:
        #   with open(self.path_file) as file:
        #        for line in file:
        #            if line.find('ACCESSION   unknown') != -1:
        #                line = line.replace('ACCESSION   unknown', 'ACCESSION   unknown' + str(count_id))
        #                count_id += 1
        #                file_to_write.write(line)


# END of magic GARY

                


        self.path_file = new_file_name




    def read_gen_bank(self):
        """
        method use to load the data into its dict_fasta_data. If the ACCESSION number is "unknow", the method correct this for the extraction of the data into dictionaries calling the read_write_gen_bank method". This last method is called when it is impossible to parse the genBank file.

        :excep ValueError: When it isn't possible to load the data into the dictionnary because of the double keys
        """
        try:
            self.data_gen_bank = SeqIO.to_dict(SeqIO.parse(self.path_file, "genbank"))
        except ValueError:
            print ("Test the substitution of the file: {0}".format(self.path_file))

            self.read_write_gen_bank()
            self.data_gen_bank = SeqIO.to_dict(SeqIO.parse(self.path_file, "genbank"))

            print("end of the substitution")

    def __str__(self):
        """
        Overwrite of the str method
        """
        message = "File name: {0}, number of sequences {1:d}".format(self.path_file, len(self.data_gen_bank))
        return message
