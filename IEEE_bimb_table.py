from objects_new.Organisms_new import *
from objects_new.Strains_new import *
from objects_new.Species_new import *
from objects_new.Genus_new import *
from objects_new.Families_new import *
from objects_new.Couples_new import *

import pandas as pd

count_taxo = {}


def dict_count(id_family, id_genus, id_specie, id_strain, qty_interact):
    global count_taxo
    if id_family in count_taxo.keys():
        #check genus
        list_genus = count_taxo[id_family][0]
        if id_genus not in list_genus:
            count_taxo[id_family][0].append(id_genus)
        #check Specie
        list_specie = count_taxo[id_family][1]
        if id_specie not in list_specie:
            count_taxo[id_family][1].append(id_specie)
        #check Strain
        list_strain = count_taxo[id_family][2]
        if id_strain not in list_strain:
            count_taxo[id_family][2].append(id_strain)
        qty_inter = count_taxo[id_family][3]
        count_taxo[id_family][3] = qty_inter + qty_interact
    else:
           count_taxo[id_family] = [[id_genus], [id_specie], [id_strain], qty_interact]

list_id_organisms = [4648,4657,4663,4677,4718,4752,4851,5221,5904,6155,6403,6452,6468,6485,6870,6936,6944,7005,7007,7012,7116,7133,7166,7168,7194,7200,7204,7283,7286,7315,7354,7414,7438,7451,7499,7528,7542,7553,7583,7585,7613,7642,7644,7668,7670,7720,7733,7736,7792,7795,7859,7940,7951,8012,8018,8028,8044,8048,8088,8159,8231,8269,8279,8280,8284,8299,8313,8315,8368,8373,8378,8381,8383,8431,8468,8540,8546,8698,8802,8864,8933,8957,8959,8962,8988,9058,9213,9224,9233,9248,9300,9360,9481,9569,9571,9662,10112,10138]

list_organisms = []
qty_couples = 0
for organism_id in list_id_organisms:
    organism_obj = Organism.get_organism_by_id(organism_id)
    list_organisms.append(organism_obj)

    id_strain = organism_obj.fk_strain
    strain_obj = Strain.get_strain_by_id(id_strain)

    id_specie = strain_obj.fk_specie
    specie_obj = Specie.get_specie_by_id(id_specie)

    id_genus = specie_obj.fk_genus
    genus_obj = Genus.get_genus_by_id(id_genus)

    id_family = genus_obj.fk_family
    family_obj = Family.get_family_by_id(id_family)


    list_couples = Couple.get_all_couples_by_type_level_source_bact_id(1, 4, 1, organism_id)
    qty_couples = len(list_couples)
    list_couples = Couple.get_all_couples_by_type_level_source_bact_id(1, 4, 2, organism_id)
    qty_couples += len(list_couples)


    dict_count(id_family, id_genus, id_specie, id_strain, qty_couples)

values_df = pd.DataFrame.from_dict(count_taxo, orient='index')
print(values_df)

matrix_values = []
aux_qty_strain = 0
for key, value in count_taxo.items():
    family_design = Family.get_family_by_id(key).designation
    qty_genus = len(value[0])
    qty_specie = len(value[1])
    qty_strain = len(value[2])
    qty_interact = value[3]
    matrix_values.append([family_design, qty_genus, qty_specie, qty_strain, qty_interact])

print(matrix_values)
df = pd.DataFrame(matrix_values)
print(df)
df.to_csv('taxonomy.csv')
print(len(list_organisms))