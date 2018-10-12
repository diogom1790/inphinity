
import pymysql

import sys
sys.path.insert(0, '..')

from factory_databases_access import *

class DAL(object):
    """
    Cette classe s occupe de tout le processus de connection et deconnection de la base de donnees
    c est egalement ici que sont faites toutes les requetes a la db (INSERT, SELECT, UPDATE, call procedures)
    """
    def __init__(self, db_name, sql_command, parameters = []):
        """
        Contructeur de l objet proteine. Tous les parametres ont une valeure par default

        :param db_name: nom de la base de donnee
        :param sql_command: numero d acsession
        :param parameters: parametres (string, int, ... en accord avec l UPDATE ou INSERT)

        :type db_name: string - obligatoir
        :type sql_command: string - obligatoir
        :type parameters: text - non obligatoir (pour INSERT et UPDATE oui)

        """
        self.db_name = db_name
        self.sqlcommand = sql_command
        self.connectionObject = ""
        self.parameters = parameters

    def connectionOpen(self):
        """
        Creer l objet de connection a la base de donnee. Utilise le pattern Factory pour ca
        Puia ouvre la connection a la base de donnees
        Pour add d autre DB il faut modifier la classe factory_databases_access.py

        """
        factoryDB = DBAccess()
        self.connectionObject = factoryDB.factory(self.db_name).getConnectionOB()

    def connectionClose(self):
        """
        Ferme la connection a la base de donnees

        """
        self.connectionObject.close()

    def executeSelect(self):
        """
        Methode utilisee pour lancer un SELECT
        s occupe d ouvrir et fermer la connection


        :return: les valeures selectionnes
        :rtype: curseur avec les resultats

        """

        self.connectionOpen()
        cursor = self.connectionObject.cursor()
        cursor.execute(self.sqlcommand)
        values = cursor.fetchall()
        self.connectionClose()
        return values

    def executeInsert(self):
        """
        Methode utilisee pour lancer un INSERT et UPDATE
        s occupe d ouvrir et fermer la connection

        :return: description de la valeur de retour (normalement un id)
        :rtype: type de la valeur de retour
        """

        self.connectionOpen()
        cursor = self.connectionObject.cursor()
        try:
            cursor.execute(self.sqlcommand, self.parameters)
            self.connectionObject.commit()
            self.connectionClose()
        except TypeError as e:
            self.connectionObject.rollback()
            print("Error during the insertion")
            print(e)
            self.connectionClose()
        return cursor

    def executeDelete(self):
        """
        Methode utilisee pour lancer un DELETE
        s occupe d ouvrir et fermer la connection

        :return: description de la valeur de retour (normalement un id)
        :rtype: type de la valeur de retour
        """

        self.connectionOpen()
        cursor = self.connectionObject.cursor()
        try:
            cursor.execute(self.sqlcommand, self.parameters)
            self.connectionObject.commit()
            self.connectionClose()
        except TypeError as e:
            self.connectionObject.rollback()
            print("Error during the deletion")
            print(e)
            self.connectionClose()
        return cursor

    def call_procedure(self):
        """
        Method used to call procedures (with arguments)

        :return: the results of the procedure
        :rtype: results.fetchall()
        """
        try:
            self.connectionOpen()
            cursor = self.connectionObject.cursor()
            cursor.callproc(self.sqlcommand, self.parameters)
            return cursor
        except Error as e:
            print(e)
        finally:
            self.connectionClose()
            result = cursor.stored_results()
            cursor.close()
            return result
