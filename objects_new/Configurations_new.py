# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 16:38:15 2018

@author: Diogo Leite
"""

from time import gmtime, strftime
from SQL_obj_new.Configurations_sql_new import _Configuration_sql_new

class Configuration(object):
    """
    This class treat the Dataset_content object has it exists in CONFIGURATIONS table database

    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, id_conf_ds_CF = -1, date_time_creation_CF = "", designation_CF = "", FK_id_DS_CF = -1, FK_id_user_US_DD = -1):
        """
        Constructor of the Configurations object. All the parameters have a default value

        :param id_conf_ds_CF: id of the configuration
        :param date_time_creation_CF: creation date of the configuration
        :param designation_CF: designation (name) of the configuration
        :param FK_id_DS_CF: id of the dataset
        :param FK_id_user_US_DD: id of the user

        :type fk_id_couple: int - required 
        :type date_time_creation_CF: datetime - required 
        :type designation_CF: string - required 
        :type FK_id_DS_CF: int - required 
        :type FK_id_user_US_DD: int - required 
        """
        self.id_conf_ds_CF = id_conf_ds_CF
        self.date_time_creation_CF = date_time_creation_CF
        self.designation_CF = designation_CF
        self.FK_id_DS_CF = FK_id_DS_CF
        self.FK_id_user_US_DD = FK_id_user_US_DD


    def get_all_configurations(self):
        """
        return an array with all the Configurations in the database

        :return: array of all the configurations
        :rtype: array(Configurations)
        """
        listOfCOnfigurations = []
        sqlObj = _Configuration_sql_new(db_name = 'INPH_proj_out')
        results = sqlObj.select_all_configurations_content_all_attributes()
        for element in results:
            listOfCOnfigurations.append(Configuration(element[0], element[1], element[2], element[3], element[4]))
        return listOfCOnfigurations


    def create_configurations(self):
        """
        Insert a Configuration in the database return it id
        The Dataset_content contain:
        - id_conf_ds_CF creation
        - date time of the creation
        - designation (name) of the configuration
        - Id of the dataset used into the configuration
        - Id of the user that creat the configuration

        :return: id configuration
        :rtype int
        """


        actual_date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        self.date_time_creation_CF = actual_date_time

        sqlObj = _Configuration_sql_new(db_name = 'INPH_proj_out')
        value_configuration = sqlObj.insert_configuration(self.date_time_creation_CF, self.designation_CF, self.FK_id_DS_CF, self.FK_id_user_US_DD)
        self.id_conf_ds_CF = value_configuration
        return value_configuration

    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d} creation date: {1} name: {2} FK user: {3} FK DS: {4}".format(self.id_conf_ds_CF, self.date_time_creation_CF, self.designation_CF, self.FK_id_DS_CF, self.FK_id_user_US_DD)
        return message_str