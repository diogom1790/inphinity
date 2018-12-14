from marshmallow import Schema, fields, post_load

from rest_client.CoupleRest import CoupleAPI


class CoupleSchema(Schema):
    """
    This class map the json into the object Family

    ..note:: see marshmallow API
    """

    id = fields.Int()
    interaction_type = fields.Int()
    bacteriophage_id = fields.Int()
    bacterium_id = fields.Int()
    level_id = fields.Int()
    lysis_id = fields.Int()
    person_responsible_id = fields.Int()
    source_data_id = fields.Int()
    validity_id = fields.Int()

    @post_load
    def make_Couple(self, data):
        return CoupleJson(**data)

class CoupleJson(object):
    """
    This class manage the object and is used to map them into json format
    """
    def __init__(self, id:int = None, interaction_type:int = None, bacteriophage_id:int = None, bacterium_id:int = None, level_id:int = None, lysis_id:int = None, person_responsible_id:int = None, source_data_id:int = None, validity_id:int = None):

        """
        Initialization of the class

        :param id: id of the couple
        :param interaction_type: type of the interaction (between 0 and 4)
        :param bacteriophage_id: ID of the bacteriophage
        :param bacterium_id: ID of the bacterium
        :param level_id: level of the interaction (in terms of taxonomy)
        :param person_responsible_id: ID of the person who has inserted the couple
        :param source_data_id: ID of the source where you know the couple
        :param validity_id: ID of the couple validity (verified, in vivo, generated,...)

        :type id: int
        :type interaction_type: int 
        :type bacteriophage_id: int
        :type bacterium_id: int
        :type level_id: int
        :type person_responsible_id: int
        :type source_data_id: int
        :type validity_id: int

        """
        self.id = id
        self.interaction_type = interaction_type
        self.bacteriophage_id = bacteriophage_id 
        self.bacterium_id = bactbacterium_id
        self.level_id = level_id
        self.lysis_id = lysis_id
        self.person_responsible_id = person_responsible_id
        self.source_data_id = source_data_id
        self.validity_id = validity_id