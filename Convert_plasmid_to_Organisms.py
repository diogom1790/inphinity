# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 11:25:47 2018

@author: Diogo
"""

from objects_new.Couples_new import *
from objects_new.WholeDNA_new import *
from objects_new.Organisms_new import *
from objects_new.Contigs_new import *
from objects_new.Gene_new import *
from objects_new.Proteins_new import *



#This class is used to merge all contigs in a same strain (given these IDS):


list_ids_organisms = [10182, 10183, 10184]

def get_all_couples(list_ids_organisms):
    #Return all couples without repetitions for all "organisms". The couples without the same phages
    list_couples = []
    list_couples_aux = []
    list_id_couple_phage = []
    for id_organism in list_ids_organisms:
        #This part is used to get all couples
        list_couples_aux =  Couple.get_all_couples_by_bacterium(id_organism)
        for couple in list_couples_aux:
            if couple.fk_phage not in list_id_couple_phage:
                list_couples.append(couple)
                list_id_couple_phage.append(couple.fk_phage)
    return list_couples

def get_all_couples_id(list_ids_organisms):
    #return all ids of the couples
    list_id_couples = []
    list_couples_aux = []
    for id_organism in list_ids_organisms:
        list_couples_aux =  Couple.get_all_couples_by_bacterium(id_organism)
        for couple in list_couples_aux:
            list_id_couples.append(couple.id_couple)
    return list_id_couples

def get_whole_genomes(list_ids_whole_genomes):
    #return all the whole_genomes of the organisms
    list_whole_genomes = []

    for id_whole_genome in list_ids_whole_genomes:
        list_whole_genomes.append(WholeDNA.get_whole_dna_by_id(id_whole_genome))
    return list_whole_genomes


def get_all_organisms(list_id_organisms):
    #return all the organisms given an list of ids
    list_organisms = []
    for id_organism in list_id_organisms:
        orga = Organism.get_organism_by_id(id_organism)
        if orga != -1:
            list_organisms.append(orga)
    return list_organisms

def get_all_contigs(list_id_whole_genome):
    #return all contigs by fk_whole_dna
    list_contigs = []
    for id_whole_dna in list_id_whole_genome:
        list_conig_bd = Contig.get_all_Contigs_bi_whole_DNA_id(id_whole_dna)
        for contig in list_conig_bd:
            list_contigs.append(contig)
    return list_contigs

def get_all_genes_by_id_organism(list_ids_organisms):
    #return all genes given list of organisms ID
    list_genes = []
    for id_organism in list_ids_organisms:
        list_genes_bd = Gene.get_all_Genes_by_organism_id(id_organism)
        for gene in list_genes_bd:
            list_genes.append(gene)
    return list_genes

def get_all_genes_by_id_organism_unic(id_organisms):
    #return all genes given list of organisms ID
    list_genes = []
    list_genes_bd = Gene.get_all_Genes_by_organism_id(id_organisms)
    for gene in list_genes_bd:
        list_genes.append(gene)
    return list_genes


####### Creation AREA #######

#Whole list dna creation
whole_dna_obj = WholeDNA(id_wholeDNA = -1, head = "No Whole DNA_diogo", head_id = "No Whole DNA", sequence = "No Whole DNA")
id_whole_dna = whole_dna_obj.create_whole_dna_no_verification()

#Organism creation
orga_obj = Organism(id_organism = -1, gi ='', acc_num = ' NZ_AP018221.1', qty_proteins =6269, assembled=1, qty_contig=6, fk_source = 1, fk_strain = 8204, fk_type = 1, fk_whole_genome = id_whole_dna, fk_source_data = 1)

id_organism = orga_obj.create_bacterium_with_verification()


##Contig, protein, genes, and couple update
print("end")
for id_organism_in_list in list_ids_organisms:
    #contig part
    contig_head = WholeDNA.get_whole_dna_by_id(id_organism_in_list).head
    contig_sequence = WholeDNA.get_whole_dna_by_id(id_organism_in_list).sequence
    contig_id_contig_db_outside = WholeDNA.get_whole_dna_by_id(id_organism_in_list).head_id
    contig_obj = Contig(id_contig_db_outside = contig_id_contig_db_outside, head = contig_head, sequence = contig_sequence, fk_id_whole_genome = id_whole_dna)
    id_contig = contig_obj.create_contig_no_verification()

    #update genes and proteins
    list_of_genes = get_all_genes_by_id_organism_unic(id_organism_in_list)
    for gene in list_of_genes:
        protien_obj = Protein.get_protein_by_id(gene.FK_id_protein)
        #update protein contig id
        protien_obj.fk_id_contig = id_contig
        protien_obj.update_protein_contig()

        #update gene: FK organism
        gene.FK_id_organism = id_organism
        gene.update_gene_fk_organism()
print("sadasdasdasd asdasdasd asdasd ")

#UPDATE ORGANISM ID
id_organism = id_organism


#Create couples AREA
list_couples = get_all_couples(list_ids_organisms)
#create the olds couples
for couple in list_couples:
    couple.fk_lysis_inter = -1
    couple.fk_bacteria = id_organism
    couple.create_couple()




###### remove AREA #######
list_organisms = get_all_organisms(list_ids_organisms)

#remove couples
for organism in list_organisms:
    id_whole_genome = organism.fk_whole_genome
    id_organism = organism.id_organism

    #remove contigs
    Contig.remove_contig_by_FK_whole_dna(id_whole_genome)


    #remove couples
    Couple.remove_couple_by_id_bacterium(id_organism)

    #remove organism
    Organism.remove_organism_by_id(id_organism)

    #remove whole dnas
    WholeDNA.remove_whole_dna_by_id(id_whole_genome)

print("fini")

#remove the olds contigs



