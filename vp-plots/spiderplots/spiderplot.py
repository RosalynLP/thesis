#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:10:35 2021

@author: s1303034
"""
# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
# Set data
df = pd.read_csv("chi2data.csv")
 
# ------- PART 1: Define a function that do a plot for one line of the dataset!
 
def make_spider( row, title, color, newplot = True):

    # number of variable
    categories=list(df)[1:]
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    if newplot == True:
        ax = plt.subplot( polar=True, )
    else:
        ax = plt.gca()
    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([0.5,1], ["0.5","1"], color="grey", size=15)
    plt.ylim(0,1.4)

    # Ind1
    values=df.loc[row].drop('Fit').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid', label=title)
    ax.fill(angles, values, color=color, alpha=0.4)
    
    ax.legend(bbox_to_anchor=(0.9, -0.1), fontsize=20)
    ax.tick_params(axis='both', which='major', labelsize=25)
    # Add a title
    #plt.title(title, size=11, color=color, y=1.1)

    
# ------- PART 2: Apply the function to all individuals
# initialize the figure
my_dpi=96
plt.figure(figsize=(8,8))
 
# Create a color palette:
my_palette = plt.cm.get_cmap("Set2", len(df.index))
 
# Loop to plot
make_spider (row = 0, title = df['Fit'][0], color=my_palette(0), newplot=True)
make_spider( row= 1, title=df['Fit'][1], color=my_palette(1), newplot=False )
make_spider( row= 6, title=df['Fit'][6], color=my_palette(6), newplot=False )
#plt.savefig("spider1.png")

plt.figure(figsize=(8,8))
make_spider( row= 2, title=df['Fit'][2], color=my_palette(2), newplot=True )
make_spider( row= 3, title=df['Fit'][3], color=my_palette(3), newplot=False )
#plt.savefig("spider2.png")

plt.figure(figsize=(8,8))
make_spider( row= 4, title=df['Fit'][4], color=my_palette(4), newplot=True )
make_spider( row= 5, title=df['Fit'][5], color=my_palette(7), newplot=False )
#plt.savefig("spider3.png")