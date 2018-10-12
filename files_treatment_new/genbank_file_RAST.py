# -*- coding: utf-8 -*-
"""
Created on Tur Jan 11 11:51:13 2018

@author: Diogo
"""
from files_treatment_new.generic_gen_bank_files import _generic_genbank_file

class Genbank_proteic_RAST(_generic_genbank_file):
    """
    Class specified in the treatment of the gen_bank RAST format file of genbank. Remember that its a heritage of the class _generic_gen_bank_files that its used to read the data from a file

    """

    def __init__(self, path_file):
        """
        Constructor of the class gen_bank class, this one contain all methods for the treatment of excel files fasta contigs of RAST platform. After the parameters initialisation, the datais loaded

        :param path_file: Complete path with file name

        :type path_file: string - required
        """
        _generic_genbank_file.__init__(self, path_file)
        self.read_gen_bank()

    def get_definition_of_the_organism(self):
        """
        Return the organism name (usualy specie - strain. E.G.: Escherichia coli - D12)

        :return: name of the organism
        :rtype: string
        """
        first_key = list(self.data_gen_bank.keys())[0]
        designation_organism = self.data_gen_bank[first_key].annotations['source']
        return designation_organism

    def get_taxonomy_array(self):
        """
        Return the taxonomy of the organims that its inside the first contig

        :return: array with the taxonomy or empty if the taxonomy doesn't exist
        :rtype: array(string)
        """
        first_key = list(self.data_gen_bank.keys())[0]
        if 'unknown' not in first_key.lower():
            taxonomy_array = self.data_gen_bank[first_key].annotations['taxonomy']
            return taxonomy_array
        else:
            return []

    def get_number_of_contigs(self):
        """
        Return the quantity of contigs in the genbank file

        :return: quantity of contigs
        :rtype: int
        """
        qty_contigs = len(list(self.data_gen_bank.keys()))
        return qty_contigs

    def get_family(self):
        """
        Return family name of the organism only if the taxonomy_array has 7 designations. In case of it has more or less it is returned "No"

        :return: family name
        :rtype:  string
        """

        taxonomy_array = self.get_taxonomy_array()
        family_name = ""
        if len(taxonomy_array) == 7:
            family_name = taxonomy_array[4]
        else:
            print("The taxonomy available in the genbank file aren't formated for this treatment")
            family_name = "No"
        return family_name


    def get_genus(self):
        """
        Return genus name of the organism only if the taxonomy_array has 7 designations. In case of it has more or less it is returned "No"

        :return: genus name
        :rtype:  string
        """

        taxonomy_array = self.get_taxonomy_array()
        genus_name = ""
        if len(taxonomy_array) == 7:
            genus_name = taxonomy_array[5]
        else:
            print("The taxonomy available in the genbank file aren't formated for this treatment")
            genus_name = "No"
        return genus_name

    def get_specie(self):
        """
        Return specie name of the organism only if the taxonomy_array has 7 designations. In case of it has more or less it is returned "No"

        :return: specie name
        :rtype:  string
        """

        taxonomy_array = self.get_taxonomy_array()
        specie_name = ""
        if len(taxonomy_array) == 7:
            specie_name = taxonomy_array[6]
        else:
            print("The taxonomy available in the genbank file aren't formated for this treatment")
            specie_name = "No"
        return specie_name

    def get_strain(self):
        """
        Return strain name of the organism only if the taxonomy_array has 7 designations and the organism has 3 "names". In case of it has more or less it is returned "No"

        :return: strain name
        :rtype:  string
        """
        organism_name = self.get_definition_of_the_organism()
        strain_name = ""
        array_organism_name = organism_name.split(" ")
        if len(array_organism_name) == 3:
            strain_name = array_organism_name[-1]
        else:
            print("The taxonomy available in the genbank file aren't formated for this treatment")
            strain_name = "No"
        return strain_name



