from configuration.configuration_api import ConfigurationAPI
from rest_client.AuthenticationRest import AuthenticationAPI


from objects_API.DomainSourceInformation import DomainSourceInformationJson


#===============================================
# Script used the domains into the new database
#===============================================


conf_obj = ConfigurationAPI()
conf_obj.load_data_from_ini()
AuthenticationAPI().createAutenthicationToken()

list_domains_source = DomainSourceInformationJson.getAllAPI()

print(list_domains_source[0])
print(list_domains_source[0])
