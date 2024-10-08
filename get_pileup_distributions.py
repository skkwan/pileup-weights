import ROOT
import os


# Enable Multi-threaded mode
ROOT.EnableImplicitMT()

for name in [
    "Cascade_VBF_MA1-15_MA2-110",
    "Cascade_VBF_MA1-15_MA2-100",
    "Cascade_VBF_MA1-20_MA2-100",
    "Cascade_VBF_MA1-15_MA2-30",
    "Cascade_VBF_MA1-15_MA2-40",
    "Cascade_VBF_MA1-20_MA2-40",
    "Cascade_VBF_MA1-15_MA2-50",
    "Cascade_VBF_MA1-20_MA2-50",
    "Cascade_VBF_MA1-15_MA2-60",
    "Cascade_VBF_MA1-20_MA2-60",
    "Cascade_VBF_MA1-30_MA2-60",
    "Cascade_VBF_MA1-15_MA2-70",
    "Cascade_VBF_MA1-20_MA2-70",
    "Cascade_VBF_MA1-30_MA2-70",
    "Cascade_VBF_MA1-15_MA2-80",
    "Cascade_VBF_MA1-20_MA2-80",
    "Cascade_VBF_MA1-30_MA2-80",
    "Cascade_VBF_MA1-15_MA2-90",
    "Cascade_VBF_MA1-20_MA2-90",
    "Cascade_VBF_MA1-30_MA2-90",

    "Cascade_ggH_MA1-15_MA2-110",
    "Cascade_ggH_MA1-15_MA2-100",
    "Cascade_ggH_MA1-20_MA2-100",
    "Cascade_ggH_MA1-15_MA2-30",
    "Cascade_ggH_MA1-15_MA2-40",
    "Cascade_ggH_MA1-20_MA2-40",
    "Cascade_ggH_MA1-15_MA2-50",
    "Cascade_ggH_MA1-20_MA2-50",
    "Cascade_ggH_MA1-15_MA2-60",
    "Cascade_ggH_MA1-20_MA2-60",
    "Cascade_ggH_MA1-30_MA2-60",
    "Cascade_ggH_MA1-15_MA2-70",
    "Cascade_ggH_MA1-20_MA2-70",
    "Cascade_ggH_MA1-30_MA2-70",
    "Cascade_ggH_MA1-15_MA2-80",
    "Cascade_ggH_MA1-20_MA2-80",
    "Cascade_ggH_MA1-30_MA2-80",
    "Cascade_ggH_MA1-15_MA2-90",
    "Cascade_ggH_MA1-20_MA2-90",
    "Cascade_ggH_MA1-30_MA2-90",

]:
 
    # Create the RDataFrame from the spec json file
    print("specs/{}.json".format(name))
    df = ROOT.RDF.Experimental.FromSpec("specs/{}.json".format(name)) 

    h = df.Histo1D(ROOT.RDF.TH1DModel("n_TrueInt", "n_TrueInt", 100, 0, 100), "Pileup_nPU")

    hFile = ROOT.TFile("outputFiles/nTrueInt_{}.root".format(name), "RECREATE")
    h.Write()