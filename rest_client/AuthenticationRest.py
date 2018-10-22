import requests
from rest_client.PostRest import PostRest
from rest_client.login_json import LoginJson
import os

class AuthenticationAPI(object):


    def __init__(self, username = '', password='', endpoint=''):
        self.username = os.environ['username_api']
        self.password = os.environ['password_api']
        self.endpoint = os.environ['endpoint_api']
    
    def createAutenthicationToken(self):
        loginData = {'username':self.username, 'password':self.password}
        postRestObj = PostRest(function='login/', dataDict=loginData, includeHeaders = False)
        jsonResult = postRestObj.performRequest()
        loginSjonObj = LoginJson(jsonValue = jsonResult)
        if loginSjonObj.lodingData != None:
            os.environ["token_api"] = loginSjonObj.jsonData['token']
            return loginSjonObj.jsonData['token']
        return None
