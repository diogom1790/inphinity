# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:40:55 2017

@author: Diogo
"""

from SQL_obj_new.Couple_sql_new import _Couple_sql_new

class Couple(object):
    """
    This class treat the Couples object has it exists in COUPLES table database

    By default, all FK are in the lasts positions in the parameters declaration

    Interactions type:
    - 1 - exists - positive
    - 0 - not exists - negative
    """
    def __init__(self, id_couple, interact_pn,  fk_bacteria, fk_phage, fk_type_inter, fk_level_interact, fk_lysis_inter = -1, fk_source_data = -1):
        """
        Constructor of the Couple object. All the parameters have a default value

        :param id_family: id of the couple - -1 if unknown
        :param interact_pn: Type of interaction (positive or negative) - -1 if unknown
        :param fk_bacteria: Bacterium FK key - -1 if unknown
        :param fk_phage: Bacterium FK key - -1 if unknown
        :param fk_type_inter: Bacterium FK key - -1 if unknown
        :param fk_level_interact: Bacterium FK key - -1 if unknown
        :param fk_lysis_inter: In case of positif interaction and if it comes from Grég, we have the information about the degree of "infection" - -1 if unknown
        :param fk_source_data: Source where we see the interaction (NCBI, PhageDB, Grég,...)

        :type id_family: int - no required
        :type interact_pn: int - required 
        :type fk_bacteria: int - required 
        :type fk_phage: int - required 
        :type fk_type_inter: int - required 
        :type fk_level_interact: int - required 
        :type fk_lysis_inter: int - not required
        :type fk_source_data: int - required
        """
        self.id_couple = id_couple
        self.fk_bacteria = fk_bacteria
        self.fk_phage = fk_phage
        self.fk_type_inter = fk_type_inter
        self.fk_level_interact = fk_level_interact
        self.interact_pn = interact_pn
        self.fk_lysis_inter = fk_lysis_inter
        self.fk_source_data = fk_source_data
        
    def get_all_couples():
        """
        return an array with all the couples in the database

        :return: array of couple
        :rtype: array(Couple)
        """
        listOfCouples = []
        sqlObj = _Couple_sql_new()
        results = sqlObj.select_all_couples_all_attributes()
        for element in results:
            listOfCouples.append(Couple(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7]))
        return listOfCouples

    def get_couples_by_list_id(list_ids):
        """
        return an array with all the couples in the database given an array with these ids

        :return: array of couple
        :rtype: array(Couple)
        """
        listOfCouples = []
        sqlObj = _Couple_sql_new()
        results = sqlObj.select_all_couples_all_attributes_by_arrays_ids(list_ids)
        for element in results:
            listOfCouples.append(Couple(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7]))
        return listOfCouples

    def get_all_couples_by_phage_id(fk_phage):
        """
        return an array with all the couples in the database based on phage fk_id

        :param fk_phage: id of the phage - -1 if unknown

        :type fk_phage: int - required

        :return: array of couple
        :rtype: array(Couple)
        """
        listOfCouples = []
        sqlObj = _Couple_sql_new()
        results = sqlObj.select_all_couples_all_attributes_by_fk_phage(fk_phage)
        for element in results:
            listOfCouples.append(Couple(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7]))
        return listOfCouples




    def get_all_positive_couples_by_phage_id(fk_phage):
        """
        return an array with all the positive couples in the database based on phage fk_id

        :param fk_phage: id of the phage - -1 if unknown

        :type fk_phage: int - required

        :return: array of couple
        :rtype: array(Couple)
        """
        listOfCouples = []
        sqlObj = _Couple_sql_new()
        results = sqlObj.select_all_positive_couples_all_attributes_by_fk_phage(fk_phage)
        for element in results:
            listOfCouples.append(Couple(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7]))
        return listOfCouples

    def get_all_positive_couples_by_phage_id_level_id(fk_phage, fk_level):
        """
        return an array with all the positive couples in the database based on phage fk_id_phage and the level id

        :param fk_phage: id of the phage - -1 if unknown

        :type fk_phage: int - required

        :return: array of couple
        :rtype: array(Couple)
        """
        listOfCouples = []
        sqlObj = _Couple_sql_new()
        results = sqlObj.select_all_positive_couples_all_attributes_by_fk_phage_level_id(fk_phage, fk_level)
        for element in results:
            listOfCouples.append(Couple(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7]))
        return listOfCouples

    def get_all_couples_by_bacterium(fk_bacterium):
        """
        return an array with all the couples in the database based on bacterium fk_id

        :param fk_bacterium: id of the bacterium - -1 if unknown

        :type fk_bacterium: int - required

        :return: array of couple
        :rtype: array(Couple)
        """
        listOfCouples = []
        sqlObj = _Couple_sql_new()
        results = sqlObj.select_all_couples_all_attributes_by_fk_bacterium(fk_bacterium)
        for element in results:
            listOfCouples.append(Couple(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7]))
        return listOfCouples

    def get_all_couples_positiv_by_bacterium_level(fk_bacterium, fk_level):
        """
        return an array with all the couples in the database based on bacterium fk_id

        :param fk_bacterium: id of the bacterium - -1 if unknown
        :param fk_level: id of the interaction leve

        :type fk_bacterium: int - required
        :type fk_level: int - required

        :return: array of couple
        :rtype: array(Couple)
        """
        listOfCouples = []
        sqlObj = _Couple_sql_new()
        results = sqlObj.select_all_couples_all_attributes_by_fk_bacterium_level_type(fk_bacterium, fk_level, 1)
        for element in results:
            listOfCouples.append(Couple(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7]))
        return listOfCouples

    def get_all_couples_negative_by_bacterium_level(fk_bacterium, fk_level):
        """
        return an array with all the couples in the database based on bacterium fk_id

        :param fk_bacterium: id of the bacterium - -1 if unknown
        :param fk_level: id of the interaction leve

        :type fk_bacterium: int - required
        :type fk_level: int - required

        :return: array of couple
        :rtype: array(Couple)
        """
        listOfCouples = []
        sqlObj = _Couple_sql_new()
        results = sqlObj.select_all_couples_all_attributes_by_fk_bacterium_level_type(fk_bacterium, fk_level, 2)
        for element in results:
            listOfCouples.append(Couple(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7]))
        return listOfCouples


    def get_all_couples_by_type_level_source(interaction_type, fk_level, fk_source):
        """
        return an array with all the couples in the database based on interaction type (positive or negative), level (specie, strain,...) and source (NCBI, Phages,...)

        :param interaction_type: id of the bacterium - -1 if unknown
        :param fk_level: id of the interaction leve
        :param fk_source: id of the interaction leve

        :type interaction_type: int - required
        :type fk_level: int - required
        :type fk_source: int - required

        :return: array of couple
        :rtype: array(Couple)
        """
        listOfCouples = []
        sqlObj = _Couple_sql_new()
        results = sqlObj.select_all_couples_all_attributes_by_type_level_source(interaction_type, fk_level, fk_source)
        for element in results:
            listOfCouples.append(Couple(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7]))
        return listOfCouples
    
    def create_couple(self):
        """
        Insert a Couple in the database if it not already exits and update its id
        The Couple contain a :
        - Interaction 
        - Bacterium
        - Phage
        - Type interaction
        - Level interaction
        - Level of lysis
        - Source of data

        :return: id of the Couple
        :rtype int
        """
        value_couple = None
        sqlObj = _Couple_sql_new()
        value_couple = sqlObj.insert_couple_if_ot_exist(self.interact_pn, self.fk_bacteria, self.fk_phage, self.fk_type_inter, self.fk_level_interact, self.fk_lysis_inter, self.fk_source_data)
        self.id_couple = value_couple
        print(value_couple)
        return value_couple

    def remove_couple_by_id(id_couple):
        """
        remove a couple given its id

        :param id_couple: id of the couple

        :type id_couple: int - required

        :return: couple it removed
        :rtype: int
        """
        sqlObj = _Couple_sql_new()
        id_couple = sqlObj.remove_couple_by_id(id_couple)
        return id_couple

    def remove_couple_by_id_bacterium(id_bacterium):
        """
        remove a couple given its id_bacterium

        :param id_bacterium: id of the couple

        :type id_bacterium: int - required

        :return: couple it removed
        :rtype: int
        """
        sqlObj = _Couple_sql_new()
        id_couple = sqlObj.remove_couple_by_fk_bacterium(id_bacterium)
        return id_couple

    def verify_couple_exist_by_phage_bact(id_bact, id_phage):
        """
        Verify if a couple exists by the couple of phage, bact

        :param id_bact: id of the couple
        :param id_phage: id of the couple

        :type id_bact: int - required
        :type id_bacterium: int - required

        :return: couple it removed
        :rtype: int
        """
        sqlObj = _Couple_sql_new()
        id_couple = sqlObj.get_id_couple_by_phage_bact(id_bact, id_phage)
        return id_couple


    def get_all_couples_by_type_level_source_bact_id(interaction_type, fk_level, fk_source, fk_bact):
        """
        return an array with all the couples in the database based on interaction type (positive or negative), level (specie, strain,...) source (NCBI, Phages,...) and bacterium id

        :param interaction_type: id of the bacterium - -1 if unknown
        :param fk_level: id of the interaction leve
        :param fk_source: id of the interaction leve
        :param fk_bact: id of the bacterium

        :type interaction_type: int - required
        :type fk_level: int - required
        :type fk_source: int - required
        :type fk_bact: int - required

        :return: array of couple
        :rtype: array(Couple)
        """
        listOfCouples = []
        sqlObj = _Couple_sql_new()
        results = sqlObj.select_all_couples_all_attributes_by_type_level_source_id_bact(interaction_type, fk_level, fk_source, fk_bact)
        for element in results:
            listOfCouples.append(Couple(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7]))
        return listOfCouples



    def __str__(self):
        """
        Ovewrite of the str method
        """
        message_str = ""
        if type(self.fk_lysis_inter) is not int:
            message_str = "ID: {0:d} Type interaction: {1}, ID bacterium {2:d}, ID phage {3:d}, Interaction state {4:d}, leve {5:d}".format(self.id_couple, self.interact_pn, self.fk_bacteria, self.fk_phage, self.fk_type_inter, self.fk_level_interact)
        elif self.interact_pn == 1:
            message_str = "ID: {0:d} Type interaction: {1}, ID bacterium {2:d}, ID phage {3:d}, Interaction state {4:d}, leve {5:d}, type of lysis {6:d} ".format(self.id_couple, self.interact_pn, self.fk_bacteria, self.fk_phage, self.fk_type_inter, self.fk_level_interact, self.fk_lysis_inter)
        elif self.interact_pn == 0:
            message_str = "ID: {0:d} Type interaction: {1}, ID bacterium {2:d}, ID phage {3:d}, Interaction state {4:d}, leve {5:d}".format(self.id_couple, self.interact_pn, self.fk_bacteria, self.fk_phage, self.fk_type_inter, self.fk_level_interact)
        return message_str    
        