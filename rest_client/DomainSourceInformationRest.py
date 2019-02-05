import json
from rest_client.GetRest import GetRest
from rest_client.PostRest import PostRest


class DomainSourceInformationAPI(object):
    """
    This class manage the requests for the Domain sources information (3DID, iPfam,...) objects into the restAPI

    :param function: the name of the function to access in the rest API
    :type function: string
    """

    def __init__(self, function='domainsourceinf/'):
        """
        Initialization of the class

        :param function: name of the function

        :type function: string (url)

        """
        self.function = function

    def get_all(self):
        """
        get all the domains sources information on the database

        :return: json file with all the data
        :rtype: string (json format)
        """
        result_get = GetRest(function = self.function).performRequest()
        return result_get

    def setDomainSOurceInformation(self, jsonData):
        """
        set new domain source information in the database

        :return: json file with the last domain source information created
        :rtype: string (json format)
        """
        jsonData = json.dumps(jsonData)
        result_post = PostRest(function = self.function, dataDict = jsonData).performRequest()
        return result_post