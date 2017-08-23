import os, os.path
import pandas as pd
import numpy as np
import re


class Unit:
    def __init__(self,filepath):
        self.filepath = filepath
        self.dataframe = None
        self.features = None
        self.classification = None
    
    def setClassification(classification):
        try:
            if(classification != None):
                str(elf.classification) = classification
        except TypeError:
            logging.exception("Invalid classification")
        return

    def setDataframe(dataframe):
        self.dataframe = dataframe
        return

    def tokenizeBySentence(dataframe):
        headers = list(dataframe.columns)
        row, col = dataframe.shape
        arr = []
        for i in range(row):
            temp = str(dataframe[headers[0]][i])
            arr.append((re.search("[^&^!@#$%^&*()_\-+=|/\\<>?'\";:\[\]{}`~.]+", str(temp)).group(0)))
        return arr

    def tokenizeByWord(_list):
        arr = []
        for i in range(len(_list)):
            element = re.search("\w+",list[i]).group(0)
            arr.append(str(element))
    return arr
