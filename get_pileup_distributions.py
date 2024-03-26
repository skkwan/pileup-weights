import ROOT
import os


# Enable Multi-threaded mode
ROOT.EnableImplicitMT()

for name in [
    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-12",
    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-15",
    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-20",
    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-25",
    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-30",
    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-35",
    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-40",
    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-50",
    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-55",
    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-60",
    "SUSYVBFHToAA_AToBB_AToTauTau_M-12",
    "SUSYVBFHToAA_AToBB_AToTauTau_M-15",
    "SUSYVBFHToAA_AToBB_AToTauTau_M-20",
    "SUSYVBFHToAA_AToBB_AToTauTau_M-25",
    "SUSYVBFHToAA_AToBB_AToTauTau_M-30",
    "SUSYVBFHToAA_AToBB_AToTauTau_M-35",
    "SUSYVBFHToAA_AToBB_AToTauTau_M-40",
    "SUSYVBFHToAA_AToBB_AToTauTau_M-50",
    "SUSYVBFHToAA_AToBB_AToTauTau_M-55",
    "SUSYVBFHToAA_AToBB_AToTauTau_M-60",
    "Cascade_VBF_MA2-100_MA1-15",
    "Cascade_VBF_MA2-100_MA1-20",
    "Cascade_VBF_MA2-40_MA1-20",
    "Cascade_VBF_MA2-40_MA1-15",
    "Cascade_VBF_MA2-60_MA1-15",
    "Cascade_VBF_MA2-60_MA1-20",
    "Cascade_VBF_MA2-60_MA1-30",
    "Cascade_VBF_MA2-80_MA1-15",
    "Cascade_VBF_MA2-80_MA1-20",
    "Cascade_VBF_MA2-80_MA1-30",
    "Cascade_ggH_MA2-100_MA1-15",
    "Cascade_ggH_MA2-100_MA1-20",
    "Cascade_ggH_MA2-40_MA1-20",
    "Cascade_ggH_MA2-40_MA1-15",
    "Cascade_ggH_MA2-60_MA1-15",
    "Cascade_ggH_MA2-60_MA1-20",
    "Cascade_ggH_MA2-60_MA1-30",
    "Cascade_ggH_MA2-80_MA1-15",
    "Cascade_ggH_MA2-80_MA1-20",
    "Cascade_ggH_MA2-80_MA1-30"
]:
 
    # Create the RDataFrame from the spec json file
    print("specs/{}.json".format(name))
    df = ROOT.RDF.Experimental.FromSpec("specs/{}.json".format(name)) 

    h = df.Histo1D(ROOT.RDF.TH1DModel("n_TrueInt", "n_TrueInt", 100, 0, 100), "Pileup_nPU")

    hFile = ROOT.TFile("outputFiles/nTrueInt_{}.root".format(name), "RECREATE")
    h.Write()