import ROOT
import os


# Enable Multi-threaded mode
ROOT.EnableImplicitMT()

for name in ["SUSYVBFHToAA_AToBB_AToTauTau_M-45", "SUSYGluGluToHToAA_AToBB_AToTauTau_M-45"]:
 
    # Create the RDataFrame from the spec json file
    df = ROOT.RDF.Experimental.FromSpec("specs/{}.json".format(name)) 

    h = df.Histo1D(ROOT.RDF.TH1DModel("n_TrueInt", "n_TrueInt", 100, 0, 100), "Pileup_nPU")

    hFile = ROOT.TFile("nTrueInt_{}.root".format(name), "RECREATE")
    h.Write()