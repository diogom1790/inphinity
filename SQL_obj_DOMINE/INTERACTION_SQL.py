# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 14:53:58 2018

@author: Diogo
"""

from DAL import *
from configuration.configuration_data import *

class _Interactions_sql(object):
    """

    This class manipulate the INTERACTION table in the database DOMINE

    Typically a domain is: PFXXXXX

    The FK are manipulated in the lasts positions of the parameters
    """

    def __init__(self, db_name = "domine_db_out"):
        self.db_name = self.get_database_name()

    def get_database_name(self):
        """
        This method is used to get the database name used in factory

        :return: database name
        :rtype string
        """
        conf_data_obj = Configuration_data('DOMINE')
        db_name = conf_data_obj.get_database()
        return db_name

    def get_all_interactions(self):
        """
        return all the interactions as in INTERACTION table in DOMINE database

        :return: cursor with all domains
        :rtype Cursor list
        """
        sql_string = "select Domain1, Domain2, iPfam, 3did, ME, RCDP, Pvalue, Fusion, DPEA, PE, GPE, DIPD, RDFF, KGIDDI, INSITE, DomainGA, PP, PredictionConfidence, SameGO from INTERACTION"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_domain_interaction_by_pfam(self, pfam_designation):
        """
        return all the DDI interactions in the DOMINE database given a pfam

        :return: cursor with all DDI
        :rtype Cursor list
        """
        sql_string = "select DISTINCT Domain1, Domain2, iPfam, 3did, ME, RCDP, Pvalue, Fusion, DPEA, PE, GPE, DIPD, RDFF, KGIDDI, INSITE, DomainGA, PP, PredictionConfidence, SameGO from INTERACTION Where Domain1 LIKE '" + str(pfam_designation) + "%' or Domain2 LIKE '" + str(pfam_designation) + "%'"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results