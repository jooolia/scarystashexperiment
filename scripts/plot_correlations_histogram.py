#!/usr/bin/env python
#coding=utf-8

import numpy as np
from scipy import io
import matplotlib.pyplot as plt
from pyNeuro import analysis

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('correlationfile')
    parser.add_argument('--save-fig')


    args = parser.parse_args()
  
    data = np.load(args.correlationfile)
    correlations = data['correlations']
  

    plt.hist(correlations.flat, bins=50)
    plt.xlabel('Correlation value [a.u.]')
    plt.ylabel('# occurrences')
    plt.savefig(args.save_fig)


