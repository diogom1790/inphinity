# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:58:54 2017

@author: Diogo Leite
"""

from configuration.configuration_data import *

import pymysql
import psycopg2

class DBAccess(object):
    """
    This class manage the db connections according to the database_config.ini

    NOTE: see pattern factory to understand the implementation
    """

    def factory(type):
        """
        Retourne les donnes d acces de la DB selon le type d objet

        param type: nom interne de la base de donnee a utiliser

        """

        conf_obj = Configuration_data(type)
        data_connect = conf_obj.get_database_connection_information()
        type_of_db = conf_obj.get_db_type()


        if type_of_db == 0:
            return mysqlConnection(type)

        if type_of_db == 1:
            return postgreSQLConnection(type)

        if type_of_db == 2:
            print("hello")


        assert 0, "Unknown database"
        
    factory = staticmethod(factory)


    def get_connection_user_data(type_db):
        conf_obj = Configuration_data(type_db)
        data_connect = conf_obj.get_database_connection_information()
        return data_connect


class mysqlConnection(DBAccess):

    def __init__(self, name_db):
        self.name_db = name_db

    def getConnectionOB(self):
        db_name = self.name_db
        data_access = DBAccess.get_connection_user_data(db_name)
        
        self.dbHost = data_access[1]
        self.dbUser = data_access[2]
        self.dbPasswd = data_access[3]
        self.dbnamePb = db_name
        
        dbConnection = pymysql.connect(host=self.dbHost, user=self.dbUser, passwd=self.dbPasswd, db=self.dbnamePb)
        return dbConnection

class postgreSQLConnection(DBAccess):

    def __init__(self, name_db):
        self.name_db = name_db

    def getConnectionOB(self):
        db_name = self.name_db
        data_access = DBAccess.get_connection_user_data(db_name)

        self.dbHost = data_access[1]
        self.dbUser = data_access[2]
        self.dbPasswd = data_access[3]
        self.dbnamePb = db_name
        dbConnection = psycopg2.connect(host=self.dbHost, user=self.dbUser, password=self.dbPasswd, dbname=self.dbnamePb)
        return dbConnection

    