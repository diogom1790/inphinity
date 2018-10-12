# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:55:34 2017

@author: Diogo
"""

# here the FK values was selected in lastas positions according to Genes_new object class

from DAL import *
from configuration.configuration_data import *

class _Gene_sql_new(object):
    """
    This class manipulate the GENE table in the database

    The FK are manipulated in the lasts positions of the parameters
    """
    def __init__(self):
        self.db_name = self.get_database_name()

    def get_database_name(self):
        """
        This method is used to get the database name used in factory

        :return: database name
        :rtype string
        """
        conf_data_obj = Configuration_data('INPHINITY')
        db_name = conf_data_obj.get_database_name()
        return db_name
        
    def select_all_genes_all_attributes(self):
        """
        return all the Genes in the database

        :return: cursor with all Genes
        :rtype Cursor list
        """
        sql_string = "SELECT id_gene_GE, gene_number_GE, dna_head_GE, dna_sequence_GE, start_position_GE, end_position_GE, FK_id_organism_OR_GE, FK_id_protein_PT_GE FROM GENES"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_genes_all_attributes_by_organism_id(self, fk_id_organism):
        """
        return all the Genes in the database by an organism id

        :param fk_id_organism: number of the gene correspond to the order of the gene in the whole sequence - -1 if unknown

        :type fk_id_organism: int - required 

        :return: cursor with all Genes
        :rtype Cursor list
        """
        sql_string = "SELECT id_gene_GE, gene_number_GE, dna_head_GE, dna_sequence_GE, start_position_GE, end_position_GE, FK_id_organism_OR_GE, FK_id_protein_PT_GE FROM GENES WHERE FK_id_organism_OR_GE = " + str(fk_id_organism)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_number_genes_by_organism_id(self, fk_id_organism):
        """
        return all the Genes in the database by an organism id. In case of inexistance of the organism return -1

        :param fk_id_organism: number of the gene correspond to the order of the gene in the whole sequence - -1 if unknown

        :type fk_id_organism: int - required 

        :return: cursor with all Genes
        :rtype Cursor list
        """
        sql_string = "SELECT count(*) FROM GENES WHERE FK_id_organism_OR_GE = " + str(fk_id_organism)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        if type(results) == tuple and results[0][0] == 0:
            return -1
        else:
            return results[0][0]
    
    def insert_gene_return_id(self, gene_number, dna_head, dna_seq, start_position, end_position, fk_organism, fk_protein):
        """
        :param gene_number: number of the gene correspond to the order of the gene in the whole sequence - -1 if unknown
        :param dna_head: fasta head first line of the gene - "No head" if unknown
        :param dna_seq: NUCLEOTIDE sequence of the Gene - "" if unknown
        :param start_position: start position of the gene in the whole genome
        :param end_position: end position of the gene in the whole genome
        :param FK_id_organism: id of the organims which the gene belongs
        :param FK_id_protein: id of the protein which the gene belongs

        :type gene_number: int - not required 
        :type dna_head: text - required
        :type dna_seq: text - required
        :type start_position: int - not required
        :type end_position: int - not required
        :type FK_id_organism: int - required
        :type FK_id_protein: int - required

        :return: id of the inserted gene
        :rtype int
        """

        sqlObj = "INSERT INTO GENES (gene_number_GE, dna_head_GE, dna_sequence_GE, start_position_GE, end_position_GE, FK_id_organism_OR_GE, FK_id_protein_PT_GE) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = [gene_number, dna_head, dna_seq, start_position, end_position, fk_organism, fk_protein]
        dalObj = DAL(self.db_name, sqlObj, params)
        results = dalObj.executeInsert()
        return results.lastrowid

    def update_organism_of_gene(self, id_gene, fk_organism):
        """
        update the organisms information given a gene id

        :param id_gene: gene id in the database
        :param fk_organism: FK of the organism

        :type id_gene: int - required
        :type fk_organism: int - required

        :return: id of the updated gene
        :rtype int
        """
        sql_string = "UPDATE GENES SET FK_id_organism_OR_GE = %s WHERE id_gene_GE = " + str(id_gene)
        params = [fk_organism]
        dalObj = DAL(self.db_name, sql_string, params)
        results = dalObj.executeInsert()
        return results

    def remove_gene_by_id_organism(self, id_organism):
        """
        remove a organism by the id of fk_organism

        :param id_organism: id of the couple 

        :type id_organism: int - required 

        :return: quantity of row deleted
        :rtype int
        """
        sql_string = "DELETE FROM GENES WHERE FK_id_organism_OR_GE = %s"
        dalObj = DAL(self.db_name, sql_string)
        params = [id_organism]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeDelete()
        return results.rowcount


    def remove_gene_by_id_protein(self, id_protein):
        """
        remove an organism by the id of fk_protein

        :param id_protein: id of the protein 

        :type id_protein: int - required 

        :return: quantity of row deleted
        :rtype int
        """
        sql_string = "DELETE FROM GENES WHERE FK_id_protein_PT_GE = %s"
        dalObj = DAL(self.db_name, sql_string)
        params = [id_protein]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeDelete()
        return results.rowcount
