# -*- coding: utf-8 -*-
"""

@author: Diogo Leite
"""

from SQL_obj_new.Domains_ds_sql_new import _Domains_ds_sql_new

class Domains_ds(object):
    """
    This class treat the Domains_ds configuration object has it exists in DOMAINS_DS table database

    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, id_domains_ds_DD = -1, range_DD = -1, auto_split_DD = False, nomralization_data_DD = False, FK_id_configuration_CF_DD = -1, FK_id_user_US_DD = -1):
        """
        Constructor of the Datasets object. All the parameters have a default value

        :param id_domains_ds_DD: id of the domains configuration - -1 if unknown
        :param range_DD: size of the range used in the splie
        :param auto_split_DD: bool used to inform if you want to have an automatic split (by interaction) [True = yes, False = no]
        :param nomralization_data_DD: bool used to inform if you want to normalize the data [True = yes, False = no]
        :param FK_id_configuration_CF_DD: FK of the configuration table
        :param FK_id_user_US_DD: FK of the user who create the configuration

        :type id_domains_ds_DD: int - not required 
        :type range_DD: int - required 
        :type auto_split_DD: bool - required
        :type nomralization_data_DD: bool - required
        :type FK_id_configuration_CF_DD: int - required
        :type FK_id_user_US_DD: int - required
        """
        self.id_domains_ds_DD = id_domains_ds_DD
        self.range_DD = range_DD
        self.auto_split_DD = auto_split_DD
        self.nomralization_data_DD = nomralization_data_DD
        self.FK_id_configuration_CF_DD = FK_id_configuration_CF_DD
        self.FK_id_user_US_DD = FK_id_user_US_DD

    def get_all_domains_configurations(self):
        """
        return an array with all the Datasets in the database

        :return: array of dataset
        :rtype: array(Dataset)
        """
        listOfDomainConfiguration = []
        sqlObj = _Domains_ds_sql_new(db_name = 'INPH_proj_out')
        results = sqlObj.select_all_domains_ds_all_attributes()
        for element in results:
            listOfDomainConfiguration.append(Domains_ds(element[0], element[1], element[2], element[3], element[4], element[5]))
        return listOfDomainConfiguration

    def get_domains_config_by_config_id(FK_id_configuration_CF_DD):
        """
        return an array with all the Datasets in the database

        :param FK_id_configuration_CF_DD: Id of the configuration

        :type FK_id_configuration_CF_DD: int - required 

        :return: array of dataset
        :rtype: array(Dataset)
        """
        listOfDomainConfiguration = []
        sqlObj = _Domains_ds_sql_new(db_name = 'INPH_proj_out')
        results = sqlObj.select_all_domains_ds_all_attributes_by_config_id(FK_id_configuration_CF_DD)
        for element in results:
            listOfDomainConfiguration.append(Domains_ds(element[0], element[1], element[2], element[3], element[4], element[5]))
        return listOfDomainConfiguration

    def create_domain_configuration(self):
        """
        Insert a Dataset in the database return it id
        The Dataset contain:
        - range_DD creation
        - auto_split_DD
        - nomralization_data_DD
        - FK_id_configuration_CF_DD
        - FK of the user

        :return: id dataset
        :rtype int
        """

        sqlObj = _Domains_ds_sql_new(db_name = 'INPH_proj_out')
        value_dataset = sqlObj.insert_domains_ds_config(self.range_DD, self.auto_split_DD, self.nomralization_data_DD, self.FK_id_user_US_DD, self.FK_id_configuration_CF_DD)
        self.id_dataset = value_dataset
        return value_dataset


    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d}, Range: {1}, Auto split: {2}, Normalization: {3}, FK user: {4}, FK configuration: {5}".format(self.id_domains_ds_DD, self.range_DD, self.auto_split_DD, self.nomralization_data_DD, self.FK_id_user_US_DD, self.FK_id_configuration_CF_DD)
        return message_str
