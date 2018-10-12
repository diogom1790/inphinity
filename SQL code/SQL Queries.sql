#ORGANISMS taxonomy by part of its name

select designation_FA, designation_GE, designation_SP, designation_ST, id_organism_OR, FK_id_type_TY_OR,
(select count(*) from GENES WHERE FK_id_organism_OR_GE = id_organism_OR) AS 'N_genes', 
(select count(*) from GENES, PROTEINS WHERE FK_id_protein_PT_GE = id_protein_PT and FK_id_organism_OR_GE = id_organism_OR) as 'N_proteins',
(select count(DISTINCT FK_id_contig_CT_PT) from PROTEINS, GENES WHERE FK_id_protein_PT_GE = id_protein_PT and FK_id_organism_OR_GE = id_organism_OR) as 'N_contigs'
from FAMILIES, GENUSES, SPECIES, STRAINS, ORGANISMS 
WHERE FK_id_family_FA_GE = id_family_FA and FK_id_genus_GE_SP = id_genus_GE and 
FK_id_specie_SP_ST = id_specie_SP and FK_id_strain_ST_OR = id_strain_ST and designation_ST LIKE '%M313%';


#Taxonomy of all organims
#Take time, 

select designation_FA, designation_GE, designation_SP, designation_ST, FK_id_strain_ST_OR, id_organism_OR, FK_id_type_TY_OR,
(select count(*) from GENES WHERE FK_id_organism_OR_GE = id_organism_OR) AS 'N_genes', 
(select count(*) from GENES, PROTEINS WHERE FK_id_protein_PT_GE = id_protein_PT and FK_id_organism_OR_GE = id_organism_OR) as 'N_proteins',
(select count(DISTINCT FK_id_contig_CT_PT) from PROTEINS, GENES WHERE FK_id_protein_PT_GE = id_protein_PT and FK_id_organism_OR_GE = id_organism_OR) as 'N_contigs'
from FAMILIES, GENUSES, SPECIES, STRAINS, ORGANISMS 
WHERE FK_id_family_FA_GE = id_family_FA and FK_id_genus_GE_SP = id_genus_GE and 
FK_id_specie_SP_ST = id_specie_SP and FK_id_strain_ST_OR = id_strain_ST order by id_organism_OR DESC LIMIT 10;


select * from WHOLE_DNA, CONTIGS, ORGANISMS WHERE FK_id_whole_genome_WD_CT = id_contig_CT and FK_id_whole_DNA_DNA_OR = id_dna_WD and id_organism_OR = 182;


#Afficher taxonomie:
 -Bactérie
select designation_SP, designation_ST, gi_OR from STRAINS, ORGANISMS, SPECIES WHERE FK_id_strain_ST_OR = id_strain_ST and FK_id_specie_SP_ST = id_specie_SP  and FK_id_type_TY_OR = 1 LIMIT 10

 -Phage
select designation_SP, designation_ST, gi_OR from STRAINS, ORGANISMS, SPECIES WHERE FK_id_strain_ST_OR = id_strain_ST and FK_id_specie_SP_ST = id_specie_SP  and FK_id_type_TY_OR = 2 LIMIT 10

 -Afficher le nombre de proteins par contigs:
select id_contig_CT, FK_id_whole_genome_WD_CT, (SELECT COUNT(*) FROM PROTEINS WHERE FK_id_contig_CT_PT =id_contig_CT) as 'qtd prots' from CONTIGS ORDER BY id_contig_CT;


Afficher le nombre de proteines dans un organisme selon son ID:
select FAMILIES.designation_FA, STRAINS.designation_ST, SPECIES.designation_SP, ORGANISMS.gi_OR, ORGANISMS.acc_num_OR,  count(GENES.id_gene_GE) FROM STRAINS, SPECIES, ORGANISMS, GENUSES, FAMILIES, GENES WHERE ORGANISMS.id_organism_OR = STRAINS.id_strain_ST and STRAINS.FK_id_specie_SP_ST = SPECIES.id_specie_SP and GENES.FK_id_organism_OR_GE = ORGANISMS.id_organism_OR and SPECIES.FK_id_genus_GE_SP = GENUSES.id_genus_GE and GENUSES.FK_id_family_FA_GE = FAMILIES.id_family_FA  and ORGANISMS.id_organism_OR = 42