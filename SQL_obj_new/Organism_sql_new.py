# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:04:45 2017

@author: Diogo
"""

# here the FK values was selected in lastas positions according to Organisms_new object class

from DAL import *
from configuration.configuration_data import *

class _Organisms_sql_new(object):
    """
    This class manipulate the ORGANISM table in the database

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
        
    def select_all_organisms_all_attributes(self):
        """
        Consult the DB and return a list with all Organisms objects with all details

        :return: cursor with all Organisms
        :rtype Cursor list
        """
        sql_string = "SELECT id_organism_OR, gi_OR, acc_num_OR, qty_proteins_OR, assembled_OR, qty_contigue, FK_id_source_SO_OR, FK_id_strain_ST_OR, FK_id_type_TY_OR, FK_id_whole_DNA_DNA_OR FROM ORGANISMS"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_organisms_all_attributes_by_type(self, fk_type):
        """
        Consult the DB and return a list with all Organisms objects with all details give a type

        :return: cursor with all Organisms
        :rtype Cursor list
        """
        sql_string = "SELECT id_organism_OR, gi_OR, acc_num_OR, qty_proteins_OR, assembled_OR, qty_contigue, FK_id_source_SO_OR, FK_id_strain_ST_OR, FK_id_type_TY_OR, FK_id_whole_DNA_DNA_OR FROM ORGANISMS WHERE FK_id_type_TY_OR = " + str(fk_type)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results
    
    def insert_organism_if_not_exist(self, gi, acc_num, qty_proteins, assembled, qty_contig, fk_source, fk_strain, fk_type, fk_whole_genome, fk_source_data):
        """
        Insert a Organism object in the database and return its id. THIS METHOD VERIFY IF ALREADY EXISTS AN ORGANISM WITH THE SAME ACCESSION NUMBER and insert if not

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

        :return: id of the ProteinDom object inserted
        :rtype int
        """
        id_organism = self.get_id_organism_by_acc(acc_num)
        if id_organism == -1:
            sql_string = "INSERT INTO ORGANISMS (gi_OR, acc_num_OR, qty_proteins_OR, assembled_OR, qty_contigue, FK_id_source_SO_OR, FK_id_strain_ST_OR, FK_id_type_TY_OR, FK_id_whole_DNA_DNA_OR, FK_id_source_data_SD_OR) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            params = [gi, acc_num, qty_proteins, assembled, qty_contig, fk_source, fk_strain, fk_type, fk_whole_genome, fk_source_data]
            dalObj = DAL(self.db_name, sql_string)
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            print("It already exists an organism with the acc N: {0} OR GI N: {1}".format(acc_num, gi))
            return id_organism


    def insert_organism_no_validation(self, gi, acc_num, qty_proteins, assembled, qty_contig, fk_source, fk_strain, fk_type, fk_whole_genome, fk_source_data):
        """
        Insert a Organism object in the database and return its id. WITHOU ANY VERIFICATION

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

        :return: id of the ProteinDom object inserted
        :rtype int
        """
        sql_string = "INSERT INTO ORGANISMS (gi_OR, acc_num_OR, qty_proteins_OR, assembled_OR, qty_contigue, FK_id_source_SO_OR, FK_id_strain_ST_OR, FK_id_type_TY_OR, FK_id_whole_DNA_DNA_OR, FK_id_source_data_SD_OR) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = [gi, acc_num, qty_proteins, assembled, qty_contig, fk_source, fk_strain, fk_type, fk_whole_genome, fk_source_data]
        dalObj = DAL(self.db_name, sql_string)
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()
        return results.lastrowid

    def get_organisme_by_GI(self, GI):
        """
        Get the id of an organism given a GI number

        :param GI: Gi of an organism

        :type GI: string - required

        :return: id of the Organism object inserted
        :rtype int
        """
        sql_string = "SELECT id_organism_OR FROM ORGANISMS WHERE gi_OR = " + str(GI)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        if type(results) == tuple and results[0][0] == 0:
            return -1
        else:
            return results[0][0]
        
        
    def get_organism_list_id_by_taxonomy_sql(self, genus_design, specie_design, strain_design):
        """
        Get the id of an organism given the complete taxonomy

        :param genus_design: designation of teh genus
        :param specie_design: designation of the specie
        :param strain_design: designation of the strain

        :type genus_design: string - required
        :type specie_design: string - required
        :type strain_design: string - required

        :return: id of the Organism object inserted
        :rtype int
        """
        sql_string = "SELECT id_organism_OR from ORGANISMS, GENUSES, SPECIES, STRAINS Where FK_id_strain_ST_OR = id_strain_ST and FK_id_specie_SP_ST = id_specie_SP and FK_id_strain_ST_OR = id_strain_ST and FK_id_genus_GE_SP = id_genus_GE and designation_GE = '" + genus_design + "' and designation_SP = '" + specie_design + "' and designation_ST = '" + strain_design +"'"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        if type(results)  == tuple and len(results) >= 1:
            list_of_ids = []
            for element in results:
                list_of_ids.append(element[0])
            return list_of_ids
        else:
            return []
        
        
    def insert_organisme_phage(self, gi, acc_num, qty_proteins, assembled, qty_contig, fk_source, fk_strain, fk_type, fk_whole_genome, fk_source_data):
        """
        Insert a Organism object where its type is a phage in the database and return its id, this method DON'T VERIFY IF EXIST ANOTHER SAME PHAGE

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

        :return: id of the Organism object inserted
        :rtype int
        """
        sql_string = "INSERT INTO ORGANISMS (gi_OR, acc_num_OR, qty_proteins_OR, assembled_OR, qty_contigue, FK_id_source_SO_OR, FK_id_strain_ST_OR, FK_id_type_TY_OR, FK_id_whole_DNA_DNA_OR, FK_id_source_data_SD_OR) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        dalObj = DAL(self.db_name, sql_string)
        params = [gi, acc_num, qty_proteins, assembled, qty_contig, fk_source, fk_strain, fk_type, fk_whole_genome, fk_source_data]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()
        return results.lastrowid
    
    def get_bacterium_id_by_gi(self, gi):
        """
        Consult the DB and return the id of an Organism given a gi

        :param gi: gi number

        :type gi: int - required

        :return: id of the organism
        :rtype int
        """
        sql_string = "SELECT id_organism_OR FROM ORGANISMS WHERE gi_OR = " + str(gi) + " AND FK_id_type_TY_OR = 1"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results[0][0]
    
    
    def get_fk_whoe_dna_from_id(self, id_organism):
        """
        Consult the DB and return the id of the whole genome given an organism id otherwise returns -1

        :param gi: gi id_organism

        :type gi: int - required

        :return: id of the organism
        :rtype int
        """
        sql_string = "SELECT FK_id_whole_DNA_DNA_OR FROM ORGANISMS WHERE id_organism_OR = " + str(id_organism)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        if type(results) == tuple and len(results) == 1:
            return results[0][0]
        else:
            return -1

        sql_string = "SELECT id_organism_OR, gi_OR, acc_num_OR, qty_proteins_OR, assembled_OR, qty_contigue, FK_id_source_SO_OR, FK_id_strain_ST_OR, FK_id_type_TY_OR, FK_id_whole_DNA_DNA_OR FROM ORGANISMS WHERE gi_OR = '" + str(gi) + "' OR acc_num_OR = '" + str(acc_num) + "'"

    def get_id_organism_by_acc(self, acc_number):
        """
        get the id of a Organims based on it acc

        :param acc_number: accession number of the organism

        :type acc_number: string - required 

        :return: id of the Organism or -1 if inexistant
        :rtype int
        """
        sql_string = "SELECT id_organism_OR FROM ORGANISMS WHERE acc_num_OR = '" + str(acc_number) + "'"
        print (sql_string)
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) == 0:
            return -1
        else:
            return results[0][0]

    def get_id_organism_by_strain_designation(self, strain_designation):
        """
        get the id of a Organims based on it strain designation

        :param strain_designation: strain of the organism

        :type strain_designation: string - required 

        :return: id of the Organism or -1 if inexistant
        :rtype int

        :note it isn't case sensitive
        """

        sql_string = "select id_organism_OR from ORGANISMS, STRAINS WHERE FK_id_strain_ST_OR = id_strain_ST and designation_ST = '" + str(strain_designation) + "'"

        print(sql_string)

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) == 0:
            return -1
        else:
            return results[0][0]

    def get_ids_all_organisms(self):
        """
        get a list of list of ids of all organisms in the database


        :return: list of list of ids
        :rtype list(list(int))
        """
        sql_string = "select id_organism_OR FROM ORGANISMS"
        dalobj = DAL(self.db_name, sql_string)
        results = dalobj.executeSelect()

        return results

    def get_ids_all_organisms_by_type_and_source_data(self, type_organism, source_data):
        """
        get a list of list of ids of all organisms in the database


        :return: list of list of ids
        :rtype list(list(int))
        """
        sql_string = "select id_organism_OR FROM ORGANISMS WHERE FK_id_type_TY_OR = " + str(type_organism) + " AND FK_id_source_data_SD_OR = " + str(source_data)
        dalobj = DAL(self.db_name, sql_string)
        results = dalobj.executeSelect()

        return results

    def get_organism_by_id(self, id_organism):
        """
        Get an organism by its id

        :return: organisms elements infos
        :rtype List(infos organism)
        """
        sql_string = "SELECT id_organism_OR, gi_OR, acc_num_OR, qty_proteins_OR, assembled_OR, qty_contigue, FK_id_source_SO_OR, FK_id_strain_ST_OR, FK_id_type_TY_OR, FK_id_whole_DNA_DNA_OR, FK_id_source_data_SD_OR FROM ORGANISMS WHERE id_organism_OR = " + str(id_organism)
        dalobj = DAL(self.db_name, sql_string)
        results = dalobj.executeSelect()

        if len(results) == 0:
            return -1
        else:
            return results[0]

    def get_organism_id_design_By_end_strain(self, strain_end_design):
        sql_string = "select id_organism_OR, FK_id_type_TY_OR, designation_ST from ORGANISMS, STRAINS WHERE designation_ST LIKE '%" + str(strain_end_design) +  "' and FK_id_strain_ST_OR = id_strain_ST;"
        print(sql_string)
        dalobj = DAL(self.db_name, sql_string)
        results = dalobj.executeSelect()
        return results

    def select_all_organisms_all_attributes_by_specie(self, fk_id_specie):
        """
        Consult the DB and return a list with all Organisms with FK_type = 1 (bacteirum) objects with all details give a specie

        :param fk_id_specie: FK id specie of the organisms

        :type fk_id_specie: int - required 

        :return: cursor with all Organisms
        :rtype Cursor list
        """
        sql_string = "SELECT id_organism_OR, gi_OR, acc_num_OR, qty_proteins_OR, assembled_OR, qty_contigue, FK_id_source_SO_OR, FK_id_strain_ST_OR, FK_id_type_TY_OR, FK_id_whole_DNA_DNA_OR, fk_id_source_data_sd_or from STRAINS, SPECIES, ORGANISMS WHERE FK_id_specie_SP_ST = id_specie_SP and FK_id_strain_ST_OR = id_strain_ST and FK_id_type_TY_OR = 1 and id_specie_SP = " + str(fk_id_specie)
        dalobj = DAL(self.db_name, sql_string)
        results = dalobj.executeSelect()
        return results

    def select_all_organisms_all_attributes_by_strain(self, fk_id_strain):
        """
        Consult the DB and return a list with all Organisms the fk strain given

        :param fk_id_strain: FK id strain of the organisms

        :type fk_id_strain: int - required 

        :return: cursor with all Organisms
        :rtype Cursor list
        """
        sql_string = "SELECT id_organism_OR, gi_OR, acc_num_OR, qty_proteins_OR, assembled_OR, qty_contigue, FK_id_source_SO_OR, FK_id_strain_ST_OR, FK_id_type_TY_OR, FK_id_whole_DNA_DNA_OR, fk_id_source_data_sd_or from ORGANISMS WHERE fk_id_strain_st_or = " + str(fk_id_strain)
        dalobj = DAL(self.db_name, sql_string)
        results = dalobj.executeSelect()
        return results


    def remove_organism_by_id(self, id_organism):
        """
        remove a whole_dna by its id

        :param id_organism: id of the organism 

        :type id_organism: int - required 

        :return: quantity of removed row
        :rtype int
        """
        sql_string = "DELETE FROM ORGANISMS WHERE id_organism_OR = %s"
        dalObj = DAL(self.db_name, sql_string)
        params = [id_organism]
        dalObj.sqlcommand = sql_string
        dalObj.parameters = params
        results = dalObj.executeInsert()