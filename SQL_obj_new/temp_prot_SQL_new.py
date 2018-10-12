# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:13:14 2017

@author: Diogo Leite
"""

from DAL import *
from configuration.configuration_data import *

class _temp_prot(object):

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


    def select_all_ids(self):
        """
        return all the Families in the database

        :return: cursor with all families
        :rtype Cursor list
        """
        sql_string = "SELECT * FROM temp_prots"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def insert_id_prots(self, id_prot):
        """
        Insert a Family if it not yet exist (based on the designation)

        :param familyName: designation of the family

        :type familyName: string - required 

        :return: id of the family inserted
        :rtype int
        """
        sql_string = "INSERT INTO temp_prots (id_prot) VALUES (%s)"
        dalObj = DAL(self.db_name, sql_string)
        params = [id_prot]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()