# -*- coding: utf-8 -*-
"""
Created on Wen Apr 11 10:38:22 2018

@author: Diogo Leite
"""

from DAL import *
from configuration.configuration_data import *

class _DB_interaction_DDI_SQL(object):
    """
    This class manipulate the DB_INTERACTIONS_DDI table in the database. It used to know the sources that give the information of a DDI


    The FK are manipulated in the lasts positions of the parameters
    """

    def __init__(self):
        self.db_name = self.get_database_name()

    def get_database_name(self):
        """
        This method is used to get the database name used in factory

        :return: database name
        :rtype string
        """
        conf_data_obj = Configuration_data('INPHINITY')
        db_name = conf_data_obj.get_database_name()
        return db_name

    def select_all_sources_DDI_name(self):
        """
        return all the sources of DDIs

        :return: cursor with all sources DDI
        :rtype Cursor list
        """
        sql_string = "SELECT id_db_int_DBI, designation_DBI FROM DB_INTERACTIONS_DDI"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def insert_DDI_source_return_id(self, DDI_source):
        """
        Insert a ddi_source WITHOUT ANY VERIFICATION.

        :param DDI_source: designation of source

        :type DDI_source: string - required 

        :return: id of the domain inserted
        :rtype int
        """
        sqlObj = "INSERT INTO DB_INTERACTIONS_DDI (designation_DBI) VALUES (%s)"
        params = [DDI_source]
        dalObj = DAL(self.db_name, sqlObj, params)
        results = dalObj.executeInsert()
        return results.lastrowid

    def insert_DDI_source_return_id_if_not_exists(self, DDI_source):
        """
        Insert a ddi_source if not exist else return its id

        :param DDI_source: designation of source

        :type DDI_source: string - required 

        :return: id of the DDI_source inserted
        :rtype int
        """
        id_DDI_source = self.get_id_DDI_source_by_name(DDI_source)
        if id_DDI_source == -1:
            sqlObj = "INSERT INTO DB_INTERACTIONS_DDI (designation_DBI) VALUES (%s)"
            params = [DDI_source]
            dalObj = DAL(self.db_name, sqlObj, params)
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            return id_DDI_source

    def get_id_DDI_source_by_name(self, DDI_source):
        """
        Return the id o a DDI source


        :param DDI_source: designation of DDI source

        :type DDI_source: string - required 

        :return: id of the interaction or -1 i don't exists
        :rtype int
        """

        sql_string = "SELECT id_db_int_DBI FROM DB_INTERACTIONS_DDI WHERE designation_DBI LIKE '" + str(DDI_source) + "'"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]