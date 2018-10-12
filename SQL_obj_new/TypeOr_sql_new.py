# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:36:42 2017

@author: Stage
"""

from DAL import *
from configuration.configuration_data import *

class _TypeOr_sql_new(object):
    """
    This class manipulate the TYPE_ORGANISM table in the database

    The FK are manipulated in the lasts positions of the parameters

    The types are, e.g.: Bacterium, phage,...
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
        
    def select_all_typesOr_all_attributes(self):
        """
        return all the Type_organism in the database

        :return: cursor with all Type_organism
        :rtype Cursor list
        """
        sql_string = "SELECT * FROM TYPE_ORGANISM"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results
