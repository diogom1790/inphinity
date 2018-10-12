# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:30:54 2017

@author: Diogo
"""

from DAL import *
from configuration.configuration_data import *

class _Couple_sql_new(object):
    """
    This class manipulate the COUPLES table in the database

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

    def select_all_couples_all_attributes(self):
        """
        return all the Couples in the database

        :return: cursor with all couples
        :rtype Cursor list
        """
        sql_string = "SELECT id_couple_CP, interaction_CP, FK_id_organism_bact_OR_CP, FK_id_organism_phage_OR_CP, FK_id_type_inter_IT_CP, FK_id_level_LI_CP, FK_id_lysis_LT_CP, FK_source_couple_SD_CP FROM COUPLES"

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_couples_all_attributes_by_arrays_ids(self, list_ids):
        """
        return all the Couples in the database given an list of ids

        :return: cursor with all couples
        :rtype Cursor list
        """
        str_lst = ','.join([str(item) for item in list_ids])
        sql_string = "SELECT id_couple_CP, interaction_CP, FK_id_organism_bact_OR_CP, FK_id_organism_phage_OR_CP, FK_id_type_inter_IT_CP, FK_id_level_LI_CP, FK_id_lysis_LT_CP, FK_source_couple_SD_CP FROM COUPLES WHERE id_couple_CP in (%s)" % str_lst

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_couples_all_attributes_by_fk_phage(self, fk_phage):
        """
        return all the Couples in the database with a phage id

        :return: cursor with all couples
        :rtype Cursor list
        """
        sql_string = "SELECT id_couple_CP, interaction_CP, FK_id_organism_bact_OR_CP, FK_id_organism_phage_OR_CP, FK_id_type_inter_IT_CP, FK_id_level_LI_CP, FK_id_lysis_LT_CP, FK_source_couple_SD_CP FROM COUPLES WHERE FK_id_organism_phage_OR_CP = " + str(fk_phage)

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_positive_couples_all_attributes_by_fk_phage(self, fk_phage):
        """
        return all the Couples in the database with a phage id

        :return: cursor with all couples
        :rtype Cursor list
        """
        sql_string = "SELECT id_couple_CP, interaction_CP, FK_id_organism_bact_OR_CP, FK_id_organism_phage_OR_CP, FK_id_type_inter_IT_CP, FK_id_level_LI_CP, FK_id_lysis_LT_CP, FK_source_couple_SD_CP FROM COUPLES WHERE interaction_CP = 1 and FK_id_organism_phage_OR_CP = " + str(fk_phage)

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_positive_couples_all_attributes_by_fk_phage_level_id(self, fk_phage, level_id):
        """
        return all the Couples in the database with a phage id

        :return: cursor with all couples
        :rtype Cursor list
        """
        sql_string = "SELECT id_couple_CP, interaction_CP, FK_id_organism_bact_OR_CP, FK_id_organism_phage_OR_CP, FK_id_type_inter_IT_CP, FK_id_level_LI_CP, FK_id_lysis_LT_CP, FK_source_couple_SD_CP FROM COUPLES WHERE interaction_CP = 1 and FK_id_organism_phage_OR_CP = " + str(fk_phage) + " AND FK_id_level_LI_CP = " + str(level_id)

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results


    def select_all_positive_couples_all_attributes_by_fk_bacterium(self, fk_bacterium):
        """
        return all the Couples in the database with a bacterium id

        :return: cursor with all couples
        :rtype Cursor list
        """
        sql_string = "SELECT id_couple_CP, interaction_CP, FK_id_organism_bact_OR_CP, FK_id_organism_phage_OR_CP, FK_id_type_inter_IT_CP, FK_id_level_LI_CP, FK_id_lysis_LT_CP, FK_source_couple_SD_CP FROM COUPLES WHERE interaction_CP = 1 and FK_id_organism_bact_OR_CP = " + str(fk_bacterium)

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_couples_all_attributes_by_fk_bacterium_level_type(self, fk_bacterium, fk_level, interaction_type):
        """
        return all the Couples in the database with a bacterium id and level of interaction

        :return: cursor with all couples
        :rtype Cursor list
        """
        sql_string = "SELECT id_couple_CP, interaction_CP, FK_id_organism_bact_OR_CP, FK_id_organism_phage_OR_CP, FK_id_type_inter_IT_CP, FK_id_level_LI_CP, FK_id_lysis_LT_CP, FK_source_couple_SD_CP FROM COUPLES WHERE interaction_CP = " + str(interaction_type) + " and FK_id_organism_bact_OR_CP = " + str(fk_bacterium) + " AND FK_id_level_LI_CP = " + str(fk_level)

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_couples_all_attributes_by_type_level_source(self, interaction_type, fk_level, fk_source):
        """
        return all the couples in the database based on interaction type (positive or negative), level (specie, strain,...) and source (NCBI, Phages,...)

        :return: cursor with all couples
        :rtype Cursor list
        """


        sql_string = "SELECT id_couple_CP, interaction_CP, FK_id_organism_bact_OR_CP, FK_id_organism_phage_OR_CP, FK_id_type_inter_IT_CP, FK_id_level_LI_CP, FK_id_lysis_LT_CP, FK_source_couple_SD_CP FROM COUPLES WHERE interaction_CP = " + str(interaction_type) + " AND FK_id_level_LI_CP = " + str(fk_level) + " AND FK_source_couple_SD_CP = " + str(fk_source) + " ORDER BY FK_id_organism_bact_OR_CP"

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results



    def select_all_couples_all_attributes_by_fk_bacterium(self, fk_bacterium):
        """
        return all the Couples in the database with a bacterium id

        :return: cursor with all couples
        :rtype Cursor list
        """
        sql_string = "SELECT id_couple_CP, interaction_CP, FK_id_organism_bact_OR_CP, FK_id_organism_phage_OR_CP, FK_id_type_inter_IT_CP, FK_id_level_LI_CP, FK_id_lysis_LT_CP, FK_source_couple_SD_CP FROM COUPLES WHERE FK_id_organism_bact_OR_CP = " + str(fk_bacterium)

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results
        
    def insert_couple_if_ot_exist(self, interaction_type, fk_bact, fk_phage, fk_type_inter, fk_level_inter, fk_lysis_inter, fk_source_data):
        """
        Insert a Couple if it not yet exist (based on the pair of bacterium AND phage id)

        :param interaction_type: value of the interaction (1 - positive; 0 - negative)
        :param fk_bact: id of the bacterium
        :param fk_phage: id of the phage
        :param fk_type_inter: id of the type of interaction (verified, not virified,...)
        :param fk_level_inter: level of interaction (family, genus,...)
        :param fk_lysis_inter: type of lysis (in case of positive interaction from grég)
        :param fk_source_data: Source where we see the interaction (NCBI, PhageDB, Grég,...)

        :type familyName: int - required 
        :type fk_bact: int - required 
        :type fk_phage: int - required 
        :type fk_type_inter: int - required 
        :type fk_level_inter: int - required 
        :type fk_lysis_inter: int - required 
        :type fk_source_data: int - required

        :return: id of the couple inserted
        :rtype int
        """

        id_couple = self.get_id_couple_by_phage_bact(fk_bact, fk_phage)
        if id_couple == -1 and (fk_lysis_inter > -1):
            print(fk_lysis_inter)
            sql_string = "INSERT INTO COUPLES (interaction_CP, FK_id_organism_bact_OR_CP, FK_id_organism_phage_OR_CP, FK_id_type_inter_IT_CP, FK_id_level_LI_CP, FK_id_lysis_LT_CP, FK_source_couple_SD_CP) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            params = [interaction_type, fk_bact, fk_phage, fk_type_inter, fk_level_inter, fk_lysis_inter, fk_source_data]

            dalObj = DAL(self.db_name, sql_string)
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params

            results = dalObj.executeInsert()
            return results.lastrowid
        elif id_couple == -1 and (fk_lysis_inter == None or fk_lysis_inter == -1):
            fk_lysis_inter = 7
            sql_string = "INSERT INTO COUPLES (interaction_CP, FK_id_organism_bact_OR_CP, FK_id_organism_phage_OR_CP, FK_id_type_inter_IT_CP, FK_id_level_LI_CP, FK_source_couple_SD_CP) VALUES (%s, %s, %s, %s, %s, %s)"
            params = [interaction_type, fk_bact, fk_phage, fk_type_inter, fk_level_inter, fk_source_data]

            dalObj = DAL(self.db_name, sql_string)
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params

            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            print("The couple with the Bacterium id: {0:d} and phage id: {1:d} already exits in the database".format(fk_bact, fk_phage))
            return id_couple

    def get_id_couple_by_phage_bact(self, fk_bact, fk_phage):
        """
        get the id of a couple based on the ids of the pair phage bacterium

        :param fk_bact: id of the bacterium 
        :param fk_phage: id of the phage

        :type fk_bact: int - required 
        :type fk_phage: int - required 

        :return: id of the couple or -1 if inexistant
        :rtype int
        """
        sql_string = "SELECT id_couple_CP FROM COUPLES WHERE FK_id_organism_bact_OR_CP = '" + str(fk_bact) + "' and FK_id_organism_phage_OR_CP = " + str(fk_phage)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]

    def get_id_couple_by_phage_bact_type_interaction(self, fk_bact, fk_phage, type_inter):
        """
        verify if a couple exist given a phage, bacterium and type interaction. If exists return the id, if not return -1

        :param fk_bact: id of the bacterium 
        :param fk_phage: id of the phage
        :param fk_type_inter: id of the phage

        :type fk_bact: int - required 
        :type fk_phage: int - required 
        :type fk_type_inter: int - required

        :return: id of the couple or -1 if inexistant
        :rtype int
        """
        sql_string = "SELECT id_couple_CP FROM COUPLES WHERE FK_id_organism_bact_OR_CP = '" + str(fk_bact) + "' and FK_id_organism_phage_OR_CP = " + str(fk_phage) + " AND interaction_CP = " + str(type_inter)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]

    def remove_couple_by_id(self, id_couple):
        """
        remove a couple by its id

        :param id_couple: id of the couple 

        :type id_couple: int - required 

        :return: quantity of row deleted
        :rtype int
        """
        sql_string = "DELETE FROM COUPLES WHERE id_couple_CP = %s"
        dalObj = DAL(self.db_name, sql_string)
        params = [id_couple]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeDelete()
        return results.rowcount

    def remove_couple_by_fk_bacterium(self, fk_id_bacterium):
        """
        remove a couple by its id

        :param fk_id_bacterium: id of the fk_bacterium 

        :type fk_id_bacterium: int - required 

        :return: quantity of row deleted row
        :rtype int
        """
        sql_string = "DELETE FROM COUPLES WHERE FK_id_organism_bact_OR_CP = %s"
        dalObj = DAL(self.db_name, sql_string)
        params = [fk_id_bacterium]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeDelete()
        return results.rowcount


    def select_all_couples_all_attributes_by_type_level_source_id_bact(self, interaction_type, fk_level, fk_source, id_bact):
        """
        return all the couples in the database based on interaction type (positive or negative), level (specie, strain,...) and source (NCBI, Phages,...)

        :return: cursor with all couples
        :rtype Cursor list
        """


        sql_string = "SELECT id_couple_CP, interaction_CP, FK_id_organism_bact_OR_CP, FK_id_organism_phage_OR_CP, FK_id_type_inter_IT_CP, FK_id_level_LI_CP, FK_id_lysis_LT_CP, FK_source_couple_SD_CP FROM COUPLES WHERE interaction_CP = " + str(interaction_type) + " AND FK_id_level_LI_CP = " + str(fk_level) + " AND FK_source_couple_SD_CP = " + str(fk_source) + " AND FK_id_organism_bact_OR_CP = " + str(id_bact) +  " ORDER BY FK_id_organism_bact_OR_CP"

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results