from configuration.configuration_api import ConfigurationAPI
from rest_client.AuthenticationRest import AuthenticationAPI
import requests
from rest_client.FamilyRest import FamilyAPI
from objects_API.FamilyJ import FamilyJson




conf_obj = ConfigurationAPI()
conf_obj.load_data_from_ini()
AuthenticationAPI().createAutenthicationToken()

#print('aaaaa')

#headers = {'Content-Type': 'application/json',
#           'Authorization': 'Bearer ' + conf_obj.token}
#url = 'http://trex.lan.iict.ch:8080/api/family/'
#r = requests.get(url, headers=headers)
#print(r)

aaa = FamilyJson().getAllAPI()
print(aaa[2])
print('asdasd')
#from objects_new.Families_new import Family
#from serializers.Families_ser import FamilySchema

#list_fam = Family.get_all_Families()


#json, error = FamilySchema().dump(list_fam[2])
#print(json)

#####------------------
#import requests

#test = {'username':'diogo_test', 'password':'17061990Dio'}

#aaa = requests.post('http://trex.lan.iict.ch:8080/api/login/', data=test)
#print(aaa.text)