import json
from rest_client.GetRest import GetRest
from rest_client.PostRest import PostRest

class BacteriumAPI(object):
    """
    This class manage the requests for the Bacteria objects into the restAPI

    :param function: the name of the function to access in the rest API
    :type function: string
    """

    def __init__(self, function='bacterium/'):
        """
        Initialization of the class

        :param function: name of the function

        :type function: string (url)

        """
        self.function = function

    def get_all(self):
        """
        get all the Bacteria on the database

        :return: json file with all the data
        :rtype: string (json format)
        """
        result_get = GetRest(function = self.function).performRequest()
        return result_get

    def set_bacterium(self, jsonData):
        """
        set new bacterium in the database

        :return: json file with the last bacterium created
        :rtype: string (json format)
        """
        jsonData = json.dumps(jsonData)
        result_post = PostRest(function = self.function, dataDict = jsonData).performRequest()
        return result_post

    def setBacteriumExistsByAcc(self, acc_value):
        """
        Verify if a bacterium exists according an accValue

        :param acc_value: accession number of the bacterium that you want to check the existence

        :type acc_value: string

        :return: json file with all the data
        :rtype: string (json format)
        """

        self.function += 'accnumber/' + acc_value + '/exists/'

        result_get = GetRest(function = self.function).performRequest()
        return result_get