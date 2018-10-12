# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:09:49 2018

@author: Diogo Leite
"""


from DAL import *
from configuration.configuration_data import *

class _Configuration_sql_new(object):
    """
    This class manipulate the CONFIGURATIONS table in the database

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


    def select_all_configurations_content_all_attributes(self):
        """
        return all the configurations of the datasets in the database

        :return: cursor with all Datasets_content
        :rtype Cursor list
        """
        sql_string = "SELECT id_conf_ds_CF, date_time_creation_CF, designation_CF, FK_id_DS_CF, FK_id_user_US_DD FROM CONFIGURATIONS"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def insert_configuration(self, date_time_creation, designation, id_ds, id_user):
        """
        Insert a dataset

        :param date_time_creation: date and time of the creation (actual)
        :param designation: configuration name
        :param id_ds: FK of the DS
        :param id_user: FK of the user

        :type date_time_creation: string (datetime sql format) - required 
        :type name: string - required 
        :type id_ds: int - required 
        :type id_user: int - required 

        :return: id of the dataset inserted
        :rtype int
        """
        
        sql_string = "INSERT INTO CONFIGURATIONS (date_time_creation_CF, designation_CF, FK_id_DS_CF, FK_id_user_US_DD) VALUES (%s, %s, %s, %s)"
        dalObj = DAL(self.db_name, sql_string)
        params = [date_time_creation, designation, id_ds, id_user]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()
        return results.lastrowid
