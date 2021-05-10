#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 16:14:32 2021

@author: s1303034

Plotting some Gaussians for the correlations chapter
"""

from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

mu=0,
sigma = 1
lambdabar = 1.4
Z = 0.7

fig, ax0 = plt.subplots(ncols=1, nrows=1, figsize=(6,4)) 
bin_centers = np.arange(-5,5, step=0.01)
prior = stats.norm.pdf(x = bin_centers, loc=mu, scale=sigma) #Compute probability density function
posterior = stats.norm.pdf(x = bin_centers, loc=1.4, scale=Z) #Compute probability density function
ax0.plot(bin_centers, prior, label="Prior",color='black')
ax0.plot(bin_centers, posterior, label="Posterior",color='red') #Plot PDF
ax0.legend()#Legend entries
ax0.set_yticks([])
ax0.set_xticks([0, lambdabar])
ax0.set_xticklabels([0, r"$\bar{\lambda}$"])
plt.text(-0.2, 0.2, '1', fontsize=20)
plt.text(1.2, 0.3, 'Z', fontsize=20)
#plt.savefig("./thesistemplate/correlations/plots/lambdapriorpost.png")