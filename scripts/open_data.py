#!/usr/bin/env python
#coding=utf-8

import numpy as np
from scipy import io
import matplotlib.pyplot as plt
from pyNeuro import analysis

if __name__ == "__main__":

    data = io.loadmat('../data/data_03_13_12_t2.mat')
    spt = data['spikeTimes']
    spt1 = spt[0][0]
    spt2 = spt[0][1]
    print(analysis.calc_corr_coef(spt1[0,:], spt2[0,:]))


