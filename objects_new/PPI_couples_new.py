# -*- coding: utf-8 -*-
"""
Created on Fri Jun 8 15:45:16 2017

@author: Diogo
"""

from SQL_obj_new.PPI_couples_sql_new import _PPI_couple_sql_new

class PPI_couple(object):
    """
    This class treat the PPI_couple object has it exists in PPI_couple table database
    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, id_PCP = -1, FK_prot_bact = -1, FK_prot_phage = -1, FK_couple = -1):
        """
        Constructor of the Organism object. All the parameters have a default value

        :param id_PCP: id of the PPI_couple - -1 if unknown
        :param FK_prot_bact: id of the bacterium protein - -1 if unknown
        :param FK_prot_phage: id of the phage bacterium
        :param FK_couple: id of the phage bacterium

        :param id_PCP: int - not required
        :param FK_prot_bact: int - required
        :param FK_prot_phage: int - required
        :param FK_couple: int - required
        """
        self.id_PCP = id_PCP
        self.FK_prot_bact = FK_prot_bact
        self.FK_prot_phage = FK_prot_phage
        self.FK_couple = FK_couple

    def create_ppi_couple(self):
        """
        Insert a PPI_couple in the database. 
        
        The id of the PPI_couple is updated

        :return: id of the PPI_couple
        :rtype: int
        """
        ppi_id = None
        sqlObj = _PPI_couple_sql_new()

        ppi_id = sqlObj.insert_PPI_couple(self.FK_prot_bact, self.FK_prot_phage, self.FK_couple)
        self.id_PCP = ppi_id
        return ppi_id

    def create_ppi_couple_if_not_exist(self):
        """
        Insert a PPI_couple in the database if not exists and return its id in case of already inserted
        
        The id of the PPI_couple is updated

        :return: id of the PPI_couple
        :rtype: int
        """
        ppi_id = None
        sqlObj = _PPI_couple_sql_new()

        ppi_id = PPI_couple.get_ppi_couple_ID_by_FKs_prots(self.FK_prot_bact, self.FK_prot_phage)
        if ppi_id == -1:
            ppi_id = sqlObj.insert_PPI_couple(self.FK_prot_bact, self.FK_prot_phage, self.FK_couple)
        self.id_PCP = ppi_id
        return ppi_id

    def get_ppis_couple_by_couple_id(couple_id):
        """
        Return all the PPI_couple for a given couple id

        :param couple_id: id of the PPI_couple - -1 if unknown

        :param couple_id: int - not required

        :return: list with all the ppi_couple objects
        :rtype: list[PPI_couple]
        """
        list_ppi_couple = []
        sqlObj = _PPI_couple_sql_new()
        results = sqlObj.select_all_ppi_preview_give_couple_id(couple_id)
        for element in results:
            list_ppi_couple.append(PPI_couple(element[0], element[1], element[2], element[3]))
        return list_ppi_couple

    def get_ppi_couple_by_FKs_prots(FK_id_prot_bact, FK_id_prot_phage):
        """
        return the the PPI_couple given ithese FKs

        :param FK_id_prot_bact: id of the couple - -1 if unknown
        :param FK_id_prot_phage: id of the couple - -1 if unknown

        :type FK_id_prot_bact: text - required 
        :type FK_id_prot_phage: text - required 

        :return: cursor with all the scores
        :rtype Cursor list
        """
        ppi_couple_obj = PPI_couple()
        sqlObj = _PPI_couple_sql_new()
        results = sqlObj.get_PPI_couple_by_FK(FK_id_prot_bact, FK_id_prot_phage)
        if (len(results) == 1):
            ppi_couple_obj = PPI_couple(results[0][0], results[0][1], results[0][2], results[0][3])
        return ppi_couple_obj

    def get_ppi_couple_ID_by_FKs_prots(FK_id_prot_bact, FK_id_prot_phage):
        """
        return the the PPI_couple ID given ithese FKs

        :param FK_id_prot_bact: id of the couple - -1 if unknown
        :param FK_id_prot_phage: id of the couple - -1 if unknown

        :type FK_id_prot_bact: text - required 
        :type FK_id_prot_phage: text - required 

        :return: id of the PPI_couple or -1 if it does not exist
        :rtype int
        """
        ppi_couple_id = 0
        sqlObj = _PPI_couple_sql_new()
        results = sqlObj.get_PPI_couple_by_FK(FK_id_prot_bact, FK_id_prot_phage)
        if (len(results) == 1):
            ppi_couple_id = results[0][0]
        else :
            ppi_couple_id = -1
        return ppi_couple_id

    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d} FK prot bact: {1} FK prot phage {2} FK couple {3}".format(self.id_PCP, self.FK_prot_bact, self.FK_prot_phage, self.FK_couple)
        return message_str