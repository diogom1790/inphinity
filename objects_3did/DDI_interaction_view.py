# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 13:17:10 2018

@author: Diogo
"""

from SQL_obj_3did.DDI_interaction_view_SQL import _DDI_interaction_view_sql
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import multiprocessing

class DDI_interaction_view(object):
    """
    This class treat the DDI interactions object has it exists in ddi_interactions_ID VIEW database 3DID

    By default, all FK are in the lasts positions in the parameters declaration
    """ 

    def __init__(self, domain_A = "", domain_B = ""):
        """

        NOTE: IT IS A VIEW

        Constructor of the ddi_interactions_v object. All the parameters have a default value

        :param domain_A: name of the domain (PFXXXXX)
        :param domain_B: name of the domain (PFXXXXX)

        :type domain_A: text - required
        :type domain_B: text - required
        """
        self.domain_A = domain_A
        self.domain_B = domain_B

    @property
    def domain_A(self):
        return self._domain_A

    @domain_A.setter
    def domain_A(self, dom):
        """
        Validation of domain format (remove the version if exists)
        """
        if len(dom.split(".")) == 2:
            self._domain_A = dom.split(".")[0]
        else:
            self._domain_A = dom

    @property
    def domain_B(self):
        return self._domain_B

    @domain_B.setter
    def domain_B(self, dom):
        """
        Validation of domain format (remove the version if exists)
        """
        if len(dom.split(".")) == 2:
            self._domain_B = dom.split(".")[0]
        else:
            self._domain_B = dom


    def get_all_pfam_interactions():
        """
        return an array with all the DDI_interaction in the database 3DID

        :return: array of DDI interactions
        :rtype: array(DDI_interaction_v)
        """
        listOfPfamInteractions = []
        sqlObj = _DDI_interaction_view_sql()
        results = sqlObj.get_all_pfam_interactions()
        for element in results:
            listOfPfamInteractions.append(DDI_interaction_view(element[0], element[1]))
        return listOfPfamInteractions


    def get_all_pfam_interactions_by_pfam(pfam):
        """
        return an array with all the pfam_interactions in the database 3DID given releated with a pfam

        :return: array of domain interactions
        :rtype: array(Pfam_interaction)
        """
        listOfPfamInteractions = []
        sqlObj = _DDI_interaction_view_sql()
        results = sqlObj.select_all_pfam_interactions_by_pfam(pfam)
        for element in results:
            listOfPfamInteractions.append(DDI_interaction_view(element[0], element[1]))
        return listOfPfamInteractions

    def search_inverted_values(list_pfInteract, domA, domB):
        print("treatment of PFAM {0} : {1}".format(str(domA), str(domB)))
        qty_values = 0
        for element in list_pfInteract:
            if element.domain_A == domA and element.domain_B == domB:
                qty_values += 1
            if element.domain_B == domA and element.domain_A == domB:
                qty_values += 1
        if qty_values > 1:
            return str(domA) + ':' + str(domB)
        else:
            return ''

    def search_duplicates_values():
        list_values = DDI_interaction_view.get_all_pfam_interactions()
        list_domains = []

        max_proce = multiprocessing.cpu_count()
        max_proce = max_proce - 2

        with ThreadPoolExecutor(max_workers=max_proce) as executor:
            futures = [executor.submit(DDI_interaction_view.search_inverted_values, list_values, pfam_interact.domain_A, pfam_interact.domain_B) for pfam_interact in list_values if pfam_interact.domain_A != pfam_interact.domain_B]
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
        message_str = "Interaction Domain: {0} - {1}".format(self.domain_A, self.domain_B)
        return message_str