# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:10:46 2017

@author: Diogo Leite
"""


from SQL_obj_new.temp_prot_SQL_new import _temp_prot 

class id_prot_temp(object):

    def __init__(self, id_prot_temp = -1):
        self.id_prot_temp = id_prot_temp


    def get_all_ids_prot(self):
        list_ids_prots = []
        sqlObj = _temp_prot(db_name = 'INPH_proj')
        results = sqlObj.select_all_ids()
        for element in results:
            list_ids_prots.append(element[0])
        return list_ids_prots


    def create_id_prot(self):
        sqlObj = _temp_prot(db_name = 'INPH_proj')
        sqlObj.insert_id_prots(self.id_prot_temp)