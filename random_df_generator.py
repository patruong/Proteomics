##!/usr/bin/env python3
## -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:17:18 2018

@author: ptruong
"""
import pandas as pd
import numpy as np
from randomwordgenerator import randomwordgenerator


def generate_dfs(num_df = 5, cols = 2, rows = 5, variable_size = True):
    """
    NOTE: randomwordgenerator is quite slow!
    
    Function generates list with dfs.
    cols = number of cols in df
    rows = number of rows in df
    variable_size = allows df to have different size
    If variable_size == True; cols = lower bound on on cols and rows, rows = upper bound cols and rows.

    """
    if ((variable_size == True) & (cols > rows)):
        print("TESTW")
        raise ValueError("variable_size == True and cols > rows!")
    
    # Parameters 
    num_df = num_df
    variable_size = variable_size
    if variable_size == False:
        # set fixed col and row sized if variable sizes are false
        df_cols = cols
        df_rows = rows
        num_words = df_rows

    df_list = []
    for i in range(num_df):
        if variable_size == True:
            df_cols = np.random.randint(cols, rows)
            df_rows = np.random.randint(cols, rows)
            num_words = df_rows
        words = randomwordgenerator.generate_random_words(n = num_words)
        if (type(words) is list) == False:
            words = [words]
        dat = np.random.rand(df_cols, df_rows)
        df = pd.DataFrame(dat, columns = words) 
        df_list.append(df)

    return df_list

def main():
    
    print("Checking function.")
    a = generate_dfs(num_df = 5, cols = 2, rows = 5, variable_size = True)
    
    print("Complete list.")
    print(a)

    print("df 1")
    print(a[0])

    print("df 2")
    print(a[1])

    print("df 3")
    print(a[2])

    print("df 4")
    print(a[3])

    print("df 5")
    print(a[4])

    print("Checking error handling.")
    a = generate_dfs(num_df = 5, cols = 3, rows = 2, variable_size = True)

if __name__ == "__main__":
    main()

    
