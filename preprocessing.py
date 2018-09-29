#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:46:54 2018

@author: ptruong
"""

import numpy as np
import matplotlib.pyplot as plt

# Todo
# - accumulate values belonging to the same spike - DONE!
# - make plot of the quantized spectrogram - DONE!
# compute the edges of bins by Matthew's paper 1 page B.

def TEST_genData():
    x = np.array([0.2, 6.4, 3.0, 1.6, 2.0, 2.1, 2.6 ,1.9])
    bins = np.array([0.0, 1.0, 2.5, 4.0, 10.0])
    return x, bins


def binMS(data, bin_intervals):
    """
    Function takes data and bin intervals. It bins and centeres 
    the data in middle of the bin_intervals.
    """
    inds = np.digitize(data, bins)
    idx_sums = np.array([])
    for i in range(len(np.unique(inds))):
        idx = np.where(inds == np.unique(inds)[i])
        idx_sum = data[idx].sum()
        idx_sums = np.append(idx_sums, idx_sum)

    bin_mu = (bins[:-1]+bins[1:])/2
    return idx_sums, bin_mu


def main():
    x, bins = TEST_genData()
    idx_sums, bin_mu = binMS(x, bins)
    plt.stem(idx_sums, bin_mu)
    plt.show()

N = 10
k = 1.000508 # constant
l_i = k
bins = np.array([l_i])

for i in range(1,N):
    l_i = k*(0.18 + i)
    bins = np.append(bins, l_i)




