from marshmallow import Schema, fields, post_load
import datetime


from rest_client.DomainInteractionSourceRest import DomainInteractionSourceAPI

class DomainInteractionSourceSchema(Schema):
    """
    This class map the json into the object Domain Interaction Source

    ..note:: see marshmallow API
    """
    id = fields.Int()
    date_creation = fields.Date()
    domain_interaction = fields.Int()
    information_source = fields.Int()

    @post_load
    def make_DomainInteractionSource(self, data):
        return DomainInteractionSourceJson(**data)

class DomainInteractionSourceJson(object):
    """
    This class manage the object and is used to map them into json format
    """

    def __init__(self,  date_creation:datetime, domain_interaction:int, information_source:int, id = None):
        """
        Initialization of the class

        :param id: name of the function
        :param date_creation: domain interaction source creation date
        :param domain_interaction_id: id of the domain interaction
        :param information_source_id: id of the information source

        :type id: int
        :type date_creation: date 
        :type domain_interaction_id: int 
        :type information_source_id: int 

        """
        self.id = id
        self.date_creation = date_creation
        self.domain_interaction = domain_interaction
        self.information_source = information_source

    def getAllAPI():

        """
        get all the domain interaction source on the database

        :return: list of Domain interaction source
        :rtype: vector[DomainInteractionSourceJson]
        """
        list_domain_interaction_source = DomainInteractionSourceAPI().get_all()
        schema = DomainInteractionSourceSchema()
        results = schema.load(list_domain_interaction_source, many=True)
        return results[0]

    def setDomainInteractionSource(self):
        """
        set new domain interaction source

        :return: new domain interaction source completed with the id
        :rtype: DomainJ
        """
        schema = DomainInteractionSourceSchema(only=['date_creation','domain_interaction','information_source'])
        json_domain = schema.dump(self)
        resultsCreation = DomainInteractionSourceAPI().setDomainInteractionSource(jsonData = json_domain.data)
        schema = DomainInteractionSourceSchema()
        results = schema.load(resultsCreation)
        return results[0]

    def __str__(self):
        """
        override the Str function 

        """
        return 'id: {0} creation date {1} interaction domain id {2} source id {3}'.format(self.id, self.date_creation, self.domain_interaction, self.information_source)