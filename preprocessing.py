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

'''
OLD FUNCTION, now not used
def binMS(data, bin_intervals):
    """
    Function takes data and bin intervals. It bins and centeres 
    the data in middle of the bin_intervals.

    ERROR!!! 

    FIX SO THAT:
    - accumulates intensities
    - bin on m/Z
    """
    inds = np.digitize(data, bin_intervals)
    idx_sums = np.array([])
    for i in range(len(np.unique(inds))):
        idx = np.where(inds == np.unique(inds)[i])
        idx_sum = data[idx].sum()
        idx_sums = np.append(idx_sums, idx_sum)

    bin_mu = (bin_intervals[:-1]+bin_intervals[1:])/2
    return idx_sums, bin_mu
'''

def fragmentPeakBinning(N):
    N = N
    k = 1.000508 # constant
    l_i = k
    #bins = np.array([l_i])
    bins = np.array([])

    for i in range(0,N):
        l_i = k*(0.18 + i)
        bins = np.append(bins, l_i)
    return bins


def TEST_randomdata():
    x, bins = TEST_genData()
    idx_sums, bin_mu = binMS(x, bins)
    plt.stem(idx_sums, bin_mu)
    plt.show()



def TEST_genSim():
    # data
    data_mz = np.random.rand(200)*10
    data_int = np.random.randn(200)*10 #100 is arbitrary
    data_int = data_int - np.min(data_int)
    return data_mz, data_int

def binMS(data_mz, data_int, N_bins):
    """
    Function takes mz, intensity and bin intervals. It bins and
    centeres the data in middle of the bin_intervals.
    """
    bin_intervals = fragmentPeakBinning(N_bins+2)
    inds = np.digitize(data_mz, bin_intervals[:-1])
    idx_sums = np.array([])

    for i in range(N_bins+1):
        idx = np.where(inds == i)
        idx_sum = data_int[idx].sum()
        idx_sums = np.append(idx_sums, idx_sum)

    bin_mu = (bin_intervals[:-1] + bin_intervals[1:])/2
    return idx_sums, bin_mu

def TEST_runBinning():
    """
    Test for generating simulated data and plot the unbinned and binned
    stem plots.
    """
    data_mz, data_int = TEST_genSim()
    idx_sums, bin_mu = binMS(data_mz, data_int, 10)
    plt.stem(data_mz, data_int)
    plt.axis([0,10,0,50]) 
    plt.show()

    plt.stem(bin_mu, idx_sums)
    plt.axis([0,10,0,1000])
    plt.show()



