import glob
import os 


dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

def completeDictAllFilesPaths(dict_organism_names, list_contigs_files, list_xls_files, extension_contig, extension_xls):
    """
    given a list of files path, parse them and insert into a dictionary of arrays

    :param dict_organism_names: dictionary with the files names as key and empty array as values
    :param list_contigs_files: list with all the contigs path files
    :param list_xls_files: list with all the excel path files
    :param extension_contig: contig file extension 
    :param extension_xls: excel file extension 

    :type dict_organism_names: dictionary{String:[]} - required
    :type list_contigs_files: List(String) - required
    :type list_xls_files: List(String) - required
    :type extension_contig: String - required
    :type extension_xls: String - required

    :return: COmpleted dictionary with all the files path for excel and contigs
    :rtype: dictionary {String: [String, String]}
    """

    for key, value in dict_organism_names.items():
        complete_file_name_contig = key + extension_contig
        complete_file_name_xls = key + extension_xls

        indice_contig = [i for i, elem in enumerate(list_contigs_files) if complete_file_name_contig in elem]
        indice_xls = [i for i, elem in enumerate(list_xls_files) if complete_file_name_xls in elem]
        
        assert len(indice_contig) == 1 and len(indice_xls) == 1

        dict_organism_names[key] = [list_contigs_files[indice_contig[0]], list_xls_files[indice_xls[0]]]
    return dict_organism_names

def parseFilesNamesIntoDictionary(list_files):
    """
    given a list of files path, parse them and insert into a dictionary of arrays

    :param list_files: List with all the path files

    :type list_files: List(String) - required

    :return: dictionary with the files name as key and empty array as value
    :rtype: dictionary {String: [empty]}
    """
    dict_files = {}
    for file_complete_path in list_files:

        assert file_complete_path.count('.') == 1

        base_file = base=os.path.basename(file_complete_path)
        file_name = os.path.splitext(base_file)[0]
        dict_files[file_name] = []
    return dict_files

def getListFiles(path):
    """
    get all the files in a given directory

    :param path: Path where you want to find the files

    :type path: string - required

    :return: list with all the files
    :rtype: List(string)
    """
    list_files = glob.glob(path)
    return list_files

def getContigsXlsFiles(path_files):
    """
    get all contigs and excel proteins files in a given path

    :param path_files: Path where you want to find the files

    :type path_files: string - required

    :return: two lists with all the files found
    :rtype: List(string), List(string)
    """


    path_extention_xls = path_files + '*.xls'
    path_extention_contigs = path_files + '*.contigs.fasta'

    list_xls_files = getListFiles(path_extention_xls)
    list_contigs_files = getListFiles(path_extention_contigs)
    assert len(list_xls_files) == len(list_contigs_files)


    return list_contigs_files, list_xls_files

    print('Hello')


    print(file_name)

path = dir_path + '/organisms/'
print(path)

list_contigs_files, list_xls_files = getContigsXlsFiles(path)


dict_bacterium_name = parseFilesNamesIntoDictionary(list_xls_files)
dict_bacterium_name = completeDictAllFilesPaths(dict_bacterium_name, list_contigs_files, list_xls_files, '.contigs.fasta', '.xls')

list_files = getListFiles(path)
print(list_files)