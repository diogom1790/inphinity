import pandas as pd
import numpy as np
from objects_API.BacteriumJ import BacteriumJson
from objects_API.BacteriophageJ import BacteriophageJson

from objects_new.Couples_new import Couple
from objects_new.Organisms_new import Organism
from objects_new.Strains_new import Strain
from objects_new.Species_new import Specie

from configuration.configuration_api import ConfigurationAPI
from rest_client.AuthenticationRest import AuthenticationAPI


def readCSVToDataFrame(path_file):
    dataframe_interactions = pd.read_csv(filepath_or_buffer = path_file, sep=',')
    return dataframe_interactions

def getCoupleFromInteractionIdOldDB(interaction_id):
    couple_obj = Couple.get_couples_by_list_id([interaction_id])[0]
    return couple_obj

def getPhageDesignationById(id_phage):
    organism_obj = Organism.get_organism_by_id(id_phage)
    id_strain = organism_obj.fk_strain
    strain_obj = Strain.get_strain_by_id(id_strain)
    strain_designation = strain_obj.designation
    return strain_designation


def getBacteriumStrainSpecieDesignationById(id_bacterium):
    organism_obj = Organism.get_organism_by_id(id_bacterium)
    id_strain = organism_obj.fk_strain
    strain_obj = Strain.get_strain_by_id(id_strain)


    id_specie = strain_obj.fk_specie


    specie_obj = Specie.get_specie_by_id(id_specie)
    specie_designation = specie_obj.designation

    strain_designation = strain_obj.designation

    taxonomy_bacterium = 'Specie: ' + specie_designation + ' Strain: ' + strain_designation

    return taxonomy_bacterium


def getBacteriophageDesignationNewDBById(id_new_phage):
    bacteriophage_obj = BacteriophageJson.getByID(id_new_phage)
    phage_designation = bacteriophage_obj.designation

    return phage_designation

path_file_name = 'data_ids_interaction_new_old_db.csv'

dataframe_data = readCSVToDataFrame(path_file_name)


conf_obj = ConfigurationAPI()
conf_obj.load_data_from_ini()
AuthenticationAPI().createAutenthicationToken()

for index, row in dataframe_data.iterrows():
    #Old couple treatment
    interaction_id = row['interaction_id_old_db']
    couple_obj = getCoupleFromInteractionIdOldDB(interaction_id)
    id_phage = couple_obj.fk_phage
    id_bacterium = couple_obj.fk_bacteria

    phage_designation = getPhageDesignationById(id_phage)
    bacterium_designation = getBacteriumStrainSpecieDesignationById(id_bacterium)

    #New couple treatment
    id_new_phage = row['id_phage']
    id_new_bacterium = row['id_bact']

    phage_designation_new = getBacteriophageDesignationNewDBById(id_new_phage)
    print(couple_obj)
print(dataframe_data)