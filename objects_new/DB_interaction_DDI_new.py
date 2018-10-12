# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:48:58 2018

@author: Diogo
"""

from SQL_obj_new.DB_interaction_DDI_sql_new import _DB_interaction_DDI_SQL

class DB_interaction_DDI(object):
    """
    This class treat the source that give the information about the DDI object has it exists in DB_interaction_DDI table database
    By default, all FK are in the lasts positions in the parameters declaration
    """  

    def __init__(self, id_db_int_DBI = -1, designation_source = "", database_name = "INPH_proj"):
        """
        Constructor of the DDI source data object. All the parameters have a default value

        :param id_db_int_DBI: id of DDI interaction - -1 if unknown
        :param designation_source: id of the domain A
        :param database_name: name of the database. See Factory_databases_access

        :type id_db_int_DBI: int - not required
        :type designation_source: int - required 
        :type database_name: text - required
        """
        self.id_db_int_DBI = id_db_int_DBI
        self.designation_source = designation_source
        self.database_name = database_name


    def get_all_DDI_sources(self):
        """
        return an array with all the DDI source in the database

        :return: array of DDI source
        :rtype: array(DB_interaction_DDI)
        """
        listOfDomainsSources = []
        sqlObj = _DB_interaction_DDI_SQL(db_name = self.database_name)
        results = sqlObj.select_all_sources_DDI_name()
        for element in results:
            listOfDomainsSources.append(DB_interaction_DDI(element[0], element[1]))
        return listOfDomainsSources

    def create_DDI_source(self):
        """
        Insert a DDI source in the database
        The ddi interaction have a:
        - designation of the source

        :return: id of the DDI source and update the id of the object
        :rtype int
        """
        sqlObj = _DB_interaction_DDI_SQL(db_name = self.database_name)
        value_interaction_id = sqlObj.insert_DDI_source_return_id(self.designation_source)
        self.id_db_int_DBI = value_interaction_id
        return value_interaction_id

    def create_DDI_source_if_not_exists(self):
        """
        Insert a DDI source in the database if not already exists
        The ddi interaction have a:
        - designation of the source

        :return: id of the DDI source and update the id of the object
        :rtype int
        """
        sqlObj = _DB_interaction_DDI_SQL(db_name = self.database_name)
        value_interaction_id = sqlObj.insert_DDI_source_return_id_if_not_exists(self.designation_source)
        self.id_db_int_DBI = value_interaction_id
        return value_interaction_id
