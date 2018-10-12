# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:06:40 2017

@author: Diogo Leite
"""

# here the FK values was selected in lastas positions according to Species_new object class

from DAL import *
from configuration.configuration_data import *

class _Species_sql_new(object):
    """
    This class manipulate the SPECIES table in the database

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
        
    def select_all_species_all_attributes(self):
        """
        return all the Species in the database

        :return: cursor with all species
        :rtype Cursor list
        """
        sql_string = "SELECT id_specie_SP, designation_SP, FK_id_genus_GE_SP FROM SPECIES"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_specie_by_bacterium_id(self, id_bacterium):
        """
        return a specie given bacterium id
        If any exist it is returned -1

        :param id_bacterium: id of the bacterium - -1 if unknown

        :type id_bacterium: int - not required 

        :return: cursor with all species
        :rtype Cursor list
        """
        sql_string = "select id_specie_SP, designation_SP, FK_id_genus_GE_SP from SPECIES, STRAINS, ORGANISMS WHERE FK_id_specie_SP_ST = id_specie_SP and FK_id_strain_ST_OR = id_strain_ST and id_organism_OR = " + str(id_bacterium)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        if len(results) == 0:
            return -1
        else:
            return results[0]

    def insert_specie_if_not_exist_in_Genus(self, specieName, genus_id):
        """
        Insert a Specie if it not yet exist (based on the designation)

        :param specieName: name of the specie
        :param genus_id: FK of the specie's genus - -1 if unknown

        :type genusName: string - required 
        :type genus_id: int - required 

        :return: id of the specie inserted
        :rtype int

        :note:: it not verify the complete taxonomy but just only if the specie already exists in a give genus.

        """
        id_specie = self.get_specie_id_by_designation_and_genus_id(specieName, genus_id)
        if id_specie == -1:
            sql_string = "INSERT INTO SPECIES (designation_SP, FK_id_genus_GE_SP) VALUES (%s, %s)"
            params = [specieName, genus_id]
            dalObj = DAL(self.db_name, sql_string)
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            print("The specie: %s already exists in the genus id: %d" %(str(specieName), genus_id))
            return id_specie

    def get_specie_id_by_designation_and_genus_id(self, designation, genus_id):
        """
        get the id of a Specie based on its designation and genus_id

        :param designation: designation of the specie
        :param genus_id: FK id_genus

        :type designation: string - required 
        :type genus_id: int - required 

        :return: id of the couple or -1 if inexistant
        :rtype int
        """
        sql_string = "SELECT id_specie_SP FROM SPECIES WHERE designation_SP = '" + str(designation) + "' AND FK_id_genus_GE_SP = " + str(genus_id)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]


    def get_specie_by_id(self, id_specie):
        """
        Get a specie by its id

        :return: Specie elements info
        :rtype List(infos species)
        """
        sql_string = "SELECT id_specie_SP, designation_SP, FK_id_genus_GE_SP FROM SPECIES WHERE id_specie_SP = " + str(id_specie)
        dalobj = DAL(self.db_name, sql_string)
        results = dalobj.executeSelect()

        return results[0]


    def get_specie_by_organism_id(self, id_organism):
        """
        Get a strain by an organism id

        :return: Strain elements info
        :rtype List(infos organism)
        """
        sql_string = "SELECT id_specie_SP, designation_SP, FK_id_genus_GE_SP FROM STRAINS, SPECIES, ORGANISMS WHERE FK_id_specie_SP_ST = id_specie_SP and id_strain_ST = FK_id_strain_ST_OR and id_organism_OR =  " + str(id_organism)
        dalobj = DAL(self.db_name, sql_string)
        results = dalobj.executeSelect()

        return results[0]

    def select_all_species_of_genus_id(self, id_genus):
        """
        return all the Species in the database based on a genus id

        :param id_genus: id of the genus  - -1 if unknown

        :type id_genus: int - not required 

        :return: cursor with all species
        :rtype Cursor list
        """
        sql_string = "SELECT id_specie_SP, designation_SP, FK_id_genus_GE_SP FROM SPECIES WHERE FK_id_genus_GE_SP = " + str(id_genus)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_species_frequency_couples_by_phage_id_positive(self, phage_id):
        """
        return the frequencies list of interactions where appear a given phage id

        :return: cursor with all species frequencies
        :rtype Cursor list
        """
        sql_string = "select id_specie_SP, designation_SP, FK_id_genus_GE_SP, count(id_specie_SP) as 'Quantity' FROM SPECIES, STRAINS, ORGANISMS, COUPLES WHERE FK_id_organism_phage_OR_CP = " + str(phage_id) + " and FK_id_organism_bact_OR_CP = id_organism_OR and FK_id_strain_ST_OR = id_strain_ST and FK_id_specie_SP_ST = id_specie_SP and interaction_CP = 1 group by id_specie_SP;"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results


