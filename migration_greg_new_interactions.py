import pandas as pd

file_results_ids_error = 'error_ids_greg.csv'
file_results_ids = 'correct_ids.csv'


def getIdOrganismContainName(datafram_data, name_organism:str):
    value = datafram_data[datafram_data['designation'].str.contains(name_organism)]

    quantity_results = value.shape[0]
    if quantity_results == 1:
        str_write = name_organism + ',' + str(value['organism_id'].item()) + '\n'
        with open(file_results_ids,'a') as fd:
            fd.write(str_write)
    else:
        str_write = name_organism + '\n'
        with open(file_results_ids_error,'a') as fd:
            fd.write(str_write)


path_excel_file_interaction = 'greg_S_aureus.xlsx'
path_excel_file_bacterium_list = 'bacteria_greg.csv'

dataframe_file_interaction = pd.read_excel(path_excel_file_interaction)
dataframe_file_bacterium_list = pd.read_csv(path_excel_file_bacterium_list)
print('Hello?')

dict_phages_id = {}
dict_phages_id['P68'] = 4968
dict_phages_id['44AHJD'] = 4546
dict_phages_id['3A'] = 4911
dict_phages_id['71'] = 4200
dict_phages_id['77'] = 4942
dict_phages_id['K'] = 4381
dict_phages_id['Sb-1'] = 4457

for index, row in dataframe_file_interaction.iterrows():
    bacterium_name = row['bac/phage']
    print(bacterium_name)
    getIdOrganismContainName(dataframe_file_bacterium_list, bacterium_name)
