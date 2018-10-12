# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:33:55 2018

@author: Diogo
"""
from SQL_obj_new.COGS_interactions_sql_new import _Cog_Interaction_sql_new

class COGS_interactions(object):
    """
    This class treat the Cog interactions object has it exists in COGS_INTERACTIONS table database

    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, id_cog = -1, FK_cog_group_A = -1, FK_cog_group_B = -1):
        """
        Constructor of the Cog_Interaction object. All the parameters have a default value

        :param id_cog: id of the cog interaction - -1 if unknown
        :param FK_cog_group_A: FK of the cog A
        :param FK_cog_group_B: FK of the cog B

        :type id_cog: int - required
        :type FK_cog_group_A: int - required 
        :type FK_cog_group_B: int - required 
        """
        self.id_cog = id_cog
        self.FK_cog_group_A = FK_cog_group_A
        self.FK_cog_group_B = FK_cog_group_B

    def get_all_interactions_cogs():
        """
        return an array with all the couples in the database

        :return: array of couple
        :rtype: array(Couple)
        """
        listOfCog = []
        sqlObj = _Cog_Interaction_sql_new()
        results = sqlObj.select_all_cog_interact()
        for element in results:
            listOfCog.append(COGS_interactions(element[0], element[1], element[2]))
        return listOfCog

    def get_all_interaction_cogs_limit(start_index, quantity_registers):
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
        sqlObj = _Cog_Interaction_sql_new()
        results = sqlObj.select_all_cog_interact_with_limit(start_index, quantity_registers)
        for element in results:
            listOfCog.append(COGS_interactions(element[0], element[1], element[2]))
        return listOfCog


    def create_cog_interaction(self):
        """
        Insert a Cog interaction in the database and update its id
        The Cog interaction contain a :
        - group cog name A 
        - group cog name B

        :return: id of the Cog interaction
        :rtype int
        """

        value_cog = None
        sqlObj = _Cog_Interaction_sql_new()
        value_cog = sqlObj.create_cog_interact_verification(self.FK_cog_group_A, self.FK_cog_group_B)
        self.id_cog = value_cog
        if value_cog is -1:
            return -1
        else:
            return value_cog

    def remove_cog_by_fk_a_fk_b(fk_cog_a, fk_cog_b):
        """
        remove cog give these FK_cogs keys only if it is not a duplicate inverted interaction

        :param FK_cog_group_A: FK of the cog A
        :param FK_cog_group_B: FK of the cog B

        :type FK_cog_group_A: int - required 
        :type FK_cog_group_B: int - required 

        :return: id of the Cog interaction deleted
        :rtype int
        """

        sqlObj = _Cog_Interaction_sql_new()
        value_cog = sqlObj.remove_COG_by_ID_duplicated(fk_cog_a, fk_cog_b)
        return value_cog

    def get_cog_interaction_id_by_fks_cogs(FK_cog_a, FK_cog_b):
        """
        get cog interactio nid given the FK of the cog_a and Fk_cog_b
        :Note that Ab and Ba are tested in the SQL class

        :param FK_cog_group_A: FK of the cog A
        :param FK_cog_group_B: FK of the cog B

        :type FK_cog_group_A: int - required 
        :type FK_cog_group_B: int - required 

        :return: id of the Cog interaction
        :rtype int
        """

        sqlObj = _Cog_Interaction_sql_new()
        value_cog = sqlObj.get_id_cog_interact_by_grpa_grpb(FK_cog_a, FK_cog_b)
        return value_cog


    def delete_cogs_interactions(qty_deletions):
        """
        Delete cogs interactions. if qty_deletions is <1 it remove all in one time (takes too much time)

        :param qty_deletions: number of register to remive

        :type qty_deletions: int - required 

        :return: index o the object if exist
        :rtype: int

        """

        sqlObj = _Cog_Interaction_sql_new()
        value_cog = sqlObj.remove_COG_by_quantities(qty_deletions)
        return value_cog

    def find_in_list(list_cogs, cog_obj):
        """
        Search in list if a given element exists

        :param list_cogs: List of objects where we need to search
        :param cog_obj: object that we need to search

        :type list_cogs: list(COGS_interactions) - required 
        :type cog_obj: COGS_interactions - required 

        :return: index o the object if exist
        :rtype: int

        """
        index = next((i for i, item in enumerate(list_cogs) if (item.FK_cog_group_A == cog_obj.FK_cog_group_A and item.FK_cog_group_B == cog_obj.FK_cog_group_B)), -1)
        return index



    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d}, ID Group A: {1}, ID group B: {2}".format(self.id_cog, self.FK_cog_group_A, self.FK_cog_group_B)
        return message_str

    def __eq__(self, couple_inter_other):
        """
        The equal only compare the FK_cogs_id NOT the ID OF THE OBJECTS

        :param couple_inter_other: couple_interaction_object that we want to compare

        :type COGS_interactions: string - required 

        """
        if isinstance(couple_inter_other, COGS_interactions):
            return (self.FK_cog_group_A == couple_inter_other.FK_cog_group_A and self.FK_cog_group_B == couple_inter_other.FK_cog_group_B)
        else:
            return False