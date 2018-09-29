#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 09:31:54 2018

@author: ptruong
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

import os
cwd = os.getcwd()
path = cwd + "/Proteomics"
os.listdir(path)
os.chdir(path)

from matching_tool import ms2_parser, spectra_plot
from LibDataParser import *
from mergeMS2 import *
from helper_functions import *

"""
NOTE to self:
    helper_functions for ms2 is aweful! Do not use!
"""


#df_data, df_scanID, df_singleComp_weight, df_charge, df_comp_weight = merge_ms2(filedir)

#spectra_plot(0, df_data, df_scanID) 

def main():
    # MaRaCluster
    start = time.time()
    filedir = path+"/LibraryData/consensus"
    #df_data_MC, df_scanID_MC, df_singleCompWeight_MC, df_charge_MC, df_compWeight_MC = merge_ms2(filedir)
    df_data_MC, df_acc_MC = mergeMS2(filedir)
    end = time.time()
    time_elapsed = end-start
    print(time_elapsed)
    
    start = time.time()
    # Sample Data
    file_directory = path+"/SampleData/"
    #df_data_S, df_scanID_S, df_singleCompWeight_S, df_charge_S, df_compWeight_S = merge_ms2(filedir)
    df_data_S, df_acc_S = mergeMS2(filedir)
    end = time.time()
    time_elapsed = end-start
    print(time_elapsed)

    
    # Export the data for quicker loading time
    dflist_to_csv(df_data_MC, folder = "/MaraClusterCSV")
    dflist_to_csv(df_data_S, folder = "/SampleCSV")
    
    
    
    
    
    
#df_data, df_scanID, df_singleComp_weight, df_charge, df_comp_weight = ms2_parser(filedir+"/"+MaRa_ms2_files[0])
spectra_plot(0, df_data_MC, df_scanID_MC) 
 

plt.stem(df_data[0]["mz"], df_data[0]["intensity"], markerfmt = ",")        
plt.title("scanID: "+str(df_scanID[0]))    

test_df = pd.DataFrame([df_scanID_MC, df_singleCompWeight_MC, df_charge_MC, df_compWeight_MC], 
                       index=["scanID", "singleCompWeight", "charge", "compWeight"])




"""
ToDo
- create list to csv exporter - DONE
- create csv to list importer - DONE
- export df_data, list of df to csv - DONE
- import df_data, .csv of dataframe to dataframes and create list object - DONE
- 

"""





                


