#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:49:19 2018

@author: ptruong
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

import os
cwd = os.getcwd()
os.listdir(cwd)


def readin_directory(filedir):
    file_list = os.listdir(filedir)
    return file_list

def getMaRaClusters(file_list):
    MaraClusters = []
    for i in file_list:
        if (i[-4:] == ".tsv" and i[0] == "M"):
            MaraClusters.append(i)
    return MaraClusters

def proc_MaRaClusters(MaraClusters, filedir):
    "process MaRaClusters into df"
    df_list = []
    files = []
    for i in range(len(MaraClusters)):
        file = filedir + MaraClusters[i]
        files.append(MaraClusters[i])
        df = pd.read_csv(file, sep = "\t", names = ["path", "scanID", "garbage", "cluster"])
        df = df.drop(df.columns[2], axis = 1)
        df_list.append(df)
    
    file = filedir + MaraClusters[-2]
    df = pd.read_csv(file, sep = "\t", skip_blank_lines = False, names = ["path", "scanID", "garbage", "cluster"])
    df = df.drop(df.columns[2], axis = 1)

    # PARSE Clusters from MaRaCluster.clusters_pX.tsv file
    import csv
    #import time
    
    #tic = time.clock()
    
    
    readin_lines = []
    header = ["path", "scanID", "garbage", "cluster"]
    cluster = 1
    
    perc_done = 0
    
    with open(file) as fd:
        rd = csv.reader(fd, delimiter = "\t")
        
        for i, row in enumerate(rd):
            
            #if i%55868 == 0:
            #    perc_done += 1
            #    print(str(perc_done)+"%")
        
            #print(row)
            #print(i)
            if row == []:
                cluster +=1
                continue
            row[-1] = cluster
            readin_lines.append(row)
            
            #if(i >= 2):
            #    break
    
    df = pd.DataFrame(readin_lines, columns = header)
    return df
    #toc = time.clock()

    #time_elapsed = toc-tic
    #print(time_elapsed)
    



"""
for i in range(len(df_list)):
    print(df_list[i].head())
    
df_concat = pd.concat(df_list, ignore_index=True)

noclickDF = pd.DataFrame([[0,123,321],[0,1543,432]], columns=['click', 'id','location'])
clickDF = pd.DataFrame([[1,123,421],[1,1543,436]], columns=['click', 'location','id'])
pd.concat([noclickDF, clickDF], ignore_index=True)
"""

if __name__=="__main__":
    file_directory = "Proteomics/LibraryData/results/"
    file_list = readin_directory(filedir = file_directory)
    MaraClusters = getMaRaClusters(file_list)
    df = proc_MaRaClusters(MaraClusters, filedir = file_directory)
    print(df.head(20))
    
    #df.cluster.value_counts()