# -*- coding: utf-8 -*-
"""
Created on Fri Jan 5 11:29:57 2018

@author: Diogo
"""

from SQL_obj_new.F_score_blast_P_sql_new import _F_score_blast_P_sql

class F_score_blast_P(object):
    """
    This class treat the Feature of score blast object has it exists in F_SCORE_BLAST_P table database
    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, id_f_score_blast_P = -1, pident = -1, length = -1, mismatch = -1, gapopen = -1, pstart = -1, pend = -1, bstart = -1, bend = -1, evalue = -1, bitscore = -1, plen = -1, blen = -1, FK_ppi_couple = -1):
        """
        Constructor of the Score Blast P object. All the parameters have a default value

        :param id_f_score_blast_P: id of the bast score - -1 if unknown
        :param pident: blast score
        :param length: i don't know - -1 if unknown
        :param mismatch: i don't know - -1 if unknown
        :param gapopen: i don't know - -1 if unknown
        :param pstart: i don't know - -1 if unknown
        :param pend: i don't know - -1 if unknown
        :param bstart: i don't know - -1 if unknown
        :param bend: i don't know - -1 if unknown
        :param evalue: i don't know - -1 if unknown
        :param bitscore: i don't know - -1 if unknown
        :param plen: i don't know - -1 if unknown
        :param blen: i don't know - -1 if unknown
        :param FK_ppi_couple: id of the PPI couple - -1 if unknown


        :type id_f_score_blast_P: int - required
        :type pident: float - required 
        :type length: int - required
        :type mismatch: int - required
        :type gapopen: int - required
        :type pstart: int - required
        :type pend: int - required
        :type bstart: int - required
        :type bend: int - required
        :type evalue: double - required
        :type bitscore: double - required
        :type plen: int - required
        :type blen: int - required
        :type FK_ppi_couple: int - required
        """

        self.id_f_score_blast_P = id_f_score_blast_P
        self.pident = pident
        self.length = length
        self.mismatch = mismatch
        self.gapopen = gapopen
        self.pstart = pstart
        self.pend = pend
        self.bstart = bstart
        self.bend = bend
        self.evalue = evalue
        self.bitscore = bitscore
        self.plen = plen
        self.blen = blen
        self.FK_ppi_couple = FK_ppi_couple

    def get_all_f_blast_p_scores(self):
        """
        return an array with all the baslt score in the database

        :return: array of score
        :rtype: array(F_score_blast)
        """
        listOfScoreBlast = []
        sqlObj = _F_score_blast_P_sql()
        results = sqlObj.select_all_score_blast_p_all_attributes()
        for element in results:
            listOfScoreBlast.append(F_score_blast_P(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9], element[10], element[11], element[12], element[13]))
        return listOfScoreBlast

    def create_f_score_blast_p_no_verification(self):
        """
        Insert a f_score_blast in the database WITHOUT ANY VERIFICATION
        
        The id of the f_score_blase is updated

        :return: id of the f_score_blast created
        :rtype: int
        """
        value_f_score_blast = None
        sqlObj = _F_score_blast_P_sql()
        value_f_score_blast = sqlObj.insert_f_score_blast_p(self.pident, self.length, self.mismatch, self.gapopen, self.pstart, self.pend, self.bstart, self.bend, self.evalue, self.bitscore, self.plen, self.blen, self.FK_ppi_couple)
        self.id_f_score_blast_P = value_f_score_blast
        return value_f_score_blast

    def delete_FK_score_bast_P_by_fk_PPI_couple(FK_ppi_couple):
        """
        remove a FK_score_bast_P given fk_protein
        :NOTE it verify for the phage and bacterium protein

        :param id_protein: id of the protein

        :type id_protein: int - required

        :return: COG_prot it removed
        :rtype: int
        """
        sqlObj = _F_score_blast_P_sql()
        id_couple = sqlObj.remove_F_score_blast_p_by_prot_id(FK_ppi_couple)
        return id_couple

    def __str__(self):
        """
        Overwrite of the str method
        """

        message_str = "ID Blast P: {0:d}, FK PPI couple: {1:d}, Score {4:.3f}, pident: {5:.3f}, length: {6:d}, mismatch: {7:d}, gapopen: {8:d}, pstart: {9:d}, pend: {10:d}, bstart: {11:d}, bend: {12:d}, bitscore: {13:.3f}, plen: {14:d}, blen: {15:d}".format(self.id_f_score_blast_P, self.FK_ppi_couple, self.evalue, self.pident, self.length, self.mismatch, self.gapopen, self.pstart, self.pend, self.bstart, self.bend, self.bitscore, self.plen, self.blen)
        return message_str




