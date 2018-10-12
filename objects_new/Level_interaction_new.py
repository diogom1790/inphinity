# -*- coding: utf-8 -*-
"""
Created on Fri Jan 5 14:16:59 2018

@author: Diogo Leite
"""
from SQL_obj_new.Level_interaction_sql_new import _Level_interaction_sql_new

class Level_interaction(object):
    """
    This class treat the Level of interaction object has it exists in LEVEL_INTERACTIONS table database
    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, id_level_interaction = -1, designation = ""):
        """
        Constructor of the Level interaction object. All the parameters have a default value

        The values here are, e.g: Family, genus, species,... that correspond at the level of interaction known

        :param id_level_interaction: id of the leve interaction object - -1 if unknown
        :param designation: description of level of interaction

        :type id_level_interaction: int - not required
        :type designation: text - required 
        """
        self.id_level_interaction = id_level_interaction
        self.designation = designation

    def get_all_leve_interactions(self):
        """
        return an array with all the levels interactions in the database

        :return: array of level of interaction
        :rtype: array(Level_interaction)
        """
        list_of_li = []
        sqlObj = _Level_interaction_sql_new()
        results = sqlObj.select_all_level_interactions_all_attributes()
        for element in results:
            list_of_li.append(Level_interaction(element[0], element[1]))
        return list_of_li

    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d}, designation: {1}".format(self.id_level_interaction, self.designation)
        return message_str

