# -*- coding: utf-8 -*-
"""
Created on Fri Jan 5 16:03:17 2018

@author: Diogo Leite
"""

from SQL_obj_new.Lysis_type_sql_new import _Lysis_type_sql_new

class Lysis_type(object):
    """
    This class treat the of Lysis type object has it exists in F_SCORE_BLAST table database
    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__ (self, id_lysis_type = -1, designation = ""):
        """
        Constructor of the Lysis type object. All the parameters have a default value

        :param id_lysis_type: if of the lysis type - -1 if unknown
        :param designation: type of lysis designation

        :type id_lysis_type: int - not required 
        :type designation: text - required 
        """

        self.id_lysis_type = id_lysis_type
        self.designation = designation

    def get_all_lysis_type(self):
        """
        return an array with all the lysis type in the database

        :return: array of lysis type
        :rtype: array(Lysis_type)
        """
        listOfLT = []
        sqlObj = _Lysis_type_sql_new()
        results = sqlObj.select_all_LT_all_attributes()
        for element in results:
            listOfLT.append(Lysis_type(element[0], element[1]))
        return listOfLT


    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d} Type of lysis: {1}".format(self.id_lysis_type, self.designation)
        return message_str




