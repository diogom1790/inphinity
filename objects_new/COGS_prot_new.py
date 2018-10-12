# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:02:29 2018

@author: Diogo
"""

from SQL_obj_new.COGS_prot_sql_new import _COGS_prot_sql_new

class COGSprot(object):
    """
    This class treat the COG_prot object has it exists in COGS_PROT table database
    By default, all FK are in the lasts positions in the parameters declaration
    This object is used to connect the COGs with the proteins
    """

    def __init__(self, id_COG_prot = -1, FK_id_COG = -1, FK_id_prot = -1):
        """
        Constructor of the Proteindomain object. All the parameters have a default value

        :param id_COG_prot: id of the COG_PROT - -1 if unknown
        :param FK_id_COG: id of the COG - -1 if unknown
        :param FK_id_prot: id of the Protein - -1 if unknown

        :type id_COG_prot: int - required 
        :type FK_id_COG: int - required 
        :type FK_id_prot: int - required
        """
        self.id_COG_prot = id_COG_prot
        self.FK_id_COG = FK_id_COG
        self.FK_id_prot = FK_id_prot

    def get_all_COG_prot():
        """
        return an array with all the COGs protein in the database


        :return: array of COGS_protein
        :rtype: array(COGS_protein)
        """
        listOfCogsProt= []
        sqlObj = _COGS_prot_sql_new()
        results = sqlObj.select_all_cogprot_all_attributes()
        for element in results:
            listOfCogsProt.append(COGSprot(element[0], element[1], element[2]))
        return listOfCogsProt

    def get_all_COGSprot_by_protein_id(id_protein):
        """
        return an array with all the COGS prot from a protein id

        :param id_protein: id of the protein - -1 if unknown

        :type id_protein: int - required 

        :return: array of COGSprot
        :rtype: array(COGSprot)
        """
        listOfProtDom = []
        sqlObj = _COGS_prot_sql_new()
        results = sqlObj.select_all_prodom_all_attributes_by_protein_id(id_protein)
        for element in results:
            listOfProtDom.append(COGSprot(element[0], element[1], element[2]))
        return listOfProtDom

    def create_COGSprot_if_not_exist(self):
        """
        Insert a COG_prot in the database if it doesn't yet exists and return it id
        The COGS_prot contain:
        - Id of the COGS
        - Id of the protein

        :return: id COGS_prot
        :rtype int
        """
        sqlObj = _COGS_prot_sql_new()
        value_protdom = sqlObj.insert_cog_prot_if_not_exist(self.FK_id_COG, self.FK_id_prot)
        return value_protdom

    def remove_COGProt_by_protein_id(id_protein):
        """
        remove a COGprot given its protein id

        :param id_protein: id of the protein

        :type id_protein: int - required

        :return: COG_prot it removed
        :rtype: int
        """
        sqlObj = _COGS_prot_sql_new()
        id_couple = sqlObj.remove_COG_protein_by_prot_id(id_protein)
        return id_couple

    def __str__(self):
        """
        Ovewrite of the str method
        """
        message_str = "ID: {0:d} COG id: {1} Protein id: {2}".format(self.id_COG_prot, self.FK_id_COG, self.FK_id_prot)
        return message_str