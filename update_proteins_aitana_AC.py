# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:57:10 2017

@author: Stage
"""

from objects_old.Bacteria_old import *

from files_treatment.bacteria_files import *

from files_treatment.fasta_proteins import *
from files_treatment.fasta_parsing import *

from objects_new.Families_new import * 
from objects_new.Genus_new import *
from objects_new.Species_new import *
from objects_new.Strains_new import *
from objects_new.Organisms_new import *
from objects_new.Genus_new import *
from objects_new.Gene_new import *

from SQL_obj_new.Organism_sql_new import *

bact_obj = Bacteria_old()
organism_sql_obj = Organisms_sql_new()


list_bacts = bact_obj.get_all_Bacteria()

print(len(list_bacts))

print(len(list_bacts[0].GI))


for bacteria in list_bacts:
    
    
    bacteria.complete_bacteria_from_old_DB()
    
    print(bacteria)
    
    print(bacteria.proteins_list[0].id_prot_DB_online)
    print(bacteria.proteins_list[0].sequence_prot)
    
    bacteria.write_csv_list_prots()
