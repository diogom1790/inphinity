# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:14:54 2017

@author: Diogo Leite
"""

# here the FK values was selected in lastas positions according to Genus_new object class

from DAL import *
from configuration.configuration_data import *

class _Genus_sql_new(object):
    """
    This class manipulate the Genus table in the database

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
        
    def select_all_genus_all_attributes(self):
        """
        return all the Genuses in the database

        :return: cursor with all genuses
        :rtype Cursor list
        """
        sql_string = "SELECT id_genus_GE, designation_GE, FK_id_family_FA_GE FROM GENUSES"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results
    
    def insert_genus_if_not_exist_in_Family(self, genusName, family_id):
        """
        Insert a GENUS if it not yet exist (based on the designation)

        :param genusName: genus designation
        :param family_id: FK of the genus's family - -1 if unknown

        :type genusName: string - required 
        :type family_id: int - required 

        :return: id of the genus inserted
        :rtype int
        """
        
        id_genus = self.get_id_gene_by_designation_and_family_id(genusName, family_id)
        if id_genus == -1 :
            sql_string = "INSERT INTO GENUSES (designation_GE, FK_id_family_FA_GE) VALUES (%s, %s)"
            dalObj = DAL(self.db_name, sql_string)
            params = [genusName, family_id]
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            print("It already exists a genus with the designation %s for the family: %d" %(str(genusName), family_id))
            return id_genus

    def get_id_gene_by_designation_and_family_id(self, designation_gene, family_id):
        """
        get the id of a Genus based on its designation and family id

        :param designation_gene: designation of the gene
        :param family_id: FK of its family

        :type designation_gene: string - required 
        :type family_id: int - required 

        :return: id of the Genus or -1 if inexistant
        :rtype int
        """

        sql_string = "SELECT id_genus_GE FROM GENUSES WHERE designation_GE = '" + str(designation_gene) + "' AND FK_id_family_FA_GE = " + str(family_id) 
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]

    def get_genus_by_id(self, id_genus):
        """
        Get a genus by its id

        :return: Genus elements info
        :rtype List(infos genus)
        """
        sql_string = "SELECT id_genus_GE, designation_GE, FK_id_family_FA_GE FROM GENUSES WHERE id_genus_GE = " + str(id_genus)
        dalobj = DAL(self.db_name, sql_string)
        results = dalobj.executeSelect()

        return results[0]

    def get_genus_by_family_id(self, id_family):
        """
        Get list of genus of an family id

        :param id_family: id of the family that we want the genus

        :type id_family: int - required 

        :return: cursor with all genuses of the family
        :rtype Cursor list
        """
        sql_string = "SELECT id_genus_GE, designation_GE, FK_id_family_FA_GE FROM GENUSES WHERE FK_id_family_FA_GE = " + str(id_family)
        dalobj = DAL(self.db_name, sql_string)
        results = dalobj.executeSelect()

        return results

