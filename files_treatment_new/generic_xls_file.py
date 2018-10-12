# -*- coding: utf-8 -*-
"""
Created on Tur Jan 11 10:35:05 2018

@author: Diogo
"""
import pandas as pd

class _generic_xls_file(object):
    """
    This class treat the exls files in general with PANDAS library to see specific files, see the heritage of the other excel classes

    """

    def __init__(self, path_file, sheet_name = "Sheet1"):
        """
        Constructor of the class excel top class, the data are loaded into panda_data_file variable. The classe only manipulate the data with the pandas library.

        :param path_file: Complete path with file name
        :param sheet_name: name of the sheet where is the information

        :type path_file: string - required
        :type sheet_name: string - required 
        """
        self.path_file = path_file
        self.sheet_name = sheet_name
        self.panda_data_file = None

    def read_xls_file(self):
        """
        method use to load the data into its panda_data_file
        """
        self.panda_data_file = pd.read_excel(self.path_file, sheet_name=self.sheet_name, header = [0])
        print("loaded, the file have {0:d} columns".format(len(self.panda_data_file.columns.values)))

    def __str__(self):
        """
        Overwrite of the str method
        """
        message = "File name: {0}, number of columns {1:d}".format(self.path_file, len(self.panda_data_file.columns.values))
        return message
