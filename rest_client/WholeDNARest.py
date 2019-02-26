import json
from rest_client.GetRest import GetRest
from rest_client.PostRest import PostRest

class WholeDNAAPI(object):
    """
    This class manage the requests for the WholeDNAs objects into the restAPI

    :param function: the name of the function to access in the rest API
    :type function: string
    """

    def __init__(self, function='wholedna/'):
        """
        Initialization of the class

        :param function: name of the function

        :type function: string (url)

        """
        self.function = function

    def get_all(self):
        """
        get all the WholeDNAs on the database

        :return: json file with all the data
        :rtype: string (json format)
        """
        result_get = GetRest(function = self.function).performRequest()
        return result_get

    def set_wholeDNA(self, jsonData):
        """
        set new wholeDNA in the database

        :return: json file with the last wholeDNA created
        :rtype: string (json format)
        """
        jsonData = json.dumps(jsonData)
        result_post = PostRest(function = self.function, dataDict = jsonData).performRequest()
        return result_post

    def getByOrganismID(self, organism_id):
        """
        get the whole_dna of a given organism

        :param organism_id: organism ID

        :type organism_id: int

        :return: whole_dna of the given organism id
        :rtype: ProteinJson
        """

        self.function += 'organism_id/' + str(organism_id)

        result_get = GetRest(function = self.function).performRequest()
        return result_get