from configuration.configuration_api import ConfigurationAPI
import requests

class getRest(object):

    def __init__(self, function):
        self.url_base = ''
        self.function = function
        self.headers = None

    def get_header():
        conf_obj = ConfigurationAPI()
        conf_obj.get_token()
        self.headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + conf_obj.token}

    def performRequest(self):
        self.get_header()
        url_get = self.url_base + self.function
        resultsJson = requests.get(url_get, headers=self.headers)
