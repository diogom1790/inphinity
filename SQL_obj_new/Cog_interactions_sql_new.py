# -*- coding: utf-8 -*-
"""
Created on Tue Jan 9 09:17:59 2017

@author: Diogo
"""

from DAL import *
from configuration.configuration_data import *

class _Cog_Interaction_Score_sql_new(object):
    """
    This class manipulate the COG_INTERACTIONS table in the database

    The FK are manipulated in the lasts positions of the parameters
    """

    def __init__(self):
        """
        Constructor of the Cong_interactions object. All the parameters have a default value

        :param db_name: name of the database to do the ACID methods

        :type db_name: string - no required
        """

        self.db_name = self.get_database_name()

    def get_database_name(self):
        """
        This method is used to get the database name used in factory

        :return: database name
        :rtype string
        """
        conf_data_obj = Configuration_data('INPHINITY')
        db_name = conf_data_obj.get_database_name()
        return db_name

    def select_all_cog_scores(self):
        """
        return all the COG scores in the database

        :return: cursor with all COG score
        :rtype Cursor list
        """

        sql_string = "SELECT id_cog_score_CI, Group1_CI, Group2_CI, Score_CI FROM COG_INTERACTION"

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_cog_scores_with_limit(self, start_index, quantity_registers):
        """
        return all the COG scores in the database

        :return: cursor with all COG score
        :rtype Cursor list
        """

        sql_string = "SELECT id_cog_score_CI, Group1_CI, Group2_CI, Score_CI FROM COG_INTERACTION LIMIT " + str(quantity_registers) + " OFFSET " + str(start_index)

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def select_all_cog_by_groups(self, group_id):
        """
        return all the COG scores in the database

        :param group_id: group id to get the designations (1 or 2)

        :type group_id: int - no required

        :return: cursor with all cog designation distinct
        :rtype Cursor list
        """
        sql_string = ''
        if group_id == 1:
            sql_string = "SELECT DISTINCT Group1_CI FROM COG_INTERACTION"
        elif group_id == 2:
            sql_string = "SELECT DISTINCT Group1_CI FROM COG_INTERACTION"
        else:
            print('The group {0} is not valid'.format(group_id))

        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()
        return results

    def create_cog_score_verification(self, grp_a, grp_b, score_cog):
        """
        Insert a Cog score and return its id if it isn't exist another cog score with the two groups

        :param grp_a: value of the interaction (1 - positive; 0 - negative)
        :param grp_b: id of the bacterium
        :param score_cog: id of the phage

        :type grp_a: string - required 
        :type grp_b: string - required 
        :type score_cog: int - required 

        :return: id of the COG score inserted
        :rtype int
        """
        id_value_COG_score = self.get_id_cog_score_by_grpa_grpb(grp_a, grp_b)
        if id_value_COG_score == -1:
            sql_string = "INSERT INTO COG_INTERACTION (Group1_CI, Group2_CI, Score_CI) VALUES (%s, %s, %s)"
            dalObj = DAL(self.db_name, sql_string)
            params = [grp_a, grp_b, score_cog]
            dalObj.sqlcommand = sql_string
            dalObj.parameters = params
            results = dalObj.executeInsert()
            return results.lastrowid
        else:
            print("Its already exists a Cog Scor with these groups")
            return id_value_COG_score

       

    def get_id_cog_score_by_grpa_grpb(self, grp_a, grp_b):
        """
        get the id of a cog score based on these groups (A and B)

        :param grp_a: designation of the group A
        :param grp_b: designation of the group B

        :type grp_a: string - required 
        :type grp_b: string - required 

        :return: id of the cog socre or -1 if inexistant
        :rtype int
        """

        sql_string = "SELECT id_cog_score_CI FROM COG_INTERACTION WHERE Group1_CI = '" + str(grp_a) + "' and Group2_CI = '" + str(grp_b) + "'"
        dalObj = DAL(self.db_name, sql_string)
        results = dalObj.executeSelect()

        if len(results) is 0:
            return -1
        else:
            return results[0][0]
