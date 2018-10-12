# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 11:47:53 2018

@author: Diogo Leite
"""

from time import gmtime, strftime
from SQL_obj_new.Dataset_sql_new import _Dataset_sql_new

class Dataset(object):
    """
    This class treat the Dataset object has it exists in DATASETS table database

    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, id_dataset = -1, date_time_creation = "", name_ds = "", FK_id_user = -1):
        """
        Constructor of the Datasets object. All the parameters have a default value

        :param id_dataset: id of the dataset - -1 if unknown
        :param date_time_creation: date and time of the dataset creation
        :param name_ds: name of the dataset - -1 if unknown
        :param FK_id_user: FK of the user who create the dataset -1 if unknown

        :type id_dataset: int - not required 
        :type date_time_creation: text (datetime format) - required 
        :type name_ds: text - required
        :type FK_id_user: int - required
        """
        self.id_dataset = id_dataset
        self.date_time_creation = date_time_creation
        self.name_ds = name_ds
        self.FK_id_user = FK_id_user

    def get_all_Datasets(self):
        """
        return an array with all the Datasets in the database

        :return: array of dataset
        :rtype: array(Dataset)
        """
        listOfDataset = []
        sqlObj = _Dataset_sql_new(db_name = 'INPH_proj_out')
        results = sqlObj.select_all_datasets_all_attributes()
        for element in results:
            listOfDataset.append(Dataset(element[0], element[1], element[2], element[3]))
        return listOfDataset

    def create_dataset(self):
        """
        Insert a Dataset in the database return it id
        The Dataset contain:
        - date_time creation
        - name
        - FK of the user

        :return: id dataset
        :rtype int
        """

        actual_date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        self.date_time_creation = actual_date_time

        sqlObj = _Dataset_sql_new(db_name = 'INPH_proj_out')
        value_dataset = sqlObj.insert_dataset(self.date_time_creation, self.name_ds, self.FK_id_user)
        self.id_dataset = value_dataset
        return value_dataset

    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d} creation date: {1} name: {2} FK user: {3}".format(self.id_dataset, self.date_time_creation, self.name_ds, self.FK_id_user)
        return message_str