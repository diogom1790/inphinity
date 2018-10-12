# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:17:12 2018

@author: Diogo
"""

from time import gmtime, strftime
from SQL_obj_new.F_score_domains_bloc_sql_new import _F_score_domains_bloc_sql

class F_score_domains_bloc(object):
    """
    This class treat the bloc of the domain score object has it exists in F_SCORE_DOMAINS_BLOC table database

    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, score_dom_bloc_id = -1, designation = "", date_creation_FSD = ""):

        """
        Constructor of the F_score_domains_bloc object

        :param score_dom_bloc_id: blast score
        :param designation: designation of the bloc
        :param date_creation_FSD: date and time of the creation (actual)

        :type score_dom_bloc_id: string - required 
        :type designation: string - required
        :type date_creation_FSD: string (datetime sql format) - required

        """

        self.score_dom_bloc_id = score_dom_bloc_id
        self.designation = designation
        self.date_creation_FSD = date_creation_FSD


    def get_all_f_dom_scor_bloc_scores():
        """
        return an array with all the bloc of the domain score in the database

        :return: array of bloc of the domain score
        :rtype: array(F_score_domains_bloc)
        """
        listOfScoreDomainBloc = []
        sqlObj = _F_score_domains_bloc_sql(db_name = 'INPH_proj_out')
        results = sqlObj.select_all_bloc_score_domain()
        for element in results:
            listOfScoreDomainBloc.append(F_score_domains_bloc(element[0], element[1], element[2]))
        return listOfScoreDomainBloc


    def create_f_score_domains_bloc_no_verification(self):
        """
        Insert a f_score_blast in the database WITHOUT ANY VERIFICATION
        
        The id of the f_score_blase is updated

        :return: id of the f_score_blast created
        :rtype: int
        """

        actual_date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        self.date_creation_FSD = actual_date_time


        value_f_score_domains_bloc = None
        sqlObj = _F_score_domains_bloc_sql(db_name = 'INPH_proj_out')
        value_f_score_domains_bloc = sqlObj.insert_bloc_score_domain(self.designation, self.date_creation_FSD)
        self.score_dom_bloc_id = value_f_score_domains_bloc
        return value_f_score_domains_bloc


    def __str__(self):
        """
        Overwrite of the str method
        """

        message_str = "ID Bloc domain: {0:d}, designation: {1}, Date of creation: {2}".format(self.score_dom_bloc_id, self.designation, self.date_creation_FSD)
        return message_str