# -*- coding: utf-8 -*-
"""
Created on Wen Mar 28 11:47:46 2018

@author: Diogo Leite
"""

from DAL import *
from configuration.configuration_data import *

class _Domains_ds_sql_new(object):
    """
    This class manipulate the DOMAINS_DS table in the database. This table create diferents configurations according the domains scores

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

    def select_all_domains_ds_all_attributes(self):
        """
        return all the Domains_ds configurations in the database

        :return: cursor with all domains_ds
        :rtype Cursor list
        """
        sql_string = "SELECT id_domains_ds_DD, range_DD, auto_split_DD, nomralization_data_DD, FK_id_configuration_CF_DD, FK_id_user_US_DD FROM DOMAINS_DS"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_domains_ds_all_attributes_by_config_id(self, FK_id_config):
        """
        :param FK_id_config: Id of the configuration

        :type FK_id_config: int - required 

        return all the Domains_ds configurations in the database given a configuration ID

        :return: cursor with all domains_ds
        :rtype Cursor list
        """
        sql_string = "SELECT id_domains_ds_DD, range_DD, auto_split_DD, nomralization_data_DD, FK_id_configuration_CF_DD, FK_id_user_US_DD FROM DOMAINS_DS WHERE FK_id_configuration_CF_DD = " + str(FK_id_config)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def insert_domains_ds_config(self, range_DD, auto_split_DD, nomralization_data_DD, id_user, id_configuration):
        """
        Insert a dataset

        :param range_DD: size of the range
        :param auto_split_DD: SK-leanr automatic split
        :param nomralization_data_DD: normalize the data
        :param id_user: FK of the user
        :param id_configuration: FK of the configuration

        :type range_DD: int - required 
        :type auto_split_DD: int - required 
        :type nomralization_data_DD: int - required 
        :type id_user: int - required 
        :type id_configuration: int - required 

        :return: id of the dataset_ds inserted
        :rtype int
        """
        
        sql_string = "INSERT INTO DOMAINS_DS (range_DD, auto_split_DD, nomralization_data_DD, FK_id_user_US_DD, FK_id_configuration_CF_DD) VALUES (%s, %s, %s, %s, %s)"
        dalObj = DAL(self.db_name, sql_string)
        params = [range_DD, auto_split_DD, nomralization_data_DD, id_user, id_configuration]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()
        return results.lastrowid
