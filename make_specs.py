import os 


prefix = "root://cmsxrootd.fnal.gov//"

template = """
{
    "samples": {
       "DATASET_NAME": {
          "trees": ["Events"],
          "files": [FILES_LIST],
          "metadata": {
             "xsecs": 1.0,
             "sumws": 1.0,
             "sample_category": "mc",
             "sample_name": "DATASET_NAME"
          }
       }
    }
}"""

datasets_to_do_2018 = [
"2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-12,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-12_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-12_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-15,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-15_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-15_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-20,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-20_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-20_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-25,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-25_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-25_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-30,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-30_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-30_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-35,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-35_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-35_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-40,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-40_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-40_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-50,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-50_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-50_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-55,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-55_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-55_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-60,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-60_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-60_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYVBFHToAA_AToBB_AToTauTau_M-12,/SUSYVBFHToAA_AToBB_AToTauTau_M-12_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-12_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYVBFHToAA_AToBB_AToTauTau_M-15,/SUSYVBFHToAA_AToBB_AToTauTau_M-15_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-15_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYVBFHToAA_AToBB_AToTauTau_M-20,/SUSYVBFHToAA_AToBB_AToTauTau_M-20_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-20_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYVBFHToAA_AToBB_AToTauTau_M-25,/SUSYVBFHToAA_AToBB_AToTauTau_M-25_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-25_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYVBFHToAA_AToBB_AToTauTau_M-30,/SUSYVBFHToAA_AToBB_AToTauTau_M-30_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-30_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYVBFHToAA_AToBB_AToTauTau_M-35,/SUSYVBFHToAA_AToBB_AToTauTau_M-35_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-35_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYVBFHToAA_AToBB_AToTauTau_M-40,/SUSYVBFHToAA_AToBB_AToTauTau_M-40_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-40_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYVBFHToAA_AToBB_AToTauTau_M-50,/SUSYVBFHToAA_AToBB_AToTauTau_M-50_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-50_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYVBFHToAA_AToBB_AToTauTau_M-55,/SUSYVBFHToAA_AToBB_AToTauTau_M-55_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-55_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,SUSYVBFHToAA_AToBB_AToTauTau_M-60,/SUSYVBFHToAA_AToBB_AToTauTau_M-60_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-60_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",

"2018,Cascade_VBF_MA1-15_MA2-110,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-110_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-110_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-15_MA2-100,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-100_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-100_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-20_MA2-100,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-100_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-100_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-15_MA2-30,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-30_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-30_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-15_MA2-40,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-40_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-40_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-20_MA2-40,/Cascade_VBFH125ToA1A2To3A1_A1ToBBorTauTau_MA2-40_MA1-20_Filter_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_Cascade_VBFH125ToA1A2To3A1_A1ToBBorTauTau_MA2-40_MA1-20_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER",
"2018,Cascade_VBF_MA1-15_MA2-50,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-50_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-50_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-20_MA2-50,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-50_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-50_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-15_MA2-60,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-60_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-20_MA2-60,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-60_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-30_MA2-60,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-60_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-15_MA2-70,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-70_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-20_MA2-70,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-70_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-30_MA2-70,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-70_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-15_MA2-80,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-80_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-20_MA2-80,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-80_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-30_MA2-80,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-80_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-15_MA2-90,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-90_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-20_MA2-90,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-90_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_VBF_MA1-30_MA2-90,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-90_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",

"2018,Cascade_ggH_MA1-15_MA2-110,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-110_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-110_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-15_MA2-100,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-100_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-100_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-20_MA2-100,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-100_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-100_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-15_MA2-30,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-30_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-30_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-15_MA2-40,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-40_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-40_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-20_MA2-40,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-40_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-40_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-15_MA2-50,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-50_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-50_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-20_MA2-50,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-50_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-50_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-15_MA2-60,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-60_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-20_MA2-60,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-60_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-30_MA2-60,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-60_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-15_MA2-70,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-70_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-20_MA2-70,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-70_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-30_MA2-70,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-70_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-15_MA2-80,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-80_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-20_MA2-80,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-80_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-30_MA2-80,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-80_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-15_MA2-90,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-90_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-20_MA2-90,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-90_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
"2018,Cascade_ggH_MA1-30_MA2-90,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-90_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER",
]


