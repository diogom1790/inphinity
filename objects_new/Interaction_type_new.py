# -*- coding: utf-8 -*-
"""
Created on Fri Jan 5 15:12:06 2018

@author: Diogo Leite
"""

from SQL_obj_new.Interaction_type_sql_new import _Interaction_type_sql_new

class Interaction_type(object):
    """
    This class treat the Level of interaction object has it exists in INTERACTIONS_TYPES table database
    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, id_interaction_type = -1, designation = ""):
        """
        Constructor of the Interaction type object. All the parameters have a default value

        The values here are, e.g: verified, unknown verification, not verified,.. This correspond to the information about the confirmation of a given interaction in laboratory

        :param id_interaction_type: id of the interaction type - -1 if unknown
        :param designation: description of interaction type

        :type id_interaction_type: int - not required
        :type designation: text - required 
        """
        self.id_interaction_type = id_interaction_type
        self.designation = designation

    def get_all_interactions_type(self):
        """
        Return all the interaction types int the database

        :return: array of interaction type
        :rtype: array(Interaction_type)
        """
        listOfIT = []
        sqlObj = _Interaction_type_sql_new()
        results = sqlObj.select_all_interaction_type_all_attributes()
        for element in results:
            listOfIT.append(Interaction_type(element[0], element[1]))
        return listOfIT

    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d}, designation: {1}".format(self.id_interaction_type, self.designation)
        return message_str