# -*- coding: utf-8 -*-
"""
Created on Fri Jun 8 15:45:16 2017

@author: Diogo
"""

from DAL import *
from configuration.configuration_data import *

class _PPI_couple_sql_new(object):
    """
    This class manipulate the PPI_couple table in the database

    The FK are manipulated in the lasts positions of the parameters
    """

    def __init__(self"):
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

    def insert_PPI_couple(self, FK_id_prot_bact, FK_id_prot_phage, Fk_couple):
        """
        Insert a ppi_couple in the database. 
        
        The id of the PPI_couple is updated

        :Note A verification id done in the database which allow to insert only a unic pair of id_prot_bact and id_prot_phage.

        :param FK_id_prot_bact: id of the couple - -1 if unknown
        :param FK_id_prot_phage: id of the couple - -1 if unknown
        :param Fk_couple: id of the couple - -1 if unknown

        :type FK_id_prot_bact: text - required 
        :type FK_id_prot_phage: text - required 
        :type Fk_couple: text - required 

        :return: id of the PPI_couple inserted
        :rtype: int
        """
        sql_string = "INSERT INTO PPI_couple (FK_prot_bact_PT_PCP, FK_prot_phage_PT_PCP, FK_couple_CP_PCP) VALUES (%s, %s, %s)"
        params = [FK_id_prot_bact, FK_id_prot_phage, Fk_couple]
        dalObj = DAL(self.db_name, sql_string)
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()
        return results.lastrowid

    def select_all_ppi_preview_give_couple_id(self, id_couple):
        """
        Consult the DB and return all PPI_couple of a give couple

        :param id_couple: id of the couple - -1 if unknown

        :type id_couple: text - required 

        :return: cursor with all the scores
        :rtype Cursor list
        """
        sql_string = "select id_PCP, FK_prot_bact_PT_PCP, FK_prot_phage_PT_PCP, FK_couple_CP_PCP FROM PPI_couple WHERE FK_couple_CP_PCP = " + str(id_couple)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def get_PPI_couple_by_FK(self, FK_id_prot_bact, FK_id_prot_phage):
        """
        return the the PPI_couple given ithese FKs

        :param FK_id_prot_bact: id of the couple - -1 if unknown
        :param FK_id_prot_phage: id of the couple - -1 if unknown

        :type FK_id_prot_bact: text - required 
        :type FK_id_prot_phage: text - required 

        :return: cursor with all the scores
        :rtype Cursor list
        """
        sql_string = "select id_PCP, FK_prot_bact_PT_PCP, FK_prot_phage_PT_PCP, FK_couple_CP_PCP FROM PPI_couple WHERE FK_prot_bact_PT_PCP = " + str(FK_id_prot_bact) + " AND FK_prot_phage_PT_PCP = " + str(FK_id_prot_phage)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def get_PPI_couple_ID_by_FK(self, FK_id_prot_bact, FK_id_prot_phage):
        """
        return the the PPI_couple ID given ithese FKs

        :param FK_id_prot_bact: id of the couple - -1 if unknown
        :param FK_id_prot_phage: id of the couple - -1 if unknown

        :type FK_id_prot_bact: text - required 
        :type FK_id_prot_phage: text - required 

        :return: cursor with all the scores
        :rtype Cursor list
        """
        sql_string = "select id_PCP WHERE FK_prot_bact_PT_PCP = " + str(FK_id_prot_bact) + " AND FK_prot_phage_PT_PCP = " + str(FK_id_prot_phage)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results
