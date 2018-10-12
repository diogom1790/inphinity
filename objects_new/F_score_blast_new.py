# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 11:29:57 2018

@author: Diogo
"""

from SQL_obj_new.F_score_blast_sql_new import _F_score_blast_sql

class F_score_blast(object):
    """
    This class treat the Feature of score blast object has it exists in F_SCORE_BLAST table database
    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, id_f_score_blast = -1, pident = -1, length = -1, mismatch = -1, gapopen = -1, pstart = -1, pend = -1, bstart = -1, bend = -1, evalue = -1, bitscore = -1, plen = -1, blen = -1, FK_id_couple_CP_FSB = -1):
        """
        Constructor of the Score Blast object. All the parameters have a default value

        :param id_f_score_blast: id of the bast score - -1 if unknown
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
        :param FK_id_couple_CP_FSB: id of the couple which belong the score - -1 if unknown


        :type id_f_score_blast: int - required
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
        :type FK_id_couple_CP_FSB: int - required
        """

        self.id_f_score_blast = id_f_score_blast
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
        self.FK_id_couple_CP_FSB = FK_id_couple_CP_FSB

    def get_all_f_bast_scores(self):
        """
        return an array with all the baslt score in the database

        :return: array of score
        :rtype: array(F_score_blast)
        """
        listOfScoreBlast = []
        sqlObj = _F_score_blast_sql()
        results = sqlObj.select_all_score_blast_all_attributes()
        for element in results:
            listOfScoreBlast.append(F_score_blast(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9], element[10], element[11], element[12], element[13]))
        return listOfScoreBlast

    def create_f_score_blast_no_verification(self):
        """
        Insert a f_score_blast in the database WITHOUT ANY VERIFICATION
        
        The id of the f_score_blase is updated

        :return: id of the f_score_blast created
        :rtype: int
        """
        value_f_score_blast = None
        sqlObj = _F_score_blast_sql()
        value_f_score_blast = sqlObj.insert_f_score_blast(self.pident, self.length, self.mismatch, self.gapopen, self.pstart, self.pend, self.bstart, self.bend, self.evalue, self.bitscore, self.plen, self.blen, self.FK_id_couple_CP_FSB)
        self.id_f_score_blast = value_f_score_blast
        return value_f_score_blast

    def __str__(self):
        """
        Overwrite of the str method
        """
        #message_str = "ID: {0:d}, fk couple: {1:d}, Score: {2:.3f}".format(self.id_f_score_blast, self.FK_id_couple_CP_FSB, self.evalue)

        message_str = "ID: {0:d}, FK couple: {1:d}, Score {2:.3f}, pident: {3:.3f}, length: {4:d}, mismatch: {5:d}, gapopen: {6:d}, pstart: {7:d}, pend: {8:d}, bstart: {9:d}, bend: {10:d}, bitscore: {11:.3f}, plen: {12:d}, blen: {13:d}".format(self.id_f_score_blast, self.FK_id_couple_CP_FSB, self.evalue, self.pident, self.length, self.mismatch, self.gapopen, self.pstart, self.pend, self.bstart, self.bend, self.bitscore, self.plen, self.blen)
        return message_str




