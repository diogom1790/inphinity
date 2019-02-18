import json
from rest_client.GetRest import GetRest
from rest_client.PostRest import PostRest

class StrainAPI(object):
    """
    This class manage the requests for the strain objects into the restAPI

    :param function: the name of the function to access in the rest API
    :type function: string
    """

    def __init__(self, function='strain/'):
        """
        Initialization of the class

        :param function: name of the function

        :type function: string (url)

        """
        self.function = function

    def get_all(self):
        """
        get all the strains on the database

        :return: json file with all the data
        :rtype: string (json format)
        """
        result_get = GetRest(function = self.function).performRequest()
        return result_get

    def set_strain(self, jsonData):
        """
        set new strain in the database

        :return: json file with the last strain created
        :rtype: string (json format)
        """
        jsonData = json.dumps(jsonData)
        result_post = PostRest(function = self.function, dataDict = jsonData).performRequest()
        return result_post

    def get_by_id(self, id_strain:int):
        """
        get a strain given it id

        :param id_strain: id of the strain

        :type id_strain: int

        :return: json file with all the data
        :rtype: string (json format)
        """

        self.function += str(id_strain) + '/'

        result_get = GetRest(function = self.function).performRequest()
        return result_get

    def getByDesignationFkSpecie(self, designation, fk_specie):
        """
        Verify if a strain already exists in the database given a designation and fk_specie

        :param designation: designation of the strain
        :param fk_specie: fk of the specie

        :type designation: string
        :type fk_specie: integer

        :return: json file with all the data
        :rtype: string (json format)
        """

        self.function += 'existdesignstrain/' + designation + '/' + str(fk_specie) + '/'

        result_get = GetRest(function = self.function).performRequest()
        return result_get