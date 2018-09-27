##!/usr/bin/env python3
## -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:17:18 2018

@author: ptruong
"""


"""
ToDo
- create list to csv exporter - DONE!
- create csv to list importer - DONE!
- export df_data, list of df to csv - DONE!
- import df_data, .csv of dataframe to dataframes and create list object - DONE!
- Check for read in files if really need os.getcwd(), make it more generalized by allowing for input both path with os.getcwd() and without???

"""
import os
os.getcwd()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import csv
from random_df_generator import *

"""
Writes a flat list as csv
"""

def list_to_csv(list, csv_dir, writeAsCols = True):

    # Write list as columns
    if writeAsCols == True:
        with open(csv_dir, "w") as output:
            writer = csv.writer(output, lineterminator="\n")
            writer.writerow(res)

    # Write list as rows
    if writeAsCols == False:
        with open(csv_dir, "w") as output:
            writer = csv.writer(output, lineterminator="\n")
            for val in res:
                writer.writerow([val])

def TEST_list_to_csv():
    res = [1,2,3, "hi", 5, "test"]
    csv_dir = "test1.csv"
    list_to_csv(res, csv_dir)
    csv_dir = "test2.csv"
    list_to_csv(res, csv_dir, False)

    res = [("This is the first line", "Line 1"),
           ("This is the second line", "Line 2"),
           ("This is the third line", "Ĺine 3")]
    csv_dir = "test3.csv"
    list_to_csv(res, csv_dir)
    list_to_csv(res, csv_dir, False)

"""
Loads csv to list
"""
def csv_to_list(csv_dir):
    # read in csv as list
    with open(csv_dir, "r") as f:
        reader = csv.reader(f)
        listFile = list(reader)
    return listFile


"""
Export list of pandas dataframes to csv:s
"""


def dflist_to_csv(df_list, folder = "/temp", output_name = "/df_"): 
    # Create new path if not exists
    path_name = folder
    gen_path = os.getcwd() + path_name
    if not os.path.exists(gen_path):
        print("Path does doesn't exist. Trying to make!")
        os.makedirs(gen_path)

    for i in range(len(df_list)):
        path = gen_path + output_name + str(i) + ".csv"
        df_list[i].to_csv(path, index = False)

def TEST_dflist_to_csv():
    # Generate test dataframe
    print("Generating dfs..")
    a = generate_dfs()
    
    # Output list of df to folder
    folder = "/temp"
    path = os.getcwd() + folder
    print("Writing dfs to path:", path) 
    dflist_to_csv(a, folder = folder, output_name = "/df_")


"""
Import list of pandas dataframes from csv:s in a directory
"""

def csv_to_dflist(path_name = "/temp"):
    # Read in all .csv files from a path and puts them in a list.
    path = os.getcwd() + path_name
    pathfiles = os.listdir(path)

    df_list = []
    for i in reversed(pathfiles):
        csv_path = path + "/" + i
        temp_df = pd.read_csv(csv_path)
        df_list.append(temp_df)

    return df_list

def TEST_csv_to_dflist():
    # Generate test dataframe
    print("Generating dfs...")
    a = generate_dfs()

    # Output list of df to folder
    folder = "/temp"
    path = os.getcwd() + folder
    print("Writing dfs to path:", path) 
    dflist_to_csv(a, folder = folder, output_name = "/df_")

    # Reading in dfs
    print("Reading in dfs from path:", path)
    b = csv_to_dflist(path_name = folder)
    print("Length of list", str(len(b)))
    print("Printing lists")
    for i in range(len(b)):
        print(b[i])






