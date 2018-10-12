"""
Created on Thu Mar 29 10:37:51 2018

@author: Diogo
"""

from SQL_obj_new.Score_domain_sql_new import _Score_domain_new

class Score_domain(object):
    """
    This class treat the Score domain has it exists in SCORE_DOMAIN table database

    By default, all FK are in the lasts positions in the parameters declaration
    """

    def __init__(self, id_score_dom = -1, score_ddi = -1.0,  fk_dom_bac = -1, fk_dom_phage = -1, fk_dom_couple = -1, fk_dom_bloc = -1):
        """
        Constructor of the Couple object. All the parameters have a default value

        :param id_score_dom: id of the score domain - -1 if unknown
        :param score_ddi: DDI score IT IS A FLOAT (FORMAT: 0.0) - -1.0 if unknown
        :param fk_dom_bac: Bacterium domain FK key - -1 if unknown
        :param fk_dom_phage: Phage domain FK key - -1 if unknown
        :param fk_dom_couple: Couple FK key - -1 if unknown
        :param fk_dom_bloc: domain_score bloc FK key - -1 if unknown


        :type id_score_dom: int - no required
        :type score_ddi: float - required 
        :type fk_dom_bac: int - required 
        :type fk_dom_phage: int - required 
        :type fk_dom_couple: int - required 
        :type fk_dom_bloc: int - required 
        """
        self.id_score_dom = id_score_dom
        self.score_ddi = score_ddi
        self.fk_dom_bac = fk_dom_bac
        self.fk_dom_phage = fk_dom_phage
        self.fk_dom_couple = fk_dom_couple
        self.fk_dom_bloc = fk_dom_bloc


    def create_score_domain(self):
        """
        Insert a Couple in the database if it not already exits and update its id
        The Couple contain a :
        - score ddi in float format 
        - FK of the Bacterium domain
        - FK of the Phage domain
        - FK of the domain score bloc
        - FK of the couple

        :return: id of the Score domain
        :rtype int
        """
        value_score_couple = None
        sqlObj = _Score_domain_new(db_name = 'INPH_proj_out')
        value_score_couple = sqlObj.insert_score_dom_if_not_exist_for_bloc(self.score_ddi, self.fk_dom_bloc, self.fk_dom_bac, self.fk_dom_phage, self.fk_dom_couple)
        self.id_score_dom = value_score_couple
        print(value_score_couple)
        return value_score_couple

    def get_all_score_domain():
        """
        return an array with all the couples in the database

        :return: array of couple
        :rtype: array(Couple)
        """
        listOfScoreDomain = []
        sqlObj = _Score_domain_new(db_name = 'INPH_proj_out')
        results = sqlObj.get_all_score_domain()
        for element in results:
            listOfScoreDomain.append(Score_domain(element[0], element[1], element[2], element[3], element[4], element[5]))
        return listOfScoreDomain

    def get_all_score_domain_by_bloc_id(bloc_id):
        """
        return an array with all the couples in the database given a score_bloc id

        :param bloc_id: id of the bloc

        :type bloc_id: int - required 

        :return: array of couple
        :rtype: array(Couple)
        """
        listOfScoreDomain = []
        sqlObj = _Score_domain_new(db_name = 'INPH_proj_out')
        results = sqlObj.get_all_score_domain_by_bloc_fk_id(bloc_id)
        for element in results:
            listOfScoreDomain.append(Score_domain(element[0], element[1], element[2], element[3], element[4], element[5]))
        return listOfScoreDomain

    def get_id_scor_domain_by_fk_dom_bac_phage_bloc(fk_dom_bact, fk_dom_phag, fk_bloc):
        """
        return the id of a score_domain give it fk dom bacterium, phage and the fk of the bloc

        :param fk_dom_bact: id of the bacterium domain
        :param fk_dom_phag: id of the phage domain
        :param fk_bloc: id of the bloc

        :type fk_dom_bact: int - required 
        :type fk_dom_phag: int - required 
        :type fk_bloc: int - required 

        :return: id of the score_domain or -1 if it don't exists
        :rtype: int
        """

        id_score_domain = None
        sqlObj = _Score_domain_new(db_name = 'INPH_proj_out')
        id_score_domain = sqlObj.get_id_score_dom_by_fk_bloc(fk_dom_bact, fk_dom_phag, fk_bloc)
        return id_score_domain


    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d}, Score value: {1}, FK bact domain: {2}, FK phage domain: {3}, FK couple: {4}, FK bloc {5}".format(self.id_score_dom, self.score_ddi, self.fk_dom_bac, self.fk_dom_phage, self.fk_dom_couple, self.fk_dom_bloc)
        return message_str