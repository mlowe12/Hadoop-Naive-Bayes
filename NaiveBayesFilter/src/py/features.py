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
    _SPAMPATH = os.path.join(os.path.dirname(__file__), '..\\..\\resources\\spam.csv') 
    _HAMPATH = os.path.join(os.path.dirname(__file__), '..\\resources\\ham.csv')
    if(dataframe1 and dataframe2 != None):
        dataframe1.to_csv(_SPAMPATH)
        dataframe2.to_csv(_HAMPATH)
        return True
    else:
        return False 
