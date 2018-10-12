# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 14:49:43 2018

@author: Diogo
"""

from SQL_obj_DOMINE.PFAM_SQL import _PFAM_sql

class PFAM_ddi(object):
    """
    This class treat the PFAM object has it exists in PFAM table database DOMINE

    By default, all FK are in the lasts positions in the parameters declaration
    """ 

    def __init__(self, domain = "", database_name = "domine_db_out"):
        """

        Constructor of the Domain object. All the parameters have a default value

        :param domain: name of the domain (PFXXXXX)
        :param database_name: name of the database. See Factory_databases_access

        :type domain: text - required
        :type database_name: text - required
        """
        self.domain = domain
        self.database_name = database_name

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, dom):
        """
        Validation of domain format (remove the version if exists)
        """
        if len(dom.split(".")) == 2:
            self._domain = dom.split(".")[0]
        else:
            self._domain = dom

    def get_all_domains():
        """
        return an array with all the domain in the database 3DID

        :return: array of domains
        :rtype: array(Domain)
        """
        listOfPfamDomains = []
        sqlObj = _PFAM_sql(db_name = 'domine_db_out')
        results = sqlObj.get_all_domains()
        for element in results:
            listOfPfamDomains.append(PFAM_ddi(element[0]))
        return listOfPfamDomains

    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "Domain id: {0}".format(self.domain)
        return message_str