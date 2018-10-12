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

        #if type =="BMC":
        #    return BMCAccess()
        #if type == "INPHINITY":
        #    return INPHINITYAccess()
        #if type == "INPH_2":
        #    return INPHINITY_VF_access()
        #if type == "INPH_proj":
        #    return INPHINITY_proj_DB()
        #if type == "INPH_proj_out":
        #    return INPHINITY_proj_DB_out()
        #if type == "pfam_db_out":
        #    return PFAM_DB_out()
        #if type == "3did_db_out":
        #    return DID3_DB_out()
        #if type == "domine_db_out":
        #    return DOMINE_DB_out()
        #if type == "student_out":
        #    return INPHINITY_std_out()
        #if type == "INPH_postgres":
        #    return INPHINITY_postgres()

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

    
class BMCAccess(DBAccess):
    """
    Classe internet qui retourne une connection pour la base de donnee phage_bact_BMC

    :return: objet connection pour la base de donnee phage_bact_BMC
    :rtype: mysql connection
    """
    def getConnectionOB(self):
        self.dbHost = "127.0.0.1"
        self.dbUser = "root"
        self.dbPasswd = "diogo"
        self.dbnamePb = "phage_bact_BMC"
        
        dbConnection = pymysql.connect(host=self.dbHost, user=self.dbUser, passwd=self.dbPasswd, db=self.dbnamePb)
        return dbConnection

        
class INPHINITYAccess(DBAccess):
    """
    Classe internet qui retourne une connection pour la base de donnee inphinityDB

    :return: objet connection pour la base de donnee inphinityDB
    :rtype: mysql connection
    """
    def getConnectionOB(self):
        self.dbHost = "127.0.0.1"
        self.dbUser = "root"
        self.dbPasswd = "Miguel1"
        self.dbnamePb = "inphinityDB_proj"
        dbConnection = pymysql.connect(host=self.dbHost, user=self.dbUser, passwd=self.dbPasswd, db=self.dbnamePb)
        return dbConnection

class INPHINITY_VF_access(DBAccess):
    """
    Classe internet qui retourne une connection pour la base de donnee inphinityDB_2

    :return: objet connection pour la base de donnee inphinityDB_2
    :rtype: mysql connection
    """
    def getConnectionOB(self):
        self.dbHost = "127.0.0.1"
        self.dbUser = "root"
        self.dbPasswd = "Miguel1"
        self.dbnamePb = "inphinityDB_proj"
        dbConnection = pymysql.connect(host=self.dbHost, user=self.dbUser, passwd=self.dbPasswd, db=self.dbnamePb)
        return dbConnection

class INPHINITY_proj_DB(DBAccess):
    """
    Classe internet qui retourne une connection pour la base de donnee inphinityDB_proj

    :return: objet connection pour la base de donnee inphinityDB_proj
    :rtype: mysql connection
    """
    def getConnectionOB(self):
        self.dbHost = "127.0.0.1"
        self.dbUser = "root"
        self.dbPasswd = "Miguel1"
        self.dbnamePb = "inphinityDB_proj"
        dbConnection = pymysql.connect(host=self.dbHost, user=self.dbUser, passwd=self.dbPasswd, db=self.dbnamePb)
        return dbConnection
    


class INPHINITY_proj_DB_out(DBAccess):
    """
    Classe internet qui retourne une connection pour la base de donnee inphinityDB_proj

    :return: objet connection pour la base de donnee inphinityDB_proj
    :rtype: mysql connection
    """
    def getConnectionOB(self):
        self.dbHost = "trex.lan.iict.ch"
        self.dbUser = "root"
        self.dbPasswd = "Miguel1"
        self.dbnamePb = "inphinityDB_proj"
        dbConnection = pymysql.connect(host=self.dbHost, user=self.dbUser, passwd=self.dbPasswd, db=self.dbnamePb)
        return dbConnection


class PFAM_DB_out(DBAccess):
    """
    Classe internet qui retourne une connection pour la base de donnee Pfam

    :return: objet connection pour la base de donnee Pfam
    :rtype: mysql connection
    """
    def getConnectionOB(self):
        self.dbHost = "trex.lan.iict.ch"
        self.dbUser = "root"
        self.dbPasswd = "Miguel1"
        self.dbnamePb = "Pfam"
        dbConnection = pymysql.connect(host=self.dbHost, user=self.dbUser, passwd=self.dbPasswd, db=self.dbnamePb)
        return dbConnection

class DID3_DB_out(DBAccess):
    """
    Classe internet qui retourne une connection pour la base de donnee Pfam

    :return: objet connection pour la base de donnee Pfam
    :rtype: mysql connection
    """
    def getConnectionOB(self):
        self.dbHost = "trex.lan.iict.ch"
        self.dbUser = "root"
        self.dbPasswd = "Miguel1"
        self.dbnamePb = "3did"
        dbConnection = pymysql.connect(host=self.dbHost, user=self.dbUser, passwd=self.dbPasswd, db=self.dbnamePb)
        return dbConnection

class DOMINE_DB_out(DBAccess):
    """
    Classe internet qui retourne une connection pour la base de donnee DOMINE

    :return: objet connection pour la base de donnee Pfam
    :rtype: mysql connection
    """
    def getConnectionOB(self):
        self.dbHost = "trex.lan.iict.ch"
        self.dbUser = "root"
        self.dbPasswd = "Miguel1"
        self.dbnamePb = "DOMINE"
        dbConnection = pymysql.connect(host=self.dbHost, user=self.dbUser, passwd=self.dbPasswd, db=self.dbnamePb)
        return dbConnection

class INPHINITY_std_out(DBAccess):
    """
    Classe internet qui retourne une connection pour la base de donnee inphinityDB_proj only select

    :return: objet connection pour la base de donnee inphinityDB_proj
    :rtype: mysql connection
    """
    def getConnectionOB(self):
        self.dbHost = "trex.lan.iict.ch"
        self.dbUser = "students"
        self.dbPasswd = "Miguel1"
        self.dbnamePb = "inphinityDB_proj"
        dbConnection = pymysql.connect(host=self.dbHost, user=self.dbUser, passwd=self.dbPasswd, db=self.dbnamePb)
        return dbConnection

class INPHINITY_postgres(DBAccess):
    """
    Classe internet qui retourne une connection pour la base de donnee inphinityDB de postgresql

    :return: objet connection pour la base de donnee inphinityDB_proj
    :rtype: mysql connection
    """
    def getConnectionOB(self):
        self.dbHost = "trex.lan.iict.ch"
        self.dbUser = "diogo.leite"
        self.dbPasswd = "diogo."
        self.dbnamePb = "inphinity_db"
        dbConnection = psycopg2.connect(host=self.dbHost, user=self.dbUser, password=self.dbPasswd, dbname=self.dbnamePb)
        return dbConnection
    