signal_datasets_to_do_2017 = [
"2017,Cascade_ggH_MA1-15_MA2-100,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-100_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-100_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-15_MA2-110,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-110_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-110_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-15_MA2-30,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-30_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-30_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-15_MA2-40,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-40_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-40_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-15_MA2-50,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-50_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-50_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-15_MA2-60,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-60_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-15_MA2-70,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-70_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-15_MA2-80,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-80_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-15_MA2-90,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-90_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-20_MA2-100,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-100_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-100_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-20_MA2-40,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-40_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-40_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-20_MA2-50,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-50_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-50_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-20_MA2-60,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-60_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-20_MA2-70,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-70_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-20_MA2-80,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-80_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-20_MA2-90,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-90_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-30_MA2-60,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-60_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-30_MA2-70,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-70_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-30_MA2-80,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-80_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_ggH_MA1-30_MA2-90,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-90_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",

"2017,Cascade_VBF_MA1-15_MA2-100,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-100_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-100_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-15_MA2-110,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-110_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-110_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-15_MA2-30,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-30_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-30_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-15_MA2-40,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-40_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-40_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-15_MA2-50,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-50_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-50_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-15_MA2-60,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-60_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-15_MA2-70,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-70_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-15_MA2-80,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-80_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-15_MA2-90,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-90_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-20_MA2-100,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-100_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-100_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-20_MA2-40,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-40_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-40_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-20_MA2-50,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-50_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-50_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-20_MA2-60,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-60_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-20_MA2-70,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-70_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-20_MA2-80,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-80_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-20_MA2-90,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-90_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-30_MA2-60,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-60_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-30_MA2-70,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-70_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-30_MA2-80,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-80_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",
"2017,Cascade_VBF_MA1-30_MA2-90,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-90_RunIISummer20UL17NanoAODv9-443bb40de6ac466e0eb3687ceac57faa/USER",

]

