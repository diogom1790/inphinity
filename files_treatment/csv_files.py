# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:29:40 2017

@author: Stage
"""

import csv

class CSV_file(object):
    def __init__(self, file_name, data, delimiter = ";"):
        self.file_name = file_name.replace(" ", "_")
        self.data = data
        self.delimiter = delimiter
        
    def create_CSV_form_list_obj_fields(self):
        print(self.file_name)
        with open(self.file_name, 'w', lineterminator ='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerow(self.data[0]._fields)
            writer.writerows(self.data)
        
        