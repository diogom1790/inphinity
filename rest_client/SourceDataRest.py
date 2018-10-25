import json
from rest_client.GetRest import GetRest
from rest_client.PostRest import PostRest

class SourceDataAPI(object):
    """
    This class manage the requests for the SourceData objects into the restAPI

    :param function: the name of the function to access in the rest API
    :type function: string
    """

    def __init__(self, function='sourcedata/'):
        """
        Initialization of the class

        :param function: name of the function

        :type function: string (url)

        """
        self.function = function

    def get_all(self):
        """
        get all the source data on the database

        :return: json file with all the data
        :rtype: string (json format)
        """
        result_get = GetRest(function = self.function).performRequest()
        return result_get

    def set_sourceData(self, jsonData):
        """
        set new source data in the database

        :return: json file with the last source data created
        :rtype: string (json format)
        """
        jsonData = json.dumps(jsonData)
        result_post = PostRest(function = self.function, dataDict = jsonData).performRequest()
        return result_post