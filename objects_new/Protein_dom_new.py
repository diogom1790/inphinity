# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:09:10 2017

@author: Diogo Leite
"""

from SQL_obj_new.Prot_dom_sql_new import _Prot_dom_sql_new
from collections import defaultdict

class ProteinDom(object):
    """
    This class treat the Protein domain object has it exists in PROTDOM table database
    By default, all FK are in the lasts positions in the parameters declaration
    This object is used to connect the domains with the proteins
    """
    def __init__(self, id_proteinDom = -1, Fk_id_protein = -1, Fk_id_domain = -1):
        """
        Constructor of the Proteindomain object. All the parameters have a default value

        :param id_proteinDom: id of the ProteinDom - -1 if unknown
        :param id_protein: id of the protein - -1 if unknown
        :param id_domain: id of the domain - -1 if unknown

        :type id_proteinDom: int - required 
        :type designation: text - required 
        :type fk_family: text - required
        """
        self.id_proteinDom = id_proteinDom
        self.Fk_id_protein = Fk_id_protein
        self.Fk_id_domain = Fk_id_domain
        
    def get_all_protein_domain():
        """
        return an array with all the ProtDom in the database


        :return: array of ProteinDom
        :rtype: array(ProteinDom)
        """
        listOfProtDom = []
        sqlObj = _Prot_dom_sql_new()
        results = sqlObj.select_all_prodom_all_attributes()
        for element in results:
            listOfProtDom.append(ProteinDom(element[0], element[1], element[2]))
        return listOfProtDom

    def get_all_protein_domain_dict():
        """
        return an array with all the ProtDom in the database in a dictionary with ['id_protein']:id_domain


        :return: dictionary of ProteinDom
        :rtype: dict(id_prot:id_dom)
        """
        dict_protein = defaultdict(list)
        sqlObj = _Prot_dom_sql_new()
        results = sqlObj.select_all_prodom_all_attributes()
        for element in results:
            dict_protein[element[1]].append(element[2])
            #if element[1] in dict_protein.keys():
            #    print(element[2])
            #    dict_protein[element[1]] = dict_protein[element[1]].append(element[2])
            #else:
            #    dict_protein[element[1]] = [element[2]]
        return dict_protein

    def get_all_protein_domain_by_protein_id(id_protein):
        """
        return an array with all the ProtDom from a protein id

        :param id_protein: id of the protein - -1 if unknown

        :type id_protein: int - required 

        :return: array of ProteinDom
        :rtype: array(ProteinDom)
        """
        listOfProtDom = []
        sqlObj = _Prot_dom_sql_new()
        results = sqlObj.select_all_prodom_all_attributes_by_protein_id(id_protein)
        for element in results:
            listOfProtDom.append(ProteinDom(element[0], element[1], element[2]))
        return listOfProtDom
    
    def create_protDom_if_not_exist(self):
        """
        Insert a ProdDom in the database if it doesn't yet exists and return it id
        The ProteinDom contain:
        - Id of the protein
        - Id of the domain

        :return: id ProteinDom
        :rtype int
        """
        sqlObj = _Prot_dom_sql_new()
        value_protdom = sqlObj.insert_protdom_if_not_exist(self.Fk_id_protein, self.Fk_id_domain)
        return value_protdom
    
    def protein_number_domains(self):
        """
        Count the number of domain for a given protein

        :return: the numver of domain
        :rtype int
        """
        sqlObj = _Prot_dom_sql_new()
        value_protdom = sqlObj.count_domains_by_protein_id(self.Fk_id_protein)
        if value_protdom == 0:
            print("No domains for the protein id: {0}".format(self.Fk_id_protein))
        return value_protdom

    def remove_prot_dom_by_protein_id(id_protein):
        """
        remove a prot_dom given its protein id

        :param id_protein: id of the protein

        :type id_protein: int - required

        :return: prot_dom it removed
        :rtype: int
        """
        sqlObj = _Prot_dom_sql_new()
        id_couple = sqlObj.remove_prot_dom_by_prot_id(id_protein)
        return id_couple

        
    def __str__(self):
        """
        Ovewrite of the str method
        """
        message_str = "ID: {0:d} Protein id: {1} Domain id: {2}".format(self.id_proteinDom, self.Fk_id_protein, self.Fk_id_domain)
        return message_str
        