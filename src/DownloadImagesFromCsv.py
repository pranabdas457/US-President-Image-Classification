# This class is responsible for downloading the images of presidents present in the input csv.
import os
import requests
import pandas as pd

class DownloadImagesFromCsv:
    def __init__(self, inputpath, parentfolder):
        self.inputPath = inputpath
        self.parentFolder = parentfolder


    def downloadImages(self):
        for files in os.listdir(self.inputPath):
            downloadedpath = os.path.join(self.parentFolder, files.split('.')[0])
            if not os.path.exists(downloadedpath):
                print("Folder Created for {}".format(downloadedpath))
                os.mkdir(downloadedpath)

            complete_path = os.path.join(self.inputPath, files)
            print("CSV Path is {}" , complete_path)
            counter = 0
            ###dataframe = pd.read_csv(complete_path, chunksize = 500)
            file1 = open(complete_path, "r")
            dataframe = file1.read().splitlines( )
            for items in dataframe:

                url =  items.replace(",","") if items.endswith(",") else items
                print("Image URL is " + url)
                try:
                    rawfile = requests.get(url, allow_redirects=True, timeout=10)
                    if rawfile is not None:
                        open(os.path.join(downloadedpath, files.split('.')[0] + "_" + str(counter) + ".jpg"), 'wb').write(
                            rawfile.content)
                        counter += 1
                except:
                    print("Unable to download the file {}" +  url)
                finally:
                    continue



inputFilePath = 'E:\\Machine learning Work zone\\ImageClassification(US Prime Minister)\\input\\Presidents'
ParentFilePath = 'E:\\Machine learning Work zone\\ImageClassification(US Prime Minister)\\input\\Images'

downloadObj = DownloadImagesFromCsv(inputFilePath,ParentFilePath)
print("******************************************")
downloadObj.downloadImages()
print("*********************DownLoad Completed**********************")