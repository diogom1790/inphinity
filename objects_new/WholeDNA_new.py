# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:58:09 2017

@author: Diogo
"""

from SQL_obj_new.WholeDNA_sql_new import _WholeDNA_sql_new

class WholeDNA(object):
    """
    This class treat the Whole DNA (called Whole Genome) object has it exists in WholeDNA table database
    By default, all FK are in the lasts positions in the parameters declaration
    """
    def __init__(self, id_wholeDNA = -1, head = "", head_id = "", sequence = ""):
        """
        Constructor of the Organism object. All the parameters have a default value

        :param id_wholeDNA: id of the WholeDNA - -1 if unknown
        :param head: Header of the whole genome (first line in fasta file) - "" if unknown
        :param head_id: accession number of the Whole_DNA - "" if unknown
        :param sequence: Sequence in nucleotide of the WholeDNA - "" if unknown

        :type id_wholeDNA: int - not required
        :type head: text - required 
        :type head_id: text - required
        :type sequence: text - required
        """
        self.id_wholeDNA = id_wholeDNA
        self.head = head
        self.head_id = head_id
        self.sequence = sequence
        
    def get_all_WholeDNA(self):
        """
        Return all WholesDNA in the database

        :return: array of WholesDNA
        :rtype: array(WholesDNA)
        """
        listOfWholeDNA = []
        sqlObj = _WholeDNA_sql_new()
        results = sqlObj.select_all_wholeDNAs_all_attributes()
        for element in results:
            listOfWholeDNA.append(WholeDNA(element[0], element[1], element[2]))
        return listOfWholeDNA
    
    @DeprecationWarning
    def create_whole_dna(self):
        """
        Insert an WholeDNA in the database. If any other exists with the same:
        - head - first line of the fasta file
        AND
        - head_id - accession number
        
        The id of the Whole DAN is updated

        :return: id of the Whole DNA created or the ID of the whole DNA existed
        :rtype: int
        """
        sqlObj = _WholeDNA_sql_new()
        value_id_whole_genome = sqlObj.insert_whole_genome_if_not_exist(self.head, self.head_id, self.sequence)
        self.id_wholeDNA = value_id_whole_genome
        return value_id_whole_genome

    
    
    def create_whole_dna_no_verification(self):
        """
        Insert an WholeDNA in the database WITHOUT ANY VERIFICATION
        
        The id of the Whole DNA is updated

        :return: id of the Whole DNA created
        :rtype: int
        """
        sqlObj = _WholeDNA_sql_new()
        value_whole_genome = sqlObj.insert_whole_genome_no_verification(self.head, self.head_id, self.sequence)
        self.id_wholeDNA = value_whole_genome
        return value_whole_genome

    def get_whole_dna_by_id(id_whole_dna):
        """
        Get a Whole_DNA by its id
  
        :return: Whole_DNA object
        :rtype: Whole_DNA
        """
        sqlObj = _WholeDNA_sql_new()
        whole_dna_results = sqlObj.get_whole_dna_by_id(id_whole_dna)
        whole_dna_obj = WholeDNA(whole_dna_results[0], whole_dna_results[1], whole_dna_results[2], whole_dna_results[3])
        return whole_dna_obj

    def remove_whole_dna_by_id(id_whole_dna):
        """
        remove a couple given its id

        :param id_whole_dna: id of the couple

        :type id_whole_dna: int - required

        :return: whole dna id removed
        :rtype: int
        """
        sqlObj = _WholeDNA_sql_new()
        id_couple = sqlObj.remove_whole_dna_by_id(id_whole_dna)
        return id_couple

    def update_whole_dna_by_id(self, id_whole_dna):
        """
        Update a Whole Dna by its ID
        
        :param id_whole_dna: id of the couple

        :type id_whole_dna: int - required

        :return: id of the Whole DNA updated
        :rtype: int
        """
        sqlObj = _WholeDNA_sql_new()
        value_whole_genome = sqlObj.update_whole_dna_by_id(self.id_wholeDNA ,self.head, self.head_id, self.sequence)
        return value_whole_genome


    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d} head: {1} head ID: {2}, Sequence: {3}".format(self.id_wholeDNA, self.head, self.head_id, self.sequence)
        return message_str


        