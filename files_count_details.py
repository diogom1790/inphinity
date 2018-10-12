from files_treatment_new.xls_gen_bank_rast import Xls_gen_bank

import os
from os import listdir
from os.path import isfile, join
from shutil import copyfile
import pandas as pd


cwd = os.getcwd()



def get_list_ids_files_in_path(path):
    """
    This method list all files in a given path and return a list with these names

    :param path: path where it necessary to list the files

    :type path: string - required

    :return list with the files paths
    :rtype list(str)

    :note when the start point is smaller than end point (int the contig), it is because the "Strand field int excel file is negative
    """

    current_path = os.getcwd() + path
    list_files = os.listdir(current_path)

    return list_files


list_files = get_list_ids_files_in_path('/RAST/SPREADSHEET/')


print(list_files)

list_values = []




for file_name in list_files:
    path_file_xls = cwd + '/RAST/SPREADSHEET/' + file_name
    xls_obj = Xls_gen_bank(path_file_xls)
    qty_prots = xls_obj.get_number_of_proteins()
    qty_contig = xls_obj.get_number_different_contigs()
    list_values.append([file_name, qty_prots, qty_contig])


df = pd.DataFrame(list_values, columns=['file name', 'qty_prots', ' qty_contigs'])

df.to_csv('info_ds.csv', sep=',')

print(df)
