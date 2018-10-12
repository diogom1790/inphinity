# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:47:58 2017

@author: Diogo
"""

from SQL_obj_new.Domain_sql_new import _Domain_sql_new

class Domain(object):
    """
    This class treat the Domain object has it exists in DOMAINS table database
    By default, all FK are in the lasts positions in the parameters declaration
    """    
    def __init__(self, id_domain = -1, designation = ""):
        """
        Constructor of the Domain object. All the parameters have a default value

        :param id_domain: id of the domain - -1 if unknown
        :param designation: name of the domain (usualy PFXXXXX)

        :type id_domain: int - not required
        :type designation: text - required 
        """
        self.id_domain = id_domain
        self.designation = designation
        
    def get_all_Domains():
        """
        return an array with all the Domains score in the database

        :return: array of domains
        :rtype: array(Domain)
        """
        listOfDomains = []
        sqlObj = _Domain_sql_new()
        results = sqlObj.select_all_domains_all_attributes()
        for element in results:
            listOfDomains.append(Domain(element[0], element[1]))
        return listOfDomains
    
    def create_domain(self):
        """
        Insert a Domain in the database if not already exists
        The domain have a:
        - designation

        :return: id of the domaine
        :rtype int
        """
        sqlObj = _Domain_sql_new()
        value_domain = sqlObj.insert_domain_if_not_exists(self.designation)
        self.id_domain = value_domain
        return value_domain

    def get_id_domain_by_description(self):
        """
        Return the id of an existing domain in the database based on its description
        The domain have a:
        - designation

        :return: id of the domaine
        :rtype int
        """
        sqlObj = _Domain_sql_new()
        id_domain = sqlObj.get_id_domain_by_description(self.designation)
        self.id_domain = id_domain
        return id_domain

        
    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d} Domain: {1}".format(self.id_domain, self.designation)
        return message_str