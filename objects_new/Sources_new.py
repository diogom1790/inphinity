# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:31:49 2017

@author: Diogo Leite
"""
from SQL_obj_new.Source_sql_new import _Source_sql_new


class Source(object):
    """
    This class treat the Sources object has it exists in SOURCES table database
    By default, all FK are in the lasts positions in the parameters declaration

    The sources are, e.g. Aitana,Grég, Xavier,...

    les sources sont les gens qui nous ont fournit les données (Aitana, Grég, Xavier,...)

    """
    def __init__(self, id_source = -1, designation = ""):
        """
        Constructor of the Source object. All the parameters have a default value

        :param id_source: id of the source - -1 if unknown
        :param designation: designation of the source

        :type id_source: int - not required 
        :type designation: text - required 
        """
        self.id_source = id_source
        self.designation = designation
        
    def get_all_Sources(self):
        """
        return an array with all the Sources in the database

        :return: array of sources
        :rtype: array(Source)
        """
        listOfSources = []
        sqlObj = _Source_sql_new()
        results = sqlObj.select_all_sources_all_attributes()
        for element in results:
            listOfSources.append(Source(element[0], element[1]))
        return listOfSources

    def __str__(self):
        """
        Ovewrite of the str method
        """
        message_str = "ID: {0:d} Name: {1}".format(self.id_source, self.designation)
        return message_str

        