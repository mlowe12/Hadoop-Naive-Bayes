import os, os.path
import pandas as pd
import numpy as np
import logging
import re

''' 

Unit object serves as a modularized entity in which data preprocessing is performed
> Object will take the a String filepath that will be the targeting location of the csv exported by Splunk to the file system
> Dataframe is created via the pandas library function pandas.read_csv:=> provides output object pandas.DataFrame
>  Classification is binary: Either a good message or a spam message. 

'''

class Unit:
    def __init__(self,filepath):
        self.filepath = filepath
        self.dataframe = None
        self.features = None
        self.classification = None
        self.absPath = os.path.abspath(os.path.dirname(__file__))

    def setClassification(self,classification):
        try:
            if(classification != None):
                self.classification = classification
        except TypeError:
            logging.exception("Invalid classification")
        return

    '''Takes entire parent dataframe and breaks it into tokenized sentences per log entry from Splunk
        > Process strips all non-alphanumeric characters from parsed sequences and returns raw text list of all sentences
    '''

    def tokenizeBySentence(self):
        self.dataframe = pd.read_csv(self.filepath)
        headers = list(self.dataframe.columns)
        row, col = self.dataframe.shape
        arr = []
        for i in range(row):
            temp = str(self.dataframe[headers[0]][i])
            arr.append((re.search("[^&^!@#$%^&*()_\-+=|/\\<>?'\";:\[\]{}`~.]+", str(temp)).group(0)))
        return arr
    '''
    Tokenizes entire class of logs into single word entities. 
    > Will be fed into MapReduce to get total word count
    '''
    def tokenizeByWord(self, _list):
        arr = []
        for i in range(len(_list)):
            element = re.search("\w+",_list[i]).group(0)
            arr.append(str(element))
        return arr

    def exportToMapReduce(self, localpath):
        temp_filepath = self.absPath + localpath
        temp_sent = self.tokenizeBySentence()
        temp_list = pd.DataFrame(self.tokenizeByWord(list(temp_sent)))
        temp_list[temp_list.columns[0]].to_csv(temp_filepath)
        return

    def unitTest(self,testcases):
        testcases = pd.read_csv(os.path.abspath(os.path.dirname(__file__)) +"/../..resources/tests/unit_test.csv")
        test_filepath = self.absPath + 



test = Unit("/Users/michaellowe/Downloads/raw-spam.csv")
test.exportToMapReduce()
