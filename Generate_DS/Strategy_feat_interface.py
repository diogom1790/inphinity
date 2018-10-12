# -*- coding: utf-8 -*-
"""
Created on Wen Mar  14 16:27:13 2018

@author: Diogo Leite
"""


class Strategy_feat_interface:
    # Line is a sequence of points:
    def feature_treatment(self, interactions_ids, vec_configuration) : pass
