# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 11:55:18 2018

@author: Diogo
"""

# here the FK values was selected in lastas positions according to F_score_blast_sql_new object class

from DAL import *
from configuration.configuration_data import *

class _F_score_blast_X_sql(object):
    """
    This class manipulate the Feature score blast table in the database

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

    def select_all_score_blast_x_all_attributes(self):
        """
        return all the blast scores in the database

        :return: cursor with all scores blast
        :rtype Cursor list
        """
        sql_string = "SELECT id_blast_FSB_X, pident_FSB_X, length_FSB_X, mismatch_FSB_X, gapopen_FSB_X, pstart_FSB_X, pend_FSB_X, bstart_FSB_X, bend_FSB_X, evalue_FSB_X, bitscore_FSB_X, plen_FSB_X, blen_FSB_X, FK_id_protein_PT_FSB_X, FK_id_couple_CP_FSB_X FROM F_SCORE_BLAST_X"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def insert_f_score_blast_x(self, pident, length, mismatch, gapopen, pstart, pend, bstart, bend, evalue, bitscore, plen, blen, FK_id_protein_PT_FSB_X, FK_id_couple_CP_FSB_x):
        """
         Insert a F_scor_blast in the database WHITOUT ANY VALIDATION

        :param pident: blast score
        :param length: i don't know
        :param mismatch: i don't know
        :param gapopen: i don't know
        :param pstart: i don't know
        :param pend: i don't know
        :param bstart: i don't know
        :param bend: i don't know
        :param evalue: i don't know
        :param bitscore: i don't know
        :param plen: i don't know
        :param blen: i don't know
        :param FK_id_protein_PT_FSB_X: i don't know
        :param FK_id_couple_CP_FSB_x: id of the couple which belong the score - -1 if unknown


        :type pident: float - required 
        :type length: int - required
        :type mismatch: int - required
        :type gapopen: int - required
        :type pstart: int - required
        :type pend: int - required
        :type bstart: int - required
        :type bend: int - required
        :type evalue: double - required
        :type bitscore: double - required
        :type plen: int - required
        :type blen: int - required
        :type FK_id_protein_PT_FSB_X: int - required
        :type FK_id_couple_CP_FSB: int - required

        :return: id of the f_score_blast object inserted
        :rtype int
        """

        sql_string = "INSERT INTO F_SCORE_BLAST_X (pident_FSB_X, length_FSB_X, mismatch_FSB_X, gapopen_FSB_X, pstart_FSB_X, pend_FSB_X, bstart_FSB_X, bend_FSB_X, evalue_FSB_X, bitscore_FSB_X, plen_FSB_X, blen_FSB_X, FK_id_protein_PT_FSB_X, FK_id_couple_CP_FSB_X) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        dalObj = DAL(self.db_name, sql_string)
        params = [pident, length, mismatch, gapopen, pstart, pend, bstart, bend, evalue, bitscore, plen, blen, FK_id_protein_PT_FSB_X, FK_id_couple_CP_FSB_x]

        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()
        return results.lastrowid

        

