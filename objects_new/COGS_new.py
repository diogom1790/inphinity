# -*- coding: utf-8 -*-
"""
Created on Tue May 18 10:11:58 2018

@author: Diogo
"""

from SQL_obj_new.COGS_sql_new import _COGS_sql_new

class COG(object):

    """
    This class treat the COG object has it exists in COGS table database
    By default, all FK are in the lasts positions in the parameters declaration
    """ 

    def __init__(self, id_cog = -1, designation = ""):
        """
        Constructor of the Domain object. All the parameters have a default value

        :param id_cog: id of the cog - -1 if unknown
        :param designation: name of the domain (usualy COGXXXX)

        :type id_cog: int - not required
        :type designation: text - required 
        """
        self.id_cog = id_cog
        self.designation = designation

    def get_all_Cogs():
        """
        return an array with all the Cogs score in the database

        :return: array of cogs
        :rtype: array(COGS)
        """
        listOfCOGS = []
        sqlObj = _COGS_sql_new()
        results = sqlObj.select_all_cogs_all_attributes()
        for element in results:
            listOfCOGS.append(COG(element[0], element[1]))
        return listOfCOGS

    def create_COG(self):
        """
        Insert a COG in the database if not already exists
        The cog have a:
        - designation

        :return: id of the cog
        :rtype int
        """
        sqlObj = _COGS_sql_new()
        value_cog = sqlObj.insert_cog_if_not_exists(self.designation)
        self.id_cog = value_cog
        return value_cog

    def get_id_COG_by_description(description):
        """
        Return the id of an existing COG in the database based on its description
        The cog have a:
        - designation

        :return: id of the cog
        :rtype int
        """
        sqlObj = _COGS_sql_new()
        id_cog = sqlObj.get_id_cog_by_description(description)
        return id_cog