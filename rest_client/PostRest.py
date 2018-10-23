import requests
import os

class PostRest(object):

    """
    This class manage the post requests

    :param function: url of the function in the API
    :type function: string

    """

    def __init__(self, function, dataDict, includeHeaders = True):
        """
        Initialization of the class

        :param url_base: receive the endpoint of the function
        :param function: receive the extension of the API url to access at the function on the server
        :param headers: the header of the request
        :param data: data that you want to post
        :param includeHeaders: inform if it is necessary to send a header

        :type url_base: string (url)
        :type function: string
        :type headers: string
        :type data: string (json)
        :type includeHeaders: bool

        """
        self.url_base = ''
        self.function = function
        self.headers = None
        self.data = dataDict
        self.includeHeaders = includeHeaders

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
            print('Creation of new token')
        elif error == 403:
            print('Login data is not vaild')
        else:
            print('Error number %d', error)

    def performRequest(self):
        """
        Create a post request on the API

        :return: the json with the content
        """
        if self.includeHeaders == True:
            self.get_header()
        self.get_url_base()
        url_post = self.url_base + self.function
        result_request = requests.post(url_post, headers=self.headers, data=self.data)
        if result_request.status_code == 200 or result_request.status_code == 201 :
            return result_request.json()
        else:
            print(result_request.json())
            self.get_new_authorization(result_request.status_code)

