# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 13:59:16 2017

@author: Diogo
"""

from DAL import *
from configuration.configuration_data import *

class _Contig_sql_new(object):
    """
    This class manipulate the CONTIG table in the database

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
        
    def insert_contig(self, id_contig_db_outside, head, sequence, fk_id_whole_genome):
        """
        Insert a Contig WITHOUT ANY VERIFICATION

        :param id_contig_db_outside: Header of the CONTIG (ACC number -1 if unknown)
        :param head: First line of the fasta file "" if unknown
        :param sequence: Sequence in nucleotide of the CONTIG - "" if unknown
        :param fk_id_whole_genome: id of the whole DNA that contain this contig

        :type id_contig_db_outside: text - not required 
        :type head: text - not required
        :type sequence: text - required
        :type fk_id_whole_genome: text - required

        :return: id of the CONTIG object inserted
        :rtype int
        """
        sql_string = "INSERT INTO CONTIGS (id_contig_db_outside_CT, head_CT, sequence_CT, FK_id_whole_genome_WD_CT) VALUES (%s, %s, %s, %s)"
        dalObj = DAL(self.db_name, sql_string)
        params = [id_contig_db_outside, head, str(sequence), fk_id_whole_genome]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()
        return results.lastrowid

    def insert_contig_if_not_exist(self, id_contig_db_outside, head, sequence, fk_id_whole_genome):
        """
        Insert a Contig if exists any other contig with the same head

        :param id_contig_db_outside: Header of the CONTIG (ACC number -1 if unknown)
        :param head: First line of the fasta file "" if unknown
        :param sequence: Sequence in nucleotide of the CONTIG - "" if unknown
        :param fk_id_whole_genome: id of the whole DNA that contain this contig

        :type id_contig_db_outside: text - not required 
        :type head: text - not required
        :type sequence: text - required
        :type fk_id_whole_genome: text - required

        :return: id of the CONTIG object inserted
        :rtype int
        """

        id_contig = self.get_id_contig_by_head(head)

        if id_contig == -1:
            sql_string = "INSERT INTO CONTIGS (id_contig_db_outside_CT, head_CT, sequence_CT, FK_id_whole_genome_WD_CT) VALUES (%s, %s, %s, %s)"
            dalObj = DAL(self.db_name, sql_string)
            params = [id_contig_db_outside, head, str(sequence), fk_id_whole_genome]
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            print("Its already exists a Contig with this head")
            return id_contig

    def get_id_contig_by_head(self, head):
        """
        get the id of the contig based on its head

        :param head: First line of the fasta file "" if unknown

        :type head: string - required 

        :return: id of the contig or -1 if inexistant
        :rtype int
        """

        sql_string = "SELECT id_contig_CT from CONTIGS WHERE head_CT = '" + str(head) + "'"

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]

    def select_all_contigs_all_attributesby_fk_whole_dna(self, fk_whole_dna):
        """
        Consult the DB and return a list with contigs which have a FK_whole_DNA

        :return: cursor with the contigs
        :rtype Cursor list
        """
        sql_string = "SELECT id_contig_CT, id_contig_db_outside_CT, head_CT, sequence_CT, FK_id_whole_genome_WD_CT FROM CONTIGS WHERE FK_id_whole_genome_WD_CT = " + str(fk_whole_dna)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def remove_contig_by_fk_whole_dna(self, fk_id_whole_dna):
        """
        remove a couple by the FK_id_whole_dna

        :param FK_id_whole_dna: id of the FK_whole_dna 

        :type FK_id_whole_dna: int - required 

        :return: number of contig removed
        :rtype int
        """
        sql_string = "DELETE FROM CONTIGS WHERE FK_id_whole_genome_WD_CT = %s"
        dalObj = DAL(self.db_name, sql_string)
        params = [fk_id_whole_dna]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()
        return results.rowcount