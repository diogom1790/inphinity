# -*- coding: utf-8 -*-
"""
Created on Tue Jan 9 09:17:55 2017

@author: Diogo
"""
from SQL_obj_new.Cog_interactions_sql_new import _Cog_Interaction_Score_sql_new

class Cog_Interaction(object):
    """
    This class treat the Cog interactions object has it exists in COG_INTERACTIONS table database

    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, id_cog_score = -1, grp_1 = "", grp_2 = "", score_value = -1):
        """
        Constructor of the Cog_Interaction object. All the parameters have a default value

        :param id_cog_score: id of the cog score - -1 if unknown
        :param grp_1: designation of the cog A
        :param grp_2: designation of the cog B
        :param score_value: Cog score - -1 if unknown

        :type id_cog_score: int - required
        :type grp_1: string - required 
        :type grp_2: string - required 
        :type score_value: int - required 
        """
        self.id_cog_score = id_cog_score
        self.grp_1 = grp_1
        self.grp_2 = grp_2
        self.score_value = score_value

    def get_all_score_cogs():
        """
        return an array with all the couples in the database

        :return: array of couple
        :rtype: array(Couple)
        """
        listOfCog = []
        sqlObj = _Cog_Interaction_Score_sql_new()
        results = sqlObj.select_all_cog_scores()
        for element in results:
            listOfCog.append(Cog_Interaction(element[0], element[1], element[2], element[3]))
        return listOfCog

    def get_all_score_cogs_limit(start_index, quantity_registers):
        """
        return an array with all the couples in the database

        :param start_index: first index to get
        :param quantity_registers: quantity of registers

        :type start_index: int - required
        :type quantity_registers: string - required 

        :return: array of couple
        :rtype: array(Couple)
        """
        listOfCog = []
        sqlObj = _Cog_Interaction_Score_sql_new()
        results = sqlObj.select_all_cog_scores_with_limit(start_index, quantity_registers)
        for element in results:
            listOfCog.append(Cog_Interaction(element[0], element[1], element[2], element[3]))
        return listOfCog


    def get_all_score_cogs_designation_by_group(group_id):
        """
        return an array with all the couples in the database

        :param group_id: id of the group - -1 if unknown

        :type group_id: int - required

        :return: array of designations
        :rtype: array(String)
        """
        listDesignationGroups = []
        sqlObj = _Cog_Interaction_Score_sql_new()
        results = sqlObj.select_all_cog_by_groups(group_id)
        for element in results:
            listDesignationGroups.append(element[0])
        return listDesignationGroups

    def create_cog_score(self):
        """
        Insert a Cog score in the database and update its id
        The Cog score contain a :
        - group cog name A 
        - group cog name B
        - Score

        :return: id of the Cog score
        :rtype int
        """

        value_cog = None
        sqlObj = _Cog_Interaction_Score_sql_new()
        value_cog = sqlObj.create_cog_score_verification(self.grp_1,self.grp_2,self.score_value)
        if value_cog is -1:
            return -1
        else:
            return value_cog


    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d}, ID Group A: {1}, ID group B: {2} Score: {3:d}".format(self.id_cog_score, self.grp_1, self.grp_2, self.score_value)
        return message_str

