# -*- coding: utf-8 -*-
"""
Created on Wen Oct 17 08:26:09 2018

@author: Diogo
"""

import configparser
from pathlib import Path
from rest_client.authentication_rest import AuthenticationAPI
from rest_client.login_json import LoginJson
import os
import getpass
import sys
import configparser


class ConfigurationAPI:
    """
    This class is called when we need to use the API to get the logi values. All the values are read in a configuration file

    :param endpoint: the API rest endpoint link
    :param username: username to connect to the API
    :param password: password of the connection
    :param token: token used for the security of the requests

    :type endpoint: text - required
    :type username: text - required
    :type password: text - required
    :type token: text - required
    """

    def __init__(self):
        self.endpoint = ""
        self.username = ""
        self.password = ""
        self.token = ""

    def get_informations(self):
        self.endpoint = input("endpoint: ")
        self.username = input("username: ")
        self.password = getpass.getpass(prompt='Password: ', stream=sys.stderr)


    def check_config_file_API(self):
        """
        This method check if a configuration file exists for the API and return it.

        :return: configparser object if exist or None in case of no
        :rtype configparser object
        """
        complete_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'configuration'))
        config_file = Path(complete_path + '/configuration_api.ini')
        if config_file.is_file() == False:
            return None
        config = configparser.ConfigParser()
        config.read(complete_path + '/configuration_api.ini')
        return config

    def create_ini_api_data(self):
        config = configparser.ConfigParser()
        config.add_section('api_rest')
        config['api_rest']['endpoint'] = self.endpoint 
        config['api_rest']['username'] = self.username
        config['api_rest']['password'] = self.password

        with open("configuration/configuration_api.ini", 'w') as f:
            config.write(f)

    def create_new_token(self):
        config = self.check_config_file_API()
        if config != None:
            self.endpoint = config['api_rest']['endpoint']
            self.username = config['api_rest']['username']
            self.password = config['api_rest']['password']
        else:
            self.get_informations()
            self.create_ini_api_data()
        authentication_obj = AuthenticationAPI(username = self.username, password=self.password, endpoint=self.endpoint)
        json_response = authentication_obj.validationAuthentication()
        loginSjonObj = LoginJson(jsonValue = json_response)
        if loginSjonObj.lodingData != None:
            self.token = loginSjonObj.jsonData['token']

    def get_token(self):
        if len(self.token) == 0:
            create_new_token()
        return self.token

    #def confirm_validity_token(self):
    #    if self.token != "":

#How to crypt key: https://stackoverflow.com/questions/42568262/how-to-encrypt-text-with-a-password-in-python/44212550