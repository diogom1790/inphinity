import requests


class AuthenticationAPI(object):


    def __init__(self, username = '', password='', endpoint=''):
        self.username = username
        self.password = password
        self.endpoint = endpoint
    
    def validationAuthentication(self):
        loginData = {'username':self.username, 'password':self.password}
        response = requests.post(self.endpoint + 'login/', data=loginData)
        if response.status_code == 200:
            return response.json()
