# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:54:31 2017

@author: Stage
"""

from DAL import *

class Phage_sql_old(object):
    
    def __init__(self):
        self.db_name = "BMC"
    
    def select_all_phages_all_attributes(self):
        sql_string = "SELECT * FROM Phages"
        dalOBJ = DAL(self.db_name, sql_string)
        results = dalOBJ.executeSelect()
        return results
    
    
    
    def select_whole_genemo_by_ID(self, id_phage):
        sql_string = "SELECT whole_genome FROM Phages WHERE Phage_id = " + str(id_phage)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results[0]
    
    def get_proteins_sequences_by_ID(self, id_phage):
        sql_string = "SELECT prot_seq FROM Phages WHERE Phage_id = " + str(id_phage)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results[0]
        
    def get_proteins_dna_sequences_by_ID(self, id_phage):
        sql_string = "SELECT dna_cod_seq FROM Phages WHERE Phage_id = " + str(id_phage)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results[0]
    
    
    def get_proteins_qty_prot_by_ID(self, id_phage):
        sql_string = "SELECT Nb_proteins FROM Phages WHERE Phage_id = " + str(id_phage)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results[0]