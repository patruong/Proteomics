#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 14:43:38 2018

@author: ptruong
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

import os
cwd = os.getcwd()
os.listdir(cwd)


def summarizeTable(df):
    """
    Function to summarize percolator.target.psms.txt crux-output
    Input - percolator.target.psms.txt
    Output - 1) scanID_list, 2) pep_list, 3) charge_list, with corresponding index
    
    """
    unique_PEPseq = df["sequence"].unique()
    
    scanID_list = []
    pep_list = []
    charge_list = []
    
    for i in range(len(unique_PEPseq)):
        temp_seq = unique_PEPseq[i] #loop
    
        df_pep = df[df["sequence"] == temp_seq][["scan", "charge"]]
        df_charges = df_pep["charge"].unique()
        
        for j in range(len(df_charges)):
            df_scans = df_pep[df_pep["charge"] == df_charges[0]] #loop
        
            scanIDs = df_scans["scan"].unique()
            scanID_list.append(scanIDs)
            
            charge_list.append(j)
            
            pep_list.append(temp_seq)
    
    return scanID_list, pep_list, charge_list   

def timeit(x):
    "Function to time process"
    start = time.time()
    
    results = x
    
    end = time.time()
    time_elapsed = end-start
    print(time_elapsed)
    return results

#res = timeit(summarizeTable(df))

#scanID = res[0]
#peptides = res[1]
#charges = res[2]

#scanID[0], peptides[0], charges[0]


"""
Read ms2 file
"""

#filedir = "Downloads/crux-output_bullseye/bullseye.pid.ms2"

def ms2_parser(filedir):
    """
    File for parsing .ms2 files
    """
    

    df_data = []
    df_scanID = []
    df_singleComp_weight = []
    df_charge = []
    df_comp_weight = []
    
    begin_msCollection = False
    
    f = open(filedir, "r")
    while True:
        text = f.readline()
        try:
            if text.split()[0] == "S":
                if begin_msCollection == True:
                    datapoints = pd.DataFrame(data_points_list, columns=["mz", "intensity"])
                    
                    df_data.append(datapoints)
                    df_scanID.append(scanID)
                    df_singleComp_weight.append(singleComp_weight)
                    df_charge.append(charge)
                    df_comp_weight.append(comp_weight)
                
                scanID = int(text.split()[1])
                singleComp_weight = float(text.split()[-1])
                
                data_points_list = []
                begin_msCollection = False
                #print("new series")
            
            elif text.split()[0] == "Z":
                charge = float(text.split()[1])
                comp_weight = float(text.split()[-1])
                begin_msCollection = True
                continue
            
            if begin_msCollection == True:
                data = text.split()
                data = [float(i) for i in data] #convert string to float
                data_points_list.append(data)
        except:
            break
    return df_data, df_scanID, df_singleComp_weight, df_charge, df_comp_weight

#df_data, df_scanID, df_singleComp_weight, df_charge, df_comp_weight = ms2_parser(filedir)

def spectra_plot(ms_number, df_data, df_scanID, markerfmt = ","):
    plt.stem(df_data[ms_number]["mz"], df_data[ms_number]["intensity"], markerfmt = markerfmt)        
    plt.title("scanID: "+str(df_scanID[ms_number]))
    
if __name__=="__main__":
    
    
    #filedir = "Downloads/crux-output_percolator/percolator.target.psms.txt"
    #df = pd.read_csv(filedir, sep = "\t")

    filedir = "Downloads/crux-output_bullseye/bullseye.pid.ms2"
    df_data, df_scanID, df_singleComp_weight, df_charge, df_comp_weight = ms2_parser(filedir)

    
    #df.cluster.value_counts()        
    plt.stem(df_data[0]["mz"], df_data[0]["intensity"], markerfmt = ",")        
    plt.title("scanID: "+str(df_scanID[0]))    
                
    plt.stem(df_data[1]["mz"], df_data[1]["intensity"], markerfmt = ",")        
    plt.title("scanID: "+str(df_scanID[1]))    
        
    # check percolator.target.psms.txt file
    # first element in file is 31309. We want to find index
    df_scanID.index(31309)       
    plt.stem(df_data[22938]["mz"], df_data[22938]["intensity"], markerfmt = ",")        
    plt.title("scanID: "+str(df_scanID[22938]))    
        
    













    