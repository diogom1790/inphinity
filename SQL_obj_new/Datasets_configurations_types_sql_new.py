# -*- coding: utf-8 -*-
"""
Created on Tue Mai 15 11:01:22 2018

@author: Diogo Leite
"""

from DAL import *
from configuration.configuration_data import *

class _Datasets_config_types_SQL(object):
    """
    This class manipulate the DATASET_CONFIGURATIONS_TYPES table in the database. It used to obtain all different configuratiosn types


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

    def select_all_Datasets_conf_type(self):
        """
        return all the connections dataset configurations types

        :return: cursor with all types of configurations
        :rtype Cursor list
        """
        sql_string = "SELECT id_configuration_DCT, designation_DCT FROM DATASET_CONFIGURATIONS_TYPES"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results