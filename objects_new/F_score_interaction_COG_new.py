# -*- coding: utf-8 -*-
"""
Created on Fri Jan 5 16:46:12 2018

@author: Diogo Leite
"""

from SQL_obj_new.F_score_interaction_COG_sql_new import _F_score_COG_sql

class F_score_interaction_COG(object):
    """
    This class treat the Feature of score COG object has it exists in F_SCORE_BLAST table database
    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, id_f_score_cog = -1, score_result = -1, FK_id_couple = -1):
        """
        Constructor of the Score COG object. All the parameters have a default value

        :param id_f_score_cog: id of the COG score - -1 if unknown
        :param score_result: spcre COG
        :param fk_id_couple: couple FK key - -1 if unknown

        :type id_f_score_cog: int - required
        :type score_result: int - required 
        :type fk_id_couple: int - required
        """
        self.id_f_score_cog = id_f_score_cog
        self.score_result = score_result
        self.FK_id_couple = FK_id_couple

    def get_all_f_COG_score(self):
        """
        return an array with all the COG score in the database

        :return: array of score
        :rtype: array(F_score_interaction_COG)
        """
        listOfCOGScore = []
        sqlObj = _F_score_COG_sql()
        results = sqlObj.select_all_score_COG_all_attributes()
        for element in results:
            listOfCOGScore.append(F_score_interaction_COG(element[0], element[1], element[2]))
        return listOfCOGScore

    def create_COG_score(self):
        """
        Insert a f_score_COG in the database WITHOUT ANY VERIFICATION
        
        The id of the f_score_COG is updated

        :return: id of the f_score_COG created
        :rtype: int
        """

        value_f_score_COG = None
        sqlObj = _F_score_COG_sql()
        value_f_score_COG = sqlObj.insert_f_score_COG(self.score_result, self.FK_id_couple)
        self.id_f_score_cog = value_f_score_COG
        return value_f_score_COG

    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d}, fk couple: {1:d}, score: {1:d} ".format(self.id_f_score_cog, self.FK_id_couple, self.score_result)
        return message_str
