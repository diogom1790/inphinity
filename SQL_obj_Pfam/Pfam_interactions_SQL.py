# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 09:41:58 2018

@author: Diogo
"""


from DAL import *
from configuration.configuration_data import *

class _pfamA_interactions(object):
    """
    This class manipulate the _pfamA_interactions table in the database PFAM

    Typically a domain is: PFXXXXX

    The FK are manipulated in the lasts positions of the parameters
    """

    def __init__(self, db_name = "pfam_db_out"):
        self.db_name = self.get_database_name()

    def get_database_name(self):
        """
        This method is used to get the database name used in factory

        :return: database name
        :rtype string
        """
        conf_data_obj = Configuration_data('iPFAM')
        db_name = conf_data_obj.get_database()
        return db_name


    def select_all_pfam_interactions(self):
        """
        return all the pfam interactions in the database PFAM

        :return: cursor with all pfam interactions
        :rtype Cursor list
        """
        sql_string = "SELECT * FROM pfamA_interactions"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_pfam_interactions_by_pfam(self, pfam_designation):
        """
        return all the pfam interactions in the PFAM database given a pfam

        :return: cursor with all pfam interactions
        :rtype Cursor list
        """
        sql_string = "select DISTINCT * from pfamA_interactions Where pfamA_acc_A = '" + str(pfam_designation) + "' or pfamA_acc_B = '" + str(pfam_designation) + "'"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results
