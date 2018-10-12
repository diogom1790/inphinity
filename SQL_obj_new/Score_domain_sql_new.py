"""
Created on Thu Mar 29 10:37:13 2018

@author: Diogo
"""

from DAL import *
from configuration.configuration_data import *

class _Score_domain_new(object):
    """
    This class manipulate the SCORE_DOMAIN table in the database

    The FK are manipulated in the lasts positions of the parameters
    """
    def __init__(self):
        self.db_name = self.get_database_name()

    def get_database_name(self):
        """
        This method is used to get the database name used in factory

        :return: database name
        :rtype string
        """
        conf_data_obj = Configuration_data('INPHINITY')
        db_name = conf_data_obj.get_database_name()
        return db_name


    def get_all_score_domain(self):
        """
        return all the Score_domain in the database

        :return: cursor with all score_domain
        :rtype Cursor list
        """
        sql_string = "SELECT score_dom_id_SD, score_ddi_SD, FK_score_dom_bloc_FSD_SD, FK_prot_dom_bact_DP_SD, FK_prot_dom_phage_DP_SD, FK_couple_CP_SD FROM SCORE_DOMAIN"

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def get_all_score_domain_by_bloc_fk_id(self, fk_bloc_id):
        """
        return all the Score_domain in the database

        :return: cursor with all score_domain
        :rtype Cursor list
        """
        sql_string = "SELECT score_dom_id_SD, score_ddi_SD, FK_score_dom_bloc_FSD_SD, FK_prot_dom_bact_DP_SD, FK_prot_dom_phage_DP_SD, FK_couple_CP_SD FROM SCORE_DOMAIN WHERE FK_score_dom_bloc_FSD_SD = " + str(fk_bloc_id)

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def get_id_score_dom_by_fk_bloc(self, fk_dom_bact, fk_dom_phag, fk_bloc):
        """
        get the id of a score_domain based on the id of the bloc and these ids of phage bact domain

        :param fk_dom_bact: id of the bacterium 
        :param fk_dom_phag: id of the phage
        :param fk_bloc: id of the phage

        :type fk_dom_bact: int - required 
        :type fk_dom_phag: int - required 
        :type fk_bloc: int - required 

        :return: id of the score_dom or -1 if inexistant
        :rtype int
        """
        sql_string = "SELECT score_dom_id_SD FROM SCORE_DOMAIN WHERE FK_prot_dom_bact_DP_SD = " + str(fk_dom_bact) + " and FK_prot_dom_phage_DP_SD = " + str(fk_dom_phag) + " and FK_score_dom_bloc_FSD_SD = " + str(fk_bloc)
        print(sql_string)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]

    def insert_score_dom_if_not_exist_for_bloc(self, score_ddi, FK_score_dom_bloc, FK_prot_dom_bact, FK_prot_dom_phage, FK_couple):

        """
        Insert a Score_domain if it not yet exist (based on the kf_dom_phag, fk_dom_bact and fk_bloc).

        IT IS A FLOAT, ATTENTION WITH THE ROUNDS...

        :param score_ddi: value of the interaction (1 - positive; 0 - negative)
        :param FK_socre_dom_bloc: score value
        :param FK_prot_dom_bact: fk of the prot_dom of the bact
        :param FK_prot_dom_phage: fk of the prot_dom of the phage
        :param FK_couple: fk of the couple

        :type score_ddi: float - required 
        :type FK_socre_dom_bloc: int - required 
        :type FK_prot_dom_bact: int - required 
        :type FK_prot_dom_phage: int - required 
        :type FK_couple: int - required 

        :return: id of the couple inserted
        :rtype int
        """

        id_score_domain = self.get_id_score_dom_by_fk_bloc(FK_prot_dom_bact, FK_prot_dom_phage, FK_couple)
        if id_score_domain == -1:
            sql_string = "INSERT INTO SCORE_DOMAIN (score_ddi_SD, FK_score_dom_bloc_FSD_SD, FK_prot_dom_bact_DP_SD, FK_prot_dom_phage_DP_SD, FK_couple_CP_SD) VALUES (%s, %s, %s, %s, %s)"
            params = [score_ddi, FK_score_dom_bloc, FK_prot_dom_bact, FK_prot_dom_phage, FK_couple]

            dalObj = DAL(self.db_name, sql_string)
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params

            results = dalObj.executeInsert()
            return results.lastrowid

        else:
            print("The score domaine with the Bacterium domain id: {0:d} and phage domain id: {1:d} for the bloc id: {2:s} already exits in the database".format(FK_prot_dom_bact, FK_prot_dom_phage, FK_socre_dom_bloc))
            return id_score_domain