from configuration.configuration_api import ConfigurationAPI
import requests

conf_obj = ConfigurationAPI()
conf_obj.create_new_token()
print('aaaaa')

headers = {'Content-Type': 'application/json',
           'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImRpb2dvX3Rlc3QiLCJleHAiOjE1Mzk3OTE4NDAsImVtYWlsIjoiZGlvZ28xNzkwQGhvdG1haWwuY29tIn0.Eb4H9Ux3ZnYeEm8dB835Lh_codS72R1ATiHdkHtdbr8a'}
url = 'http://trex.lan.iict.ch:8080/api/family/'
r = requests.get(url, headers=headers)
print(r)
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