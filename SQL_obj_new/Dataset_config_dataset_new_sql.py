# -*- coding: utf-8 -*-
"""
Created on Tue Mai 15 11:31:22 2018

@author: Diogo Leite
"""

from DAL import *
from configuration.configuration_data import *

class _DS_config_DS_SQL(object):
    """
    This class manipulate the Dataset_config_dataset table in the database. It used to know from which DDB coms the information of the DDI

    NOTE: it is a connection table (N to N)

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

    def select_dataset_conf_ds(self):
        """
        return all the connections dataset_conf_dataset

        :return: cursor with all sources dataset_conf_dataset
        :rtype Cursor list
        """
        sql_string = "SELECT id_ds_conf_ds_DCD, value_config_DCD, FK_id_configuration_DCT_DCD, FK_id_dataset_DS_DCD FROM DATASET_CONF_DS"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def insert_DS_conf_DS_return_id_if_not_exists(self, value_configuration, FK_id_configuration_DCT_DCD, FK_id_dataset_DS_DCD):
        """
        Insert a ddi_source WITHOUT ANY VERIFICATION.

        :param value_bins: value of the configuration
        :param FK_id_configuration_DCT_DCD: FK of the configuration
        :param FK_id_dataset_DS_DCD: FK of the dataset

        :type value_bins: int - required 
        :type FK_id_configuration_DCT_DCD: int - required 
        :type FK_id_dataset_DS_DCD: int - required 


        :return: id of the dataset configuration inserted or ID of the existant
        :rtype int
        """
        id_conf_ds = self.get_id_ds_conf_ds_by_value_and_fks(value_configuration, FK_id_configuration_DCT_DCD, FK_id_dataset_DS_DCD)
        if id_conf_ds == -1:
            sqlObj = "INSERT INTO DATASET_CONF_DS (value_config_DCD, FK_id_configuration_DCT_DCD, FK_id_dataset_DS_DCD) VALUES (%s, %s, %s)"
            params = [value_configuration, FK_id_configuration_DCT_DCD, FK_id_dataset_DS_DCD]
            dalObj = DAL(self.db_name, sqlObj, params)
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            return id_conf_ds


    def get_id_ds_conf_ds_by_value_and_fks(self, value_configuration, FK_id_configuration_DCT_DCD, FK_id_dataset_DS_DCD):
        """
        Return the id o a ds_conf_Ds


        :param value_configuration: value of the configurations
        :param FK_id_configuration_DCT_DCD: dFk of the configuration (DATASET_CONFIGURATIONS_TYPES)
        :param FK_id_dataset_DS_DCD: fk of the dataset (DATASETS)

        :type value_configuration: int - required 
        :type FK_id_configuration_DCT_DCD: int - required 
        :type FK_id_dataset_DS_DCD: int - required 

        :return: id of the DATASET_CONF_DS or -1 i don't exists
        :rtype int
        """

        sql_string = "SELECT id_ds_conf_ds_DCD FROM DATASET_CONF_DS WHERE value_config_DCD = '" + str(value_configuration) + "' AND FK_id_configuration_DCT_DCD = '" + str(FK_id_configuration_DCT_DCD)  + "' AND FK_id_dataset_DS_DCD = '" + str(FK_id_dataset_DS_DCD) + "'"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]