# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 11:27:58 2018

@author: Diogo
"""

from DAL import *
from configuration.configuration_data import *


class _DDI_interaction_view_sql(object):
    """
    TODO: You need to create a view: 
    
    CREATE VIEW ddi_interactions_id AS select (select Pfam_id from Domain WHERE Name = DDI1.domain1) as 'domain A', (select Pfam_id from Domain WHERE Name = DDI1.domain2) as 'domain B' from DDI1;

    This class manipulate the pfam interactions VIEW interactions in the database 3did

    Typically a domain is: PFXXXXX

    The FK are manipulated in the lasts positions of the parameters
    """

    def __init__(self, db_name = "3did_db_out"):
        self.db_name = self.get_database_name()

    def get_database_name(self):
        """
        This method is used to get the database name used in factory

        :return: database name
        :rtype string
        """
        conf_data_obj = Configuration_data('3DID')
        db_name = conf_data_obj.get_database()
        return db_name

    def get_all_pfam_interactions(self):
        """
        return all the pfam interactions in the database 3DID. Return only the ACC

        :return: cursor with all pfam interactions
        :rtype Cursor list
        """
        sql_string = "SELECT DISTINCT domain_A, domain_B domain FROM ddi_interactions_id"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_pfam_interactions_by_pfam(self, pfam_designation):
        """
        return all the pfam interactions in the 3DID database given a pfam

        :return: cursor with all pfam interactions
        :rtype Cursor list
        """
        sql_string = "select DISTINCT * from ddi_interactions_id Where domain_A LIKE '" + str(pfam_designation) + "%' or domain_B LIKE '" + str(pfam_designation) + "%'"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results


