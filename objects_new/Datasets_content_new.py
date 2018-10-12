# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 11:47:53 2018

@author: Diogo Leite
"""

from SQL_obj_new.Datasets_content_sql_new import _Dataset_content_sql_new

class Dataset_content(object):
    """
    This class treat the Dataset_content object has it exists in DATASETS_CONTENT table database

    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, fk_id_couple = -1, fk_id_dataset = -1):
        """
        Constructor of the Datasets object. All the parameters have a default value

        :param fk_id_couple: id of the couple
        :param fk_id_dataset: id of the dataset

        :type fk_id_couple: int - required 
        :type fk_id_dataset: int - required 
        """
        self.fk_id_couple = fk_id_couple
        self.fk_id_dataset = fk_id_dataset

    def get_all_Datasets_content(self):
        """
        return an array with all the Datasets_content in the database

        :return: array of dataset_content
        :rtype: array(Dataset)
        """
        listOfDatasetContent = []
        sqlObj = _Dataset_content_sql_new(db_name = 'INPH_proj_out')
        results = sqlObj.select_all_datasets_content_all_attributes()
        for element in results:
            listOfDatasetContent.append(Dataset_content(element[0], element[1]))
        return listOfDatasetContent

    def get_all_Datasets_content_by_dataset_id(id_dataset):
        """
        return an array with all the Datasets_content in the database by a dataset id

        :return: array of dataset_content
        :rtype: array(Dataset)
        """
        listOfDatasetContent = []
        sqlObj = _Dataset_content_sql_new(db_name = 'INPH_proj_out')
        results = sqlObj.select_all_datasets_content_all_attributes_by_dataset_id(id_dataset)
        for element in results:
            listOfDatasetContent.append(Dataset_content(element[0], element[1]))
        return listOfDatasetContent

    def create_dataset_content(self):
        """
        Insert a Dataset_content in the database
        The Dataset_content contain:
        - fk_id_couple creation
        - fk_id_dataset

        """

        sqlObj = _Dataset_content_sql_new(db_name = 'INPH_proj_out')
        sqlObj.insert_dataset_content(self.fk_id_couple, self.fk_id_dataset)


    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "FK dataset: {0:d} FK couple: {1}".format(self.fk_id_dataset, self.fk_id_couple)
        return message_str