from configuration.configuration_api import ConfigurationAPI
from rest_client.AuthenticationRest import AuthenticationAPI


from objects_API.DomainSourceInformationJ import DomainSourceInformationJson
from objects_API.DomainInteractionPairJ import DomainInteractionPairJson


#===============================================
# Script used the domains into the new database
#===============================================


conf_obj = ConfigurationAPI()
conf_obj.load_data_from_ini()
AuthenticationAPI().createAutenthicationToken()

list_domains_source = DomainSourceInformationJson.getAllAPI()

print(list_domains_source[0])
print(list_domains_source[0])

dom_int_pai_obj = DomainInteractionPairJson(domain_a = 869,domain_b = 866)
dom_int_pai_obj.setDomainInteractionPair()

list_interaction_pairs = DomainInteractionPairJson.getAllAPI()
print(list_interaction_pairs[0])