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
    
    def setClassification(self,classification):
        try:
            if(classification != None):
                self.classification = classification
        except TypeError:
            logging.exception("Invalid classification")
        return

    def setDataframe(dataframe):
        self.dataframe = dataframe
        return

    '''Takes entire parent dataframe and breaks it into tokenized sentences per log entry from Splunk
        > Process strips all non-alphanumeric characters from parsed sequences and returns raw text list of all sentences
    '''

    def tokenizeBySentence(dataframe):
        headers = list(dataframe.columns)
        row, col = dataframe.shape
        arr = []
        for i in range(row):
            temp = str(dataframe[headers[0]][i])
            arr.append((re.search("[^&^!@#$%^&*()_\-+=|/\\<>?'\";:\[\]{}`~.]+", str(temp)).group(0)))
        return arr
    '''
    Tokenizes entire class of logs into single word entities. 
    > Will be fed into MapReduce to get total word count
    '''
    def tokenizeByWord(_list):
        arr = []
        for i in range(len(_list)):
            element = re.search("\w+",_list[i]).group(0)
            arr.append(str(element))
        return arr

    def exportToMapReduce(_list):
        return

