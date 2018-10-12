# -*- coding: utf-8 -*-
"""
Created on Tue Mai 15 11:09:22 2018

@author: Diogo Leite
"""

from SQL_obj_new.Datasets_configurations_types_sql_new import _Datasets_config_types_SQL

class DS_configurations_types(object):
    """
    This class treat the configurations type available for the datasets creation

    By default, all FK are in the lasts positions in the parameters declaration
    """ 

    def __init__(self, id_dataset_conf_type = -1, designation = ""):
        """
        Constructor of the DS_configurations_types object. All the parameters have a default value

        :param id_dataset_conf_type: id of dataset_configuration_type - -1 if unknown
        :param designation: designation of the configuration type - "" if unknown

        :type id_dataset_conf_type: int - not required
        :type designation: text - required 
        """

        self.id_dataset_conf_type = id_dataset_conf_type
        self.designation = designation

    def get_all_configurations_ds_types():
        """
        return an array with all the dataset configurations types in the database

        :return: array of dataset configuration type
        :rtype: array(DS_configurations_types)
        """
        listOfdsConfType = []
        sqlObj = _Datasets_config_types_SQL()
        results = sqlObj.select_all_Datasets_conf_type()
        for element in results:
            listOfdsConfType.append(DS_configurations_types(element[0], element[1]))
        return listOfdsConfType        


    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d} Configuration type: {1}".format(self.id_dataset_conf_type, self.designation)
        return message_str