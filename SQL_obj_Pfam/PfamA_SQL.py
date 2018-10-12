# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 10:27:58 2018

@author: Diogo
"""



from DAL import *


class _pfamA_SQL(object):
    """
    This class manipulate the Pfam table in the database PFAM

    Typically a domain is: PFXXXXX

    The FK are manipulated in the lasts positions of the parameters
    """

    def __init__(self, db_name = "pfam_db_out"):
        self.db_name = db_name

    def get_all_pfam_acc(self):
        """
        return all the pfam in the database PFAM. Return only tha ACC

        :return: cursor with all pfam interactions
        :rtype Cursor list
        """
        sql_string = "SELECT DISTINCT pfamA_acc FROM pfamA"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results