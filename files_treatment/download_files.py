# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:59:57 2017

@author: Stage
"""

import urllib
from xml.dom import minidom
from Bio import SeqIO
import io
import tempfile


class Download_file(object):
    
    def __init__(self, base_url, parameters_url):
        self.base_url = base_url
        self.parameters_url = parameters_url
       
    def request_url(self):
        url_params_encoded = urllib.parse.urlencode(self.parameters_url)
        url_complete = self.base_url + "?" + url_params_encoded
        print(url_complete)
        request_id = urllib.request.urlopen(url_complete)

        result_content = request_id.read()
        request_id.close()        
        return result_content
        
    def request_xml_file(self):
        xml_content = self.request_url()
        xmldoc = minidom.parseString(xml_content)
        return xmldoc
    
    def request_fasta_file(self):
        fasta_content = self.request_url()
        print(type(fasta_content))
        self.write_temp_file(fasta_content)
        #fasta_dict = SeqIO.index('/tmp/temp_fasta.fasta', "fasta")
        fasta_dict = SeqIO.to_dict(SeqIO.parse('/tmp/temp_fasta.fasta', "fasta"))
        print(len(fasta_dict))
        return fasta_dict
    
    def write_temp_file(self, content):
        path_file = '/tmp/temp_fasta.fasta'
        with open(path_file, "w") as out:
            out.write(content.decode('utf-8'))
        out.close()
        