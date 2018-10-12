# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:36:21 2017

@author: Diogo Leite
"""

from SQL_obj_new.TypeOr_sql_new import _TypeOr_sql_new

class Type_OR(object):
    """
    This class treat the Types of organisms object has it exists in TYPE_ORGANISM table database
    By default, all FK are in the lasts positions in the parameters declaration

    les types d'organisms sont: Bacterium, phage,...

    """
    def __init__(self, id_type = -1, designation = ""):
        """
        Constructor of the Specie object. All the parameters have a default value

        :param id_type: id of the type of organism - -1 if unknown
        :param designation: designation of the type of organism

        :type id_type: int - not required 
        :type designation: text - required 
        """
        self.id_type = id_type
        self.designation = designation
        
    def get_all_Sources(self):
        """
        return an array with all the Sources in the database

        :return: array of Source
        :rtype: array(Source)
        """
        listOfTypesOr = []
        sqlObj = _TypeOr_sql_new()
        results = sqlObj.select_all_typesOr_all_attributes()
        for element in results:
            listOfTypesOr.append(Type_OR(element[0], element[1]))
        return listOfTypesOr

    def __str__(self):
        """
        Ovewrite of the str method
        """
        message_str = "ID: {0:d} Type of Organism: {1}".format(self.id_type, self.designation)
        return message_str

        