# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 13:52:10 2018

@author: Diogo Leite
"""


import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)


import configparser
import os
from os import listdir

import numpy as np

from Strategy_features import *

from objects_new.Couples_new import *

#global variables:
list_ids = []

#Method to developpe
# - Something that recive the ids of the couples and get them
#    - Based on these ids, it is necessary to take each one and generate the features according to the configuration file
# - Something that takes the couples and generate the diferents features
# Use strategy design pattern to do this https://www.tutorialspoint.com/design_pattern/strategy_pattern.htm

# - Don't forget to save all the information in the database


def get_ids(config_obj):
    """
    get a list of ids available in the ini file

    :param config_obj: configuration object which contains all the details

    :type config_obj: configparser - required 

    :return: list of interactions id
    :rtype numpy array (int)
    """
    list_ids = Config.get('id_interaction', 'id_all_interaction')
    list_ids = list_ids.replace('\'', '')
    list_ids = list_ids.split(',')
    list_ids = np.asarray(list_ids)
    list_ids = list_ids.astype(np.int)
    return list_ids


def convert_string_to_bool(string_value):
    """
    simple method used to convert a tring to a bool

    :param string_value: True or False string value

    :type string_value: string - required 

    :return: bool True or False
    :rtype bool
    """
    if string_value == 'True':
        return True
    else:
        return False

def get_configs_by_tag(config_obj, tag_search):
    """
    return a list with the configuration for a given feature

    :param config_obj: configuration object which contains all the details
    :param tag_search: feature name in the init file

    :type config_obj: configparser - required 
    :type tag_search: string - required 

    :return: list of three list with the configurations
    :rtype list(list(range values, range_by_interact, norm))
    """
    list_values_configuration = []
    array_config = []

    list_config_domine = Config[tag_search]
    for configuration in list_config_domine:
        params = config_obj[tag_search][configuration]
        params = params.split(',')
        
        value = params[1].split(':')[1]
        range_value = int(params[0].split(':')[1])
        range_by_interact = convert_string_to_bool(params[1].split(':')[1])
        norm = convert_string_to_bool(params[2].split(':')[1])

        array_config = [range_value, range_by_interact, norm]
        list_values_configuration.append(array_config)

    return list_values_configuration

def dataset_creation(feature_type, list_configurations):
    """
    use to start the datasetcreations

    :param feature_type: type of feature used in dataset
    :param list_configurations: list of configurations

    :type feature_type: Features - required 
    :type list_configurations: list[[a,b,c]] - required 

    :return: list of three list with the configurations
    :rtype list(list(range values, range_by_interact, norm))
    """
    global list_ids

    for configuration in list_configurations:
        feature_extraction.attribue_algo(list_ids,configuration)
        print(configuration)

Config = configparser.ConfigParser()
Config


Config.read("config.ini")


#Get ids:
list_ids = get_ids(Config)
#get tags, the first element was removed, it contains the tag for the interactions ids

print(list_ids)
print(len(list_ids))

list_aux = list(set(list_ids))
print(len(list_aux))
print(list_ids[0])
list_tags = Config.sections()
del list_tags[0]


#get config by tag
feature_extraction = None
for section_element in list_tags:
    list_configurations = get_configs_by_tag(Config, section_element)
    if section_element == 'domine':
        feature_extraction = Features(Domains_feature())
    elif section_element == 'feature_blast_n':
        feature_extraction = Features(Blast_n_feature())
    elif section_element == 'feature_blast_x':
        feature_extraction = Features(Blast_x_feature())
    elif section_element == 'feature_blast_p':
        feature_extraction = Features(Blast_p_feature())
    elif section_element == 'feature_blast_cog':
        feature_extraction = Features(Blast_cog_feature())

    dataset_creation(feature_extraction, list_configurations)


list_configurations = get_configs_by_tag(Config, 'feature_blast_p')
print(list_configurations)


feature_extraction = Features(Domains_feature())
feature_extraction.attribue_algo([1,2,3,4],[1,2,3,4])

couple_obj = Couple.get_couple_by_id(937)
print(couple_obj)