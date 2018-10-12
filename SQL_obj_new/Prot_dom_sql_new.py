# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:43:29 2017

@author: Diogo
"""

from DAL import *
from configuration.configuration_data import *

class _Prot_dom_sql_new(object):
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

    def select_all_prodom_all_attributes(self):
        """
        return all the PROT_DOM in the database

        :return: cursor with all domains
        :rtype Cursor list
        """
        sql_string = "SELECT id_prot_dom_DP, FK_id_protein_PT_DP, FK_id_domain_DO_DP FROM PROT_DOM"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_prodom_all_attributes_by_protein_id(self, protein_id):
        """
        return all the PROT_DOM in the database given a protein id

        :param protein_id: id of a protein

        :type protein_id: int - required

        :return: cursor with all domains
        :rtype Cursor list
        """
        sql_string = "SELECT id_prot_dom_DP, FK_id_protein_PT_DP, FK_id_domain_DO_DP FROM PROT_DOM WHERE FK_id_protein_PT_DP = " + str(protein_id)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results
    
    def count_domains_by_protein_id(self, fk_protein):
        """
        Consult the DB and return the number of domains belong a protein id

        :param fk_protein: id of a protein

        :type fk_protein: int - required

        :return: number of domains
        :rtype int
        """
        sql_string = "SELECT count(id_prot_dom_DP) FROM PROT_DOM WHERE FK_id_protein_PT_DP = " + str(fk_protein)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        if type(results) == tuple and len(results) == 0 :
            return 0
        else:
            return results[0][0]
    ########################## PAUSE


    def insert_prodom_return_id(self, fk_protein, fk_domain):
        """
        Insert a proteinDom object in the database and return its id. THIS METHOD DON'T VERIFY IF THE OBJECT ALREADY EXISTS IN THE DATABASE

        :param fk_protein: id of a protein
        :param fk_domain: id of a domain

        :type fk_protein: int
        :type fk_domain: int

        :return: id of the ProteinDom object inserted
        :rtype int
        """
        sqlObj = " INSERT INTO PROT_DOM (FK_id_protein_PT_DP, FK_id_domain_DO_DP) VALUES (%s, %s)"
        params = [fk_protein, fk_domain]
        dalObj = DAL(self.db_name, sqlObj, params)
        results = dalObj.executeInsert()
        return results.lastrowid
    
    def insert_protdom_if_not_exist(self, fk_protein, fk_domain):
        """
        Verify if the a object with the same Fks don't exists and insert it in the database

        :param fk_protein: id of a protein
        :param fk_domain: id of a domain

        :type fk_protein: int
        :type fk_domain: int

        :return: id of the ProteinDom object inserted
        :rtype int
        """
        id_prot_dom = self.get_id_prot_dom_by_id_prot_id_domain(fk_protein, fk_domain)
        if id_prot_dom == -1 :
            sql_string = "INSERT INTO PROT_DOM (FK_id_protein_PT_DP, FK_id_domain_DO_DP) VALUES (%s, %s)"
            params = [fk_protein, fk_domain]
            dalObj = DAL(self.db_name, sql_string)
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            print("This protein-domain: {0} - {1} pair already exists".format(fk_protein, fk_domain))
            return id_prot_dom 


    def get_id_prot_dom_by_id_prot_id_domain(self, FK_id_protein, FK_id_domain):
        """
        get the id of a prot_dom based on the id of the protein and domain

        :param FK_id_protein: designation of the group A
        :param FK_id_domain: designation of the group B

        :type FK_id_protein: int - required 
        :type FK_id_domain: int - required 

        :return: id of the Prot_dom or -1 if inexistant
        :rtype int
        """
        sql_string = "SELECT id_prot_dom_DP FROM PROT_DOM WHERE FK_id_protein_PT_DP = " + str(FK_id_protein) + " AND FK_id_domain_DO_DP = " + str(FK_id_domain)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]

    def remove_prot_dom_by_prot_id(self, fk_id_protein):
        """
        remove a prot_dom by its id

        :param fk_id_protein: id of the fk_bacterium 

        :type fk_id_protein: int - required 

        :return: quantity of row deleted row
        :rtype int
        """
        sql_string = "DELETE FROM PROT_DOM WHERE FK_id_protein_PT_DP = %s"
        dalObj = DAL(self.db_name, sql_string)
        params = [fk_id_protein]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeDelete()
        return results.rowcount


   
