from marshmallow import Schema, fields

"""
Created on Wed Oct 17 10:100446 2018

@author: Diogo Leite
"""

class FamilySchema(Schema):
    id = fields.Integer(attribute='id_family')
    designation = fields.Str(required=True, attribute='designation')
