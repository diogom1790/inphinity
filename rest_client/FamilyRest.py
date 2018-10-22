import json
from rest_client.GetRest import GetRest


class FamilyAPI(object):

    def __init__(self, function='family/'):
        self.function = function
        

    def get_all(self):
        result_get = GetRest(function = self.function).performRequest()
        return result_get
