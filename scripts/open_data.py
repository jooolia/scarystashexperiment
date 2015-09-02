#!/usr/bin/env python
#coding=utf-8

import numpy as np
from scipy import io
import matplotlib.pyplot as plt
from pyNeuro import analysis

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('datafile')
    parser.add_argument('--save')
    args = parser.parse_args()

    fname = args.datafile 
    outfname = args.save
    data = io.loadmat(fname)
    spt = data['spikeTimes']
    n_spt = spt.shape[1]
    print(spt.shape)
    correlations = np.zeros((n_spt, n_spt))
    for i in range(n_spt):
        for j in range(n_spt):
            correlations[i,j] = analysis.calc_corr_coef(spt[0][i][0,:], spt[0][j][0,:])

    # plot the histogram
    if args.save:
        np.savez(args.save, correlations=correlations)
    else:
        plt.hist(correlations.flat, bins=50)
        plt.xlabel('Correlation value [a.u.]')
        plt.ylabel('# occurrences')
        plt.show()


