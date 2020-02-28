#include <fstream>
#include <TH1F.h>
#include <iostream>
#include <TChain.h>
void Cout_event(){

//TChain *t =new TChain("Ele");
//TChain *t =new TChain("Ele_VIDHEEP7");
TChain *t =new TChain("LL");
//t->Add("./reskim_out/for_Zprime/old_ZToEE/ZToEE_M_120_200.root");
t->Add("./reskim_out/for_Zprime/ZToEE_M_120_200.root");

ULong_t ev_run=0;
ULong_t ev_lumi=0;
ULong_t ev_event=0;
float e1_eta=0;
float e2_eta=0;
float e1_Et=0;
float e2_Et=0;
float mass=0;
float mass_gsf=0;
//t->SetBranchAddress("mee",&mass);
//t->SetBranchAddress("mee_gsf",&mass_gsf);
//t->SetBranchAddress("e1_eta",&e1_eta);
//t->SetBranchAddress("e1_Et", &e1_Et);
//t->SetBranchAddress("e2_eta",&e2_eta);
//t->SetBranchAddress("e2_Et", &e2_Et);
t->SetBranchAddress("ev_run",&ev_run);
t->SetBranchAddress("ev_luminosityBlock",&ev_lumi);
t->SetBranchAddress("ev_event",&ev_event);

ofstream fout("list_120_200_new.txt");
TH1F *h =new TH1F("h","",200,0.9,1.1);
h->GetXaxis()->SetTitle("m(sc)/m(gsf)");
h->GetYaxis()->SetTitle("Number");
for(long i=0; i<t->GetEntries(); i++){
t->GetEntry(i);
//if(fabs(e1_eta)>1.566 && fabs(e2_eta)>1.566) continue;
//if((fabs(e1_eta)<1.4442 && fabs(e2_eta)>1.566 && fabs(e2_eta)<2.5) || (fabs(e2_eta)<1.4442 && fabs(e1_eta)>1.566 && fabs(e1_eta)<2.5)){ 
//if(mass_gsf<900) continue;
//fout <<ev_run<<" "<<ev_lumi<<" "<<ev_event<<" "<<mass_gsf<<"\n";
fout <<ev_run<<" "<<ev_lumi<<" "<<ev_event<<"\n";
//}
}
fout << flush; 
fout.close();
}
