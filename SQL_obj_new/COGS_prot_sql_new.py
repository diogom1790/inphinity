# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:43:29 2018

@author: Diogo
"""

from DAL import *
from configuration.configuration_data import *

class _COGS_prot_sql_new(object):
    """
    This class manipulate the PROT_DOM table in the database

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

    def select_all_cogprot_all_attributes(self):
        """
        return all the COGS_PROT in the database

        :return: cursor with all COGS_prots
        :rtype Cursor list
        """
        sql_string = "SELECT id_cog_prot_CP, FK_id_cog_CO_CP, FK_id_protein_PT_CP FROM COGS_PROT"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_prodom_all_attributes_by_protein_id(self, fk_protein):
        """
        return all the COGS_PROT in the database given a protein id

        :param fk_protein: id of a protein

        :type fk_protein: int - required

        :return: cursor with all domains
        :rtype Cursor list
        """
        sql_string = "SELECT id_cog_prot_CP, FK_id_cog_CO_CP, FK_id_protein_PT_CP FROM COGS_PROT WHERE FK_id_protein_PT_CP = " + str(fk_protein)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def count_COGS_by_protein_id(self, fk_protein):
        """
        Consult the DB and return the number of COGS belong a protein FK id

        :param fk_protein: id of a protein

        :type fk_protein: int - required

        :return: number of COGS
        :rtype int
        """
        sql_string = "SELECT count(id_cog_prot_CP) FROM COGS_PROT WHERE FK_id_protein_PT_CP = " + str(fk_protein)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        if type(results) == tuple and len(results) == 0 :
            return 0
        else:
            return results[0][0]

    def get_id_cog_prot_by_id_cog_id_prot(self, FK_id_cog, FK_id_protein):
        """
        get the id of a prot_dom based on the id of the protein and domain

        :param FK_id_cog: id of the COG
        :param FK_id_protein: id of the protein

        :type FK_id_cog: int - required 
        :type FK_id_protein: int - required 

        :return: id of the COG_protein or -1 if inexistant
        :rtype int
        """
        sql_string = "SELECT id_cog_prot_CP FROM COGS_PROT WHERE FK_id_cog_CO_CP = " + str(FK_id_cog) + " AND FK_id_protein_PT_CP = " + str(FK_id_protein)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]

    def insert_cogs_prot_return_id(self, FK_cog, fk_protein):
        """
        Insert a COGS_PROTEIN object in the database and return its id. THIS METHOD DON'T VERIFY IF THE OBJECT ALREADY EXISTS IN THE DATABASE

        :param FK_cog: id of a cog
        :param fk_protein: id of a protein

        :type FK_cog: int
        :type fk_protein: int

        :return: id of the COGS_PROT object inserted
        :rtype int
        """
        sqlObj = " INSERT INTO COGS_PROT (FK_id_cog_CO_CP, FK_id_protein_PT_CP) VALUES (%s, %s)"
        params = [FK_cog, fk_protein]
        dalObj = DAL(self.db_name, sqlObj, params)
        results = dalObj.executeInsert()
        return results.lastrowid


    def insert_cog_prot_if_not_exist(self, FK_id_COG, FK_id_prot):
        """
        Verify if the a object with the same Fks don't exists and insert it in the database

        :param FK_id_COG: id of a cog
        :param FK_id_prot: id of a protein

        :type FK_id_COG: int
        :type FK_id_prot: int

        :return: id of the ProteinDom object inserted
        :rtype int
        """
        id_prot_dom = self.get_id_cog_prot_by_id_cog_id_prot(FK_id_COG, FK_id_prot)
        if id_prot_dom == -1 :
            sql_string = "INSERT INTO COGS_PROT (FK_id_cog_CO_CP, FK_id_protein_PT_CP) VALUES (%s, %s)"
            params = [FK_id_COG, FK_id_prot]
            dalObj = DAL(self.db_name, sql_string)
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            print("This COGprotein : {0} - {1} pair already exists".format(FK_id_COG, FK_id_prot))
            return id_prot_dom 


    def remove_COG_protein_by_prot_id(self, fk_id_protein):
        """
        remove a COGProt by its id

        :param fk_id_protein: id of the protein 

        :type fk_id_protein: int - required 

        :return: quantity of row deleted row
        :rtype int
        """
        sql_string = "DELETE FROM COGS_PROT WHERE FK_id_protein_PT_CP = %s"
        dalObj = DAL(self.db_name, sql_string)
        params = [fk_id_protein]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeDelete()
        return results.rowcount
