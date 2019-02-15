import pandas as pd
from objects_API.BacteriumJ import BacteriumJson
from objects_API.BacteriophageJ import BacteriophageJson

from configuration.configuration_api import ConfigurationAPI
from rest_client.AuthenticationRest import AuthenticationAPI

def get_data_interactions_by_csv(path_file):
    dataframe_interaction = pd.read_csv(filepath_or_buffer = path_file)
    return dataframe_interaction


def get_id_bacterium_by_acc(bacterium_acc):
    bacterium_obj = BacteriumJson.getByAccnumber(bacterium_acc)
    bacterium_id = bacterium_obj.id
    return bacterium_id

def get_id_bacteriophage_by_designation(phage_designation:str):
    bacteriophage_obj = BacteriophageJson.getBydesignation(phage_designation)
    bacteriophage_id = bacteriophage_obj.id
    return bacteriophage_id


def get_dictionary_index_bacterium(dataframe_interactions):
    dataframe_data = dataframe_data.sort_values(by=['acc_bacterium'], ascending=[1])
    old_acc = ''
    dict_ids_bact = {}
    for index, row in dataframe_data.iterrows():
        bacterium_acc = row["acc_bacterium"]
        if bacterium_acc != old_acc:
            try:
                bacterium_id = get_id_bacterium_by_acc(bacterium_acc)
                old_acc = bacterium_acc
                dict_ids_bact[bacterium_acc] = bacterium_id
            except:
                dict_ids_bact[bacterium_acc] = -1

    return dict_ids_bact

def getIdsBacteriophagesByDataframe(dataframe_interactions):
    dataframe_data = dataframe_data.sort_values(by=['phage_name'], ascending=[1])
    old_design = ''
    dict_designation_id = {}
    for index, row in dataframe_data.iterrows():
        bacteriophage_design = row["phage_name"]
        if bacteriophage_design != old_design:
            try:
                bacteriophage_id = get_id_bacteriophage_by_designation(bacteriophage_design)
                old_design = bacteriophage_design
                dict_designation_id[bacteriophage_design] = bacteriophage_id
            except:
                dict_designation_id[bacteriophage_design] = -1
    return dict_designation_id

conf_obj = ConfigurationAPI()
conf_obj.load_data_from_ini()
AuthenticationAPI().createAutenthicationToken()

path_csv_file = 'data_interactions.csv'

dataframe_data = get_data_interactions_by_csv(path_csv_file)
dataframe_data = dataframe_data.sort_values(by=['acc_bacterium'], ascending=[1])





print(dict_designation_id)