from marshmallow import Schema, fields, post_load

from objects_API.PersonResponsibleJ import PersonResponsibleSchema
from objects_API.SourceDataJ import SourceDataSchema

class OrganismSchema(Schema):
    """
    This class map the json into the object Organism

    ..note:: see marshmallow API
    """
    #id = fields.Int()
    acc_number = fields.Str()
    gi_number = fields.Str(required=False, allow_none=True)
    source_data = fields.Int()
    person_responsible = fields.Int()
    organism_gene = fields.List(fields.Url())
    organism_contig = fields.List(fields.Url())
    organism_wholeDNA = fields.List(fields.Url())
    protein_organism = fields.List(fields.Url())

    #@post_load
    #def make_OrganismSchema(self, data):
    #    return OrganismSchema(**data)

class OrganismJson(object):
    """
    This class manage the object and is used to map them into json format
    """

    def __init__(self, acc_number = None, gi_number= None,  person_responsible = None, source_data = None, organism_gene = None, organism_contig = None, organism_wholeDNA = None, protein_organism = None):
        """
        Initialization of the class

        :param id: name of the function
        :param acc_number: id of the database where the dna comes
        :param gi_number: DNA sequence
        :param source_data: head of the fasta from where the DNA was extracted
        :param person_responsible: id of the organism
        :param organism_gene: id of the organism
        :param organism_contig: id of the organism
        :param organism_wholeDNA: id of the organism
        :param protein_organism: id of the organism

        :type id: int
        :type acc_number: string 
        :type gi_number: string
        :type source_data: string
        :type person_responsible: int
        :type organism_gene: int
        :type organism_contig: int
        :type organism_wholeDNA: int
        :type protein_organism: int


        """
        self.id = id
        self.acc_number = acc_number
        self.gi_number = gi_number
        self.source_data = source_data
        self.person_responsible = person_responsible
        self.organism_gene = organism_gene
        self.organism_contig = organism_contig
        self.organism_wholeDNA = organism_wholeDNA
        self.protein_organism = protein_organism

    def __str__(self):
        """
        override the Str function 

        """
        return 'id: {0} acc number head {1}'.format(self.id, self.acc_number)