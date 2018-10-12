# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:57:32 2017

@author: Diogo
"""

from DAL import *
from configuration.configuration_data import *

class _WholeDNA_sql_new(object):
    """
    This class manipulate the WHOLE_DNA table in the database

    The FK are manipulated in the lasts positions of the parameters
    """
    def __init__(self):
        self.db_name = self.get_database_name()

    def get_database_name(self):
        """
        This method is used to get the database name used in factory

        :return: database name
        :rtype string
        """
        conf_data_obj = Configuration_data('INPHINITY')
        db_name = conf_data_obj.get_database_name()
        return db_name
        
    def select_all_wholeDNAs_all_attributes(self):
        """
        Consult the DB and return a list with all WHOLE_DNA objects with all details

        :return: cursor with all WHOLE_DNA
        :rtype Cursor list
        """

        sql_string = "SELECT * FROM WHOLE_DNA"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results
    
    def insert_whole_genome_if_not_exist(self, head, head_id, sequence):
        """
        Insert a Whole DNA only but verify if doesn't exist another one with the same head and head_id

        :param head: Header of the whole genome (first line in fasta file) - "" if unknown
        :param head_id: accession number of the Whole_DNA - "" if unknown
        :param sequence: Sequence in nucleotide of the WholeDNA - "" if unknown

        :type head: text - required 
        :type head_id: text - required
        :type sequence: text - required

        :return: id of the WholeDNA object inserted or ID of the WHoleDNA existing 
        :rtype int
        """
        id_wholeDNA = self.get_id_whole_genome_by_head_and_head_id(head, head_id)
        if id_wholeDNA == -1:
            sql_string = "INSERT INTO WHOLE_DNA (head_WD, head_id_WD, sequence_WD) VALUES (%s, %s, %s)"
            dalObj = DAL(self.db_name, sql_string)
            params = [head, head_id, sequence]
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            print("It already exists an Whole DNA with these heads data")
            return id_wholeDNA
    
    
    def insert_whole_genome_no_verification(self,  head, head_id, sequence):
        """
        Insert a Whole DNA WITHOUT ANY VERIFICATION

        :param head: Header of the whole genome (first line in fasta file) - "" if unknown
        :param head_id: accession number of the Whole_DNA - "" if unknown
        :param sequence: Sequence in nucleotide of the WholeDNA - "" if unknown

        :type head: text - required 
        :type head_id: text - required
        :type sequence: text - required

        :return: id of the Whole_DNA object inserted
        :rtype int
        """
        sql_string = "INSERT INTO WHOLE_DNA (head_WD, head_id_WD, sequence_WD) VALUES (%s, %s, %s)"
        params = [head, head_id, sequence]
        dalObj = DAL(self.db_name, sql_string)
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()
        return results.lastrowid

    def get_id_whole_genome_by_head_and_head_id(self, head, head_id):
        """
        get the id of a Whole_genome based on its fasta head and head id

        :param head: head of the whole genome
        :param head_id: id tag of the head

        :type grp_a: head - required 
        :type grp_b: head_id - required 

        :return: id of the Whole DNA or -1 if inexistant
        :rtype int
        """
        sql_string = "SELECT id_dna_WD FROM WHOLE_DNA WHERE head_WD = \"" + str(head) + "\" AND head_id_WD = \"" + str(head_id) + "\""
        print(sql_string)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]

    def get_whole_dna_by_id(self, id_whole_dna):
        """
        Get a Whole_DNA by its id

        :return: Whole_DNA elements info
        :rtype List(infos Whole_DNA)
        """
        sql_string = "SELECT id_dna_WD, head_WD, head_id_WD, sequence_WD FROM WHOLE_DNA WHERE id_dna_WD = " + str(id_whole_dna)
        dalobj = DAL(self.db_name, sql_string)
        results = dalobj.executeSelect()

        return results[0]

    def remove_whole_dna_by_id(self, id_whole_dna):
        """
        remove a whole_dna by its id

        :param id_whole_dna: id of the whole_dna 

        :type id_whole_dna: int - required 

        :return: quantity of removed row
        :rtype int
        """
        sql_string = "DELETE FROM WHOLE_DNA WHERE id_dna_WD = %s"
        dalObj = DAL(self.db_name, sql_string)
        params = [id_whole_dna]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeDelete()
        return results.rowcount
            

    def update_whole_dna_by_id(self, id_whole_dna, head, head_id, sequence):
        """
        update the contig information given a protein id

        :param id_whole_dna: wholde dna id in the database
        :param head: heat of the whole dna (first line of the fasta file)
        :param head_id: acc number
        :param sequence: sequence in nucleotid of the whole dna

        :type id_whole_dna: int - required
        :type head: string - required
        :type head_id: int - required
        :type sequence: string - required

        :return: id of the updated protein
        :rtype int
        """
        sql_string = "UPDATE WHOLE_DNA SET head_WD = %s, sequence_WD = %s, head_id_WD = %s WHERE id_dna_WD = " + str(id_whole_dna)
        params = [head, sequence, head_id]
        dalObj = DAL(self.db_name, sql_string, params)
        results = dalObj.executeInsert()
        return results