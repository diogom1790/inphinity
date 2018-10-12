# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:43:29 2018

@author: Diogo
"""

from DAL import *
from configuration.configuration_data import *

class _COGS_preview_sql_new(object):
    """
    This class manipulate the COGS_preview table in the database

    The FK are manipulated in the lasts positions of the parameters
    """

    def __init__(self):
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

    def insert_COGS_preview(self, fk_prot_cog_bact, fk_prot_cog_phage, fk_interactiong_cogs, fk_id_couple_CP_CPR):
        """
        Insert a COGS_Preview in the database. 
        
        The id of the COGS_Preview is updated

        :return: id of the COGS_Preview inserted
        :rtype: int
        """
        sql_string = "INSERT INTO COGS_preview (FK_id_prot_cog_bact_CP_CPR, FK_id_prot_cog_phage_CP_CPR, FK_id_interaction_cog_source_CSI_CPR, FK_id_couple_CP_CPR) VALUES (%s, %s, %s, %s)"
        params = [fk_prot_cog_bact, fk_prot_cog_phage, fk_interactiong_cogs, fk_id_couple_CP_CPR]
        dalObj = DAL(self.db_name, sql_string)
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()
        return results.lastrowid

    def select_all_COGS_preview_grouped_by_couple_id(self, id_couple):
        """
        Consult the DB and return all the COGS_preview of a given Couple id

        :param id_couple: id of the couple - -1 if unknown

        :type id_couple: text - required 

        :return: cursor with all the scores
        :rtype Cursor list
        """
        sql_string = "select id_CPR, FK_id_prot_cog_bact_CP_CPR, FK_id_prot_cog_phage_CP_CPR, FK_id_interaction_cog_source_CSI_CPR, FK_id_couple_CP_CPR FROM COGS_preview WHERE FK_id_couple_CP_CPR = " + str(id_couple)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_COGS_preview(self):
        """
        Consult the DB and return all the different COGS preview

        :return: cursor with all the scores
        :rtype Cursor list
        """
        sql_string = "select id_CPR, FK_id_prot_cog_bact_CP_CPR, FK_id_prot_cog_phage_CP_CPR, FK_id_interaction_cog_source_CSI_CPR, FK_id_couple_CP_CPR FROM COGS_preview"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def remove_COG_preview_by_prot_id(self, fk_id_prot_cog):
        """
        remove a COG_preview by its id prot_cog

        :param fk_id_prot_cog: id of the prot_cog

        :type fk_id_prot_cog: int - required 

        :return: quantity of row deleted row
        :rtype int
        """
        sql_string = "DELETE FROM COGS_preview WHERE FK_id_prot_cog_bact_CP_CPR = %s or FK_id_prot_cog_phage_CP_CPR = %s"
        dalObj = DAL(self.db_name, sql_string)
        params = [fk_id_prot_cog, fk_id_prot_cog]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeDelete()
        return results.rowcount

    def remove_COG_preview_by_interaction_id(self, fk_id_cog_interact):
        """
        remove a COG_preview by its id cog interaction

        :param fk_id_cog_interact: id of the cog interaction

        :type fk_id_cog_interact: int - required 

        :return: quantity of row deleted row
        :rtype int
        """
        sql_string = "DELETE FROM COGS_preview WHERE FK_id_interaction_cog_source_CSI_CPR = %s"
        dalObj = DAL(self.db_name, sql_string)
        params = [fk_id_cog_interact]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeDelete()
        return results.rowcount

    def remove_COG_preview_by_id(self, id_cog_preview):
        """
        remove a COG_preview by its id cog interaction

        :param fk_id_cog_interact: id of the cog interaction

        :type fk_id_cog_interact: int - required 

        :return: quantity of row deleted row
        :rtype int
        """
        sql_string = "DELETE FROM COGS_preview WHERE id_CPR = %s"
        dalObj = DAL(self.db_name, sql_string)
        params = [id_cog_preview]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeDelete()
        return results.rowcount

    def get_COGS_ppi_preview_by_fk_id_interactions(self, FK_id_interaction_cog_source):
        """
        return all COGS_preview give a FK_id_interaction_cog_source

        :param FK_id_interaction_cog_source: id of the cog interaction

        :type FK_id_interaction_cog_source: int - required 

        :return: quantity of row deleted row
        :rtype int
        """

        sql_string = "SELECT id_CPR, FK_id_prot_cog_bact_CP_CPR, FK_id_prot_cog_phage_CP_CPR, FK_id_interaction_cog_source_CSI_CPR, FK_id_couple_CP_CPR FROM COGS_preview WHERE FK_id_interaction_cog_source_CSI_CPR = " + str(FK_id_interaction_cog_source) 
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def verify_COG_preview_exits(self, FK_id_prot_back, FK_id_prot_phage, FK_id_interact_cog, fk_id_couple):
        """
        verify if a give COG_preview exist

        :param FK_id_interaction_cog_source: id of the cog interaction

        :type FK_id_interaction_cog_source: int - required 

        :return: quantity of row deleted row
        :rtype int
        """

        sql_string = "SELECT count(*) FROM COGS_preview WHERE FK_id_prot_cog_bact_CP_CPR = " + str(FK_id_prot_back) + " and FK_id_prot_cog_phage_CP_CPR = " + str(FK_id_prot_phage) + " and FK_id_interaction_cog_source_CSI_CPR = " + str(FK_id_interact_cog) + " and FK_id_couple_CP_CPR = " + str(fk_id_couple)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        if results[0] == 0:
            return 0
        else: 
            return results[0]

    def update_id_interaction_cog_by_cog_preview_id(self, id_cog_preview, FK_id_interact_cog):
        """
        verify if a give COG_preview exist

        :param id_cog_preview: id of the cog_preview
        :param FK_id_interact_cog: FK id of the cog interaction

        :type id_cog_preview: int - required 
        :type FK_id_interact_cog: int - required 

        :return: quantity of row updated row
        :rtype int
        """

        sql_string = "UPDATE COGS_preview SET FK_id_interaction_cog_source_CSI_CPR = %s WHERE id_CPR = %s"
        params = [FK_id_interact_cog, id_cog_preview]
        dalObj = DAL(self.db_name, sql_string)
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()
        return results