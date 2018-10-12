# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:06:02 2017

@author: Diogo Leite
"""

from SQL_obj_new.Species_sql_new import _Species_sql_new

class Specie(object):
    """
    This class treat the Species object has it exists in SPECIES table database

    By default, all FK are in the lasts positions in the parameters declaration
    """
    def __init__(self, id_specie = -1, designation = "", fk_genus = -1):
        """
        Constructor of the Specie object. All the parameters have a default value

        :param id_genus: id of the specie - -1 if unknown
        :param designation: designation of the specie
        :param fk_family: FK of the specie's genus - -1 if unknown

        :type id_specie: int - not required 
        :type designation: text - required 
        :type fk_genus: text - required
        """
        self.id_specie = id_specie
        self.fk_genus = fk_genus
        self.designation = designation
        
    def get_all_Species(self):
        """
        return an array with all the Species in the database

        :return: array of specie
        :rtype: array(Specie)
        """
        listOfSpecies = []
        sqlObj = _Species_sql_new()
        results = sqlObj.select_all_species_all_attributes()
        for element in results:
            listOfSpecies.append(Species(element[0], element[1], element[2]))
        return listOfSpecies

    def get_specie_by_bacterium_id(id_bacterium):
        """
        return a Specie of a given bacterium
        If any exist it is returned -1

        :param id_bacterium: id of the bacterium - -1 if unknown

        :type id_bacterium: int - not required 

        :return: specie object
        :rtype: Specie
        """
        specie_obj = None
        sqlObj = _Species_sql_new()
        results = sqlObj.select_specie_by_bacterium_id(id_bacterium)
        if results != -1:
            specie_obj = Specie(results[0], results[1], results[2])
            return specie_obj
        else:
            return -1
    
    def create_specie(self):
        """
        Insert a Specie in the database if it doesn't yet exists in the genus and return it id
        The Specie contain:
        - Designation
        - Id of the genus

        :return: id Specie
        :rtype int
        """

        sqlObj = _Species_sql_new()
        value_specie = sqlObj.insert_specie_if_not_exist_in_Genus(self.designation, self.fk_genus)
        self.id_specie = value_specie
        return value_specie

    def get_specie_by_id(id_specie):
        """
        Get a specie by its id
  
        :return: Specie object
        :rtype: Specie
        """
        sqlObj = _Species_sql_new()
        specie_result = sqlObj.get_specie_by_id(id_specie)
        specie_obj = Specie(specie_result[0], specie_result[1], specie_result[2])
        return specie_obj

    def get_specie_id_by_organism_id(organism_id):
        """
        Get a strain by an id of a organisms
  
        :return: Strain object
        :rtype: Strain
        """
        sqlObj = _Species_sql_new()
        specie_result = sqlObj.get_specie_by_organism_id(organism_id)
        strain_obj = Specie(specie_result[0], specie_result[1], specie_result[2])
        return strain_obj

    def get_all_species_by_genus_id(id_genus):
        """
        return an array with all the Species of a given genus

        :param id_genus: id of the genus  - -1 if unknown

        :type id_genus: int - not required 

        :return: array of specie
        :rtype: array(Specie)
        """
        listOfSpecies = []
        sqlObj = _Species_sql_new()
        results = sqlObj.select_all_species_of_genus_id(id_genus)
        for element in results:
            listOfSpecies.append(Specie(element[0], element[1], element[2]))
        return listOfSpecies

    def get_all_quantity_couple_by_specie_by_phage_id_positive(id_phage):
        """
        return a dictionnary with strain objects and these quantites

        :param id_phage: id of the phage  - -1 if unknown

        :type id_phage: int - not required 

        :return: dictionary of specie frequencies
        :rtype: dictionray{Specie obj : int}
        """
        dictionaryFrequencies = {}
        sqlObj = _Species_sql_new()
        results = sqlObj.select_all_species_frequency_couples_by_phage_id_positive(id_phage)
        for element in results:
            SpecieObj = Specie(element[0], element[1], element[2])
            dictionaryFrequencies[SpecieObj] = element[3]
        return dictionaryFrequencies

    def __str__(self):
        """
        Ovewrite of the str method
        """
        message_str = "ID: {0:d}, Genus id {1:d}, Type of Specie: {2}".format(self.id_specie, self.fk_genus, self.designation)
        return message_str