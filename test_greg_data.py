from files_treatment_new.xls_gen_bank_rast import Xls_gen_bank
from files_treatment_new.fasta_contigs_RAST import Fasta_contigs_RAST

from files_treatment_new.genbank_file_RAST import Genbank_proteic_RAST


import os

import time

cwd = os.getcwd()


############# TEST EXCEL FILES ############# 
#Test load xls
print(cwd)
xls_obj = Xls_gen_bank(cwd + '\RAST\\SPREADSHEET\\525717-Escherichia_coli_CFT079.xls')
#xls_obj.read_xls_file()

#Test get row number X
xls_obj.get_row_by_number(1)

#Test get all contigs
listas = xls_obj.get_contigs_id_sorted()
print(type(listas))
print(listas[0])

#Test get all proteins from a given contig id
list_prot = xls_obj.get_proteins_ids_by_contig_id("out_1")
print(type(list_prot))
print(list_prot[0])

#Test get information from a given protein id
www = xls_obj.get_information_line_by_protein_id(list_prot[0])

print(xls_obj.get_number_of_proteins())

print("end")

############# TEST CONTIGS FASTA FILES ############# 

fasta_contigs_file = Fasta_contigs_RAST(cwd + '\RAST\\CONTIGS\\525717-Escherichia_coli_CFT079.contigs.fa')



sequence_contig_nucleic = fasta_contigs_file.get_contig_seq_by_id(listas[0])


############# TEST CONTIGS genbank FILES ############# 

genbank_file = Genbank_proteic_RAST(cwd + '\RAST\\GEN_BANK\\525717-Escherichia_coli_CFT079.gbk')


aaaa = genbank_file.get_definition_of_the_organism()
print(aaaa)
www = genbank_file.get_taxonomy_array()
print(www)

print(type(genbank_file.data_gen_bank))

print(list(genbank_file.data_gen_bank.keys())[0])

qty_contig = genbank_file.get_number_of_contigs()

print(genbank_file.get_family())

print(genbank_file.get_genus())

print(genbank_file.get_specie())

print(genbank_file.get_strain())

print("--------")



##### Start test for one organisme
start_time = time.time()
print("Start organism")
for contig in listas:
    print("pass contig: {0}".format(contig))
    list_prot = xls_obj.get_proteins_ids_by_contig_id(contig)
    for protein in list_prot:
        protein_info = xls_obj.get_information_line_by_protein_id(protein)

print("End organism")
end_time = time.time()
total_time = end_time - start_time
print("It takes {0:f} seconds".format(total_time))