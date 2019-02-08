
import datetime
from configuration.configuration_api import ConfigurationAPI
from rest_client.AuthenticationRest import AuthenticationAPI


from objects_API.DomainSourceInformationJ import DomainSourceInformationJson
from objects_API.DomainInteractionPairJ import DomainInteractionPairJson

from objects_API.DomainInteractionSourceJ import DomainInteractionSourceJson

from objects_API.DomainJ import DomainJson

from objects_3did.DDI_interaction_view import DDI_interaction_view
from objects_Pfam.Pfam_interactions import Pfam_interaction
from objects_DOMINE.INTERACTION import interaction_ddi

#===============================================
# Script used the domains into the new database
#===============================================


##Test domains Source information
#list_domains_source = DomainSourceInformationJson.getAllAPI()

#print(list_domains_source[0])
#print(list_domains_source[0])


##Test Domains information Pairs
#dom_int_pai_obj = DomainInteractionPairJson(domain_a = 869,domain_b = 887)
##dom_int_pai_obj.setDomainInteractionPair()

#list_interaction_pairs = DomainInteractionPairJson.getAllAPI()
#print(list_interaction_pairs[0])

##Test Domain Interaction Source
#data_day = datetime.datetime.now().date()

#doma_interact_source = DomainInteractionSourceJson(date_creation = data_day, domain_interaction = 28, information_source = 1)

##doma_interact_source.setDomainInteractionSource()

#list_interaction_source = DomainInteractionSourceJson.getAllAPI()
#print(list_interaction_pairs[0])


conf_obj = ConfigurationAPI()
conf_obj.load_data_from_ini()
AuthenticationAPI().createAutenthicationToken()


def get_list_domains():
    """
    This method get all the pfam domains in the django database and put them into a dictionary

    :return dictionary{pfam_designation: id}
    :rtype dictionary

    """
    dictionary_pfam = {}
    list_domains = DomainJson.getAllAPI()
    dictionary_pfam = { pfam_element.designation: pfam_element.id for pfam_element in list_domains }

    return dictionary_pfam


def get_pfam_interactions_3did():
    """
    This method get all the ddi couples in 3did DB

    :return List[tuple(domain_a, domain_b)
    :rtype List(tuple)

    """
    list_interactions = DDI_interaction_view.get_all_pfam_interactions()

    data_couples = [(ddi_couple.domain_A, ddi_couple.domain_B) for ddi_couple in list_interactions]

    return data_couples

def get_pfam_interactions_iPfam():
    """
    This method get all the ddi couples in iPfam DB

    :return List[tuple(domain_a, domain_b)
    :rtype List(tuple)

    """
    list_interactions = Pfam_interaction.get_all_pfam_interactions()

    data_couples = [(ddi_couple.pfam_a, ddi_couple.pfam_b) for ddi_couple in list_interactions]

    return data_couples

def get_pfam_interactions_DOMINE():
    """
    This method get all the ddi couples in DOMINE DB

    :return List of interactions objects
    :rtype List(INTERACTION)

    """
    list_interactions = interaction_ddi.get_all_pfam_interactions()

    return list_interactions

def insertNewDomain(domain_designation):
    domain_obj = DomainJson(designation = pfam_a)
    domain_obj_json = domain_obj.setDomain()
    return domain_obj_json


def insertDDIIpfam(pfam_a, pfam_b, dict_pfams, id_source_information):
    date_day = datetime.datetime.now().date
    if pfam_a not in dict_pfams:
        domain_json = insertNewDomain(pfam_a)
        dict_pfams[domain_obj_json.designation] = domain_obj_json.id

    if pfam_b not in dict_pfams:
        domain_json = insertNewDomain(pfam_b)
        dict_pfams[domain_obj_json.designation] = domain_obj_json.id

    id_ddi_pair = DomainInteractionPairJson.verifyDDIpairExistence(pfam_a,pfam_b)
    if id_ddi_pair == -1:
        id_pfam_a = dict_pfams[pfam_a]
        id_pfam_b = dict_pfams[pfam_b]
        ddi_inserted = DomainInteractionPairJson(domain_a = id_pfam_a, domain_b = id_pfam_b)
        ddi_inserted = ddi_inserted.setDomainInteractionPair()
        id_ddi_pair = ddi_inserted.id

    id_ddi_source_information = DomainInteractionSourceJson.verifyDDIpairSourceExistence(id_ddi_pair, id_source_information)
    if id_ddi_source_information == -1:
        ddi_source_obj = DomainInteractionSourceJson(date_creation = date_day, domain_interaction = id_ddi_pair, information_source = id_source_information)
        print(ddi_source_obj)
        print('B---------------')
        ddi_source_obj = ddi_source_obj.setDomainInteractionSource()

def insertIpfamDDI(list_tuples, dict_elements):
    for dom_a, dom_b in list_tuples:
       insertDDIIpfam(dom_a, dom_b, dict_elements, 1)

#Verify the DDI existence
dict_values = get_list_domains()
id_ddi_pair = DomainInteractionPairJson.verifyDDIpairExistence('PF02029','PF04545')

list_tuples_iPfam = get_pfam_interactions_iPfam()
insertIpfamDDI(list_tuples_iPfam, dict_values)


list_interactions_DOMINE = get_pfam_interactions_DOMINE()
list_tuples_iPfam = get_pfam_interactions_iPfam()
list_tuple_interactions_3did = get_pfam_interactions_3did()





print(dict_values['PF02567'])


