# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 11:47:46 2018

@author: Diogo Leite
"""

from DAL import *
from configuration.configuration_data import *

class _Dataset_sql_new(object):
    """
    This class manipulate the DATASETS table in the database

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

    def select_all_datasets_all_attributes(self):
        """
        return all the Datasets in the database

        :return: cursor with all datasets
        :rtype Cursor list
        """
        sql_string = "SELECT id_dataset_DS, date_time_creation_DS, name_DS, FK_id_user_US_DS FROM DATASETS"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results


    def insert_dataset(self, date_time_creation, name, id_user):
        """
        Insert a dataset

        :param date_time_creation: date and time of the creation (actual)
        :param name: dataset name
        :param id_user: FK of the user

        :type date_time_creation: string (datetime sql format) - required 
        :type name: string - required 
        :type id_user: int - required 

        :return: id of the dataset inserted
        :rtype int
        """
        
        sql_string = "INSERT INTO DATASETS (date_time_creation_DS, name_DS, FK_id_user_US_DS) VALUES (%s, %s, %s)"
        dalObj = DAL(self.db_name, sql_string)
        params = [date_time_creation, name, id_user]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()
        return results.lastrowid
