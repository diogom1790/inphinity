# -*- coding: utf-8 -*-
"""
Created on Fri Jan 5 14:58:59 2018

@author: Diogo Leite
"""
from DAL import *
from configuration.configuration_data import *

class _Level_interaction_sql_new(object):
    """
    This class manipulate the level_interaction table in the database

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

    def select_all_level_interactions_all_attributes(self):
        """
        return all the Level interaction in the database

        :return: cursor with all Leve interaction
        :rtype Cursor list
        """

        sql_string = "SELECT id_level_LI, designation_LI FROM LEVEL_INTERACTIONS"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results