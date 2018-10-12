# -*- coding: utf-8 -*-
"""
Created on Fri Jan 5 16:45:57 2018

@author: Diogo Leite
"""

from DAL import *
from configuration.configuration_data import *

class _F_score_COG_sql(object):
    """
    This class manipulate the Feature score COG table in the database

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

    def select_all_score_COG_all_attributes(self):
        """
        return all the COG scores in the database

        :return: cursor with all scores COG
        :rtype Cursor list
        """
        sql_string = "SELECT id_score_int_cog_FSIC, score_result_FSIC, FK_id_couple_CP_FSIC FROM F_SCORE_INTERACTIONS_COG"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def insert_f_score_COG(self, score_result, FK_id_couple_CP_FSIC):
        """
         Insert a F_scor_COG in the database WHITOUT ANY VALIDATION

        :param score_result: COG score
        :param FK_id_couple_CP_FSIC: id of the couple which belong the score - -1 if unknown

        :type score_result: int - required 
        :type FK_id_couple_CP_FSIC: int - required

        :return: id of the f_score_COG object inserted
        :rtype int
        """
        sql_string = "INSERT INTO F_SCORE_INTERACTIONS_COG (score_result_FSIC, FK_id_couple_CP_FSIC) VALUES (%s, %s)"
        dalObj = DAL(self.db_name, sql_string)
        params = [score_result, FK_id_couple_CP_FSIC]

        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()
        return results.lastrowid


