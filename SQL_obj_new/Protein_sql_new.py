# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:14:57 2017

@author: Diogo Leite
"""


# here the FK values was selected in lastas positions according to Proteins_new object class

from DAL import *
from configuration.configuration_data import *

class _Protein_sql_new(object):
    """
    This class manipulate the PROTEINS table in the database

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

    def get_database_name(self):
        """
        This method is used to get the database name used in factory

        :return: database name
        :rtype string
        """
        conf_data_obj = Configuration_data('INPHINITY')
        db_name = conf_data_obj.get_database()
        return db_name
        
    def select_all_proteins_all_attributes(self):
        """
        return all the Proteins in the database

        :return: cursor with all proteins
        :rtype Cursor list
        """

        sql_string = "SELECT id_protein_PT, id_protein_BD_online_PT, designation_PT, sequence_PT, DNA_sequence_PT, start_point_PT, end_point_PT, start_point_cnt_PT, end_point_cnt_PT, FK_id_contig_CT_PT FROM PROTEINS"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_protein_by_id(self, id_protein):
        """
        return all the Proteins in the database

        :param id_protein: id of the protein

        :type id_protein: int - required

        :return: cursor with all proteins
        :rtype Cursor list
        """

        sql_string = "SELECT id_protein_PT, id_protein_BD_online_PT, designation_PT, sequence_PT, DNA_sequence_PT, start_point_PT, end_point_PT, start_point_cnt_PT, end_point_cnt_PT, FK_id_contig_CT_PT FROM PROTEINS WHERE id_protein_PT = " + str(id_protein)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results


    def select_all_proteins_all_attributes_limited(self, qty_elements, offset_position):
        """
        return all the Proteins in the database

        :return: cursor with all proteins
        :rtype Cursor list
        """

        sql_string = "SELECT id_protein_PT, id_protein_BD_online_PT, designation_PT, sequence_PT, DNA_sequence_PT, start_point_PT, end_point_PT, start_point_cnt_PT, end_point_cnt_PT, FK_id_contig_CT_PT FROM PROTEINS LIMIT " + str(qty_elements) + " OFFSET " + str(offset_position) 
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_proteins_not_in_temp_prot(self):
        """
        return all the Proteins in the database which are not treated (not in temp_prots)

        :return: cursor with all proteins
        :rtype Cursor list
        """
        sql_string = "select id_protein_PT, id_protein_BD_online_PT, designation_PT, sequence_PT, DNA_sequence_PT, start_point_PT, end_point_PT, start_point_cnt_PT, end_point_cnt_PT, FK_id_contig_CT_PT FROM PROTEINS WHERE id_protein_PT NOT IN (select * from temp_prots)"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    
    def insert_protein_return_id(self, id_accession, designation, sequence_prot, sequence_dna, start_point, end_point):
        """
        Insert a PROTEIN and return its id, insert only with the parameters cited below. ANY VERIFICATION ARE DONE

        :param id_accession: accession number - -1 if unknown
        :param designation: the text following ">" in the fasta file (first line) - if unknown empty string
        :param sequence_prot: proteic sequence - if unknown empty string
        :param sequence_dna: nucleic sequence - if unknown empty string
        :param start_point: start position in the gene - -1 if unknown
        :param end_point: end position in the gene - -1 if unknown

        :return: id of the protein
        :rtype int
        """
        sqlObj = "INSERT INTO PROTEINS (id_protein_BD_online_PT, designation_PT, sequence_PT, DNA_sequence_PT, start_point_PT, end_point_PT) VALUES (%s, %s, %s, %s, %s, %s)"
        params = [id_accession, designation, sequence_prot, sequence_dna, start_point, end_point]
        dalObj = DAL(self.db_name, sqlObj, params)
        results = dalObj.executeInsert()
        return results.lastrowid


    def insert_protein_all_info_return_id_procedure(self, id_accession, designation, sequence_prot, sequence_dna, start_point, end_point, start_point_cnt, end_point_cnt, fk_id_contig, organism_id):
        """
        Insert a PROTEIN and return its id, insert only with the parameters cited below. ANY VERIFICATION ARE DONE

        :param id_accession: accession number - -1 if unknown
        :param designation: the text following ">" in the fasta file (first line) - if unknown empty string
        :param sequence_prot: proteic sequence - if unknown empty string
        :param sequence_dna: nucleic sequence - if unknown empty string
        :param start_point: start position in the gene - -1 if unknown
        :param end_point: end position in the gene - -1 if unknown
        :param start_point_cnt: start position in the contig - -1 if unknown
        :param end_point_cnt: end position in the contig - -1 if unknown
        :param fk_id_contig: fk_contig -1 if unknown
        :param id_organism: if of the organism of the protein -1 if unknown

        :return: id of the protein
        :rtype int
        """

        sqlObj = "insert_protein_secure"
        params = [id_accession, designation, sequence_prot, sequence_dna, start_point, end_point, start_point_cnt, end_point_cnt, fk_id_contig, organism_id]
        print(params)
        dalObj = DAL(self.db_name, sqlObj, params)
        results = dalObj.call_procedure()
        return results.lastrowid

    @DeprecationWarning
    def insert_protein_all_info_return_id(self, id_accession, designation, sequence_prot, sequence_dna, start_point, end_point, start_point_cnt, end_point_cnt, fk_id_contig):
        """
        Insert a PROTEIN and return its id, insert only with the parameters cited below. ANY VERIFICATION ARE DONE

        :param id_accession: accession number - -1 if unknown
        :param designation: the text following ">" in the fasta file (first line) - if unknown empty string
        :param sequence_prot: proteic sequence - if unknown empty string
        :param sequence_dna: nucleic sequence - if unknown empty string
        :param start_point: start position in the gene - -1 if unknown
        :param end_point: end position in the gene - -1 if unknown
        :param start_point_cnt: start position in the contig - -1 if unknown
        :param end_point_cnt: end position in the contig - -1 if unknown
        :param fk_id_contig: fk_contig -1 if unknown

        :return: id of the protein
        :rtype int
        """
        sqlObj = "INSERT INTO PROTEINS (id_protein_BD_online_PT, designation_PT, sequence_PT, DNA_sequence_PT, start_point_PT, end_point_PT, start_point_cnt_PT, end_point_cnt_PT, FK_id_contig_CT_PT) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = [id_accession, designation, sequence_prot, sequence_dna, start_point, end_point, start_point_cnt, end_point_cnt, fk_id_contig]
        print(params)
        dalObj = DAL(self.db_name, sqlObj, params)
        results = dalObj.executeInsert()
        return results.lastrowid
        
    def get_protein_id_by_designation(self, designation):
        """
        get the id of the protein given a description, if nothing exists return -1

        :param designation: the text existing after the symbol ">" of the fasta (first line) - string vide si rien

        :type designation: string - obligatoir

        :return: protein id or -1
        :rtype int
        """
        sql_string = "SELECT id_protein_PT FROM PROTEINS WHERE designation_PT = '" + designation + "'"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        if type(results)  == tuple and len(results) == 1:
            return results[0][0]
        else:
            return -1

    def get_protein_id_by_accession(self, accession):
        """
        return the protein id by the accession number, -1 if exists any one

        :param accession: accession value

        :type accession: string - required

        :return: id proteine or -1 if unknown
        :rtype int
        """

        sql_string =  "SELECT id_protein_PT FROM PROTEINS WHERE id_protein_BD_online_PT = '" + accession + "'"
        print(sql_string)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        if type(results)  == tuple and len(results) >= 1:
            return results[0][0]
        else:
            return -1

    def get_qty_proteins_by_organism_is(self, id_organism):
        """
        return the quantity of proteins given a organism id

        :param id_organism: id of the organism

        :type id_organism: int - required

        :return: quantity of proteins or -1 if unknown
        :rtype int
        """

        sql_string =  "select count(*) from GENES, PROTEINS WHERE FK_id_organism_OR_GE = " + str(id_organism) + " and FK_id_protein_PT_GE = id_protein_PT"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        if type(results)  == tuple and len(results) >= 1:
            return results[0][0]
        else:
            return -1
        
    def set_contig_protein_by_id(self, id_protein, start_cnt, end_cnt, fk_contig):
        """
        update the contig information given a protein id

        :param id_protein: protein id in the database
        :param start_cnt: start position in the contig
        :param end_cnt: end position in the contig
        :param fk_contig: FK of the contig

        :type id_protein: int - required
        :type start_point_cnt: int - not required
        :type end_point_cnt: int - not required
        :type fk_id_contig: int - required

        :return: id of the updated protein
        :rtype int
        """
        sql_string = "UPDATE PROTEINS SET start_point_cnt_PT = %s, end_point_cnt_PT = %s, FK_id_contig_CT_PT = %s WHERE id_protein_PT = " + str(id_protein)
        params = [start_cnt, end_cnt, fk_contig]
        dalObj = DAL(self.db_name, sql_string, params)
        results = dalObj.executeInsert()
        return results

    def select_all_proteins_all_attributes_by_fk_contig(self, fk_contig):
        """
        Consult the DB and return a list with proteins which have a fk_contig

        :return: cursor with the proteins
        :rtype Cursor list
        """
        sql_string = "SELECT id_protein_PT, id_protein_BD_online_PT, designation_PT, sequence_PT, DNA_sequence_PT, start_point_PT, end_point_PT, start_point_cnt_PT, end_point_cnt_PT, FK_id_contig_CT_PT FROM PROTEINS WHERE FK_id_contig_CT_PT = " + str(fk_contig)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_proteins_all_attributes_by_organism_id(self, id_organism):
        """
        Consult the DB and return a list with proteins from an organism id

        :return: cursor with the proteins
        :rtype Cursor list
        """
        sql_string = "SELECT id_protein_PT, id_protein_BD_online_PT, designation_PT, sequence_PT, DNA_sequence_PT, start_point_PT, end_point_PT, start_point_cnt_PT, end_point_cnt_PT, FK_id_contig_CT_PT FROM PROTEINS, GENES WHERE id_protein_PT = FK_id_protein_PT_GE and FK_id_organism_OR_GE = " + str(id_organism)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_proteins_all_attributes_with_domains_by_organism_id(self, id_organism):
        """
        Consult the DB and return a list with proteins from an organism id.
        It only return the proteins with a minimum of one domain

        :return: cursor with the proteins
        :rtype Cursor list
        """
        sql_string = "select distinct id_protein_PT, id_protein_BD_online_PT, designation_PT, sequence_PT, DNA_sequence_PT, start_point_PT, end_point_PT, start_point_cnt_PT, end_point_cnt_PT, FK_id_contig_CT_PT from GENES,  PROTEINS, PROT_DOM  WHERE FK_id_organism_OR_GE = " + str(id_organism) + " and FK_id_protein_PT_GE = id_protein_PT and id_protein_PT = FK_id_protein_PT_DP group by (id_protein_PT)"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def remove_protein_by_its_id(self, id_protein):
        """
        remove a protein by its id

        :param id_protein: id of the fk_bacterium 

        :type id_protein: int - required 

        :return: quantity of row deleted row
        :rtype int
        """
        sql_string = "DELETE FROM PROTEINS WHERE id_protein_PT = %s"
        dalObj = DAL(self.db_name, sql_string)
        params = [id_protein]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeDelete()
        return results.rowcount

    def get_protein_id_by_sequence_location(self, sequence, location_start, location_end, fk_id_organism):
        """
        get ids of the proteins with a given sequence and position in the genome for a given organism

        :param sequence: id of the fk_bacterium 
        :param location_start: id of the fk_bacterium 
        :param location_end: id of the fk_bacterium 

        :type sequence: int - required 
        :type location_start: int - required 
        :type location_end: int - required 

        :return: list of proteins id
        :rtype cursor(int)
        """
        sql_string = "SELECT id_protein_PT FROM PROTEINS, GENES WHERE FK_id_organism_OR_GE = " + str(fk_id_organism) + " and FK_id_protein_PT_GE = id_protein_PT AND sequence_PT = '" + sequence + "' AND start_point_PT = " + str(location_start) + " AND end_point_PT = " + str(location_end) 
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results


    def get_duplicates_sequences_orga_id(self, id_organism):
        """
        get ids of proteins which have the same sequence and position in a organism id

        :param sequence_pt: sequence of th bacterium

        :type sequence_pt: string - required 

        :return: list of sequences, start and end position
        :rtype Cursor list
        """

        sql_string = "SELECT sequence_PT, start_point_PT, end_point_PT, count(*) from GENES, PROTEINS WHERE FK_id_organism_OR_GE = " + str(id_organism) + " and id_protein_PT = FK_id_protein_PT_GE group by sequence_PT, start_point_PT, end_point_PT having count(*) > 1;"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

