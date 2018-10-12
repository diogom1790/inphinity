# -*- coding: utf-8 -*-
"""
Created on Fri Jan 5 16:28:34 2018

@author: Diogo Leite
"""

from DAL import *
from configuration.configuration_data import *

class _Lysis_type_sql_new(object):
    """
    This class manipulate the LYSIS_TYPE table in the database

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

    def select_all_LT_all_attributes(self):
        """
        return all the lysis type in the database

        :return: cursor with all lysis type
        :rtype Cursor list
        """
        sql_strin = "SELECT * FROM LYSIS_TYPE"
        dalObj = DAL(self.da_name, sql_strin)
        results = dalObj.executeSelect()
        return results
