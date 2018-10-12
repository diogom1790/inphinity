# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:38:22 2017

@author: Diogo Leite
"""

#https://github.com/chapmanb/bcbio-nextgen/blob/master/bcbio/hmmer/search.py

from DAL import *
from configuration.configuration_data import *

class _Domain_interaction_DB_SQL(object):
    """
    This class manipulate the DDI_INTERACTIONS table in the database. It used to know the sources which gives the information about the interaction

    Typically a domain is: PFXXXXX

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
        

    def select_all_ddi_interactions(self):
        """
        return all the DDI in the database

        :return: cursor with all DDI
        :rtype Cursor list
        """
        sql_string = "SELECT id_DDI_inter_DD, FK_domain_a_DD, FK_domain_b_DD FROM DDI_INTERACTIONS"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_ddi_interactions_by_db(self, Fk_id_DB):
        """
        return all the DDI in the database by an DB FK

        :return: cursor with all DDI
        :rtype Cursor list
        """
        sql_string = "select id_DDI_inter_DD, FK_domain_a_DD, FK_domain_b_DD from DDI_INTERACTIONS, DDI_INTERACTIONS_DB Where id_DDI_inter_DD = FK_id_interaction_DD_DDB and FK_id_db_interaction_DDB = " + str(Fk_id_DB)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def insert_DDI_interaction_return_id(self, FK_domain_A, FK_domain_B):
        """
        Insert a ddi_interaction WITHOUT ANY VERIFICATION

        :param FK_domain_A: designation of the domain A
        :param FK_domain_B: designation of the domain B

        :type FK_domain_A: string - required 
        :type FK_domain_B: string - required 

        :return: id of the domain inserted
        :rtype int
        """
        sqlObj = "INSERT INTO DDI_INTERACTIONS (FK_domain_a_DD, FK_domain_b_DD) VALUES (%s, %s)"
        params = [FK_domain_A, FK_domain_B]
        dalObj = DAL(self.db_name, sqlObj, params)
        results = dalObj.executeInsert()
        return results.lastrowid


    def insert_DDI_interaction_if_not_exists_return_id(self, FK_domain_A, FK_domain_B):
        """
        Insert a ddi_interaction. If the interaction already exist it return its ID

        :param FK_domain_A: designation of the domain A
        :param FK_domain_B: designation of the domain B

        :type FK_domain_A: string - required 
        :type FK_domain_B: string - required 

        :return: id of the interaction inserted
        :rtype int
        """

        id_interaction = self.get_id_interaction_by_domA_domB(FK_domain_A, FK_domain_B)

        if id_interaction == -1:
            sqlObj = "INSERT INTO DDI_INTERACTIONS (FK_domain_a_DD, FK_domain_b_DD) VALUES (%s, %s)"
            params = [FK_domain_A, FK_domain_B]
            dalObj = DAL(self.db_name, sqlObj, params)
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            return id_interaction

    def get_id_interaction_by_domA_domB(self, domain_A, domain_B):
        """
        :NOTE (domain_A - domain_B) is different of (domain_B - domain_A). Boths are verified
        
        Return the id o an interaction (Domain_A, domain_B)


        :param FK_domain_A: designation of the domain A
        :param FK_domain_B: designation of the domain B

        :type FK_domain_A: string - required 
        :type FK_domain_B: string - required 

        :return: id of the interaction or -1 i don't exists
        :rtype int
        """

        sql_string = "SELECT id_DDI_inter_DD FROM DDI_INTERACTIONS WHERE FK_domain_a_DD = '" + str(domain_A) + "' and FK_domain_b_DD = '" + str(domain_B) + "'"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        if len(results) is 0:
            sql_string = "SELECT id_DDI_inter_DD FROM DDI_INTERACTIONS WHERE FK_domain_a_DD = '" + str(domain_B) + "' and FK_domain_b_DD = '" + str(domain_A) + "'"
            dalObj = DAL(self.db_name, sql_string)
            results = dalObj.executeSelect()


        if len(results) is 0:
            return -1
        else:
            return results[0][0]

    def get_all_qty_of_scores_by_domains(self):
        """
        :NOTE (domain_A - domain_B) is different of (domain_B - domain_A)
        
        return the quantity of interaction by domain_A and domain_B


        :param FK_domain_A: designation of the domain A
        :param FK_domain_B: designation of the domain B

        :type FK_domain_A: string - required 
        :type FK_domain_B: string - required 

        :return: id of the interaction or -1 i don't exists
        :rtype int
        """
        sql_string = "select id_DDI_inter_DD, FK_domain_a_DD, FK_domain_b_DD, count(*) as 'qty' from DDI_INTERACTIONS, DDI_INTERACTIONS_DB WHERE id_DDI_inter_DD = FK_id_interaction_DD_DDB group by FK_id_interaction_DD_DDB"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results