# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:13:14 2017

@author: Diogo Leite
"""

from DAL import *
from configuration.configuration_data import *

class _Family_sql_new(object):
    """
    This class manipulate the FAMILIES table in the database

    The FK are manipulated in the lasts positions of the parameters
    """
    def __init__(self):
        """
        Constructor of the Family_sql object. All the parameters have a default value

        :param db_name: name of the database to do the ACID methods

        :type db_name: string - no required
        """

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
        
    def select_all_families_all_attributes(self):
        """
        return all the Families in the database

        :return: cursor with all families
        :rtype Cursor list
        """
        sql_string = "SELECT * FROM FAMILIES"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results
    
    def insert_family_if_not_exist(self, familyName):
        """
        Insert a Family if it not yet exist (based on the designation)

        :param familyName: designation of the family

        :type familyName: string - required 

        :return: id of the family inserted
        :rtype int
        """
        id_family = self.get_id_family_by_designation(familyName)
        if id_family == -1:
            sql_string = "INSERT INTO FAMILIES (designation_FA) VALUES (%s)"
            dalObj = DAL(self.db_name, sql_string)
            params = [familyName]
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            print("It already exists a Family with the name: " + str(familyName))
            return id_family

    def get_id_family_by_designation(self, familyName):
        """
        get the id of a family based on its designation

        :param familyName: designation of the family

        :type familyName: string - required 

        :return: id of the family or -1 if inexistant
        :rtype int
        """

        sql_string = "SELECT id_family_FA FROM FAMILIES WHERE designation_FA = '" + str(familyName) + "'"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]

    def get_family_by_id(self, id_genus):
        """
        Get a family by its id

        :return: Family elements info
        :rtype List(infos family)
        """
        sql_string = "SELECT id_family_FA, designation_FA FROM FAMILIES WHERE id_family_FA = " + str(id_genus)
        dalobj = DAL(self.db_name, sql_string)
        results = dalobj.executeSelect()

        return results[0]
        
        
