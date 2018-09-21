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
path = cwd+"/Proteomics"
os.listdir(path)
os.chdir(path)

from matching_tool import ms2_parser, spectra_plot
from LibDataParser import *


"""
Read in MaRaClusters
"""
filedir = path+"/LibraryData/consensus"
MaRa_ms2_files = []
for i in os.listdir(filedir):
    if i[-4:] == ".ms2":
        MaRa_ms2_files.append(i)    

df_data = []
df_scanID = []
df_singleComp_weight = []
df_charge = []
df_comp_weight = []

start = time.time()    
for i in MaRa_ms2_files:
    temp_df_data, temp_df_scanID, temp_df_singleComp_weight, temp_df_charge, temp_df_comp_weight = ms2_parser(filedir+"/"+i)
    df_data += temp_df_data
    df_scanID += temp_df_scanID
    df_singleComp_weight += temp_df_singleComp_weight
    df_charge += temp_df_charge
    df_comp_weight += temp_df_comp_weight

end = time.time()
time_elapsed = end-start
print(time_elapsed)
    

#df_data, df_scanID, df_singleComp_weight, df_charge, df_comp_weight = ms2_parser(filedir+"/"+MaRa_ms2_files[0])
spectra_plot(0, df_data, df_scanID) 


plt.stem(df_data[0]["mz"], df_data[0]["intensity"], markerfmt = ",")        
plt.title("scanID: "+str(df_scanID[0]))    
                

"""
Read in 
"""
file_directory = "Proteomics/LibraryData/results/"

