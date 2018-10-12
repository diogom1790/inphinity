# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 10:30:14 2018

@author: Diogo
"""

from SQL_obj_Pfam.PfamA_SQL import _pfamA_SQL

class Pfam_pfamDB(object):
    """
    This class treat the pfam object has it exists in pfamA table database Pfam

    By default, all FK are in the lasts positions in the parameters declaration
    """  

    def __init__(self, pfam_designation = "", database_name = "pfam_db_out"):
        """

        NOTE: I don't put all the 15 attributes, just those that i need

        Constructor of the pfamA object. All the parameters have a default value

        :param pfam_designation: name of the domain (PFXXXXX)
        :param database_name: name of the database. See Factory_databases_access

        :type pfam_designation: text - required
        :type database_name: text - required
        """
        self.pfam_designation = pfam_designation
        self.database_name = database_name

    def get_all_pfam_only_Acc():
        """
        return an array with all the pfam in the database Pfam

        :return: array of pfam
        :rtype: array(Pfam)
        """
        listOfPfamInteractions = []
        sqlObj = _pfamA_SQL(db_name = 'pfam_db_out')
        results = sqlObj.get_all_pfam_acc()
        for element in results:
            listOfPfamInteractions.append(Pfam_pfamDB(element[0]))
        return listOfPfamInteractions

    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "Pfam Acc: {0}".format(self.pfam_designation)
        return message_str