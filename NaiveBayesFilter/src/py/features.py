import numpy as np
import pandas as pd
import os, os.path

'''
Extraction of Splunk Logged Data into two classified datasets

'''

def getDataFrame(filepath):
    if(os.path.dirname(filepath) != None):
        temp_frame = pd.read_csv(str(filepath))
        return temp_frame
    else:
        return None

def extractFeatures(dataframe):
    if(dataframe == None):
        return None
    else:
        _raw = dataframe[dataframe.columns[0]]
        _class = dataframe[dataframe.columns[1]]
        _row = dataframe[dataframe.columns[2]]
        return _raw, _class, _row


def assignPath(dataframe1, dataframe2):
    localpath1 = '../../resources/spam.csv'
    localpath2 = '../../resources/ham.csv'
    _GOODSET = os.path.abspath(os.path.dirname(__file__) + str(localpath1))`
    _BADSET = os.path.abspath(os.path.dirname(__file__) + str(localpath2))
    if(dataframe1 and dataframe2 != None):
        dataframe1.to_csv(_GOODSET)
        dataframe2.to_csv(_BADSET)
        return True
    else:
        return False

testpath = '/test1/test2'
print(os.path.abspath(os.path.dirname(__file__)) + str(testpath))
