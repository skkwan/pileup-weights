import os 


prefix = "root://cms-xrd-global.cern.ch/"

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

datasets_to_do = [
# "2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-12,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-12_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-12_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-15,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-15_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-15_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-20,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-20_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-20_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-25,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-25_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-25_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-30,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-30_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-30_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-35,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-35_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-35_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-40,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-40_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-40_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-50,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-50_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-50_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-55,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-55_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-55_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYGluGluToHToAA_AToBB_AToTauTau_M-60,/SUSYGluGluToHToAA_AToBB_AToTauTau_M-60_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYGluGluToHToAA_AToBB_AToTauTau_M-60_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYVBFHToAA_AToBB_AToTauTau_M-12,/SUSYVBFHToAA_AToBB_AToTauTau_M-12_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-12_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYVBFHToAA_AToBB_AToTauTau_M-15,/SUSYVBFHToAA_AToBB_AToTauTau_M-15_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-15_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYVBFHToAA_AToBB_AToTauTau_M-20,/SUSYVBFHToAA_AToBB_AToTauTau_M-20_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-20_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYVBFHToAA_AToBB_AToTauTau_M-25,/SUSYVBFHToAA_AToBB_AToTauTau_M-25_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-25_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYVBFHToAA_AToBB_AToTauTau_M-30,/SUSYVBFHToAA_AToBB_AToTauTau_M-30_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-30_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYVBFHToAA_AToBB_AToTauTau_M-35,/SUSYVBFHToAA_AToBB_AToTauTau_M-35_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-35_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYVBFHToAA_AToBB_AToTauTau_M-40,/SUSYVBFHToAA_AToBB_AToTauTau_M-40_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-40_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYVBFHToAA_AToBB_AToTauTau_M-50,/SUSYVBFHToAA_AToBB_AToTauTau_M-50_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-50_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYVBFHToAA_AToBB_AToTauTau_M-55,/SUSYVBFHToAA_AToBB_AToTauTau_M-55_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-55_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,SUSYVBFHToAA_AToBB_AToTauTau_M-60,/SUSYVBFHToAA_AToBB_AToTauTau_M-60_FilterTauTauTrigger_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_SUSYVBFHToAA_AToBB_AToTauTau_M-60_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",

# "2018,Cascade_VBF_MA1-15_MA2-110,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-110_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-110_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-15_MA2-100,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-100_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-100_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-20_MA2-100,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-100_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-100_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-15_MA2-30,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-30_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-30_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-15_MA2-40,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-40_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-40_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-20_MA2-40,/Cascade_VBFH125ToA1A2To3A1_A1ToBBorTauTau_MA2-40_MA1-20_Filter_TuneCP5_13TeV_madgraph_pythia8/skkwan-NanoPost_Cascade_VBFH125ToA1A2To3A1_A1ToBBorTauTau_MA2-40_MA1-20_RunIISummer20UL18NanoAODv9-1cea6da0d07fd8de4a53b465a6714af5/USER,1000",
# "2018,Cascade_VBF_MA1-15_MA2-50,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-50_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-50_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-20_MA2-50,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-50_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-50_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-15_MA2-60,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-60_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-20_MA2-60,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-60_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-30_MA2-60,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-60_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-15_MA2-70,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-70_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-20_MA2-70,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-70_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-30_MA2-70,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-70_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-15_MA2-80,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-80_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-20_MA2-80,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-80_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-30_MA2-80,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-80_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-15_MA2-90,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-90_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-20_MA2-90,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-90_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_VBF_MA1-30_MA2-90,/Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_VBFH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-90_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",

# "2018,Cascade_ggH_MA1-15_MA2-110,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-110_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-110_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-15_MA2-100,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-100_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-100_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-20_MA2-100,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-100_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-100_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-15_MA2-30,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-30_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-30_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-15_MA2-40,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-40_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-40_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-20_MA2-40,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-40_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-40_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-15_MA2-50,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-50_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-50_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-20_MA2-50,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-50_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-50_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-15_MA2-60,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-60_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-20_MA2-60,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-60_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-30_MA2-60,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-60_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-60_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-15_MA2-70,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-70_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-20_MA2-70,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-70_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-30_MA2-70,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-70_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-70_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-15_MA2-80,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-80_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-20_MA2-80,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-80_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-30_MA2-80,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-80_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-80_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-15_MA2-90,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-90_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-20_MA2-90,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-20_MA2-90_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",
# "2018,Cascade_ggH_MA1-30_MA2-90,/Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-90_TauFilter_TuneCP5_13TeV-madgraph-pythia8/skkwan-NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-30_MA2-90_RunIISummer20UL18NanoAODv9-731836dbf6cca2314c65da54f8e0a2cf/USER,1000",


]

dataset_names = []

for line in datasets_to_do:
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