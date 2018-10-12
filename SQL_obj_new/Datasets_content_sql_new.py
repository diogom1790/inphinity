# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:09:15 2018

@author: Diogo Leite
"""

from DAL import *
from configuration.configuration_data import *

class _Dataset_content_sql_new(object):
    """
    This class manipulate the DATASETS_CONTENT table in the database

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

    def select_all_datasets_content_all_attributes(self):
        """
        return all the Datasets_content in the database

        :return: cursor with all Datasets_content
        :rtype Cursor list
        """
        sql_string = "SELECT FK_id_couple_CP_DC, FK_id_dataset_DS_DC FROM DATASET_CONTENT"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_datasets_content_all_attributes_by_dataset_id(self, id_dataset):
        """
        return all the Datasets_content in the database by a dataset ID

        :return: cursor with Datasets_content
        :rtype Cursor list
        """
        sql_string = "SELECT FK_id_couple_CP_DC, FK_id_dataset_DS_DC FROM DATASET_CONTENT WHERE FK_id_dataset_DS_DC = " + str(id_dataset)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results


    def insert_dataset_content(self, fk_id_couple, fk_id_dataset):
        """
        Insert a dataset_content

        :param fk_id_couple: id of the couple that you want in the dataset
        :param fk_id_dataset: id of the dataset

        :type fk_id_couple: int - required 
        :type fk_id_dataset: int - required 

        """
        
        sql_string = "INSERT INTO DATASET_CONTENT (FK_id_couple_CP_DC, FK_id_dataset_DS_DC) VALUES (%s, %s)"
        dalObj = DAL(self.db_name, sql_string)
        params = [fk_id_couple, fk_id_dataset]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        dalObj.executeInsert()


