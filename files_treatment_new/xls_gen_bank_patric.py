# -*- coding: utf-8 -*-
"""
Created on Tur Jan 11 11:51:13 2018

@author: Diogo
"""
import pandas as pd
import numpy as np
from files_treatment_new.generic_xls_file import _generic_xls_file
from natsort import natsorted, ns
import numpy as np
from objects_new.Proteins_new import *

class XlsGenBankPatric(_generic_xls_file):
    """
    Class specified in the treatment of the gen_bank format file of xls. Remember that its a heritage of the class _generic_xls_file that its used to read the data from a file

    """

    def __init__(self, path_file, sheet_name = "Sheet1"):
        """
        Constructor of the class excel gen_bank class, this one contain all methods for the treatment of excel files gen mark of RAST platform. After the parameters initialisation, the file is loaded in the init method.

        :param path_file: Complete path with file name
        :param sheet_name: name of the sheet where is the information

        :type path_file: string - required
        :type sheet_name: string - required 
        """
        _generic_xls_file.__init__(self, path_file, sheet_name)
        self.read_xls_file()

    def get_contigs_id_sorted(self):
        """
        Get all the contigs id sorted naturally.

        :return: array of string of id_contigs
        :rtype: array(string)
        """
        ids_contigs = self.panda_data_file["contig_id"].unique()
        if isinstance(ids_contigs[0], str) == True:
            ids_contigs = np.asarray(natsorted(ids_contigs, key=lambda y: y.lower()))
        return ids_contigs


    def get_proteins_ids_by_contig_id(self, contig_id):
        """
        Given a contig id, its return all proteins associated. in the file, these one are called "feature_id"

        :param contig_id: contig id

        :type contig_id: string - required

        :return: array of string of id_proteins
        :rtype: array(string)
        """

        self.panda_data_file['contig_id'] = self.panda_data_file['contig_id'].astype(str)
        ids_proteins = self.panda_data_file.loc[(self.panda_data_file["contig_id"] == contig_id, ["feature_id"])]
        ids_proteins = ids_proteins["feature_id"].values
        return ids_proteins

    def get_information_line_by_protein_id(self, protein_id):
        """
        Given a protein id return a dictionary with all details of the protein, where:
        - Key: key value in the excel document
        - value: value of the detail in string format

        :param protein_id: contig id

        :type protein_id: string - required

        :return: dictionary with the details of the protein
        :rtype: dictionary
        """
        prot = self.panda_data_file["feature_id"] == protein_id
        protein_line = self.panda_data_file[self.panda_data_file["feature_id"] == protein_id].iloc[0].to_dict()
        if isinstance(protein_line['aa_sequence'], float) == True:
            protein_line['aa_sequence'] = ' '
        return protein_line

    def get_number_of_proteins(self):
        """
        Return the number of lines in the dataframe
        """
        qty_proteins = self.panda_data_file.shape[0]
        return qty_proteins

    def get_number_different_contigs(self):
        """
        Return the quantity of contigs in excel files
        """
        qty_contigs = np.size(pd.unique(self.panda_data_file['contig_id']))
        return qty_contigs

    def get_row_by_number(self, row_number):
        print(self.panda_data_file.iloc[row_number])


    def get_proteins_information_in_excel(self):
        """
        This method get the information of all the proteins in the xls file

        :param path: path where it necessary to list the files

        :type path: string - required

        :return list of dictionaries with all details
        :rtype list(dictionary{})
        """
        list_dict_proteins = []


        contigs_ids_listed = self.get_contigs_id_sorted()
        for contig_id in contigs_ids_listed:
            list_prot = self.get_proteins_ids_by_contig_id(contig_id)
            for protein in list_prot:
                list_dict_proteins.append(self.get_information_line_by_protein_id(protein))
        return list_dict_proteins


    def get_proteins_objects_by_contig_id(self, contig_id):
        """
        Gest a list of proteins based on the contig id

        :param contig_id: contig id

        :type contig_id: string - required

        :return list of Proteins Obj
        :rtype list(Protein)
        """
        list_proteins_ids = self.get_proteins_ids_by_contig_id(contig_id)
        proteins_obj_list = []
        for protein_id in list_proteins_ids:
            dict_prot = self.get_information_line_by_protein_id(protein_id)
            protein_pt = Protein(id_protein = 0, id_accession = dict_prot.get('feature_id'), designation = dict_prot.get('function'), sequence_prot = dict_prot.get('aa_sequence'), sequence_dna = dict_prot.get('nucleotide_sequence'), start_point_cnt = int(dict_prot.get('start')), end_point_cnt = int(dict_prot.get('stop')), fk_id_contig = dict_prot.get('contig_id') )
            proteins_obj_list.append(protein_pt)
        return proteins_obj_list



    def create_proteins_from_file(self):
        """
        This method creat a list of protein objects given the excel file name

        :param file_name: name of the excel file

        :type path: string - required

        :return list of Proteins Obj
        :rtype list(Protein)
        """
        proteins_obj_list = []
        list_proteins_ids = self.get_proteins_information_in_excel()

        print("qty of proteins: {0}".format(len(list_proteins_ids)))
        for protein_design in list_proteins_ids:
            protein_pt = Protein(id_protein = 0, id_accession = protein_design['feature_id'], designation = protein_design['function'], sequence_prot = protein_design['aa_sequence'], sequence_dna = protein_design['nucleotide_sequence'], start_point_cnt = protein_design['start'], end_point_cnt = protein_design['stop'], fk_id_contig = protein_design['contig_id'] )
            proteins_obj_list.append(protein_pt)

        return proteins_obj_list
