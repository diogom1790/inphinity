# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:32:45 2017

@author: Stage
"""
from DAL import *



class Bacterium_sql_old(object):
    
    def __init__(self):
        self.db_name = "BMC"
        
    def select_all_bacteria_all_attributes(self):
        sql_string = "SELECT * FROM Bacteria ORDER BY GI"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_whole_genemo_by_GI(self, gi):
        sql_string = "SELECT whole_genome FROM Bacteria WHERE GI = " + str(gi)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results[0]
    
    def get_proteins_sequences_by_GI(self, gi):
        sql_string = "SELECT prot_seq FROM Bacteria WHERE GI = " + str(gi)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results[0]
    
    def get_proteins_dna_sequences_by_GI(self, gi):
        sql_string = "SELECT dna_cod_seq FROM Bacteria WHERE GI = " + str(gi)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results[0]
    
    def get_proteins_qty_prot_by_GI(self, gi):
        sql_string = "SELECT Nb_proteins FROM Bacteria WHERE GI = " + str(gi)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results[0]
    
    