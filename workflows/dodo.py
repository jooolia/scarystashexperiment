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
    
def mk_figurename(p):
    directory, filename = os.path.split(p)
    core, ext = os.path.splitext(filename)
    filename = core + '.png'
    return os.path.join('../results', filename)
       
src = glob.glob('../data/data_02*.mat')   
targets = list(map(mk_targetname, src))
correlations = list(map(mk_figurename, src))

def task_open_data():
    for inp, out in zip(src, targets):
        yield {
            'actions' : ['python open_data.py %(dependencies)s --save %(targets)s'],
            'file_dep' : [inp],
            'targets' : [out],
            'name' : os.path.split(inp)[1]
            }

def task_all_correlations():
    for inp, out in zip(targets, correlations):
        yield {
        'actions' : ['python plot_correlations_histogram.py %(dependencies)s --save %(targets)s'],
            'file_dep' : [inp],
            'targets' : [out],
            'name' : os.path.split(inp)[1]
            }

