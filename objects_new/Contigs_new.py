# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 13:56:03 2017

@author: Diogo
"""

from SQL_obj_new.Contig_sql_new import _Contig_sql_new

class Contig(object):
    """
    This class treat the Contigs object has it exists in Contig table database
    By default, all FK are in the lasts positions in the parameters declaration
    """
    def __init__(self, id_contig = None, id_contig_db_outside = None, head = None, sequence = None, fk_id_whole_genome = None):
        """
        Constructor of the Contig object. All the parameters have a default value

        :param id_contig: id of the Contig - -1 if unknown
        :param id_contig_db_outside: id of the Contig for outside databas (Accession number if exists)
        :param head: first line of the fasta file which contain the contig - "" if unknown
        :param sequence: NUCLEOTIDE sequence of the CONTIG - "" if unknown
        :param fk_id_whole_genome: id of the whole DNA that contain this contig

        :type id_contig: int - not required
        :type id_contig_db_outside: text - required 
        :type head: text - required
        :type sequence: text - required
        :type fk_id_whole_genome: text - required
        """
        self.id_contig = id_contig
        self.id_contig_db_outside = id_contig_db_outside
        self.head = head
        self.sequence = sequence
        self.fk_id_whole_genome = fk_id_whole_genome
        
 
    def create_contig(self):
        """
        Insert a Contig in the database if any other Contig exists with the same head (first fasta line)
        
        The id of the CONTIG is updated

        :return: id of the CONTIG created
        :rtype: int
        """
        value_contig = None
        sqlObj = _Contig_sql_new()
        value_contig = sqlObj.insert_contig_if_not_exist(self.id_contig_db_outside, self.head, self.sequence, self.fk_id_whole_genome)
        self.id_contig = value_contig
        return value_contig

    def create_contig_no_verification(self):
        """
        Insert a Contig in the database WITHOUT ANY VERIFICATION
        
        The id of the CONTIG is updated

        :return: id of the CONTIG created
        :rtype: int
        """
        value_contig = None
        sqlObj = _Contig_sql_new()
        value_contig = sqlObj.insert_contig(self.id_contig_db_outside, self.head, self.sequence, self.fk_id_whole_genome)
        self.id_contig = value_contig
        return value_contig

    def get_all_Contigs_by_whole_DNA_id(fk_whole_dna):
        """
        Return all contig based on the fk_id_whole_genome in the database

        :return: array of Contig
        :rtype: array(Contig)
        """
        listOfOrganisms = []
        sqlObj = _Contig_sql_new()
        results = sqlObj.select_all_contigs_all_attributesby_fk_whole_dna(fk_whole_dna)
        for element in results:
            listOfOrganisms.append(Contig(element[0], element[1], element[2], element[3], element[4]))
        return listOfOrganisms

    def get_all_Contigs_by_organism_id(id_organism):
        """
        Return all contig based on the id_organism in the database

        :return: array of Contig
        :rtype: array(Contig)
        """
        listOfOrganisms = []
        sqlObj = _Contig_sql_new()
        results = sqlObj.get_contig_by_organism_id(id_organism)
        for element in results:
            listOfOrganisms.append(Contig(element[0], element[1], element[2], element[3], element[4]))
        return listOfOrganisms


    def get_contig_by_id(idContig):
        """
        return a contig given its ID

        :param idContig: id of the contig

        :type idContig: int - required 

        :return:  Contig
        :rtype: Contig
        """

        sqlObj = _Contig_sql_new()
        results = sqlObj.select_contig_by_id(idContig)
        contig_obj = Contig(results[0][0], results[0][1], results[0][2], results[0][3], results[0][4])
        return contig_obj

    def remove_contig_by_FK_whole_dna(fk_whole_dna):
        """
        remove a contig given the fk_whole dna

        :param fk_whole_dna: id of the fk_whole_dna

        :type fk_whole_dna: int - required

        :return: couple it removed
        :rtype: int
        """
        sqlObj = _Contig_sql_new()
        id_couple = sqlObj.remove_contig_by_fk_whole_dna(fk_whole_dna)
        return id_couple


    def __str__(self):
        """
        Overwrite of the str method
        """
        message_str = "ID: {0:d}, fk wholeDNA: {1:d}, ACC: {2} head: {3}, Sequence: {4}".format(self.id_contig, self.fk_id_whole_genome, self.id_contig_db_outside, self.head, self.sequence)
        return message_str



