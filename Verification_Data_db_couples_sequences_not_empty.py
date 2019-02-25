from configuration.configuration_api import ConfigurationAPI
from rest_client.AuthenticationRest import AuthenticationAPI



from objects_API.CoupleJ import CoupleJson
from objects_API.ProteinJ import ProteinJson
from objects_API.WholeDNAJ import WholeDNAJson
from objects_API.ContigJ import ContigJson



def getAllCouples():
    list_couple = CoupleJson.getAllAPI()
    return list_couple


def getProteinsListByOrganismId(organism_id:int):
    list_proteins = ProteinJson.getByOrganismID(organism_id)
    return list_proteins

def getWholeGenomeByOrganismId(organism_id:int):
    whole_dna_obj = WholeDNAJson.getByOrganismID(organism_id)
    return whole_dna_obj


def getContigsByOrganismId(organism_id:int):
    list_contig = ContigJson.getByOrganismID(organism_id)
    return list_contig


conf_obj = ConfigurationAPI()
conf_obj.load_data_from_ini()
AuthenticationAPI().createAutenthicationToken()

list_ids_bacteria = []
list_ids_phage = []

list_couples = getAllCouples()
list_ids_bacteria = [couple_obj.bacterium for couple_obj in list_couples]
list_ids_bacteria = list(set(list_ids_bacteria))

list_ids_phage = [couple_obj.bacteriophage for couple_obj in list_couples]
list_ids_phage = list(set(list_ids_phage))

bacterium_id = list_ids_bacteria[0]

list_proteins = getProteinsListByOrganismId(bacterium_id)
whole_dna_obj = getWholeGenomeByOrganismId(bacterium_id)
list_contigs = getContigsByOrganismId(bacterium_id)



print('Hello')