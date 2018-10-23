import requests
import os

class GetRest(object):

    """
    This class manage the get requests

    :param function: url of the function in the API
    :type function: string

    """

    def __init__(self, function):

        """
        Initialization of the class

        :param url_base: receive the endpoint of the function
        :param function: receive the extension of the API url to access at the function on the server
        :param headers: the header of the request

        :type url_base: string (url)
        :type function: string
        :type headers: string

        """
        self.url_base = ''
        self.function = function
        self.headers = None

    def get_header(self):
        """
        Initialize the header parameter getting the token from a environment variable

        """
        self.headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + os.environ['token_api']}
    
    def get_url_base(self):
        """
        Initialize the header parameter getting the endpoint from a environment variable

        """
        self.url_base = os.environ['endpoint_api']

    def get_new_authorization(self, error):
        """
        Treat the exception

        .. todo:: implement their treatment
        """
        if error == 401:
            print('Need to create a new token')
        elif error == 403:
            print('Login data is not valid')
        else:
            print('Error number %d', error)

    def performRequest(self):
        """
        Create a get request on the API

        :return: the json with the content
        """
        self.get_header()
        self.get_url_base()
        url_get = self.url_base + self.function
        result_request = requests.get(url_get, headers=self.headers)
        if result_request.status_code == 200:
            return result_request.json()
        else:
            self.get_new_authorization(result_request.status_code)
