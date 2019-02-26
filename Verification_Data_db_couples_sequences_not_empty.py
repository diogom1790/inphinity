from configuration.configuration_api import ConfigurationAPI
from rest_client.AuthenticationRest import AuthenticationAPI



from objects_API.CoupleJ import CoupleJson
from objects_API.ProteinJ import ProteinJson
from objects_API.WholeDNAJ import WholeDNAJson
from objects_API.ContigJ import ContigJson



def checkSequenceProteins(list_proteins:ProteinJson):
    """
    check if the sequence exists for a protein given a list of them

    :param list_proteins: list of the proteins

    :type id: array[ProteinJ]

    :return: dictionary with the ids and sequences if they are to short or inexistent
    :rtype: dict[id_prot]:sequence
    """
    dict_proteins_error = {}
    for protein in list_proteins:
        if len(protein.sequence_AA) < 15:
            print('error')
            id_prot = protein.id
            sequence_prot = protein.sequence_AA
            dict_proteins_error[id_prot] = sequence_prot

    return dict_proteins_error

def checkWholeDna(whole_dna):
    """
    check if the sequence exists for a whwhole_dna

    :return: dictionary with the id and sequences if they are to short or inexistent
    :rtype: dict[id_whole_dna]:sequence
    """
    dict_whole_dna_error = {}
    if len(whole_dna.sequence_DNA) < 1000:
        dict_whole_dna_error[whole_dna.id] = whole_dna.sequence_DNA
    return dict_whole_dna_error

def checkSequenceContigs(list_contigs):
    """
    check if the sequence exists for a contig given a list of them

    :return: dictionary with the ids and sequences if they are to short or inexistent
    :rtype: dict[id_contig]:sequence
    """
    dict_contigs_error = {}
    for contig in list_contigs:
        if len(contig.sequence_DNA) < 15:
            print('error')
            id_contig = contig.id
            contig_sequence = contig.sequence_DNA
            dict_contigs_error[id_contig] = contig_sequence

    return dict_contigs_error

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
print('Hello')