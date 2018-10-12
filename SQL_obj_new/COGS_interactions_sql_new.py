# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:05:59 2018

@author: Diogo
"""

from DAL import *
from configuration.configuration_data import *


class _Cog_Interaction_sql_new(object):
    """
    This class manipulate the COG_INTERACTIONS table in the database

    The FK are manipulated in the lasts positions of the parameters
    """

    def __init__(self):
        """
        Constructor of the Cong_interactions object. All the parameters have a default value

        :param db_name: name of the database to do the ACID methods

        :type db_name: string - no required
        """

        self.db_name = self.get_database_name()

    def get_database_name(self):
        """
        This method is used to get the database name used in factory

        :return: database name
        :rtype string
        """
        conf_data_obj = Configuration_data('INPHINITY')
        db_name = conf_data_obj.get_database_name()
        return db_name

    def select_all_cog_interact(self):
        """
        return all the COG interaction in the database

        :return: cursor with all COG interaction
        :rtype Cursor list
        """

        sql_string = "SELECT id_cogs_inter_CI, FK_cog_a_CI, FK_cog_b_CI FROM COGS_INTERACTIONS"

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_cog_interact_with_limit(self, start_index, quantity_registers):
        """
        return all the COG interaction in the database

        :param start_index: start position to get the registers
        :param quantity_registers: quantity of registers

        :type start_index: int - required 
        :type quantity_registers: int - required 

        :return: cursor with all COG interaction
        :rtype Cursor list
        """

        sql_string = "SELECT id_cogs_inter_CI, FK_cog_a_CI, FK_cog_b_CI FROM COGS_INTERACTIONS LIMIT " + str(quantity_registers) + " OFFSET " + str(start_index)

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results


    def create_cog_interact_verification(self, FK_group_cog_a, FK_group_cog_b):
        """
        Insert a Cog groupe based on the FK ids of both.

        :param FK_group_cog_a: fk id of the group cog A
        :param FK_group_cog_b: fk id of the group cog B

        :type FK_group_cog_a: int - required 
        :type FK_group_cog_b: int - required 

        :return: id of the COG interaction
        :rtype int
        """
        id_value_COG_interact = self.get_id_cog_interact_by_grpa_grpb(FK_group_cog_a, FK_group_cog_b)
        if id_value_COG_interact == -1:
            sql_string = "INSERT INTO COGS_INTERACTIONS (FK_cog_a_CI, FK_cog_b_CI) VALUES (%s, %s)"
            dalObj = DAL(self.db_name, sql_string)
            params = [FK_group_cog_a, FK_group_cog_b]
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            print("Its already exists a Cog Scor with these groups")
            return id_value_COG_interact

    def get_id_cog_interact_by_grpa_grpb(self, FK_group_cog_a, FK_group_cog_b):
        """
        get the id of a cog interaction based on these groups (A and B)
        :Note that the invertion is tested (A-B and B-A)

        :param FK_group_cog_a: designation of the group A
        :param FK_group_cog_b: designation of the group B

        :type FK_group_cog_a: string - required 
        :type FK_group_cog_b: string - required 

        :return: id of the cog socre or -1 if inexistant
        :rtype int
        """

        sql_string = "SELECT id_cogs_inter_CI FROM COGS_INTERACTIONS WHERE FK_cog_a_CI = '" + str(FK_group_cog_a) + "' and FK_cog_b_CI = '" + str(FK_group_cog_b) + "'"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            sql_string = "SELECT id_cogs_inter_CI FROM COGS_INTERACTIONS WHERE FK_cog_a_CI = '" + str(FK_group_cog_b) + "' and FK_cog_b_CI = '" + str(FK_group_cog_a) + "'"
            dalObj = DAL(self.db_name, sql_string)
            results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]

    def remove_COG_by_ID_duplicated(self, FK_group_cog_a, FK_group_cog_b):
        """
        remove cog interaction by FK cogs (A and B). remove only if its not a duplicate interaction

        :param FK_group_cog_a: designation of the group A
        :param FK_group_cog_b: designation of the group B

        :type FK_group_cog_a: string - required 
        :type FK_group_cog_b: string - required 
        """

        id_value_COG_interact = self.get_id_cog_interact_by_grpa_grpb(FK_group_cog_b, FK_group_cog_a)
        if id_value_COG_interact != -1:
            sql_string = "DELETE FROM COGS_INTERACTIONS WHERE FK_cog_a_CI = '" + str(FK_group_cog_a) + "' and FK_cog_b_CI = '" + str(FK_group_cog_b) + "'"
            dalObj = DAL(self.db_name, sql_string)
            dalObj.executeDelete()


    def remove_COG_by_quantities(self, qty_elements):
        """
        remove the COGS interaction withou any restriction, just the number of samples. If 0 it remove all in one time

        :param qty_elements: qty of cog interaction that you want to remove

        :type qty_elements: int - required 
        """
        if qty_elements > 0:
            sql_string = "delete from COGS_INTERACTIONS LIMIT " + str(qty_elements) + ";"
        else:
            sql_string = "DELETE FROM COGS_INTERACTIONS"
        print(sql_string)
        dalObj = DAL(self.db_name, sql_string)
        dalObj.executeDelete()
