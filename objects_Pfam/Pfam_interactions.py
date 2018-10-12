# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:08:58 2018

@author: Diogo
"""

from SQL_obj_Pfam.Pfam_interactions_SQL import _pfamA_interactions
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import multiprocessing

class Pfam_interaction(object):
    """
    This class treat the ppfam_interaction object has it exists in pfamA_interactions table database Pfam

    By default, all FK are in the lasts positions in the parameters declaration
    """  

    def __init__(self, pfam_a = "", pfam_b = ""):
        """
        Constructor of the pfam_interaction object. All the parameters have a default value

        :param pfam_a: name of the domain (PFXXXXX)
        :param pfam_b: name of the domain (PFXXXXX)

        :type pfam_a: text - required
        :type pfam_b: text - required 
        """
        self.pfam_a = pfam_a
        self.pfam_b = pfam_b

    def get_all_pfam_interactions():
        """
        return an array with all the pfam_interactions score in the database Pfam

        :return: array of pfam interactions
        :rtype: array(Domain)
        """
        listOfPfamInteractions = []
        sqlObj = _pfamA_interactions()
        results = sqlObj.select_all_pfam_interactions()
        for element in results:
            listOfPfamInteractions.append(Pfam_interaction(element[0], element[1]))
        return listOfPfamInteractions

    def get_all_pfam_interactions_by_pfam(pfam):
        """
        return an array with all the pfam_interactions in the database Pfam given releated with a pfam

        :return: array of pfam interactions
        :rtype: array(Pfam_interaction)
        """
        listOfPfamInteractions = []
        sqlObj = _pfamA_interactions()
        results = sqlObj.select_all_pfam_interactions_by_pfam(pfam)
        for element in results:
            listOfPfamInteractions.append(Pfam_interaction(element[0], element[1]))
        return listOfPfamInteractions

    def search_inverted_values(list_pfInteract, domA, domB):
        print("treatment of PFAM {0} : {1}".format(str(domA), str(domB)))
        qty_values = 0
        for element in list_pfInteract:
            if element.pfam_a == domA and element.pfam_b == domB:
                qty_values += 1
            if element.pfam_b == domA and element.pfam_a == domB:
                qty_values += 1
        if qty_values > 1:
            return str(domA) + ':' + str(domB)
        else:
            return ''

    def search_duplicates_values():
        list_values = Pfam_interaction.get_all_pfam_interactions()
        list_domains = []

        max_proce = multiprocessing.cpu_count()
        max_proce = max_proce - 2

        with ThreadPoolExecutor(max_workers=max_proce) as executor:
            futures = [executor.submit(Pfam_interaction.search_inverted_values, list_values, pfam_interact.pfam_a, pfam_interact.pfam_b) for pfam_interact in list_values if pfam_interact.pfam_a != pfam_interact.pfam_b]
            for future in as_completed(futures):
                results_value = future.result()
                if len(results_value) > 1:
                    list_domains.append(results_value)
        print(list_domains)
        return list_domains

    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "Pfam interactions: {0} - {1}".format(self.pfam_a, self.pfam_b)
        return message_str