# -*- coding: utf-8 -*-
"""
Created on Wen Mar  14 16:32:26 2018

@author: Diogo Leite
"""

from Strategy_feat_interface import *

# The various strategies:
class Blast_cog_feature(Strategy_feat_interface):
    def feature_treatment(self, interactions_ids, vec_configuration):
        return [ 1.1, 2.2 ] # Dummy