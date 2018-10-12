# -*- coding: utf-8 -*-
"""
@author: Diogo Leite
"""

from SQL_obj_new.Source_data_sql_new import _Source_data_sql_new

class Source_data(object):
    """
    This class treat the Source of data object has it exists in SOURCE_DATA table database
    By default, all FK are in the lasts positions in the parameters declaration

    The data sources are, e.g. NCBI, RAST, PhageDB,...


    """

    def __init__(self, id_source_data = -1, designation = ""):
        """
        Constructor of the source_data object. All the parameters have a default value

        :param id_source_data: id of the source - -1 if unknown
        :param designation: designation od the source

        :type id_source: int - not required 
        :type designation:  text - required 

        """
        self.id_source_data = id_source_data
        self.designation = designation


    def get_all_Source_data():
        """
        return an array with all the source_data in the database

        :return: array of Source_data
        :rtype: array(Source_data)
        """

        listOfSourceData = []
        sqlObj = _Source_data_sql_new(db_name = 'INPH_proj_out')
        results = sqlObj.select_all_data_sources_all_attributes()
        for element in results:
            listOfSourceData.append(Source_data(element[0], element[1]))
        return listOfSourceData


    def __str__(self):
        """
        Ovewrite of the str method
        """
        message_str = "ID: {0:d} Data Srouce: {1}".format(self.id_source_data, self.designation)
        return message_str

        

