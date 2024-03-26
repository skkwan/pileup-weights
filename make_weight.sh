# for name in VBFHToTauTau DYJetsToLL_M-50 DYJetsToLL_M-50-ext1 DYJetsToLL_M-10to50 DY1JetsToLL DY2JetsToLL DY3JetsToLL DY4JetsToLL VVTo2L2Nu WZTo2Q2L WZTo3LNu ZZTo4L ZZTo2Q2L WJetsToLNu W1JetsToLNu W2JetsToLNu W3JetsToLNu W4JetsToLNu GluGluHToTauTau GluGluHToWWTo2L2Nu GluGluZH_HToWWTo2L2Nu GluGluZH_HToWW_ZTo2L HWplusJ_HToWW HWminusJ_HToWW HZJ_HToWW VBFHToWWTo2L2Nu WminusHToTauTau WplusHToTauTau ZHToTauTau ttHToNonbb ttHTobb TTTo2L2Nu TTToHadronic TTToSemiLeptonic ST_tW_antitop; do

for name in SUSYGluGluToHToAA_AToBB_AToTauTau_M-12; do
cat > temp.C << EOF
{
TFile *g1 = TFile::Open("outputFiles/nTrueInt_${name}.root");
TFile *g2 = TFile::Open("commonFiles/PileupHistogram-goldenJSON-13tev-2018-69200ub-99bins.root");
TFile *g3 = TFile::Open("commonFiles/PileupHistogram-goldenJSON-13tev-2018-66000ub-99bins.root");
TFile *g4 = TFile::Open("commonFiles/PileupHistogram-goldenJSON-13tev-2018-72400ub-99bins.root");

TH1D *h1 = (TH1D*)g1->Get("n_TrueInt");
TH1D *h2 = (TH1D*)g2->Get("pileup");
TH1D *h3 = (TH1D*)g3->Get("pileup");
TH1D *h4 = (TH1D*)g4->Get("pileup");

if (h1->Integral()!=0) h1->Scale(1/h1->Integral());
if (h2->Integral()!=0) h2->Scale(1/h2->Integral());
if (h3->Integral()!=0) h3->Scale(1/h3->Integral());
if (h4->Integral()!=0) h4->Scale(1/h4->Integral());

TH1F *weight = new TH1F("puweight_nominal","puweight_nominal",100,0,100);
TH1F *weight_down = new TH1F("puweight_down","puweight_down",100,0,100);
TH1F *weight_up = new TH1F("puweight_up","puweight_up",100,0,100);

for(int i = 1; i <= 100; i++){
  float num = h2->GetBinContent(i);
  float num_down = h3->GetBinContent(i);
  float num_up = h4->GetBinContent(i);
  float den = h1->GetBinContent(i);
  if(den > 0) { 
    weight->SetBinContent(i, num/den);
    weight_down->SetBinContent(i, num_down/den);
    weight_up->SetBinContent(i, num_up/den); 
  }
}

TFile* file = TFile::Open("outputFiles/weightFile_${name}.root","RECREATE");
h1->Write();
h2->Write();
h3->Write();
h4->Write();
weight->Write();
weight_down->Write();
weight_up->Write();
file->Close();
delete weight; delete weight_down; delete weight_up;
delete file;
}

EOF

root -l -b -q temp.C

rm -rf temp.C

done
