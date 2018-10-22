from marshmallow import Schema, fields, post_load

from rest_client.FamilyRest import FamilyAPI


class FamilySchema(Schema):
    id = fields.Int()
    designation = fields.Str()
    genuses = fields.List(fields.Url)

    @post_load
    def make_Family(self, data):
        return FamilyJson(**data)

class FamilyJson(object):


    def __init__(self, id = None, designation = '', genuses=()):
        self.id = id
        self.designation = designation
        self.genuses = genuses

    def __str__(self):
        return 'id: {0} designation {1}'.format(self.id, self.designation)



    def getAllAPI(self):
        list_family = FamilyAPI().get_all()
        schema = FamilySchema()
        results = schema.load(list_family, many=True)

        return results[0]