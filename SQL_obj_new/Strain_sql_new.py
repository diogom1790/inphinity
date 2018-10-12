# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:24:30 2017

@author: Diogo Leite
"""

# here the FK values was selected in lastas positions according to Strain_new object class

from DAL import *
from configuration.configuration_data import *

class _Strain_sql_new(object):
    """
    This class manipulate the Strain table in the database

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
        
    def select_all_strains_all_attributes(self):
        """
        return all the Strain in the database

        :return: cursor with all genuses
        :rtype Cursor list
        """
        sql_string = "SELECT id_strain_ST, designation_ST, FK_id_specie_SP_ST FROM STRAINS"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results
    
    def insert_strain_if_not_exist_in_Specie(self, strainName, specie_id):
        """
        Insert a STRAIN if it not yet exist (based on the designation)

        :param strainName: strain designation
        :param specie_id: FK of the strain's specie - -1 if unknown

        :type strainName: string - required 
        :type specie_id: int - required 

        :return: id of the strain inserted
        :rtype int
        """
        id_strain = self.get_strain_id_based_strain_name_and_specie_id(strainName, specie_id)
        if id_strain == -1:
            sql_string = "INSERT INTO STRAINS (designation_ST, FK_id_specie_SP_ST) VALUES (%s, %s)"
            dalObj = DAL(self.db_name, sql_string)
            params = [strainName, specie_id]
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            print("The strain {0} already exists in the specie id: {1:d}".format(strainName, specie_id))
            return id_strain

    def get_strain_id_based_strain_name_and_specie_id(self, strainName, specie_id):
        """
        get the id of a Strain based its name and specie id

        :param strainName: designation of the strain
        :param specie_id: id of the specie of the strain

        :type strainName: string - required 
        :type specie_id: int - required 

        :return: id of the Strain or -1 if inexistant
        :rtype int
        """

        sql_string = "SELECT id_strain_ST FROM STRAINS WHERE designation_ST = '" + str(strainName) + "' AND FK_id_specie_SP_ST = " + str(specie_id)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]


    def get_strain_by_id(self, id_strain):
        """
        Get a strain by its id

        :return: Strain elements info
        :rtype List(infos organism)
        """
        sql_string = "SELECT id_strain_ST, designation_ST, FK_id_specie_SP_ST FROM STRAINS WHERE id_strain_ST = " + str(id_strain)
        dalobj = DAL(self.db_name, sql_string)
        results = dalobj.executeSelect()

        return results[0]

    def remove_strain_by_id(self, id_Strain):
        """
        remove a Strain by its id

        :param id_Strain: id of the Strain 

        :type id_Strain: int - required 

        :return: quantity of row deleted row
        :rtype int
        """
        sql_string = "DELETE FROM STRAINS WHERE id_strain_ST = %s"
        dalObj = DAL(self.db_name, sql_string)
        params = [id_Strain]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeDelete()
        return results.rowcount

