# -*- coding: utf-8 -*-
"""
Created on Fri May 4 08:57:54 2018

@author: Diogo
"""

from DAL import *
from configuration.configuration_data import *

class _PPIpreview_sql_new(object):
    """
    This class manipulate the PPI_preview table in the database

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

    def insert_PPI(self, score, type_score, fk_couple, fk_prot_bact, fk_prot_phage):
        """
        Insert a ppi_score in the database. 
        
        The id of the PPI_preview is updated

        :return: id of the PPI_preview inserted
        :rtype: int
        """
        sql_string = "INSERT INTO PPI_preview (score_value_PPI, type_score_PPI, FK_couple_CP_PPI, FK_protein_bact_PT_PPI, FK_protein_phage_PT_PPI) VALUES (%s, %s, %s, %s, %s)"
        params = [score, type_score, fk_couple, fk_prot_bact, fk_prot_phage]
        dalObj = DAL(self.db_name, sql_string)
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()
        return results.lastrowid


    def select_all_ppi_preview_grouped_by_couple_id(self, id_couple):
        """
        Consult the DB and return all the scores of a given Couple id grouped by PPI

        :param id_couple: id of the couple - -1 if unknown

        :type id_couple: text - required 

        :return: cursor with all the scores
        :rtype Cursor list
        """
        sql_string = "select FK_protein_bact_PT_PPI, FK_protein_phage_PT_PPI, sum(score_value_PPI) as 'Sum PPI score' from PPI_preview WHERE FK_couple_CP_PPI = " + str(id_couple) + " group by FK_protein_bact_PT_PPI, FK_protein_phage_PT_PPI"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_ppi_preview_possible_scores(self):
        """
        Consult the DB and return all the differents scores (possibles scores)

        :return: cursor with all the scores
        :rtype Cursor list
        """
        sql_string = "select distinct sum(score_value_PPI) as 'possible_scores' from PPI_preview group by FK_protein_bact_PT_PPI, FK_protein_phage_PT_PPI"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_ppi_preview_fk_couples(self):
        """
        Consult the DB and return all the differents couples treated

        :return: cursor with all the scores
        :rtype Cursor list
        """
        sql_string = "select distinct FK_couple_CP_PPI from PPI_preview"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_score_PPI(self):
        """
        Consult the DB and return all the different PPI scores

        :NOTE THIS METHOS RIQUIERED TO BE RE DO

        :return: cursor with all the scores
        :rtype Cursor list
        """
        sql_string = "select FK_protein_bact_PT_PPI, FK_protein_phage_PT_PPI, sum(score_value_PPI) as 'Sum_PPI_score' from PPI_preview group by FK_protein_bact_PT_PPI, FK_protein_phage_PT_PPI"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def count_ppi_preview_by_ids_ppi(self, FK_prot_Bact, FK_prot_phag):
        """
        Consult the DB and count the number of PPI score by the protein of the bacterium and phage

        :param FK_prot_Bact: id of the fk_bacterium 
        :param FK_prot_phag: id of the fk_phage 

        :type FK_prot_Bact: int - required 
        :type FK_prot_phag: int - required 

        :return: cursor with all the scores
        :rtype Cursor list
        """
        sql_string = "SELECT COUNT(*) FROM PPI_preview WHERE FK_protein_bact_PT_PPI = " + str(FK_prot_Bact) + " AND FK_protein_phage_PT_PPI = " + str(FK_prot_phag)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def remove_PPI_preview_by_prot_id(self, fk_id_protein):
        """
        remove a PPI_preview by the protein id (phage and bacterium)

        :param fk_id_protein: id of the fk_bacterium 

        :type fk_id_protein: int - required 

        :return: quantity of row deleted row
        :rtype int
        """
        sql_string = "DELETE FROM PPI_preview WHERE FK_protein_bact_PT_PPI = %s OR FK_protein_phage_PT_PPI = %s"
        dalObj = DAL(self.db_name, sql_string)
        params = [fk_id_protein, fk_id_protein]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeDelete()
        return results.rowcount