#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:32:05 2021

@author: s1303034
"""

import lhapdf
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler

# Reading in PDF set and setting x and Q values
pdfsets     = {"global_base": "200609-ern-001",
               "global_ite_2_dw": "NNPDF31_nnlo_as_0118_global_deut_ite",
               "global_ite_2_sh":  "NNPDF31_nnlo_as_0118_global_deut_ite_shift"}

Q           = 10
xlha        = np.linspace(1e-5, 0.98, num=100)

fig, ax = plt.subplots(figsize=(8,6))
# Matching colours to those in paper
ax.set_prop_cycle(cycler("color", ["mediumseagreen", "sandybrown", "cornflowerblue"]))
allRs = []
for (setname, pdfset) in pdfsets.items():
# Reading in PDF sets
    p    = lhapdf.mkPDF(pdfset, 0)
    pdfs = lhapdf.mkPDFs(pdfset)    
    N    = len(pdfs)
    R = []
    errs = []
    # Loop over flavours and members to fill matrices with values
    for x in xlha:
        Rx = []
        for k in range(0,N):
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
