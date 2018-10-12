# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:10:46 2017

@author: Diogo Leite
"""

from SQL_obj_new.Family_sql_new import _Family_sql_new

class Family(object):
    """
    This class treat the Family object has it exists in FAMILIES table database
    By default, all FK are in the lasts positions in the parameters declaration
    """
    def __init__(self, id_family = -1, designation = ""):
        """
        Constructor of the Family object. All the parameters have a default value

        :param id_family: id of the family - -1 if unknown
        :param designation: designation of the family

        :type id_family: int - no required
        :type designation: text - required 
        """
        self.id_family = id_family
        self.designation = designation
        
    def get_all_Families():
        """
        return an array with all the Families in the database

        :return: array of families
        :rtype: array(Family)
        """
        listOfFamilies = []
        sqlObj = _Family_sql_new()
        results = sqlObj.select_all_families_all_attributes()
        for element in results:
            listOfFamilies.append(Family(element[0], element[1]))
        return listOfFamilies
    
    def create_family(self):
        """
        Insert a family in the database if it not already exits
        The family contain a :
        - designation

        :return: id of the family
        :rtype int
        """
        sqlObj = _Family_sql_new()
        value_fam = sqlObj.insert_family_if_not_exist(self.designation)
        self.id_family = value_fam
        return value_fam

    def get_family_by_id(id_family):
        """
        Get a family by its id
  
        :return: Family object
        :rtype: Family
        """
        sqlObj = _Family_sql_new()
        family_result = sqlObj.get_family_by_id(id_family)
        family_obj = Family(family_result[0], family_result[1])
        return family_obj

    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d} Family: {1}".format(self.id_family, self.designation)
        return message_str
            

        