# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:01:54 2018

@author: Diogo
"""


from DAL import *
from configuration.configuration_data import *

class _F_score_domains_bloc_sql(object):
    """
    This class manipulate the feature of domains bloc used in the scores ddi table in the database. 

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

    def select_all_bloc_score_domain(self):
        """
        return all the domains score bloc in the database

        :return: cursor with all domains score bloc
        :rtype Cursor list
        """

        sql_string = "SELECT score_dom_bloc_id_FSD, designation_FSD, date_creation_FSD FROM F_SCORE_DOMAINS_BLOC"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def insert_bloc_score_domain(self, designation, create_date):
        """
        Insert a F_scor_blast in the database WHITOUT ANY VALIDATION

        :param designation: blast score
        :param create_date: date and time of the creation (actual)

        :type designation: string - required 
        :type create_date: string (datetime sql format) - required

        :return: id of the bloc score domain object inserted
        :rtype int
        """

        sql_string = "INSERT INTO F_SCORE_DOMAINS_BLOC (designation_FSD, date_creation_FSD) VALUES (%s, %s)"

        dalObj = DAL(self.db_name, sql_string)
        params = [designation, create_date]

        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()
        return results.lastrowid