# -*- coding: utf-8 -*-
"""
Created on Wen Apr 11 13:01:22 2018

@author: Diogo Leite
"""

from DAL import *
from configuration.configuration_data import *

class _DDI_interaction_DB_SQL(object):
    """
    This class manipulate the DDI_INTERACTIONS_DB table in the database. It used to know from which DDB coms the information of the DDI


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

    def select_all_DDI_DB(self):
        """
        return all the connections DDI-DB sources

        :return: cursor with all sources DDI_interactions_DB
        :rtype Cursor list
        """
        sql_string = "SELECT id_DDI_interaction_DDB, date_insertion_DDB, FK_id_interaction_DD_DDB, FK_id_db_interaction_DDB FROM DDI_INTERACTIONS_DB"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_DDI_DB_id_by_pair_domain(self, id_domain_a, id_domain_b):
        """
        return all the connections DDI-DB sources

        :NOTE the pairs test normal and invertion (domA - domB and domB -domA)

        :return: cursor with all sources DDI_interactions_DB
        :rtype Cursor list
        """
        sql_string = "select Fk_id_db_interaction_DDB from DDI_INTERACTIONS_DB, DDI_INTERACTIONS WHERE FK_id_interaction_DD_DDB = id_DDI_inter_DD and ((FK_domain_a_DD = " + str(id_domain_a) + " and FK_domain_b_DD = " + str(id_domain_b) + ") or (FK_domain_a_DD = " + str(id_domain_b) + " and FK_domain_b_DD = " + str(id_domain_a) + "))"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        return results

    def insert_DDI_source_return_id_if_not_exists(self, date_creation, FK_DDI_interaction, FK_Source_DDI_DB):
        """
        Insert a ddi_source WITHOUT ANY VERIFICATION.

        :param date_creation: creation date of the register
        :param FK_DDI_interaction: FK of the DDI interaction
        :param FK_Source_DDI_DB: FK of the database tha give the information

        :type date_creation: int - required 
        :type FK_DDI_interaction: int - required 
        :type FK_Source_DDI_DB: string (datetime sql format) - required 


        :return: id of the domain inserted or ID of the existant
        :rtype int
        """
        id_DDI_DB_source = self.get_id_DDI_interaction_DB_by_FK_keys(FK_DDI_interaction, FK_Source_DDI_DB)
        if id_DDI_DB_source == -1:
            sqlObj = "INSERT INTO DDI_INTERACTIONS_DB (date_insertion_DDB, FK_id_interaction_DD_DDB, FK_id_db_interaction_DDB) VALUES (%s, %s, %s)"
            params = [date_creation, FK_DDI_interaction, FK_Source_DDI_DB]
            dalObj = DAL(self.db_name, sqlObj, params)
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            return id_DDI_DB_source


    def get_id_DDI_interaction_DB_by_FK_keys(self, FK_DDI_pair, FK_DDI_source):
        """
        Return the id o a DDI source


        :param FK_DDI_pair: designation of DDI source
        :param FK_DDI_source: designation of DDI source

        :type FK_DDI_pair: string - required 
        :type FK_DDI_source: string - required 

        :return: id of the DDI_pair_source or -1 i don't exists
        :rtype int
        """

        sql_string = "SELECT id_DDI_interaction_DDB FROM DDI_INTERACTIONS_DB WHERE FK_id_interaction_DD_DDB = '" + str(FK_DDI_pair) + "' AND FK_id_db_interaction_DDB = '" + str(FK_DDI_source) + "'"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]