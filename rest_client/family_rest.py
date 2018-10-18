import json

from decorest import DELETE, GET, POST, PUT
from decorest import HttpStatus, RestClient
from decorest import accept, body, content, endpoint, header, on, query


@header('user-agent', 'decorest/0.0.2')
@content('application/json')
@accept('application/json')
@endpoint('http://trex.lan.iict.ch:8080/api/family/')

class FamilyAPI(RestClient):
    
    def __init__(self, endpoint=None):
        """Construct FamilyAPI."""
        super(FamilyAPI, self).__init__(endpoint)

    @GET('family/')
    def get_all(self):
        return self.a
