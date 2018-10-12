# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:12:58 2018

@author: Diogo
"""

from SQL_obj_new.Ddi_interactions_sql_new import _Domain_interaction_DB_SQL
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import multiprocessing
from collections import defaultdict

class DDI_interaction(object):
    """
    This class treat the DDI_interaction object has it exists in DDI_INTERACTIONS table database
    By default, all FK are in the lasts positions in the parameters declaration
    """  
    
    def __init__(self, id_ddi_interaction = -1, FK_id_domain_A = -1, FK_id_domain_B = -1):
        """
        Constructor of the Domain object. All the parameters have a default value

        :param id_ddi_interaction: id of DDI interaction - -1 if unknown
        :param FK_id_domain_A: id of the domain A
        :param FK_id_domain_B: id of the domain B

        :type id_ddi_interaction: int - not required
        :type FK_id_domain_A: int - required 
        :type FK_id_domain_B: int - required 
        """
        self.id_ddi_interaction = id_ddi_interaction
        self.FK_id_domain_A = FK_id_domain_A
        self.FK_id_domain_B = FK_id_domain_B

    def get_all_DDI_interaction():
        """
        return an array with all the DDI_interactions in the database

        :return: array of DDI interactions
        :rtype: array(DDI_interaction)
        """
        listOfDomainsInteraction = []
        sqlObj = _Domain_interaction_DB_SQL()
        results = sqlObj.select_all_ddi_interactions()
        for element in results:
            listOfDomainsInteraction.append(DDI_interaction(element[0], element[1], element[2]))
        return listOfDomainsInteraction

    def get_all_DDI_interaction_to_dictionary():
        """
        return an dictionary with all the DDI_interactions in the database

        :return: dicitonary of DDI interactions
        :rtype: dict[tuple(dom_A, domB)]:interaction_id
        """
        dictionaryOfDomainsInteraction = defaultdict(list)
        sqlObj = _Domain_interaction_DB_SQL()
        results = sqlObj.select_all_ddi_interactions()
        for element in results:
            tuple_domains = (element[1], element[2])
            dictionaryOfDomainsInteraction[tuple_domains] = element[0]
        return dictionaryOfDomainsInteraction


    def get_all_DDI_interaction_by_fk_db(FK_database):
        """
        return an array with all the DDI_interactions in the database by a FK_database

        :return: array of DDI interactions
        :rtype: array(DDI_interaction)
        """
        listOfDomainsInteraction = []
        sqlObj = _Domain_interaction_DB_SQL()
        results = sqlObj.select_all_ddi_interactions_by_db(FK_database)
        for element in results:
            listOfDomainsInteraction.append(DDI_interaction(element[0], element[1], element[2]))
        return listOfDomainsInteraction

    def create_DDI_interaction(self):
        """
        Insert a DDI_interaction in the database
        The ddi interaction have a:
        - domain A
        - domain B

        :return: id of the DDI interaction
        :rtype int
        """
        sqlObj = _Domain_interaction_DB_SQL()
        value_interaction = sqlObj.insert_DDI_interaction_return_id(self.FK_id_domain_A, self.FK_id_domain_B)
        self.id_ddi_interaction = value_interaction
        return value_interaction

    def create_DDI_interaction_if_not_exists(self):
        """
        Insert a DDI_interaction in the database
        The ddi interaction have a:
        - domain A
        - domain B

        :return: id of the DDI interaction, if exist return the if exist return the correspondent id
        :rtype int
        """
        sqlObj = _Domain_interaction_DB_SQL()
        value_interaction = sqlObj.insert_DDI_interaction_if_not_exists_return_id(self.FK_id_domain_A, self.FK_id_domain_B)
        self.id_ddi_interaction = value_interaction
        return value_interaction

    def get_dictionary_qty_interactions_by_dom():
        """
        get and dictionary with the quantity of interactions by domains pairs (domA- domB != domB - domA)

        :return: id of the DDI interaction, if exist return the if exist return the correspondent id
        :rtype int
        """
        dict_values = {}
        sqlObj = _Domain_interaction_DB_SQL()
        results = sqlObj.get_all_qty_of_scores_by_domains()
        for element in results:
            dict_values[(element[1], element[2])] = element[3]
        return dict_values


    def search_inverted_values(list_pfInteract, domA, domB):
        print("treatment of PFAM {0} : {1}".format(str(domA), str(domB)))
        qty_values = 0
        for element in list_pfInteract:
            if element.FK_id_domain_A == domA and element.FK_id_domain_B == domB:
                qty_values += 1
            if element.FK_id_domain_B == domA and element.FK_id_domain_A == domB:
                qty_values += 1
        if qty_values > 1:
            return str(domA) + ':' + str(domB)
        else:
            return ''

    def search_duplicates_values():
        list_values = DDI_interaction.get_all_DDI_interaction()
        list_domains = []

        max_proce = multiprocessing.cpu_count()
        max_proce = max_proce - 2

        with ThreadPoolExecutor(max_workers=max_proce) as executor:
            futures = [executor.submit(DDI_interaction.search_inverted_values, list_values, pfam_interact.FK_id_domain_A, pfam_interact.FK_id_domain_B) for pfam_interact in list_values if pfam_interact.FK_id_domain_A != pfam_interact.FK_id_domain_B]
            for future in as_completed(futures):
                results_value = future.result()
                if len(results_value) > 1:
                    list_domains.append(results_value)
        print(list_domains)
        return list_domains