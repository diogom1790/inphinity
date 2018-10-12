# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 17:11:53 2017

@author: Stage
"""

from objects_old.Bacteria_old import *
from files_treatment.download_files import Download_file
from xml.dom import minidom

class BacteriaFile(object):
    def __init__(self, bacterium):
        self.bacterium = bacterium
        self.file_sequece_info = ""
        self.file_taxonomy = ""
        self.objectId = -1
        self.genus = ""
        self._specie = ""
        self.family = ""
        self.strain = ""
        self.accession_num = ""

    @property
    def specie(self):
        return self._specie

    @specie.setter
    def specie(self, value):
        if "sp." in value.lower():
            self._specie = "sp."
        else:
            self._specie = value
        
    def __str__(self):
        return 'from new __str__: ' + object.__str__(self)
    
    
    def get_obj_id(self):
        self.getXML_all_information_without_seq()
        vec_ids_obj = self.file_sequece_info.getElementsByTagName("Object-id_id")
        self.objectId = vec_ids_obj[0].firstChild.nodeValue
        vec_genus = self.file_sequece_info.getElementsByTagName("BinomialOrgName_genus")
        if len(vec_genus) != 0:
            self.genus = vec_genus[0].firstChild.nodeValue
        else:
            self.genus = "Unclassified Genus"
        vec_specie = self.file_sequece_info.getElementsByTagName("BinomialOrgName_species")
        if len(vec_specie) != 0:
            self.specie = vec_specie[0].firstChild.nodeValue
        else:
            self.specie = "Unclassified Specie"
        
        vec_acc_num = self.file_sequece_info.getElementsByTagName("Textseq-id_accession")
        self.accession_num = vec_acc_num[0].firstChild.nodeValue
        
        vec_strain_value = self.file_sequece_info.getElementsByTagName("OrgMod")
        for element in vec_strain_value:
            if element.getElementsByTagName("OrgMod_subtype")[0].getAttribute("value") == "strain":
                self.strain = element.getElementsByTagName("OrgMod_subname")[0].firstChild.nodeValue
        self.get_taxonomy_info()
        
    def get_taxonomy_info(self):
        self.getXML_taxonomyById()
        vec_taxonomy_nodes = self.file_taxonomy.getElementsByTagName("Taxon")
        for taxon in vec_taxonomy_nodes:
            if taxon.getElementsByTagName("Rank")[0].firstChild.nodeValue == "family":
                self.family = taxon.getElementsByTagName("ScientificName")[0].firstChild.nodeValue
            if taxon.getElementsByTagName("Rank")[0].firstChild.nodeValue == "genus":
                self.genus = taxon.getElementsByTagName("ScientificName")[0].firstChild.nodeValue
            if self.specie == "" and taxon.getElementsByTagName("Rank")[0].firstChild.nodeValue == "species":
                self.specie = taxon.getElementsByTagName("ScientificName")[0].firstChild.nodeValue
            
        
    
    def getXML_all_information_without_seq(self):  
        dict_url_values = {}
        dict_url_values["db"] = "sequences"
        dict_url_values["id"] = self.bacterium.GI
        dict_url_values["rettype"] = "native"
        dict_url_values["retmode"] = "xml"
        objFildD = Download_file("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi", dict_url_values)
        file_xml = objFildD.request_xml_file()
        self.file_sequece_info = file_xml
    
    def getXML_taxonomyById(self):
        dict_url_values = {}
        print(self.objectId)
        dict_url_values["db"] = "taxonomy"
        dict_url_values["id"] = self.objectId
        dict_url_values["rettype"] = "native"
        dict_url_values["retmode"] = "xml"
        objFildD = Download_file("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi", dict_url_values)
        file_xml = objFildD.request_xml_file()
        self.file_taxonomy = file_xml
        