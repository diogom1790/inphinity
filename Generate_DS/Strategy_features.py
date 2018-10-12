# -*- coding: utf-8 -*-
"""
Created on Wen Mar  14 16:00:13 2018

@author: Diogo Leite
"""

from Blast_cog_feature import *
from Blast_n_feature import *
from Blast_p_feature import *
from Blast_x_feature import *
from Domains_feature import *


# The "Context" controls the strategy design pattern
class Features:

    def __init__(self, strategy):
        self.strategy = strategy

    def attribue_algo(self, interactions_ids, vec_configuration):
        return self.strategy.feature_treatment(interactions_ids, vec_configuration)

    def changeAlgorithm(self, newAlgorithm):
        self.strategy = newAlgorithm


