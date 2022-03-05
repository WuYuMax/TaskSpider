import os
import codecs
import csv
from abc import abstractmethod

class Writer:
    @abstractmethod
    def write(self,message):
        pass

class CSVWriter(Writer):
    __file = None
    __csv_writer:csv.writer = None
    __writedTitle:bool = False

    def __init__(self,fileName:str,mode:str):
        # print(fileName)
        self.__file = codecs.open(fileName,mode,'gbk','ignore')
        self.__csv_writer = csv.writer(self.__file)
    def __del__(self):

        if self.__file is not None and  self.__file.closed is False:
            self.close()
    def writedTitle(self)->bool:
        return self.writedTitle
    def close(self):
        self.__file.close()
    def write(self, message):
        self.__csv_writer.writerow(message)
