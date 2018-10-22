# -*- coding: utf-8 -*-
"""
Created on Wen Oct 17 08:26:09 2018

@author: Diogo
"""

import configparser
from pathlib import Path
import os
import getpass
import sys
import configparser
from rest_client.AuthenticationRest import AuthenticationAPI


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
        self.saveEnvirVariables()

        with open("configuration/configuration_api.ini", 'w') as f:
            config.write(f)


    def load_data_from_ini(self):
        config = self.check_config_file_API()
        if config != None:
            self.endpoint = config['api_rest']['endpoint']
            self.username = config['api_rest']['username']
            self.password = config['api_rest']['password']
            self.token = config['api_rest']['token']
            self.saveEnvirVariables()

    def get_endpoint(self):
        config = self.check_config_file_API()
        if config != None:
            self.endpoint = config['api_rest']['endpoint']
            return self.endpoint

    def create_new_token(self):
        config = self.check_config_file_API()
        if config != None:
            self.load_data_from_ini()
        else:
            self.get_informations()
            self.create_ini_api_data()
        authentication_obj = AuthenticationAPI(username = self.username, password=self.password, endpoint=self.endpoint)
        token = authentication_obj.createAutenthicationToken()
        if token != None:
            os.environ["token_api"] = token
            self.token = token
    
    def getTokenFromIni(self):
        config = self.check_config_file_API()
        if config != None:
            self.token = config['api_rest']['token']
        else:
            self.create_new_token()
        return self.token

    def saveEnvirVariables(self):
        os.environ["token_api"] = self.token
        os.environ["endpoint_api"] = self.endpoint
        os.environ["username_api"] = self.username
        os.environ["password_api"] = self.password

    #def confirm_validity_token(self):
    #    if self.token != "":

#How to crypt key: https://stackoverflow.com/questions/42568262/how-to-encrypt-text-with-a-password-in-python/44212550