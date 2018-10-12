# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 08:26:09 2018

@author: Diogo
"""

import configparser
from pathlib import Path
import os




class Configuration_data:
    """
    This class is called when we need to insert values in the database to select it
    """

    def __init__(self, db_name = "INPHINTY"):
        """
        Constructor of the object of configuration. if any configuration file exists, it always used the "interal" database

        :param db_name: name of the database (INPHINITY, DOMINE,...) accoding these in mySQL

        :type db_name: text - required
        """
        self.db_name = db_name
        self.host_ip = ""
        self.usr_name = ""
        self.pwd_db = ""

    def check_config_file(self):
        """
        This method check if a configuration file exists and return it.

        :return: configparser object if exist or None in case of no
        :rtype configparser object
        """
        complete_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'configuration'))
        config_file = Path(complete_path + '/database_config.ini')
        if config_file.is_file():
            config = configparser.ConfigParser()
            config.read(complete_path + '/database_config.ini')
            return config
        else:
            print('No configuration file, db inside is considered')
            return None

    def get_inphinity_db(self):
        """
        This method return the INPHINTY database nam used

        :return: name of the database inphinity
        :rtype string
        """
        database_name = 'INPH_proj'
        config = self.check_config_file()
        if config != None:
            database_name = config['DATABASE']['name_database_inphinity']
        return database_name

    def get_domine_db(self):
        """
        This method return the DOMINE database nam used

        :return: name of the database DOMINE
        :rtype string
        """
        database_name = 'domine_db_out'
        config = self.check_config_file()
        if config != None:
            database_name = config['DATABASE']['name_database_domine']
        return database_name

    def get_3did_db(self):
        """
        This method return the 3did database nam used

        :return: name of the database 3did
        :rtype string
        """
        database_name = '3did_db_out'
        config = self.check_config_file()
        if config != None:
            database_name = config['DATABASE']['name_database_3did']
        return database_name

    def get_iPFAM_db(self):
        """
        This method return the 3did database nam used

        :return: name of the database 3did
        :rtype string
        """
        database_name = 'pfam_db_out'
        config = self.check_config_file()
        if config != None:
            database_name = config['DATABASE']['name_database_iPFAM']
        return database_name

    def get_db_type(self):
        """
        This method return the type of database used
        Typically: 0 = mysql and 1 = postgresql

        :return: type of database used
        :rtype int
        """
        id_db_used = -1
        config = self.check_config_file()
        if config != None:
            id_db_used = config['CONFIG_ACCESS']['db_access']

        return int(id_db_used)

    def get_db_access(self):
        """
        This method return the tags used to obtain the database access data and if it is from the server or local
        Typically DB: 0 = mysql, 1 = postgresql
        Typically connection: 0 = inside, 1 = outside

        :return: list[tag_host, tag_user, tag_pwd]
        :rtype list[]
        """

        type_database = -1
        type_connection = -1
        list_tags_db_access = []
        config = self.check_config_file()
        if config != None:
            type_database = self.get_db_type()
            type_connection = config['CONFIG_ACCESS']['db_connection']


        if type_connection == 0:
            list_tags_db_access.append('host_inside_trex')
        else:
            list_tags_db_access.append('host_outside_trex')

        if type_database == 0:
            list_tags_db_access.extend(('usr_mysql','pwd_mysql'))
        else:
            list_tags_db_access.extend(('usr_postgres','pwd_postgres'))


        return list_tags_db_access

    def get_host_ip(self, connection_location_tag):
        """
        This method return the host ip used for the connection (typically inside or outside)

        :param connection_location_tag: tag in the .ini file to obtain the IP
        :type connection_location_tag: string - mandatory

        :return: host adresse
        :rtype string
        """
        host_ip = ""
        config = self.check_config_file()
        if config != None:
            host_ip = config['HOST'][connection_location_tag]
        return host_ip

    def get_user_data(self, usr_db, pwd_db):
        """
        This method return the connection data used to perform the login

        :param usr_db: tag in the .ini file to obtain the username
        :param pwd_db: tag in the .ini file to obtain the pwd

        :type usr_db: string - mandatory
        :type pwd_db: string - mandatory

        :return: list[username, pwd]
        :rtype list[]
        """
        data_connection = []
        config = self.check_config_file()
        if config != None:
            data_connection.append(config['USER'][usr_db])
            data_connection.append(config['PWD'][pwd_db])
        return data_connection

    def get_database_name(self):
        """
        Return the name of the database according the ini file

        :return: name of the database
        :rtype string object
        """

        database_name = ""

        if self.db_name is 'INPHINITY':
            database_name = self.get_inphinity_db()
        if self.db_name is 'DOMINE':
            database_name = self.get_domine_db()
        if self.db_name is '3DID':
            database_name = self.get_3did_db()
        if self.db_name is 'iPFAM':
            database_name = self.get_iPFAM_db()

        return database_name

    def get_database_connection_information(self):
        """
        Return the data necessary for the database connection

        :return: list[host, user, pwd, db_name]
        :rtype list[]
        """
        db_data_access = []

        database_name = self.get_database_name()

        list_accessdb = self.get_db_access()
        host_ip = self.get_host_ip(list_accessdb[0])
        user_pwd = self.get_user_data(list_accessdb[1], list_accessdb[2])
        db_data_access = [database_name, host_ip, user_pwd[0], user_pwd[1]]

        assert len(db_data_access) == 4

        return db_data_access


