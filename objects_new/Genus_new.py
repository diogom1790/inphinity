# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:16:59 2017

@author: Diogo Leite
"""

from SQL_obj_new.Genus_sql_new import _Genus_sql_new

class Genus(object):
    """
    This class treat the Genus object has it exists in GENUESES table database
    By default, all FK are in the lasts positions in the parameters declaration
    """
    def __init__(self, id_genus = -1, designation = "", fk_family = -1):
        """
        Constructor of the Genus object. All the parameters have a default value

        :param id_genus: id of the genus - -1 if unknown
        :param designation: designation of the genus
        :param fk_family: family FK key - -1 if unknown

        :type id_genus: int - not required 
        :type designation: text - required 
        :type fk_family: text - required
        """
        self.id_genus = id_genus
        self.fk_family = fk_family
        self.designation = designation
        
    def get_all_Genus(self):
        """
        Retourne une liste de touts les genres qui sont dans la base de données

        :return: array de genres
        :rtype: array(Genus)
        """
        listOfGenus = []
        sqlObj = _Genus_sql_new()
        results = sqlObj.select_all_genus_all_attributes()
        for element in results:
            listOfGenus.append(Genus(element[0], element[1], element[2]))
        return listOfGenus
    
    
    def create_genus(self):
        """
        Créer un genre, l'insert dans la base de données et retourne son id
        le genre créé contient:
        - une désignation
        - l'id de famille à laquelle il appartient

        :return: id genre
        :rtype int
        """
        sqlObj = _Genus_sql_new()
        value_genus = sqlObj.insert_genus_if_not_exist_in_Family(self.designation, self.fk_family)
        self.id_genus = value_genus
        return value_genus

    def get_genus_by_family_id(id_family):
        """
        Get a list of genuses of a given family id

        :param id_family: id of the family that we want the genus

        :type id_family: int - required 
  
        :return: array of genus
        :rtype: array(Genus)
        """
        listOfGenus = []
        sqlObj = _Genus_sql_new()
        results = sqlObj.get_genus_by_family_id(id_family)
        for element in results:
            listOfGenus.append(Genus(element[0], element[1], element[2]))
        return listOfGenus

    def get_genus_by_id(id_genus):
        """
        Get a genus by its id
  
        :return: Genus object
        :rtype: Genus
        """
        sqlObj = _Genus_sql_new()
        element = sqlObj.get_genus_by_id(id_genus)
        genus_obj = Genus(element[0], element[1], element[2])
        return genus_obj


    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d} Family FK: {1:d}, Genus name {2}".format(self.id_genus, self.fk_family, self.designation)
        return message_str
