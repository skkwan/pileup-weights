import ROOT
import os


# Enable Multi-threaded mode
ROOT.EnableImplicitMT()

for name in ["SUSYGluGluToHToAA_AToBB_AToTauTau_M-12"]:
 
    # Create the RDataFrame from the spec json file
    print("specs/{}.json".format(name))
    df = ROOT.RDF.Experimental.FromSpec("specs/{}.json".format(name)) 

    h = df.Histo1D(ROOT.RDF.TH1DModel("n_TrueInt", "n_TrueInt", 100, 0, 100), "Pileup_nPU")

    hFile = ROOT.TFile("outputFiles/nTrueInt_{}.root".format(name), "RECREATE")
    h.Write()