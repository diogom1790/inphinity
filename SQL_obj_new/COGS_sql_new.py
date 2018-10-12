# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:38:22 2018

@author: Diogo Leite
"""

#https://github.com/chapmanb/bcbio-nextgen/blob/master/bcbio/hmmer/search.py

from DAL import *
from configuration.configuration_data import *


class _COGS_sql_new(object):
    """
    This class manipulate the COGS table in the database

    Typically a COG is: COGXXXX

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

    def select_all_cogs_all_attributes(self):
        """
        return all the cogs in the database

        :return: cursor with all cogs
        :rtype Cursor list
        """
        sql_string = "SELECT * FROM COGS"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def insert_cog_return_id(self, designation_cog):
        """
        Insert a COG WITHOUT ANY VERIFICATION

        :param designation_cog: designation of the COG

        :type designation_cog: string - required 

        :return: id of the cog inserted
        :rtype int
        """
        sqlObj = "INSERT INTO COGS (designation_CO) VALUES (%s)"
        params = [designation_cog]
        dalObj = DAL(self.db_name, sqlObj, params)
        results = dalObj.executeInsert()
        return results.lastrowid

    def get_id_cog_by_description(self, designation_cog):
        """
        get the id of a cog based on its description

        :param designation_cog: designation of the cog

        :type designation_cog: string - required 

        :return: id of the cog or -1 if inexistant
        :rtype int
        """

        sql_string = "SELECT id_cog_CO FROM COGS WHERE designation_CO = '" + str(designation_cog) + "'"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]

    def insert_cog_if_not_exists(self, designation_cog):
        """
        Insert a COG if it not yet exist (based on the designation)

        :param designation_cog: designation of the COG

        :type designation_cog: string - required 

        :return: id of the cog inserted
        :rtype int
        """
        id_cog = self.get_id_cog_by_description(designation_cog)
        if id_cog == -1 :
            sql_string = "INSERT INTO COGS (designation_CO) VALUES (%s)"
            dalObj = DAL(self.db_name, sql_string)
            params = [designation_cog]
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            print("The COG {0} already extis in the database".format(designation_cog))
            return id_cog