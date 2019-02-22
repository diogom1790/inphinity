import json
from rest_client.GetRest import GetRest
from rest_client.PostRest import PostRest


class SpecieAPI(object):

    """
    This class manage the requests for the specie objects into the restAPI

    :param function: the name of the function to access in the rest API
    :type function: string
    """

    def __init__(self, function='specie/'):
        """
        Initialization of the class

        :param function: name of the function

        :type function: string (url)

        """
        self.function = function

    def get_all(self):
        """
        get all the species on the database

        :return: json file with all the data
        :rtype: string (json format)
        """
        result_get = GetRest(function = self.function).performRequest()
        return result_get

    def set_specie(self, jsonData):
        """
        set new specie in the database

        :return: json file with the last specie created
        :rtype: string (json format)
        """
        jsonData = json.dumps(jsonData)
        result_post = PostRest(function = self.function, dataDict = jsonData).performRequest()
        return result_post

    def get_by_id(self, id_specie:int):
        """
        get a specie given it id

        :param id_specie: id of the specie

        :type id_specie: int

        :return: json file with all the data
        :rtype: string (json format)
        """

        self.function += str(id_specie) + '/'

        result_get = GetRest(function = self.function).performRequest()
        return result_get