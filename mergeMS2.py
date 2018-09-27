#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:39:15 2018

@author: ptruong
"""

"""
Read and merge files
"""
import os
import pandas as pd
from matching_tool import ms2_parser, spectra_plot

def mergeMS2(filedir):
    """
    Merges ms2 files in a filedir location.
    """
    ms2_files = []
    for i in os.listdir(filedir):
        if i[-4:] == ".ms2":
            ms2_files.append(i)

    df_data = []
    df_scanID = []
    df_singleComp_weight = []
    df_charge = []
    df_comp_weight = []


    for i in ms2_files:
        temp_df_data, temp_df_scanID, temp_df_singleComp_weight, temp_df_charge, temp_df_comp_weight = ms2_parser(filedir+"/"+i)
        df_data += temp_df_data
        df_scanID += temp_df_scanID
        df_singleComp_weight += temp_df_singleComp_weight
        df_charge += temp_df_charge
        df_comp_weight += temp_df_comp_weight
    
    
    df_scanID = pd.DataFrame(df_scanID, columns=["scanID"])
    df_singleComp_weight = pd.DataFrame(df_singleComp_weight, columns=["singleComp_weight"])
    df_charge = pd.DataFrame(df_charge, columns=["charge"])
    df_comp_weight = pd.DataFrame(df_comp_weight, columns=["comp_weight"])
    
    df_acc = pd.concat([df_scanID, df_singleComp_weight, df_charge, df_comp_weight], axis = 1)
    
    return df_data, df_acc
    #return df_data, df_scanID, df_singleComp_weight, df_charge, df_comp_weight