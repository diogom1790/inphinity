from objects_new.Families_new import *
from objects_new.Couples_new import *


list_fam = Family.get_all_Families()

print(len(list_fam))

list_couple = Couple.get_all_couples()

print(len(list_couple))


