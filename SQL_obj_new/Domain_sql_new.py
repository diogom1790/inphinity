# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:38:22 2017

@author: Diogo Leite
"""

#https://github.com/chapmanb/bcbio-nextgen/blob/master/bcbio/hmmer/search.py

from DAL import *
from configuration.configuration_data import *

class _Domain_sql_new(object):
    """
    This class manipulate the DOMAINS table in the database

    Typically a domain is: PFXXXXX

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
        
    def select_all_domains_all_attributes(self):
        """
        return all the Domains in the database

        :return: cursor with all domains
        :rtype Cursor list
        """
        sql_string = "SELECT * FROM DOMAINS"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results
    
    def insert_domain_return_id(self, designation_domain):
        """
        Insert a DOMAIN WITHOUT ANY VERIFICATION

        :param designation_domain: designation of the domain

        :type designation_domain: string - required 

        :return: id of the domain inserted
        :rtype int
        """
        sqlObj = "INSERT INTO DOMAINS (designation_DO) VALUES (%s)"
        params = [designation_domain]
        dalObj = DAL(self.db_name, sqlObj, params)
        results = dalObj.executeInsert()
        return results.lastrowid
    
    def insert_domain_if_not_exists(self, designation_domain):
        """
        Insert a DOMAIN if it not yet exist (based on the designation)

        :param designation_domain: designation of the domain

        :type designation_domain: string - required 

        :return: id of the domain inserted
        :rtype int
        """
        id_domain = self.get_id_domain_by_description(designation_domain)
        if id_domain == -1 :
            sql_string = "INSERT INTO DOMAINS (designation_DO) VALUES (%s)"
            print(self.db_name)
            dalObj = DAL(self.db_name, sql_string)
            params = [designation_domain]
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            print("The domain {0} already extis in the database".format(designation_domain))
            return id_domain

    def get_id_domain_by_description(self, designation_domain):
        """
        get the id of a domain based on its description

        :param designation_domain: designation of the domain

        :type designation_domain: string - required 

        :return: id of the domain or -1 if inexistant
        :rtype int
        """

        sql_string = "SELECT id_domain_DO FROM DOMAINS WHERE designation_DO = '" + str(designation_domain) + "'"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]