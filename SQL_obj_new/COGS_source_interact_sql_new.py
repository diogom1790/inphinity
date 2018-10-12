# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:05:59 2018

@author: Diogo
"""

from DAL import *
from configuration.configuration_data import *

class _Cog_interact_source_sql_new(object):
    """
    This class manipulate the COG_SOURCES_INTERACT table in the database

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

    def select_all_cog_interact_source(self):
        """
        return all the COG scores in the database

        :return: cursor with all COG score
        :rtype Cursor list
        """

        sql_string = "SELECT id_score_interact_COG_CSI, score_CSI, FK_id_cog_source_CS_CSI, FK_id_cog_interaction_CI_CSI FROM COG_SOURCES_INTERACT"

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_cog_interact_source_by_fk_cog_couple(self, FK_id_cog_couple):
        """
        return all the COG scores in the database with a give FK_cog_couple_id

        :return: cursor with all COG score
        :rtype Cursor list
        """

        sql_string = "SELECT id_score_interact_COG_CSI, score_CSI, FK_id_cog_source_CS_CSI, FK_id_cog_interaction_CI_CSI FROM COG_SOURCES_INTERACT WHERE FK_id_cog_interaction_CI_CSI = " + str(FK_id_cog_couple)

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_cog_interact_source_by_limit(self, start_index, quantity_registers):
        """
        return all the COG scores in the database

        :param start_index: start position to get the registers
        :param quantity_registers: quantity of registers

        :type start_index: int - required 
        :type quantity_registers: int - required 

        :return: cursor with all COG score
        :rtype Cursor list
        """

        sql_string = "SELECT id_score_interact_COG_CSI, score_CSI, FK_id_cog_source_CS_CSI, FK_id_cog_interaction_CI_CSI FROM COG_SOURCES_INTERACT LIMIT " + str(quantity_registers) + " OFFSET " + str(start_index)

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def create_cog_interact_source_verification(self, score_interaction_COG, Fk_source, Fk_interaction):
        """
        Insert a Cog groupe based on the FK ids of both.

        :param score_interaction_COG: score of the cog interaction
        :param Fk_source: FK of the source
        :param FK_interaction: FK of the interaction

        :type score_interaction_COG: int - required 
        :type Fk_source: string - required 
        :type FK_interaction: string - required  

        :return: id of the COG interaction
        :rtype int
        """
        id_source_itneract_cog = self.get_id_cog_interact_by_source_interaction(Fk_source, Fk_interaction)
        if id_source_itneract_cog == -1:
            sql_string = "INSERT INTO COG_SOURCES_INTERACT (score_CSI, FK_id_cog_source_CS_CSI, FK_id_cog_interaction_CI_CSI) VALUES (%s, %s, %s)"
            dalObj = DAL(self.db_name, sql_string)
            params = [score_interaction_COG, Fk_source, Fk_interaction]
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            print("Its already exists a Cog Score with these groups")
            return id_source_itneract_cog

    def get_id_cog_interact_by_source_interaction(self, Fk_source, FK_interaction):
        """
        get the id of a cog interaction based on these groups (A and B)

        :param Fk_source: FK of the source
        :param FK_interaction: FK of the interaction

        :type Fk_source: string - required 
        :type FK_interaction: string - required 

        :return: id of the cog socre or -1 if inexistant
        :rtype int
        """

        sql_string = "SELECT id_score_interact_COG_CSI FROM COG_SOURCES_INTERACT WHERE FK_id_cog_source_CS_CSI = '" + str(Fk_source) + "' and FK_id_cog_interaction_CI_CSI = '" + str(FK_interaction) + "'"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]

    def delete_cog_interaction_source_by_FK_interaction_cog(self, FK_id_interaction):
        """
        delete the cog interactions source give its id

        :param FK_interaction: FK of the interaction

        :type FK_interaction: string - required 

        """

        sql_string = "DELETE FROM COG_SOURCES_INTERACT WHERE FK_id_cog_interaction_CI_CSI = " + str(FK_id_interaction)
        dalObj = DAL(self.db_name, sql_string)
        dalObj.executeDelete()

    def delete_cog_interaction_source_by_FK_interaction_cog(self, FK_id_cog_interaction):
        """
        delete the cog interactions source give the id of the cog interaction

        :param FK_id_cog_interaction: FK of the cog interaction

        :type FK_id_cog_interaction: string - required 

        """

        sql_string = "DELETE FROM COG_SOURCES_INTERACT WHERE FK_id_cog_interaction_CI_CSI = " + str(FK_id_cog_interaction)
        dalObj = DAL(self.db_name, sql_string)
        dalObj.executeDelete()