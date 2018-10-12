# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:14:40 2017

@author: Diogo Leite
"""

from SQL_obj_new.Protein_sql_new import _Protein_sql_new


class Protein(object):
    """
    This class treat the Protein object has it exists in PROTDOM table database
    By default, all FK are in the lasts positions in the parameters declaration
    """
    def __init__(self, id_protein = -1, id_accession = "", designation = "", sequence_prot = "", sequence_dna = "", start_point = -1, end_point = -1, start_point_cnt = -1, end_point_cnt = -1, fk_id_contig= -1):
        """
        Constructor of the Protein object. All the parameters have a default value

        :param id_protein: id of the protein - -1 si inconnu
        :param id_accession: accession number - -1 si inexistant
        :param designation: contains the text that follow ">" in the fasta file - string empty if nothing exists
        :param sequence_prot: proteic sequence - string empty if nothing
        :param sequence_dna: nucleic sequence - string empty if nothing
        :param start_point: start position of the protein in the gene - -1 if unknown
        :param end_point: end position of the protein in the gene - -1 if unknown
        :param start_point_cnt: start position of the protein in the contig - -1 if unknown
        :param end_point_cnt: end position of the protein in the contig - -1 if unknown
        :param fk_id_contig: FK key of the contig where appear the protein - -1 if unknown

        :type id_protein: int - required 
        :type id_accession: text - not required 
        :type designation: text - required 
        :type sequence_prot: text - required 
        :type sequence_dna: text - not required 
        :type start_point: int - not required 
        :type end_point: int - not required 
        :type start_point_cnt: int - not required 
        :type end_point_cnt: int - not required 
        :type fk_id_contig: int - not required 

        """
        self.id_protein = id_protein
        self.id_accession = id_accession
        self.designation = designation
        self.sequence_prot = sequence_prot
        self.sequence_dna = sequence_dna
        self.start_point = start_point
        self.end_point = end_point
        self.start_point_cnt = start_point_cnt
        self.end_point_cnt = end_point_cnt
        self.fk_id_contig = fk_id_contig


    #def __setattr__(self, name, value):
       
    #   """
    #    if name == 'start_point' and not isinstance(value, int):
    #        raise TypeError('Protein.start_point must be an int')
    #    if name == 'end_point' and not isinstance(value, int):
    #        raise TypeError('Protein.end_point must be an int')
    #    if name == 'start_point_cnt' and not isinstance(value, int):
    #        raise TypeError('Protein.start_point_cnt must be an int')
    #    if name == 'end_point_cnt' and not isinstance(value, int):
    #        raise TypeError('Protein.end_point_cnt must be an int')
    #    super().__setattr__(name, value)
    #    """    #def __setattr__(self, name, value):
       
    #   """
    #    if name == 'start_point' and not isinstance(value, int):
    #        raise TypeError('Protein.start_point must be an int')
    #    if name == 'end_point' and not isinstance(value, int):
    #        raise TypeError('Protein.end_point must be an int')
    #    if name == 'start_point_cnt' and not isinstance(value, int):
    #        raise TypeError('Protein.start_point_cnt must be an int')
    #    if name == 'end_point_cnt' and not isinstance(value, int):
    #        raise TypeError('Protein.end_point_cnt must be an int')
    #    super().__setattr__(name, value)
    #    """

    def get_all_Proteins(self):
        """
        return an array with all the Protein in the database


        :return: array of Protein
        :rtype: array(Protein)
        """
        listOfProteins = []
        sqlObj = _Protein_sql_new()
        results = sqlObj.select_all_proteins_all_attributes()
        for element in results:
            listOfProteins.append(Protein(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9]))
        return listOfProteins

    def get_protein_by_id(id_protein):
        """
        return a proteing given its ID

        :param id_protein: id of the protein

        :type id_protein: int - required 

        :return:  Protein
        :rtype: Protein
        """
        sqlObj = _Protein_sql_new()
        results = sqlObj.select_protein_by_id(id_protein)
        protein_obj = Protein(results[0][0], results[0][1], results[0][2], results[0][3], results[0][4], results[0][5], results[0][6], results[0][7], results[0][8], results[0][9])
        return protein_obj


    def get_all_Proteins_limited(quantity_prots, offset_position):
        """
        return an array with all the Protein in the database limited by an offset

        :param quantity_prots: number of proteins
        :param offset_position: where start the collect

        :return: array of Protein
        :rtype: array(Protein)
        """
        listOfProteins = []
        sqlObj = _Protein_sql_new()
        results = sqlObj.select_all_proteins_all_attributes_limited(quantity_prots, offset_position)
        for element in results:
            listOfProteins.append(Protein(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9]))
        return listOfProteins

    def get_all_Proteins_not_in_temp_prot(self):
        """
        return an array with all the Protein in the database which are not in temp_prots (not treated)

        :return: array of Protein
        :rtype: array(Protein)
        """
        listOfProteins = []
        sqlObj = _Protein_sql_new()
        results = sqlObj.select_all_proteins_not_in_temp_prot()
        for element in results:
            listOfProteins.append(Protein(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9]))
        return listOfProteins
    
    def get_id_prot_by_designation(self):
        """
        Return the id of the protein given its description

        :return: id of the protein
        :rtype int
        """
        sqlObj = _Protein_sql_new()
        id_protein = sqlObj.get_protein_id_by_designation(self.designation)        
        return id_protein
    
    def create_protein(self):
        """
        Insert a Protein in the database if it doesn't yet exists and return it id WITHOUT ANY VERIFICATIONS
        The protein contains
        - accession number
        - designation (header)
        - proteic sequence
        - nucleic sequence
        - position start in the gene
        - position end in the gene

        :return: id of the protein
        :rtype int
        """
        sqlObj = _Protein_sql_new()
        id_prot = sqlObj.insert_protein_return_id(self.id_accession, self.designation, self.sequence_prot, self.sequence_dna, self.start_point, self.end_point)
        self.id_protein = id_prot
        return id_prot

    def create_protein_all_details_procedure(self, id_organism):
        """
        Insert a Protein in the database if it doesn't yet exists and return it id WITHOUT ANY VERIFICATIONS
        The protein contains
        - accession number
        - designation (header)
        - proteic sequence
        - nucleic sequence
        - position start in the gene
        - position end in the gene
        - position start in the contig
        - position end in the contig
        - fk_contig

        :return: id of the protein
        :rtype int
        """
        sqlObj = _Protein_sql_new()
        id_prot = sqlObj.insert_protein_all_info_return_id_procedure(self.id_accession, self.designation, self.sequence_prot, self.sequence_dna, self.start_point, self.end_point, self.start_point_cnt, self.end_point_cnt, self.fk_id_contig, id_organism)
        self.id_protein = id_prot
        return id_prot

    @DeprecationWarning
    def create_protein_all_details(self):
        """
        Insert a Protein in the database if it doesn't yet exists and return it id WITHOUT ANY VERIFICATIONS
        The protein contains
        - accession number
        - designation (header)
        - proteic sequence
        - nucleic sequence
        - position start in the gene
        - position end in the gene
        - position start in the contig
        - position end in the contig
        - fk_contig

        :return: id of the protein
        :rtype int
        """
        sqlObj = _Protein_sql_new()
        id_prot = sqlObj.insert_protein_all_info_return_id(self.id_accession, self.designation, self.sequence_prot, self.sequence_dna, self.start_point, self.end_point, self.start_point_cnt, self.end_point_cnt, self.fk_id_contig)
        self.id_protein = id_prot
        return id_prot


    def create_protein_secure(self):
        """
        Insert a Protein in the database if it doesn't yet exists and return it id, verify if any other protein with the same accession number exists
        The protein contains
        - accession number
        - designation (header)
        - proteic sequence
        - nucleic sequence
        - position start in the gene
        - position end in the gene

        :return: id of the protein
        :rtype int
        """
        sqlObj = _Protein_sql_new()
        id_protein = sqlObj.get_protein_id_by_accession(self.id_accession)
        if id_protein == -1:
            id_protein = self.create_protein()
            return id_protein
        else:
            print("It already exists a protein with the accession number n: " + str(self.id_accession))
            return id_protein


    
    def update_protein_contig(self):
        """
        Update the data of the contig for a given protein id, it updates:
        - position start of the contig
        - position end of the contig
        - FK contig key

        :return: if of the updated protein
        :rtype int
        """
        sqlObj = _Protein_sql_new()
        id_prot = sqlObj.set_contig_protein_by_id(self.id_protein, self.start_point_cnt, self.end_point_cnt, self.fk_id_contig)
        self.id_protein = id_prot
        return id_prot    
    
    def get_all_Proteins_by_fk_contig(fk_contig):
        """
        return an array with all the Protein in the database with a FK_contig

        :return: array of Protein
        :rtype: array(Protein)
        """
        listOfProteins = []
        sqlObj = _Protein_sql_new()
        results = sqlObj.select_all_proteins_all_attributes_by_fk_contig(fk_contig)
        for element in results:
            listOfProteins.append(Protein(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9]))
        return listOfProteins

    def get_all_Proteins_by_organism_id(organism_id):
        """
        return an array with all the Protein by an organism id

        :param organism_id: id of the protein

        :type organism_id: int - required 

        :return: array of Protein
        :rtype: array(Protein)
        """
        listOfProteins = []
        sqlObj = _Protein_sql_new()
        results = sqlObj.select_all_proteins_all_attributes_by_organism_id(organism_id)
        for element in results:
            listOfProteins.append(Protein(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9]))
        return listOfProteins

    def get_all_Proteins_with_domains_by_organism_id(organism_id):
        """
        return an array with all the Protein by an organism id.
        Return only the proteins with a minimum of 1 domain

        :param organism_id: id of the protein

        :type organism_id: int - required 

        :return: array of Protein
        :rtype: array(Protein)
        """
        listOfProteins = []
        sqlObj = _Protein_sql_new()
        results = sqlObj.select_all_proteins_all_attributes_with_domains_by_organism_id(organism_id)
        for element in results:
            listOfProteins.append(Protein(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9]))
        return listOfProteins

    def remove_protein_by_its_id(id_protein):
        """
        remove a protein given its id

        :param id_protein: id of the protein

        :type id_protein: int - required

        :return: prot_dom it removed
        :rtype: int
        """
        sqlObj = _Protein_sql_new()
        id_couple = sqlObj.remove_protein_by_its_id(id_protein)
        return id_couple

    def get_qty_proteins_by_organism_id(id_organism):
        """
        get quantity of proteins given a organism id

        :param id_organism: id of the organism

        :type id_organism: int - required

        :return: quantity of proteins or -1 if unknown the organism
        :rtype: int
        """

        sqlObj = _Protein_sql_new()
        id_couple = sqlObj.get_qty_proteins_by_organism_is(id_organism)
        return id_couple

    def get_protein_id_by_sequence_location(sequence, location_start, location_end, fk_id_organism):
        """
        get id protein with a give sequence, location start and end in a Fk id organism

        :param sequence: id of the organism
        :param location_start: id of the organism
        :param location_end: id of the organism
        :param fk_id_organism: id of the organism

        :type sequence: int - required
        :type location_start: int - required
        :type location_end: int - required
        :type fk_id_organism: int - required

        :return: list with the proteins ids
        :rtype: List(int)
        """

        list_ids = []
        sqlObj = _Protein_sql_new()
        results = sqlObj.get_protein_id_by_sequence_location(sequence, location_start, location_end, fk_id_organism)
        for element in results:
            list_ids.append(element[0])
        return list_ids


    def get_duplicates_sequence_by_organism_id(id_organism):
        """
        get list of ids of proteins duplicates

        :param id_organism: id of the organism

        :type id_organism: int - required

        :return: list with the proteins ids
        :rtype: List((sequence, start_point, end_point))
        """
        list_values = []
        sqlObj = _Protein_sql_new()
        results = sqlObj.get_duplicates_sequences_orga_id(id_organism)
        if len(results) > 0:
            for element in results:
                list_values.append((element[0], element[1], element[2]))
            return list_values
        else:
            return list_values


    def get_duplicates_sequences_ids_by_organism_id(id_organism):
        """
        get list of ids of proteins duplicates

        :param id_organism: id of the organism

        :type id_organism: int - required

        :return: list with the proteins ids
        :rtype: List((int, int))
        """

        list_duplicate_prots_ids = []
        list_duplicate_sequence = Protein.get_duplicates_sequence_by_organism_id(id_organism)
        if len(list_duplicate_sequence) > 0:
            for sequence, start_point, end_point in list_duplicate_sequence:
                if start_point != None and end_point != None:
                    sqlObj = _Protein_sql_new()
                    sequence = sequence.replace("'", "")
                    results = sqlObj.get_protein_id_by_sequence_location(sequence, start_point, end_point, id_organism)
                    assert len(results) > 1
                    default_val = results[0][0]
                    for element in results[1:]:
                        list_duplicate_prots_ids.append((default_val, element[0]))
                else:
                    with open("proteins_none.txt", "a") as myfile:
                        myfile.write((str(id_organism) + "," + sequence))
        return list_duplicate_prots_ids

