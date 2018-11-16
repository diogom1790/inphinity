from robobrowser import RoboBrowser
import os, time
import pandas as pd
import numpy as np
import multiprocessing as mp
import numpy

def read_CSV(pathCSV):
    dataframCSV = pd.read_csv(pathCSV, converters={'organismIDRAST': str})
    return dataframCSV

def confirmExistanceFile(pathName, idOrganism, extentionName):
    existance =os.path.isfile(pathName + idOrganism + extentionName)
    return existance

def downloadFile(jobId, idOrganism, pathFile, extentionFile, outputValue):
    try:
        resultExistance = confirmExistanceFile(pathFile, idOrganism, extentionFile)
        if resultExistance == False:
            browser = RoboBrowser()
            login_url = 'http://rast.nmpdr.org/rast.cgi'
            browser.open(login_url)
            form = browser.get_form(id='login_form')
            form['login'].value = 'gresch' 
            form['password'].value = 'sequencing'
            browser.submit_form(form)

            browser.open('http://rast.nmpdr.org/rast.cgi?page=JobDetails&job='+ str(jobId))
            form = browser.get_form(id='download')
            #try:#Sometimes it didn't work then it did, I don't know why
            form['file'].value = str(idOrganism) + extentionFile
            submit_field = form['do_download']
            submit_field.value = 'Authorize'
            browser.submit_form(form,submit=submit_field)
            f=open(pathFile + str(idOrganism) + extentionFile,"wb")
            f.write(browser.response.content)
            f.close()
            outputValue.put('-1')
    except:
        retults = extentionFile
        outputValue.put(retults)

def writeFilesSaved(arrayResults, idOrganism):
    arrayResults.insert(0, idOrganism)
    f=open('filesDownloaded.csv','a')
    numpy.savetxt(f, arrayResults, delimiter="," , fmt="%s", newline=" ")
    f.write('\n')
    f.close()

def openBrowser(jobId, idOrganism):
    outputValue = mp.Queue()
    filesExtention = ['.faa','.fna','.xls','.contigs.fa']
    pathToSave =['Fasta_AA/','Fasta/','Xls/','Contig/']
    qtyFiles = len(filesExtention)

    processes = [mp.Process(target=downloadFile, args=(jobId, idOrganism, pathToSave[x], filesExtention[x], outputValue)) for x in range(4)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = [outputValue.get() for p in processes]
    print(results)
    
    writeFilesSaved(results, idOrganism)


    #resultExistance = confirmExistanceFile(pathToSave[0], idOrganism, filesExtention[0])



    #browser = RoboBrowser()
    #login_url = 'http://rast.nmpdr.org/rast.cgi'
    #browser.open(login_url)
    #form = browser.get_form(id='login_form')
    #form['login'].value = 'gresch' 
    #form['password'].value = 'sequencing'
    #browser.submit_form(form)

    #for indexValues in range(0, qtyFiles):
    #    browser.open('http://rast.nmpdr.org/rast.cgi?page=JobDetails&job='+ str(jobId))
    #    form = browser.get_form(id='download')
    #    #try:#Sometimes it didn't work then it did, I don't know why
    #    form['file'].value = str(idOrganism) + filesExtention[indexValues]
    #    submit_field = form['do_download']
    #    submit_field.value = 'Authorize'
    #    browser.submit_form(form,submit=submit_field)
    #    f=open(pathToSave[indexValues] + str(idOrganism) + str(filesExtention[indexValues]),"wb")
    #    f.write(browser.response.content)
    #    f.close()

def convertFilesToFloat(listStringsIDS):
    listFloat = []
    for stringID in listStringsIDS:
        stringID = stringID[:-4]
        floatValue = float(stringID)
        listFloat.append(floatValue)
    return listFloat


def fileExistance(listFiles, listIDS):
    for idFile in listIDS:
        if float(idFile) not in listFiles:
            print(idFile)

def listFilesInPath(pathLocation):
    listFiles = os.listdir(path=pathLocation)
    return listFiles

if __name__ == '__main__':   
    pathFilsIDS = "jobIdOrgaRAST.csv"


    dataDF = read_CSV(pathFilsIDS)

    for rowValue in dataDF.iterrows():
        openBrowser(rowValue[1][0],rowValue[1][1])

    ###########Test downloaded files
    #dataframFilesLoaded = read_CSV('filesDownloaded.csv')
    #listFiles = listFilesInPath('Xls/')

    #listFloatsFiles = convertFilesToFloat(listFiles)
    #listFloatRAST = dataframFilesLoaded['IDS'].tolist()

    #formatted_list = []
    #for item in listFloatRAST:
    #    formatted_list.append("%.6f"%item)
    #fileExistance(listFloatsFiles, formatted_list)

    #print('Hello')