mc_datasets_to_do_2017 = [
"2017,DY1JetsToLL,/DY1JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/skkwan-NanoPost_DY1JetsToLL_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,DY2JetsToLL,/DY2JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/skkwan-NanoPost_DY2JetsToLL_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,DY3JetsToLL,/DY3JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/skkwan-NanoPost_DY3JetsToLL_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,DY4JetsToLL,/DY4JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/skkwan-NanoPost_DY4JetsToLL_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,DYJetsToLL_M-10to50,/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/skkwan-NanoPost_DYJetsToLL_M-10to50_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,DYJetsToLL_M-50-ext1,/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skkwan-NanoPost_DYJetsToLL_M-50-ext1_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,DYJetsToLL_M-50,/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/skkwan-NanoPost_DYJetsToLL_M-50_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,GluGluHToTauTau,/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/skkwan-NanoPost_GluGluHToTauTau_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,GluGluHToWWTo2L2Nu,/GluGluHToWWTo2L2Nu_M125_TuneCP5_PSw_13TeV-powheg2-pythia8/skkwan-NanoPost_GluGluHToWWTo2L2Nu_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,GluGluZH_HToWW_ZTo2L,/GluGluZH_HToWW_ZTo2L_M-125_TuneCP5_13TeV-powheg-pythia8/skkwan-NanoPost_GluGluZH_HToWW_ZTo2L_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,HWminusJ_HToWW,/HWminusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/skkwan-NanoPost_HWminusJ_HToWW_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,HWplusJ_HToWW,/HWplusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/skkwan-NanoPost_HWplusJ_HToWW_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,HZJ_HToWW,/HZJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/skkwan-NanoPost_HZJ_HToWW_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,ST_t-channel_antitop,/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/skkwan-NanoPost_ST_t-channel_antitop_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,ST_t-channel_top,/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/skkwan-NanoPost_ST_t-channel_top_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,ST_tW_antitop,/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/skkwan-NanoPost_ST_tW_antitop_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,ST_tW_top,/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/skkwan-NanoPost_ST_tW_top_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,TTTo2L2Nu,/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/skkwan-NanoPost_TTTo2L2Nu_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,TTToHadronic,/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/skkwan-NanoPost_TTToHadronic_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,TTToSemiLeptonic,/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/skkwan-NanoPost_TTToSemiLeptonic_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,VBFHToTauTau,/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/skkwan-NanoPost_VBFHToTauTau_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,VBFHToWWTo2L2Nu,/VBFHToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/skkwan-NanoPost_VBFHToWWTo2L2Nu_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,VVTo2L2Nu,/VVTo2L2Nu_MLL-1toInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/skkwan-NanoPost_VVTo2L2Nu_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,W1JetsToLNu,/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/skkwan-NanoPost_W1JetsToLNu_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,W2JetsToLNu,/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/skkwan-NanoPost_W2JetsToLNu_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,W3JetsToLNu,/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/skkwan-NanoPost_W3JetsToLNu_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,W4JetsToLNu,/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/skkwan-NanoPost_W4JetsToLNu_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,WJetsToLNu,/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/skkwan-NanoPost_WJetsToLNu_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,WZTo2Q2L,/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/skkwan-NanoPost_WZTo2Q2L_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,WZTo3LNu,/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/skkwan-NanoPost_WZTo3LNu_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,WminusHToTauTau,/WminusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/skkwan-NanoPost_WminusHToTauTau_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,WplusHToTauTau,/WplusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/skkwan-NanoPost_WplusHToTauTau_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,ZHToTauTau,/ZHToTauTau_M125_CP5_13TeV-powheg-pythia8/skkwan-NanoPost_ZHToTauTau_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,ZZTo2Q2L,/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/skkwan-NanoPost_ZZTo2Q2L_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,ZZTo4L,/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/skkwan-NanoPost_ZZTo4L_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,ttHToNonbb,/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/skkwan-NanoPost_ttHToNonbb_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",
"2017,ttHTobb,/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/skkwan-NanoPost_ttHTobb_RunIISummer20UL17NanoAODv9-76de701442013e6ff941c86cd482e64d/USER",

]

dataset_names = []

for line in signal_datasets_to_do_2017:
    # https://stackoverflow.com/questions/4071396/how-to-split-by-comma-and-strip-white-spaces-in-python
    cleaned = [x.strip() for x in line.split(",")]
    dataset_name = cleaned[1]
    dataset_names.append(dataset_name)
    das_name = cleaned[2]
    # Query DAS to get file names 
    if das_name.endswith("/USER"):
        command = 'dasgoclient --query="file dataset={} instance=prod/phys03 status=VALID" > logRun'.format(das_name)
    else:
        command = 'dasgoclient --query="file dataset={} > logRun'.format(das_name)
    os.system(command)
    filesToGet = ""
    with open("logRun", "r") as logFile:
        rawLines = logFile.read().splitlines()
        for rawLine in rawLines:
            # If not the last line
            if (rawLine != rawLines[-1]):
                filesToGet += ('"{}{}", '.format(prefix, rawLine))
            else:
                filesToGet += ('"{}{}"'.format(prefix, rawLine))
    print(filesToGet)
    out = template.replace("DATASET_NAME", dataset_name).replace("FILES_LIST", filesToGet)
    with open("specs/{}.json".format(dataset_name), "w") as fOut:
        fOut.write(out)
print(out)

print(">>> In the next step, do these datasets: \n")
for n in dataset_names:
    print(n)