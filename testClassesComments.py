from objects_new.Proteins_new import *
from objects_new.Organisms_new import *
from objects_new.Contigs_new import *
from objects_new.Gene_new import *

from files_treatment_new.xls_gen_bank_rast import *
from files_treatment_new.fasta_contigs_RAST import *


from objects_new.PPI_couples_new import *

from objects_new.Strains_new import *

from objects_new.WholeDNA_new import *



#JUST FOR TEST.....
def verify_contigs_in_list(list_id_cnt_excel, list_ids_cnt_fasta):
    quantity_elms = 0
    same_size = False
    if len(list_id_cnt_excel) == len(list_ids_cnt_fasta):
        for element in list_id_cnt_excel:
            if element in list_ids_cnt_fasta:
                quantity_elms += 1
    if quantity_elms == len(list_ids_cnt_fasta):
        same_size = True
    else: 
        same_size = False

    return same_size


#contigs excel file
xls_object = Xls_gen_bank(path_file = r'C:\Users\Stage\Documents\GitHub\inphinity\Patrice\Acinetobacter baumannii Ab26.xls', sheet_name = 'Features in Acinetobacter bauma')

list_contigs_in_xls = xls_object.get_contigs_id_sorted()

#contigs fasta file
contig_file = Fasta_contigs_RAST(path_file = r'C:\Users\Stage\Documents\GitHub\inphinity\Patrice\Acinetobacter baumannii Ab26.contigs.fasta')
list_contigs_ids = contig_file.get_list_contigs_id()
list_contigs_obj = contig_file.create_contigs_from_file()

size_lists = verify_contigs_in_list(list_contigs_in_xls, list_contigs_ids)

qty_contigs_organism = len(list_contigs_ids)
qty_proteins_organism = xls_object.get_number_of_proteins()

aux = 0

for contig in list_contigs_obj:
    list_proteins = xls_object.get_proteins_objects_by_contig_id(contig.head)
    aux += len(list_proteins)

assert aux == qty_proteins_organism

#Strain
designation_strain = "Ab26"
strain_obj = Strain(designation = designation_strain, fk_specie = 527)


#Whole DNA OBJ
id_strain = strain_obj.create_strain()

whole_dna_obj = WholeDNA(id_wholeDNA = -1, head = "Unknown_test", head_id = "Unknown", sequence = "Unknown")
id_whole_dna = whole_dna_obj.create_whole_dna_no_verification()

#Organism
organism_obj = Organism(gi = "", acc_num = "", qty_proteins = qty_proteins_organism, assembled = True, qty_contig = qty_contigs_organism, fk_source = 2, fk_strain = id_strain, fk_type = 1, fk_whole_genome = id_strain, fk_source_data = 5)

id_organism_Created = organism_obj.create_organism()

list_proteins = None
aux = 0
for contig in list_contigs_obj:
    list_proteins = xls_object.get_proteins_objects_by_contig_id(contig.head)
    contig.fk_id_whole_genome = id_whole_dna
    contig_id = contig.create_contig_no_verification()
    for protein_obj in list_proteins:
        protein_obj.fk_id_contig = contig_id
        id_protein = protein_obj.create_protein()
        gene_obj = Gene(FK_id_organism = id_organism_Created, FK_id_protein = id_protein)
        gene_obj.create_gene()

print(len(list_proteins))

