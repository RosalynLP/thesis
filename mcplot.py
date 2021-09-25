#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:13:48 2021

@author: s1303034
"""
import numpy as np
import matplotlib.pyplot as plt

expdata = np.array([0.4, 0.51, 0.42, 0.46, 0.38, 0.44, 0.45])
uncs =    np.array([0.1, 0.08, 0.01, 0.03, 0.07, 0.03, 0.04])

fig, ax = plt.subplots()
plt.errorbar(np.arange(len(expdata)), expdata, yerr=uncs, marker="o", color="black", linestyle=" ")
ax.set_title("Experimental data")
ax.set_ylim([0.2, 0.7])
plt.savefig("mcreps_upper.png")


n = 5
pseudodata_arrays = []
for _ in range(n):
    pdat = []
    for dat, unc in zip(expdata, uncs):
        shift = np.random.normal(dat, unc)
        pdat.append(shift)
    pseudodata_arrays.append(np.array(pdat))
    
fig, ax = plt.subplots()
ax.set_ylim([0.2, 0.7])
ax.set_title("Monte Carlo replicas")
for pdat in pseudodata_arrays:
    plt.plot(pdat, "o")
    
plt.savefig("mcreps_lower.png")