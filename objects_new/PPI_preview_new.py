# -*- coding: utf-8 -*-
"""
Created on Fri May 4 09:05:16 2018

@author: Diogo
"""

from SQL_obj_new.PPI_preview_sql_new import _PPIpreview_sql_new

class PPI_preview(object):
    """
    This class treat the PPI_preview object has it exists in PPI_preview table database
    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, id_ppi_prev = -1, score_ppi_prev = -1, type_ppi_prev = -1, fk_couple = -1, fk_prot_bact = -1, fk_prot_phage = -1):
        """
        Constructor of the Organism object. All the parameters have a default value

        :param id_ppi_prev: id of the PPI_prev - -1 if unknown
        :param score_ppi_prev: gi of the score of the PPI - -1 if unknown
        :param type_ppi_prev: type of PPI (1 - 3DID, 2 - iPfam, 3 - ME, 4 - sum other) - -1 if unknown
        :param fk_couple: fk of the couple - -1 if unknown
        :param fk_prot_bact: fk of the bacterium protein- -1 if unknown
        :param fk_prot_phage: fk of the phage protein - -1 if unknown

        :param id_ppi_prev: int - not required
        :param score_ppi_prev: int - required
        :param type_ppi_prev: int - required
        :param fk_couple: int - required
        :param fk_prot_bact: int - required
        :param fk_prot_phage: int - required
        :type fk_source_data: int - required
        """
        self.id_ppi_prev = id_ppi_prev
        self.score_ppi_prev = score_ppi_prev
        self.type_ppi_prev = type_ppi_prev
        self.fk_couple = fk_couple
        self.fk_prot_bact = fk_prot_bact
        self.fk_prot_phage = fk_prot_phage

    def create_ppi_preview(self):
        """
        Insert a PPI_preview in the database. 
        
        The id of the PPI_preview is updated

        :return: id of the PPI_preview
        :rtype: int
        """
        ppi_id = None
        sqlObj = _PPIpreview_sql_new()

        ppi_id = sqlObj.insert_PPI(self.score_ppi_prev, self.type_ppi_prev, self.fk_couple, self.fk_prot_bact, self.fk_prot_phage)
        self.id_ppi_prev = ppi_id
        return ppi_id

    def get_ppi_preview_scores_grouped_by_couple_id(couple_id):
        """
        Return all PPI scores grouped in a array given its couple id

        :param id_couple: id of the couple - -1 if unknown

        :type id_couple: text - required 

        :return: array of PPI_preview scores
        :rtype: array(int)
        """
        list_scores_PPI = []
        sqlObj = _PPIpreview_sql_new()
        results = sqlObj.select_all_ppi_preview_grouped_by_couple_id(couple_id)
        for element in results:
            list_scores_PPI.append(int(element[2]))
        return list_scores_PPI

    def get_all_ppi_preview_couple():
        """
        Return all PPI preview couple treated

        :return: array of PPI_preview fk couples
        :rtype: array(int)
        """
        list_scores_PPI_fk_couple = []
        sqlObj = _PPIpreview_sql_new()
        results = sqlObj.select_all_ppi_preview_fk_couples()
        for element in results:
            list_scores_PPI_fk_couple.append(element[0])
        return list_scores_PPI_fk_couple

    def get_max_ppi_score():
        """
        Return the max ppi score obtained in the DB

        :return: biggest ppi score
        :rtype: int
        """
        list_scores_PPI_fk_couple = []
        sqlObj = _PPIpreview_sql_new()
        results = sqlObj.select_all_score_PPI()
        for element in results:
            list_scores_PPI_fk_couple.append(element[2])
        max_value = max(list_scores_PPI_fk_couple)
        return max_value

    def get_number_ppi_score_by_bact_phage_prots(fk_prot_bac, fk_prot_phage):
        """
        Return the ppi score given the bacterium and phage protein ids

        :param fk_prot_bac: fk of the bacterium protein - -1 if unknown
        :param fk_prot_phage: fk of the phage protein - -1 if unknown

        :type fk_prot_bac: text - required 
        :type fk_prot_phage: text - required 

        :return: quantity of scores
        :rtype: int
        """

        sqlObj = _PPIpreview_sql_new()
        results = sqlObj.count_ppi_preview_by_ids_ppi(fk_prot_bac, fk_prot_phage)
        return results[0][0]

    def remove_PPI_preview_by_protein_id(id_protein):
        """
        remove a PPI_preview given the protein id

        :param id_protein: id of the protein

        :type id_protein: int - required

        :return: prot_dom it removed
        :rtype: int
        """
        sqlObj = _PPIpreview_sql_new()
        id_couple = sqlObj.remove_PPI_preview_by_prot_id(id_protein)
        return id_couple



