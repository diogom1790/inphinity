# -*- coding: utf-8 -*-
"""
Created on Tue Mai 15 11:34:22 2018

@author: Diogo Leite
"""

from SQL_obj_new.Dataset_config_dataset_new_sql import _DS_config_DS_SQL

class Dataset_conf_ds(object):
    """
    This class treat the datasets configuration connection tables object has it exists in DATASET_CONF_DS table database

    NOTE: It consistes on a conection class (N to N) to know for each dataset with a given configuration

    By default, all FK are in the lasts positions in the parameters declaration
    """ 

    def __init__(self, id_ds_conf_ds = -1, value_configuration = -1, FK_id_configuration_DCT_DCD = -1, FK_id_dataset_DS_DCD = -1):
        """
        Constructor of the DDI_interactionDB object. All the parameters have a default value

        :param id_ds_conf_ds: id of the configurations dataset - -1 if unknown
        :param value_configuration: value of the bins - -1 if unknown
        :param FK_id_configuration_DCT_DCD: FK of the configurations (see table DATASET_CONFIGURATIONS_TYPES)- -1 if unknown
        :param FK_id_dataset_DS_DCD: FK of the dataset (see table DATASETS)

        :type id_ds_conf_ds: int - not required
        :type value_configuration: int - not required
        :type FK_id_configuration_DCT_DCD: text (date format) - required 
        :type FK_id_dataset_DS_DCD: int - required 
        """

        self.id_ds_conf_ds = id_ds_conf_ds
        self.value_configuration = value_configuration
        self.FK_id_configuration_DCT_DCD = FK_id_configuration_DCT_DCD
        self.FK_id_dataset_DS_DCD = FK_id_dataset_DS_DCD

    def get_all_datasets_conf_ds():
        """
        return an array with all the configurations of datasets in the database

        :return: array of datasets configurations
        :rtype: array(DDI_interaction_DB)
        """
        listOfDatasetDSConfig = []
        sqlObj = _DS_config_DS_SQL()
        results = sqlObj.select_all_DDI_DB()
        for element in results:
            listOfDatasetDSConfig.append(Dataset_conf_ds(element[0], element[1], element[2], element[3]))
        return listOfDatasetDSConfig

    def create_ds_config_ds(self):
        """
        Insert a dataset configuration of Dataset in the database return it id
        The ds_conf_ds contain:
        - value of the creation
        - FK of the configuration
        - FK of the dataset

        :return: id Dataset_conf_ds
        :rtype int
        """


        sqlObj = _DS_config_DS_SQL()
        value_id_ds_conf_ds = sqlObj.insert_DS_conf_DS_return_id_if_not_exists(self.value_configuration, self.FK_id_configuration_DCT_DCD, self.FK_id_dataset_DS_DCD)
        
        self.id_ds_conf_ds = value_id_ds_conf_ds
        return value_id_ds_conf_ds