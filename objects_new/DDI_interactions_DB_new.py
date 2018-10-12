# -*- coding: utf-8 -*-
"""
Created on Wen Apr 11 13:20:22 2018

@author: Diogo Leite
"""

from time import gmtime, strftime
from SQL_obj_new.DDI_interactions_DB_sql_new import _DDI_interaction_DB_SQL
from collections import defaultdict

class DDI_interaction_DB(object):
    """
    NOTE: Here the date is only the date and it create automatically when an DDI_interaction_DB is inserted (only the day of the insertion is considered)

    This class treat the DDI interaction DB object has it exists in DDI_INTERACTIONS_DB table database


    It consistes on a conection class (N to N) to know for each DDI which source give the information

    By default, all FK are in the lasts positions in the parameters declaration
    """ 

    def __init__(self, id_ddi_interact_DB = -1, date_creation = "", FK_DDI_interaction = -1, FK_DB_source = -1, database_name = "INPH_proj_out"):
        """
        Constructor of the DDI_interactionDB object. All the parameters have a default value

        :param id_ddi_interact_DB: id of DDI interaction DB - -1 if unknown
        :param date_creation: Date of the creation - -1 if unknown
        :param FK_DDI_interaction: id of the DDI
        :param FK_DB_source: id of the Source
        :param database_name: name of the database. See Factory_databases_access

        :type id_ddi_interact_DB: int - not required
        :type date_creation: text (date format) - required 
        :type FK_DDI_interaction: int - required 
        :type FK_DB_source: int - required 
        :type database_name: text - required
        """

        self.id_ddi_interact_DB = id_ddi_interact_DB
        self.date_creation = date_creation
        self.FK_DDI_interaction = FK_DDI_interaction
        self.FK_DB_source = FK_DB_source
        self.database_name = database_name

    def get_all_DDI_interactionDB():
        """
        return an array with all the DDI interactions db in the database

        :return: array of DDI interactions DB
        :rtype: array(DDI_interaction_DB)
        """
        listOfDDIIntDB = []
        sqlObj = _DDI_interaction_DB_SQL()
        results = sqlObj.select_all_DDI_DB()
        for element in results:
            listOfDDIIntDB.append(DDI_interaction_DB(element[0], element[1], element[2], element[3]))
        return listOfDDIIntDB

    def get_all_DDI_interactionDB_to_dictionary():
        """
        return an array with all the DDI interactions db in the database

        :return: dictionary of DDI interactions DB
        :rtype: dictionary[id_interaction]:[list_id_dbs]
        """
        dict_OfDDIIntDB = defaultdict(list)
        sqlObj = _DDI_interaction_DB_SQL()
        results = sqlObj.select_all_DDI_DB()
        for element in results:
            dict_OfDDIIntDB[element[2]].append(element[3])
        return dict_OfDDIIntDB

    def get_DDI_interact_db_id_by_id_domains(id_domain_a, id_domain_b):
        """
        :NOTE the pairs test normal and invertion (domA - domB and domB -domA)
        :NOTE 2 :The DB 16 it is not considered as a DB

        return an array with all the DDI interactions db in the database given a pair of Domains

        :return: array of DDI interactions DB
        :rtype: array(DDI_interaction_DB)
        """
        listOfDDIid = []
        sqlObj = _DDI_interaction_DB_SQL()
        results = sqlObj.select_all_DDI_DB_id_by_pair_domain(id_domain_a, id_domain_b)
        for element in results:
            if element[0] != 16:
                listOfDDIid.append(element[0])
        return listOfDDIid

    def create_DDI_interactions_DB(self):
        """
        Insert a DDI interaction DB in the database return it id
        The DDI int DB contain:
        - date_time creation
        - FK of the DDI
        - FK of the Source

        :return: id DDI_interaction_DB
        :rtype int
        """

        actual_date_time = strftime("%Y-%m-%d", gmtime())
        self.date_creation = actual_date_time

        sqlObj = _DDI_interaction_DB_SQL()
        value_dataset = sqlObj.insert_DDI_source_return_id_if_not_exists(self.date_creation, self.FK_DDI_interaction, self.FK_DB_source)
        return value_dataset