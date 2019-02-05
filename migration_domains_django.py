
import datetime
from configuration.configuration_api import ConfigurationAPI
from rest_client.AuthenticationRest import AuthenticationAPI


from objects_API.DomainSourceInformationJ import DomainSourceInformationJson
from objects_API.DomainInteractionPairJ import DomainInteractionPairJson

from objects_API.DomainInteractionSourceJ import DomainInteractionSourceJson

from objects_API.DomainJ import DomainJson


#===============================================
# Script used the domains into the new database
#===============================================


conf_obj = ConfigurationAPI()
conf_obj.load_data_from_ini()
AuthenticationAPI().createAutenthicationToken()

#Test domains Source information
list_domains_source = DomainSourceInformationJson.getAllAPI()

print(list_domains_source[0])
print(list_domains_source[0])


#Test Domains information Pairs
dom_int_pai_obj = DomainInteractionPairJson(domain_a = 869,domain_b = 887)
#dom_int_pai_obj.setDomainInteractionPair()

list_interaction_pairs = DomainInteractionPairJson.getAllAPI()
print(list_interaction_pairs[0])

#Test Domain Interaction Source
data_day = datetime.datetime.now().date()

doma_interact_source = DomainInteractionSourceJson(date_creation = data_day, domain_interaction = 28, information_source = 1)

#doma_interact_source.setDomainInteractionSource()

list_interaction_source = DomainInteractionSourceJson.getAllAPI()
print(list_interaction_pairs[0])


list_domains = DomainJson.getAllAPI()
print(list_domains[0])