# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:05:16 2017

@author: Diogo
"""

from SQL_obj_new.Organism_sql_new import _Organisms_sql_new

class Organism(object):
    """
    This class treat the Organism object has it exists in Organism table database
    By default, all FK are in the lasts positions in the parameters declaration
    """
    def __init__(self, gi, acc_num, qty_proteins = None, assembled = None, qty_contig = None, id_organism = None, fk_source = None, fk_strain = None, fk_type = None, fk_whole_genome = None, fk_source_data = None):
        """
        Constructor of the Organism object. All the parameters have a default value

        :param id_organism: id of the organism - -1 if unknown
        :param gi: gi of the organism - -1 if unknown
        :param acc_num: accession number of the organism - -1 if unknown
        :param qty_proteins: Number of proteins in the organism - -1 if unknown
        :param assembled: if the organism genome was assembled - -1 if unknown
        :param qty_contig: Number of contigs of the organism - -1 if unknown
        :param fk_source: Who find the organism inserted - -1 if unknown
        :param fk_strain: Strain of the organism - -1 if unknown
        :param fk_type: Type of organism (typically phage or bacterium) - -1 if unknown
        :param fk_whole_genome: Whole genome of the organism - -1 if unknown
        :param fk_source_data: From where the organism data coms (typically NCBI, PhageDB, RAST,...) - -1 if unknown

        :type id_organism: int - not required
        :type gi: text - required 
        :type acc_num: text - required
        :type qty_proteins: text - required
        :type assembled: text - required
        :type qty_contig: text - required
        :type fk_source: text - required
        :type fk_strain: text - required
        :type fk_type: text - required
        :type fk_whole_genome: text - required
        :type fk_source_data: text - not required
        """
        self.id_organism = id_organism
        self.gi = gi
        self.acc_num = acc_num
        self.qty_proteins = qty_proteins
        self.assembled = assembled
        self.qty_contig = qty_contig
        self.fk_source = fk_source
        self.fk_strain = fk_strain
        self.fk_type = fk_type
        self.fk_whole_genome = fk_whole_genome
        self.fk_source_data = fk_source_data
        
    def get_all_Organisms():
        """
        Return all organisms in the database

        :return: array of Organism
        :rtype: array(Organism)
        """
        listOfOrganisms = []
        sqlObj = _Organisms_sql_new()
        results = sqlObj.select_all_organisms_all_attributes()
        for element in results:
            listOfOrganisms.append(Organism(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9]))
        return listOfOrganisms

    def create_organism(self):
        """
        Insert an organism in the database. If its a:
        - Phage, insert without verify if it exists in the database
        - Bacterium, insert after verifying if any other bacterium with the same GI OR accession number exists in the database
        
        The id of the organis is updated

        :return: id of the organism
        :rtype: int
        """
        value_organisme = None
        sqlObj = _Organisms_sql_new()
        if self.fk_type == 2:
            value_organisme = sqlObj.insert_organisme_phage(self.gi, self.acc_num, self.qty_proteins, self.assembled, self.qty_contig, self.fk_source, self.fk_strain, self.fk_type, self.fk_whole_genome, self.fk_source_data)
        else:
            value_organisme = sqlObj.insert_organism_if_not_exist(self.gi, self.acc_num, self.qty_proteins, self.assembled, self.qty_contig, self.fk_source, self.fk_strain, self.fk_type, self.fk_whole_genome, self.fk_source_data)
        self.id_organism = value_organisme
        return value_organisme

    def create_phage_with_verification(self, strain_name):
        """
        Insert a Phage (organism) in the database only if any other phage exists with the same designation
        
        The id of the organis is updated

        :return: id of the organism
        :rtype: int
        """
        id_phage = -1
        if (self.fk_type == 2):
            id_phage = get_id_organism_by_designation(strain_name)
            if (id_phage == -1):
                id_phage = create_organism()
        return id_phage

    def create_bacterium_with_verification(self):
        """
        Insert a Bacterium (organism) in the database only if any other phage exists with the same designation
        
        The id of the organis is updated

        :return: id of the organism
        :rtype: int
        """
        sqlObj = _Organisms_sql_new()
        id_organism = sqlObj.insert_organism_no_validation(self.gi, self.acc_num, self.qty_proteins, self.assembled, self.qty_contig, self.fk_source, self.fk_strain, self.fk_type, self.fk_whole_genome, self.fk_source_data)
        self.id_organism = id_organism
        return id_organism

    
    def get_id_organism_by_taxonomy(self, genus, specie, strain):
        """
        get the organism id based on the taxonomy designations.
        
        :param genus: designation of the genus
        :param specie: designation of the specie
        :param strain: designation of the strain

        :type genus: string - required
        :type specie: string - required
        :type strain: string - required

        :return: id of the organism
        :rtype: int
        """
        sqlObj = _Organisms_sql_new()
        id_organism = sqlObj.get_organism_list_id_by_taxonomy_sql(genus, specie, strain)
        return id_organism

    def get_id_fk_whole_dna_by_id(self, id_organism):
        """
        get the organism ID given the whole genome ID
        
        :param id_organism: Whole genome id
        
        :type id_organism: id_organism - required

        :return: id of the organism
        :rtype: int
        """
        sqlObj = _Organisms_sql_new()
        fk_whole_dna = sqlObj.get_fk_whoe_dna_from_id(id_organism)
        return fk_whole_dna   
    

    def get_organism_id_by_acc_or_designation(acc, designation):
        """
        get the organism ID given the acc and the designation. First the acc is checked and if it is 'NA' it check the designation in strain table. It check that the organisme need to be a phage. The organism need to be a phage. If there is any one it is return -1
        
        :param designation: designation of the Phage
        
        :type designation: id_organism - required

        :return: id of the organism
        :rtype: int
        """
        id_organism = -1
        sqlObj = _Organisms_sql_new()
        if (acc.lower() != 'na'):
            id_organism = sqlObj.get_id_organism_by_acc(acc)
        elif(id_organism == -1):
            id_organism = sqlObj.get_id_organism_by_strain_designation(designation)
        return id_organism


    def get_id_organism_by_acc(acc):
        """
        get id organism based on its acc. it is work only if the acc is different that NA
  
        :return: id of the organism
        :rtype: int
        """
        id_organism = -1
        sqlObj = _Organisms_sql_new()
        if (acc.lower() != 'na'):
            id_organism = sqlObj.get_id_organism_by_acc(acc)
        return id_organism


    def get_id_organism_by_designation(designation):
        """
        get id organism based on its designation

        :param designation: designation of the organism
        
        :type designation: designation - required
  
        :return: id of the organism
        :rtype: int
        """
        sqlObj = _Organisms_sql_new()
        id_organism = -1
        id_organism = sqlObj.get_id_organism_by_strain_designation(designation)
        return id_organism

    def get_ids_all_organisms():
        """
        get a list of all organisms ids in the database
  
        :return: list of ids
        :rtype: list(int)
        """
        list_ids = []
        sqlObj = _Organisms_sql_new()
        results = sqlObj.get_ids_all_organisms()
        if len(results) > 0:
            for element in results:
                list_ids.append(element[0])
        return list_ids

    def get_ids_all_organisms_by_params(type_organism = 1, source_data = 1):
        """
        get a list of all organisms by type and source of data

        :param type_organism: type of organism (Bacterium, Phage,...)
        :param source_data: source of data (NCBI, PhageDB, RAST,...)
        
        :type type_organism: designation - required
        :type source_data: designation - required
  
        :return: list of ids
        :rtype: list(int)
        """
        list_ids = []
        sqlObj = _Organisms_sql_new()
        results = sqlObj.get_ids_all_organisms_by_type_and_source_data(type_organism, source_data)
        if len(results) > 0:
            for element in results:
                list_ids.append(element[0])
        return list_ids



    def get_organism_by_id(id_organism):
        """
        Get an organism by its id
  
        :return: Organism object
        :rtype: Organism
        """
        sqlObj = _Organisms_sql_new()
        orga_result = sqlObj.get_organism_by_id(id_organism)
        if orga_result != -1:
            orga_obj = Organism(orga_result[0], orga_result[1], orga_result[2], orga_result[3], orga_result[4], orga_result[5], orga_result[6], orga_result[7], orga_result[8], orga_result[9], orga_result[10])
            return orga_obj
        else:
            print('No organism with this id')
            return -1


    def get_organism_id_by_strain_like(strain_design_end):
        dict_orga = {}
        sqlObj = _Organisms_sql_new()
        orga_result = sqlObj.get_organism_id_design_By_end_strain(strain_design_end)
        for elements in orga_result:
            dict_orga[elements[0]] = [elements[1], elements[2]]
        return dict_orga

    def get_all_organisms_by_type(fk_type):
        """
        get all organisms by type.
        NOTE: 1 - Bacteirum
              2- Phage
  
        :param fk_type: id of the type
        
        :type fk_type: int - required
  
        :return: list of organisms
        :rtype: int
        """

        listOfOrganisms = []
        sqlObj = _Organisms_sql_new()
        results = sqlObj.select_all_organisms_all_attributes_by_type(fk_type)
        for element in results:
            listOfOrganisms.append(Organism(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9]))
        return listOfOrganisms

    def get_all_bacteria_by_id_specie(fk_id_specie):
        """
        get all bacterium with a strain.
        NOTE: 1 - Bacteirum
              2 - Phage
  
        :param fk_id_specie: id of the specie
        
        :type fk_id_specie: int - required
  
        :return: list of organisms
        :rtype: int
        """

        listOfOrganisms = []
        sqlObj = _Organisms_sql_new()
        results = sqlObj.select_all_organisms_all_attributes_by_specie(fk_id_specie)
        for element in results:
            listOfOrganisms.append(Organism(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9]))
        return listOfOrganisms

    def get_organism_by_fk_strain(fk_id_strain):
        """
        get all organism give the fk of the strain
  
        :param fk_id_strain: id of the specie
        
        :type fk_id_strain: int - required
  
        :return: list of organisms
        :rtype: int
        """

        listOfOrganisms = []
        sqlObj = _Organisms_sql_new()
        results = sqlObj.select_all_organisms_all_attributes_by_specie(fk_id_specie)
        for element in results:
            listOfOrganisms.append(Organism(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9]))
        return listOfOrganisms

    def remove_organism_by_id(id_organism):
        """
        remove an organism given its id

        :param id_organism: id of the organism

        :type id_organism: int - required

        :return: whole dna id removed
        :rtype: int
        """
        sqlObj = _Organisms_sql_new()
        id_couple = sqlObj.remove_organism_by_id(id_organism)
        return id_couple


    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d} Acc: {1} GI: {2}, qty of proteins: {3}, assembled: {4}, Qty of contigs: {5}, FK source: {6:d}, FK Strain {7:d}, FK Whole Genome {8:d}, FK source data {9:d}, FK Source data {10:d}".format(self.id_organism, self.acc_num, self.gi, self.qty_proteins, self.assembled, self.qty_contig, self.fk_source, self.fk_strain, self.fk_whole_genome, self.fk_source_data, self.fk_source_data)
        return message_str
