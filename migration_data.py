from configuration.configuration_api import ConfigurationAPI
import requests

conf_obj = ConfigurationAPI()
conf_obj.create_new_token()
print('aaaaa')

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + conf_obj.token}
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