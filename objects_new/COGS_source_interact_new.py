# -*- coding: utf-8 -*-
"""
Created on Tue May 22 15:19:12 2018

@author: Diogo
"""
from SQL_obj_new.COGS_source_interact_sql_new import _Cog_interact_source_sql_new


class Cog_source_interact(object):
    """
    This class treat the Cog interactions object has it exists in COG_SOURCES_INTERACT table database. THis table contain the interactions cog scores

    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, id_source_interact = -1, score = -1, FK_source = -1, FK_interact = -1):
        """
        Constructor of the COG_SOURCES_INTERACT object. All the parameters have a default value

        :param id_source_interact: id of the cog score - -1 if unknown
        :param score: designation of the cog A
        :param FK_source: designation of the cog B
        :param FK_interact: Cog score - -1 if unknown

        :type id_source_interact: int - required
        :type score: string - required 
        :type FK_source: string - required 
        :type FK_interact: int - required 
        """
        self.id_source_interact = id_source_interact
        self.score = score
        self.FK_source = FK_source
        self.FK_interact = FK_interact

    def get_all_source_interact():
        """
        return an array with all the source cog interact score in the database

        :return: array of couple
        :rtype: array(Couple)
        """
        listCOgInteractScore = []
        sqlObj = _Cog_interact_source_sql_new()
        results = sqlObj.select_all_cog_interact_source()
        for element in results:
            listCOgInteractScore.append(Cog_source_interact(element[0], element[1], element[2], element[3]))
        return listCOgInteractScore

    def get_all_source_interact_by_fk_if_cog_couple(FK_id_cog_couple):
        """
        return an array with all the source cog interact score in the database

        :return: array of couple
        :rtype: array(Couple)
        """
        listCOgInteractScore = []
        sqlObj = _Cog_interact_source_sql_new()
        results = sqlObj.select_all_cog_interact_source_by_fk_cog_couple(FK_id_cog_couple)
        for element in results:
            listCOgInteractScore.append(Cog_source_interact(element[0], element[1], element[2], element[3]))
        return listCOgInteractScore


    def get_all_source_interact_limit(start_index, quantity_registers):
        """
        return an array with all the source cog interact score in the database with a limit of registers

        :param start_index: first index to get
        :param quantity_registers: quantity of registers

        :type start_index: int - required
        :type quantity_registers: string - required 

        :return: array of couple
        :rtype: array(Couple)
        """
        listOfCogSourceInteract = []
        sqlObj = _Cog_interact_source_sql_new()
        results = sqlObj.select_all_cog_interact_source_by_limit(start_index, quantity_registers)
        for element in results:
            listOfCogSourceInteract.append(Cog_Interaction(element[0], element[1], element[2], element[3]))
        return listOfCogSourceInteract


    def create_cog_score_interaction_score(self):
        """
        Insert a Cog score in the database and update its id
        The Cog source interaction score contain a :
        - score
        - Fk source
        - Fk interaction

        :return: id of the Cog score
        :rtype int
        """

        value_cog = None
        sqlObj = _Cog_interact_source_sql_new()
        value_cog_score_interact = sqlObj.create_cog_interact_source_verification(self.score,self.FK_source,self.FK_interact)
        if value_cog_score_interact is -1:
            return -1
        else:
            return value_cog_score_interact

    def delete_cog_score_interaction_score_give_it_id(fk_id_interaction):
        """
        delete a cog_source_interactions given its interaction id

        :param fk_id_interaction: FK id of the source

        :type fk_id_interaction: int - required

        """

        value_cog_score_interact = None
        sqlObj = _Cog_interact_source_sql_new()
        value_cog_score_interact = sqlObj.delete_cog_interaction_source_by_FK_interaction_cog(fk_id_interaction)
        if value_cog_score_interact is -1:
            return -1
        else:
            return value_cog_score_interact


    def delete_cog_score_interaction_score_give_Fk_interaction_cog_source_id(fk_id_cog_interaction):
        """
        delete a cog_source_interactions given its F of the cog interaction

        :param fk_id_cog_interaction: FK id of the cog interaction

        :type fk_id_cog_interaction: int - required

        """

        value_cog_score_interact = None
        sqlObj = _Cog_interact_source_sql_new()
        value_cog_score_interact = sqlObj.delete_cog_interaction_source_by_FK_interaction_cog(fk_id_cog_interaction)
        if value_cog_score_interact is -1:
            return -1
        else:
            return value_cog_score_interact