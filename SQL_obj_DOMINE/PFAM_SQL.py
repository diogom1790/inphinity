# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 13:28:58 2018

@author: Diogo
"""

from DAL import *

class _PFAM_sql(object):
    """

    This class manipulate the PFAM table in the database DOMINE

    Typically a domain is: PFXXXXX

    The FK are manipulated in the lasts positions of the parameters
    """

    def __init__(self, db_name = "domine_db_out"):
        self.db_name = db_name

    def get_all_domains(self):
        """
        return all the domains in the database DOMINE. Return only the id (PFXXXXX)

        :return: cursor with all domains
        :rtype Cursor list
        """
        sql_string = "select DomainAcc from PFAM"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results