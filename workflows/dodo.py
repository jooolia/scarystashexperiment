#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import glob
import os 

def mk_targetname(p):
    directory, filename = os.path.split(p)
    core, ext = os.path.splitext(filename)
    filename = core + '.npz'
    return os.path.join('../results', filename)
    

src = glob.glob('../data/data_02*.mat')
targets = list(map(mk_targetname, src))

def task_open_data():
    for inp, out in zip(src, targets):
        yield {
            'actions' : ['python open_data.py %(dependencies)s --save %(targets)s'],
            'file_dep' : [inp],
            'targets' : [out],
            'name' : os.path.split(inp)[1]
            }

def task_plot_correlations():
    return {
        'actions' : ['python plot_correlations_histogram.py %(dependencies)s --save %(targets)s'],
        'file_dep' : ['../results/correlations.npz'],
        'targets' : ['../figures/correlations.png']
        }

