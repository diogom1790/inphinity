import glob
import os 


class ImportFilesPatric(object):
    """

    This class manipulate the files of the organisms extract from patric. This is prepared for extract the xls and contig fasta files

    """
    def __init__(self, path_directory, contig_extension, excel_extension):
        """
        Initialization of the class

        :param path_directory: directory that you want to extract the files
        :param contig_extension: extension of the contigs fasta files
        :param excel_extension: extension of the excel files

        :type function: string
        :type contig_extension: string
        :type excel_extension: string

        """

        self.path_directory = path_directory
        self.contig_extension = contig_extension
        self.excel_extension = excel_extension



    def completeDictAllFilesPaths(self, dict_organism_names, list_contigs_files, list_xls_files, extension_contig, extension_xls):
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

    def parseFilesNamesIntoDictionary(self, list_files):
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

    def getListFiles(self, path):
        """
        get all the files in a given directory

        :param path: Path where you want to find the files

        :type path: string - required

        :return: list with all the files
        :rtype: List(string)
        """
        list_files = glob.glob(path)
        return list_files

    def getContigsXlsFiles(self, path_files):
        """
        get all contigs and excel proteins files in a given path

        :param path_files: Path where you want to find the files

        :type path_files: string - required

        :return: two lists with all the files found
        :rtype: List(string), List(string)
        """


        path_extention_xls = path_files + '*' + self.excel_extension
        path_extention_contigs = path_files + '*' +  self.contig_extension


        list_xls_files = self.getListFiles(path_extention_xls)
        list_contigs_files = self.getListFiles(path_extention_contigs)
        assert len(list_xls_files) == len(list_contigs_files)

        return list_xls_files, list_contigs_files

    def getOrganismsFiles(self):
        """
        return a dictionary where the key correspond to the organisms names and the values to an array with the paths of the sequence files

        :return: dictionary with all the file path for each organism
        :rtype: dict{String: [String]}
        """

        list_xls_files, list_contigs_files = self.getContigsXlsFiles(self.path_directory)

        dict_bacterium_name_empty = self.parseFilesNamesIntoDictionary(list_xls_files)
        dict_bacterium_name = self.completeDictAllFilesPaths(dict_bacterium_name_empty, list_contigs_files, list_xls_files, self.contig_extension, self.excel_extension)
        return dict_bacterium_name
