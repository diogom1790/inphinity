# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:30:54 2017

@author: Diogo
"""

#Websit where is the description of the API: http://treelib.readthedocs.io/en/latest/examples.html

from treelib import Node, Tree
from objects_new.Families_new import *
from objects_new.Genus_new import *
from objects_new.Species_new import *


class TaxoNode(object):
    """
    Internal class used to create custom nodes in the tree
    """
    def __init__(self, id_db, designation, level_taxo):
        """
        Type of data for the nodes of the taxonomy tree

        :param id_db: id of the object, according to its taxonomy type, in the database
        :param designation: Name of the taxonomy
        :param type_taxo: level of taxonomy (1 = strain, 2 = specie, 3 = Genus, 4 = Family, 0 = root node)


        :type id_db: int - required 
        :type designation: text - required
        :type type_taxo: int  (between 0 - 4) - required
        """
        self.id_db = id_db
        self.designation = designation
        self.level_taxo = level_taxo


class Taxonomy_tree(object):
    """
    This class is used to create an tree with all the taxonomy in the database and is used to in the generations of dataset
    """

    def __init__(self):
        """
        No parameters until now

        the names of nodes correspond have this aspect: Fami_01 -> Fami = family and 01 = id (G_154 = Genus id 154)
        """
        self.tree_taxo = Tree()


    def get_species_by_genus(self, genusNodeName, genusObj):
        list_species = Specie.get_all_species_by_genus_id(genusObj.id_genus)

        for specie in list_species:
            specie_name_taxonomy = specie.designation + '_' + str(specie.id_specie)
            self.tree_taxo.create_node(specie_name_taxonomy.upper(), specie_name_taxonomy.lower(), parent = genusNodeName, data=TaxoNode(specie.id_specie, specie.designation, 2))


    def get_genus_by_family(self, familyNodeName, familyObj):
        list_genus = Genus.get_genus_by_family_id(familyObj.id_family)

        for genus in list_genus:
            genus_name_taxonomy = genus.designation + '_' + str(genus.id_genus)
            self.tree_taxo.create_node(genus_name_taxonomy.upper(), genus_name_taxonomy.lower(), parent = familyNodeName, data=TaxoNode(genus.id_genus, genus.designation,3))
            self.get_species_by_genus(genus_name_taxonomy.lower(), genus)

    def get_families(self, rootNodeName):
        list_families = Family.get_all_Families()
        for family in list_families:
            family_name_taxonomy = family.designation + '_' + str(family.id_family)
            self.tree_taxo.create_node(family_name_taxonomy.upper(), family_name_taxonomy.lower(), parent = rootNodeName, data=TaxoNode(family.id_family, family.designation,4))
            self.get_genus_by_family(family_name_taxonomy.lower(), family)



    def generate_tree(self):
        list_families = []
        list_genus = []
        list_specie = []
        rootNodeName = 'root'
        family_name_taxonomy = ''
        self.tree_taxo.create_node(rootNodeName.upper(),rootNodeName.lower(), data=(TaxoNode(-1, 'root node',0 )))

        self.get_families(rootNodeName)

