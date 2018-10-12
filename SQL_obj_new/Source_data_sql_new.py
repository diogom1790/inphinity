
# -*- coding: utf-8 -*-
"""
@author: Diogo Leite
"""

from DAL import *
from configuration.configuration_data import *

class _Source_data_sql_new(object):
    """
    This class manipulate the SOURCES_DATA table in the database

    Theses one correspond to the database from where comes the data (NCBI, PhageDB, RAST,...)

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

    def select_all_data_sources_all_attributes(self):
        """
        return all the SOURCE_DATA in the database

        :return: cursor with all source_data_
        :rtype Cursor list
        """

        sql_string = "SELECT * FROM SOURCE_DATA"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

