# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:26:31 2017

@author: Diogo Leite
"""

from SQL_obj_new.Strain_sql_new import _Strain_sql_new

class Strain(object):
    """
    This class treat the Strains object has it exists in STRAINS table database
    By default, all FK are in the lasts positions in the parameters declaration
    """
    def __init__(self, id_strain = -1, designation = "", fk_specie = -1):
        """
        Constructor of the Strains object. All the parameters have a default value

        :param id_strain: id of the strain - -1 if unknown
        :param designation: designation of the strain
        :param fk_specie: FK of the strain's specie - -1 if unknown

        :type id_strain: int - not required 
        :type designation: text - required 
        :type fk_specie: text - required
        """
        self.id_strain = id_strain
        self.fk_specie = fk_specie
        self.designation = designation
        
    def get_all_Strains(self):
        """
        return an array with all the Strains in the database

        :return: array of strains
        :rtype: array(Strain)
        """
        listOfStrains = []
        sqlObj = _Strain_sql_new()
        results = sqlObj.select_all_species_all_attributes()
        for element in results:
            listOfStrains.append(Strain(element[0], element[1], element[2]))
        return listOfStrains
    
    def create_strain(self):
        """
        Insert a Strain in the database if it doesn't yet exists in the specie and return it id
        The Strain contain:
        - Designation
        - id of the specie

        :return: id of the specie
        :rtype int
        """
        sqlObj = _Strain_sql_new()
        value_strain = sqlObj.insert_strain_if_not_exist_in_Specie(self.designation, self.fk_specie)
        print(value_strain)
        self.id_strain = value_strain
        return value_strain

    def get_id_strin_based_on_design_fk(self, fk_specie):
        """
        get the id of a Strain based its name and specie id

        :param fk_specie: id of the specie of the strain

        :type fk_specie: int - required 

        :return: id of the Strain or -1 if inexistant
        :rtype int
        """
        sqlObj = _Strain_sql_new()
        id_strain = sqlObj.get_strain_id_based_strain_name_and_specie_id(self.designation, fk_specie)
        return id_strain

    def get_strain_by_id(id_strain):
        """
        Get a strain by its id
  
        :return: Strain object
        :rtype: Strain
        """
        sqlObj = _Strain_sql_new()
        strain_result = sqlObj.get_strain_by_id(id_strain)
        strain_obj = Strain(strain_result[0], strain_result[1], strain_result[2])
        return strain_obj


    def remove_strain_by_id(id_strain):
        """
        remove a strain given its id

        :param id_strain: id of the strain

        :type id_strain: int - required

        :return: couple it removed
        :rtype: int
        """
        sqlObj = _Strain_sql_new()
        id_couple = sqlObj.remove_strain_by_id(id_strain)
        return id_couple


    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d} FK Specie: {1} Designation: {2}".format(self.id_strain, self.fk_specie, self.designation)
        return message_str
