# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:55:51 2017

@author: Diogo
"""

from SQL_obj_new.Gene_sql_new import _Gene_sql_new

class Gene(object):
    """
    This class treat the genes object has it exists in GENES table database
    By default, all FK are in the lasts positions in the parameters declaration
    """
    def __init__(self, id_gene = -1, gene_number = -1, dna_head = "No head", 
                 dna_sequence = "No sequence", start_position = -1, 
                 end_position = -1, FK_id_organism = -1, FK_id_protein = -1):
        """
        Constructor of the Gene object. All the parameters have a default value

        :param id_gene: id of the Gene - -1 if unknown
        :param gene_number: number of the gene correspond to the order of the gene in the whole sequence - -1 if unknown
        :param dna_head: fasta head first line of the gene - "No head" if unknown
        :param dna_sequence: NUCLEOTIDE sequence of the Gene - "" if unknown
        :param start_position: start position of the gene in the whole genome
        :param end_position: end position of the gene in the whole genome
        :param FK_id_organism: id of the organims which the gene belongs
        :param FK_id_protein: id of the protein which the gene belongs

        :type id_gene: int - not required
        :type gene_number: int - not required 
        :type dna_head: text - required
        :type dna_sequence: text - required
        :type start_position: int - not required
        :type end_position: int - not required
        :type FK_id_organism: int - required
        :type FK_id_protein: int - required
        """
        self.id_gene = id_gene
        self.gene_number = gene_number
        self.dna_head = dna_head
        self.dna_sequence = dna_sequence
        self.start_position = start_position
        self.end_position = end_position
        self.FK_id_organism = FK_id_organism
        self.FK_id_protein = FK_id_protein
        
    def get_all_Genes(self):
        """
        return an array with all the genes in the database

        :return: array of genes
        :rtype: array(Gene)
        """
        listOfGenes = []
        sqlObj = _Gene_sql_new()
        results = sqlObj.select_all_genes_all_attributes()
        for element in results:
            listOfGenes.append(Gene(element[0], element[1], element[2], element[3]))
        return listOfGenes

    def get_all_Genes_by_organism_id(fk_id_organism):
        """
        return an array with all the genes in the database of an organism ID

        :param fk_id_organism: id of the organism - -1 if unknown

        :type fk_id_organism: int - required

        :return: array of genes
        :rtype: array(Gene)
        """
        listOfGenes = []
        sqlObj = _Gene_sql_new()
        results = sqlObj.select_all_genes_all_attributes_by_organism_id(fk_id_organism)
        for element in results:
            listOfGenes.append(Gene(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7]))
        return listOfGenes

    def get_number_of_Genes_by_organism_id(fk_id_organism):
        """
        return the number of genes by organism id. In case of the inexistance of the organis return -1

        :param fk_id_organism: id of the organism - -1 if unknown

        :type fk_id_organism: int - required

        :return: array of genes
        :rtype: array(Gene)
        """
        listOfGenes = []
        sqlObj = _Gene_sql_new()
        results = sqlObj.select_number_genes_by_organism_id(fk_id_organism)
        return results
    
    def create_gene(self):
        """
        Insert a Gene in the database WITHOUT ANY VERIFICATION
        
        The id of the GENE is updated

        :return: id of the GENE created
        :rtype: int
        """
        sqlObj = _Gene_sql_new()
        id_gene = sqlObj.insert_gene_return_id(self.gene_number, self.dna_head, self.dna_sequence, self.start_position, self.end_position, self.FK_id_organism, self.FK_id_protein)
        self.id_gene = id_gene
        return id_gene

    def update_gene_fk_organism(self):
        """
        Update the data of the organism for a given organism id, it updates:
        - FK organism key

        :return: if of the updated organism
        :rtype int
        """
        sqlObj = _Gene_sql_new()
        id_gene = sqlObj.update_organism_of_gene(self.id_gene, self.FK_id_organism)
        self.id_gene = id_gene
        return id_gene 

    def delete_gene_from_id_organism(id_organism):
        """
        remove a genes given its fk_id_organism

        :param id_organism: id of the couple

        :type id_organism: int - required

        :return: id_organism removed
        :rtype: int
        """
        sqlObj = _Gene_sql_new()
        id_couple = sqlObj.remove_gene_by_id_organism(id_organism)
        return id_couple

    def delete_gene_from_id_protein(id_protein):
        """
        remove a genes given its fk_id_protein

        :param id_protein: id of the protein

        :type id_protein: int - required

        :return: id_organism removed
        :rtype: int
        """
        sqlObj = _Gene_sql_new()
        id_couple = sqlObj.remove_gene_by_id_protein(id_protein)
        return id_couple

    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d}, fk organism: {1:d}, fk protein: {1:d} gene number: {2:d}, DNA head: {3}, DNA sequence: {4}, Start position: {5:d}, End position: {6:d}".format(self.id_gene, self.FK_id_organism, self.FK_id_protein, self.dna_head, self.dna_sequence, self.start_position, self.end_position)
        return message_str
