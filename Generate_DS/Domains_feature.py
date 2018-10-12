# -*- coding: utf-8 -*-
"""
Created on Wen Mar  14 16:29:58 2018

@author: Diogo Leite
"""

from Strategy_feat_interface import *
from objects_new.Couples_new import *

#matrix where are saved the results
matrix_bins_range = None
matrix_bins_range_zeros = None
matrix_results_ds = None
matrix_results_ds_zeros = None

# The various strategies:
class Domains_feature(Strategy_feat_interface):

    def feature_treatment(self, interactions_ids, vec_configuration):
        """
        method called to create the datasets based on the bins size

        :param interactions_ids: id of the couples used
        :param vec_configuration: vector of multiples

        :type feature_type: Features - required 
        :type list_configurations: list[[a,b,c]] - required 

        :return: list of three list with the configurations
        :rtype list(list(range values, range_by_interact, norm))
        """
        list_couples = Couple.get_couples_by_list_id(interactions_ids)
        print("--------")
        print(len(list_couples))
        azx_list = list(set(list_couples))
        print(len(azx_list))
        print("HEEEELL556565LLOOOO")
        return [ 1.1, 2.5 ] # Dummy