import glob
import os 

from files_treatment_new.xls_gen_bank_patric import XlsGenBankPatric
from files_treatment_new.fasta_contigs_patric import FastaContigsPatric

from objects_new.Contigs_new import Contig

from objects_API.ContigJ import ContigJson

from Patric.ImportFiles import ImportFilesPatric


def createContig(contigObj, organismID):
    """
    insert a Contig into a REST API

    :param contigObj: Contig DBA object that you want to insert
    :param organismID: ID of the organism which has this wholeDNA
    :param listProtein: List of the proteins of the contig

    :type contigObj: WholeDNA
    :type organismID: int
    :type listProtein: List[int]

    :return: id of the Contig inserted
    :rtype int
    """
    contigObjJson = ContigJson(id_db_online = contigObj.id_contig_db_outside, sequence_DNA= contigObj.sequence, fasta_head = contigObj.head, organism = organismID)
    contigObjJson = contigObjJson.setContig()
    return contigObjJson.id

def createContigNew(contigObj, bacteriumId):
    head_cnt = ''
    if '>' not in contigObj.head:
        head_cnt = '>' + contigObj.head
    else: 
        head_cnt = contigObj.head

    contigObj = Contig(id_contig_db_outside = contigObj.id_contig_db_outside, head = head_cnt, sequence = contigObj.sequence)
    idContig = createContig(contigObj, bacteriumId)
    return idContig

def createAndInsertElements(contig_obj):
    #listProts = xls_genbank_patric_obj.get_proteins_information_in_excel()
    list_proteins = xls_genbank_patric_obj.get_proteins_objects_by_contig_id(contig_obj.head)
    list_proteins_ids = xls_genbank_patric_obj.get_proteins_ids_by_contig_id(contig_obj.head)

    createContigNew(contig_old, 456796)

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

path = dir_path + '/Patric/organisms/'
print(path)

import_files_obj = ImportFilesPatric(path, '.contigs.fasta','.xls')
dict_files = import_files_obj.getOrganismsFiles()

for key, values in dict_files.items():
    contig_path_file = values[0]
    excel_path_file = values[1]

    xls_genbank_patric_obj = XlsGenBankPatric(path_file= excel_path_file, sheet_name = 'Features in Acinetobacter bauma')
    contig_fasta_file_patric_obj = FastaContigsPatric(path_file = contig_path_file)

    list_contigs_ids_fasta = contig_fasta_file_patric_obj.get_list_contigs_id()

    list_contigs_ids_xls = xls_genbank_patric_obj.get_contigs_id_sorted()

    assert len(list_contigs_ids_fasta) == len(list_contigs_ids_xls)

    list_of_contigs = contig_fasta_file_patric_obj.create_contigs_from_file()

    for contig_old in list_of_contigs:
        createAndInsertElements(contig_old)
        


    #### Test old methods
    for contig_id in list_contigs_ids_fasta:
        print(contig_id)
        list_proteins = xls_genbank_patric_obj.get_proteins_objects_by_contig_id(contig_id)
print('fini')