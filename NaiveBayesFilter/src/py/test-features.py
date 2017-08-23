import features
import numpy as numpy
import pandas as pd
import os, os.path
import logging


class UnitTest:

    def __init__(self,dataframe1, dataframe2, instanceID):
        self.dataframe1 = dataframe1
        self.dataframe2 = dataframe2
        self.instanceID = instanceID
   
    def assertDataframe(self,filepath, filename):
        if(filepath != None or len(filepath) > 0):
            try:
                dataframe = pd.read_csv(str(filepath))
                temp_cols = dataframe.columns


            except FileNotFoundError:
                logging.exception("FILE NOT FOUND dir = %s filename = %s \n", filepath, filepath[len(filename)])
            
                
                