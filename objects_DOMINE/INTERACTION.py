# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 14:59:10 2018

@author: Diogo
"""

from SQL_obj_DOMINE.INTERACTION_SQL import _Interactions_sql
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import multiprocessing

class interaction_ddi(object):
    """

    This class treat the interaction DDI object has it exists in INTERACTION table database DOMINE

    Typically a domain is: PFXXXXX

    The FK are manipulated in the lasts positions of the parameters
    """

    def __init__(self, domain_A = "", domain_B = "", iPfam = -1, did3 = -1, ME = -1, RCDP = -1, Pvalue = -1, Fusion = -1, DPEA = -1, PE = -1, GPE = -1, DIPD = -1, RDFF = -1, KGIDDI = -1, INSITE = -1, DomainGA = -1, PP = -1, PredictionConfidence = "", SameGO = -1):
        """

        NOTE: IT IS A VIEW

        Constructor of the ddi_interactions_v object. All the parameters have a default value

        :param Domain1: name of the domain (PFXXXXX)
        :param Domain2: name of the domain (PFXXXXX)
        :param iPfam: Interaction view in Pfam database
        :param did3: Interaction view in 3did database
        :param ME: Interaction predicted with this method
        :param RCDP: Interaction predicted with this method
        :param Pvalue: Interaction predicted with this method
        :param Fusion: Interaction predicted with this method
        :param DPEA: Interaction predicted with this method
        :param PE: Interaction predicted with this method
        :param GPE: Interaction predicted with this method
        :param DIPD: Interaction predicted with this method
        :param RDFF: Interaction predicted with this method
        :param KGIDDI: Interaction predicted with this method
        :param INSITE: Interaction predicted with this method
        :param DomainGA: Interaction predicted with this method
        :param PP: Interaction predicted with this method
        :param PredictionConfidence: Confidence of the prediction [HC, LC, NA, MC]
        :param SameGO: Interaction predicted with this method

        :type Domain1: text - required
        :type Domain2: text - required
        :type iPfam: text - required
        :type did3: text - required
        :type ME: text - required
        :type RCDP: text - required
        :type Pvalue: text - required
        :type Fusion: text - required
        :type DPEA: text - required
        :type PE: text - required
        :type GPE: text - required
        :type DIPD: text - required
        :type RDFF: text - required
        :type KGIDDI: text - required
        :type INSITE: text - required
        :type DomainGA: text - required
        :type PP: text - required
        :type PredictionConfidence: text - required
        :type SameGO: text - required
        """
        self.domain_A = domain_A
        self.domain_B = domain_B
        self.iPfam = iPfam
        self.did3 = did3
        self.ME = ME
        self.RCDP = RCDP
        self.Pvalue = Pvalue
        self.Fusion = Fusion
        self.DPEA = DPEA
        self.PE = PE
        self.GPE = GPE
        self.DIPD = DIPD
        self.RDFF = RDFF
        self.KGIDDI = KGIDDI
        self.INSITE = INSITE
        self.DomainGA = DomainGA
        self.PP = PP
        self.PredictionConfidence = PredictionConfidence
        self.SameGO = SameGO


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
        return an array with all the Interaction in the database DOMINE

        :return: array of Interaction
        :rtype: array(Interaction)
        """
        listOfPfamInteractions = []
        sqlObj = _Interactions_sql()
        results = sqlObj.get_all_interactions()
        for element in results:
            listOfPfamInteractions.append(interaction_ddi(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9], element[10], element[11], element[12], element[13], element[14], element[15], element[16], element[17], element[18]))
        return listOfPfamInteractions

    def get_all_pfam_all_info_by_pfam(pfam):
        """
        return an array with all the Interaction in the database DOMINE

        :return: array of Interaction
        :rtype: array(Interaction)
        """
        listOfPfamInteractions = []
        sqlObj = _Interactions_sql()
        results = sqlObj.select_all_domain_interaction_by_pfam(pfam)
        for element in results:
            listOfPfamInteractions.append(interaction_ddi(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9], element[10], element[11], element[12], element[13], element[14], element[15], element[16], element[17], element[18]))
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
        list_values = interaction_ddi.get_all_pfam_interactions()
        list_domains = []

        max_proce = multiprocessing.cpu_count()
        max_proce = max_proce - 2

        with ThreadPoolExecutor(max_workers=max_proce) as executor:
            futures = [executor.submit(interaction_ddi.search_inverted_values, list_values, pfam_interact.domain_A, pfam_interact.domain_B) for pfam_interact in list_values if pfam_interact.domain_A != pfam_interact.domain_B]
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
        message_str = "Interaction Domain: {0} - {1} \n".format(self.domain_A, self.domain_B)
        message_str += "Databases where it appear: "
        message_str += "iPfam: {0} 3did: {1} ME: {2} RCDP: {3} Pvalue: {4} Fusion: {5} DPEA: {6} PE: {7} GPE: {8} DIPD: {9} RDFF: {10} KGIDDI: {11} INSITE: {12} DomainGA: {13} PP: {14}\n".format(self.iPfam, self.did3, self.ME, self.RCDP, self.Pvalue, self.Fusion, self.DPEA, self.PE, self.GPE, self.DIPD, self.RDFF, self.KGIDDI, self.INSITE, self.DomainGA, self.PP)
        message_str += "Confidence: {0} - SameGO: {1}".format(self.PredictionConfidence, self.SameGO)
        return message_str