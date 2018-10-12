# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:02:25 2017

@author: Stage
"""


from files_treatment.domain_json_file_hmm import *

class DomainJsonFile(object):
    def __init__(self, json_file):
        self.json_file = json_file
        self.list_domains = []
        
    def search_domains(self):
        for domains in self.json_file['results']['hits']:
            print(domains['acc'])
            domain = self.split_domain(domains['acc'])
            self.list_domains.append(domain)
            
    def split_domain(self, domain_version):
        domain = domain_version.split('.')[0]
        return domain