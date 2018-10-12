# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 13:28:58 2018

@author: Diogo
"""

from DAL import *

class _Domain_sql(object):
    """

    This class manipulate the Domains table in the database 3did

    Typically a domain is: PFXXXXX

    The FK are manipulated in the lasts positions of the parameters
    """

    def __init__(self, db_name = "3did_db_out"):
        self.db_name = db_name

    def get_all_domains(self):
        """
        return all the domains in the database 3DID. Return only the id (PFXXXXX.XX)

        :return: cursor with all domains
        :rtype Cursor list
        """
        sql_string = "select Pfam_id from Domain"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results