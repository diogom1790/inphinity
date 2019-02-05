
import datetime
from configuration.configuration_api import ConfigurationAPI
from rest_client.AuthenticationRest import AuthenticationAPI


from objects_API.DomainSourceInformationJ import DomainSourceInformationJson
from objects_API.DomainInteractionPairJ import DomainInteractionPairJson

from objects_API.DomainInteractionSourceJ import DomainInteractionSourceJson

from objects_API.DomainJ import DomainJson

from objects_3did.DDI_interaction_view import DDI_interaction_view


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


list_tuple_interactions_3did = get_pfam_interactions_3did()

dict_values = get_list_domains()

print(dict_values['PF02567'])


