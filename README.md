# Theory uncertainties in parton distribution functions

This is the source code for my thesis which can be found [here](https://era.ed.ac.uk/handle/1842/38570).

## Abstract

We are now in the era of high precision particle physics, spurred on by a wealth of new data from the Large Hadron Collider (LHC). In order to match the precision set by modern experiments and test the limits of the Standard Model, we must increase the sophistication of our theoretical predictions. Much of the data available involve the interaction of protons, which are composite particles. These interactions are described by combining perturbative Quantum Chromodynamics (QCD) with parton distribution functions (PDFs), which encapsulate the non-perturbative behaviour. Increasing accuracy and precision of these PDFs is therefore of great value to modern particle physics. PDFs are determined by multi-dimensional fits of experimental data to theoretical predictions from QCD. Uncertainties in PDFs arise from those in the experimental data and theoretical predictions, as well as from the fitting procedure itself. Those in the theory come from many sources. Here we consider two of the most important: the first are missing higher order uncertainties (MHOUs), arising due to truncating the predictions’ perturbative expansion; the second are nuclear uncertainties, due to difficulty making predictions in a nuclear environment. In this thesis we consider how to include theory uncertainties in PDF fits by constructing a theory covariance matrix and adding this to the experimental one. MHOUs are estimated and included as a proof of concept in next-to-leading order PDFs. We find that these capture many of the important features of the known PDFs at the next order above. We then investigate nuclear uncertainties, estimate their magnitude and assess their impact on the PDFs. Finally, we consider how to make predictions with theory uncertainties using PDFs which themselves include theory uncertainties. Here there are correlations between the PDFs and the predictions, which can lead to a shift in the predictions and their uncertainties, which can significantly improve their accuracy and precision.

## Code layout

* `diagrams` contains code and output for .tex diagrams e.g. Feynman diagrams

* `vp-plots` contains code (`python` scripts and `yaml` runcards for [nnpdf](https://github.com/NNPDF/nnpdf)) and outputs for various PDF plots

* `thesistemplate` contains the .tex code for the thesis itself, with a sub-folder for each chapter (including a couple which didn't appear :) )
