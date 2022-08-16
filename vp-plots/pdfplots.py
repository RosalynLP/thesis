#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:54:12 2021

@author: s1303034
"""
import lhapdf
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler

# Reading in PDF set and setting x and Q values
pdfsets     = {"NLO C": "NNPDF31_nlo_as_0118_kF_1_kR_1",
               "NLO C+S (9pt)": "NNPDF31_nlo_as_0118_scalecov_9pt",
               "NNLO C":  "NNPDF31_nnlo_as_0118_kF_1_kR_1",
               "NLO C+S (3pt)": "NNPDF31_nlo_as_0118_scalecov_3pt", 
               "NLO C+S (7pt)": "NNPDF31_nlo_as_0118_scalecov_7pt",
               "NLO C+S baseline(9pt)": "190406-ern-nlo-global",
               "NLO C+S fitting (9pt)": "190324-tg-nlo-global-fitting-only",
               "NLO C+S sampling (9pt)": "190324-tg-nlo-global-sampling-only",
               }

Qs           = [1.6, 10]
xlha        = np.linspace(1e-5, 0.98, num=100)

fig, ax = plt.subplots(figsize=(8,6))
# Matching colours to those in paper
ax.set_prop_cycle(cycler("color", ["mediumseagreen", "sandybrown", "cornflowerblue"]))

Qsetoutputs = [] # one setoutput for each Q val
for Q in Qs:
    setoutputs = [] # a list of len(x) by n_flav arrays, one for each PDF set
    for (setname, pdfset) in pdfsets.items():
        # Reading in PDF sets
        p    = lhapdf.mkPDF(pdfset, 0)
        pdfs = lhapdf.mkPDFs(pdfset)    
        N    = len(pdfs)
        pdfarray = []
        errarray = []
        # Loop over flavours and members to fill matrices with values
        for x in xlha:
            Rx = []
            for k in range(0,N):
                for flav in p.flavors():
                    
                    ratio = pdfs[k].xfxQ(1, x, Q)/pdfs[k].xfxQ(2, x, Q)
                    Rx.append(ratio)
                    err = np.sqrt(np.mean(np.square(Rx[1:])) - np.square(np.mean(Rx[1:])))
                    errs.append(err)
                    R.append(Rx[0])
            
        allRs.append(R)
    
    for setname, R in zip(pdfsets.keys(), allRs):
        plt.plot(xlha, [a/b for (a,b) in zip(R,allRs[0])], label=f"{setname}")
        plt.fill_between(xlha, [(a-b)/c for (a,b,c) in zip(R,errs, allRs[0])], [(a+b)/c for (a,b, c) in zip(R,errs, allRs[0])], alpha=0.5)
        ax.set_xlabel("x", fontsize="20")
        ax.set_ylabel("Normalised to global_base", fontsize="16")
        ax.set_ylim([0.8,1.2])
        ax.set_xlim([0,1])
        plt.title(rf"$d/u$ (Q={Q} GeV)", fontsize="28")
        ax.tick_params(labelsize="16")
        ax.legend(fontsize="15")
    plt.savefig(f"duratio_{Q}.png")
