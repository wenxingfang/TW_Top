#include <TH1.h>
#include <TMath.h>
#include <TH1F.h>
#include <TH1D.h>
#include <TH1D.h>
#include <TChain.h>
#include <TFile.h>
#include <TH2.h>
#include <TAxis.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TRandom3.h>
#include <TLorentzVector.h>
#include <TF1.h>
#include <time.h>
#include <iostream>
#include <fstream>
#include <map>
const float PI_F=3.14159265358979;
const float m_el = 0.000511 ;
const float m_mu = 0.10566  ;

double Nu_pz( TLorentzVector lepton, TLorentzVector met, TString soultion, bool &isNegative);
void fill(TH1D* &hist , float value, float weight);
void fill_hist(TString input_file, TString output_file);
void select_save_LHE( TString Uncert){
TString dir_in ="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/tW_13TeV/";
TString dir_out="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/ntuple/Reza_final_tW_13TeV/";
fill_hist(dir_in+"tW_Vtb_13TeV.root"    , dir_out+"hist_Vtb.root");
fill_hist(dir_in+"tW_Vts_13TeV.root"    , dir_out+"hist_Vts.root");
fill_hist(dir_in+"tW_Vtd_13TeV.root"    , dir_out+"hist_Vtd.root");
}


void fill_hist(TString input_file, TString output_file){

TH1::SetDefaultSumw2(kTRUE);
TString t_name="IIHEAnalysis";
TChain *t = new TChain(t_name);
t->Add(input_file);

vector<int>   *LHE_status =0; 
vector<float> *LHE_Pt     =0; 
vector<float> *LHE_Eta    =0; 
vector<float> *LHE_Phi    =0; 
vector<float> *LHE_E      =0; 
vector<int>   *LHE_pdgid  =0; 

t->SetBranchAddress("LHE_status"   , &LHE_status   ) ;
t->SetBranchAddress("LHE_Pt"       , &LHE_Pt       ) ;
t->SetBranchAddress("LHE_Eta"      , &LHE_Eta      ) ;
t->SetBranchAddress("LHE_Phi"      , &LHE_Phi      ) ;
t->SetBranchAddress("LHE_E"        , &LHE_E        ) ;
t->SetBranchAddress("LHE_pdgid"    , &LHE_pdgid    ) ;

double jet_Pt_bin[8]={20,30,45,60,75,100,150,300};
double jet_rapid_bin[5]={0,1.2,1.7,2.2,2.4};
TH1D *H_lp_pt         =new TH1D("H_lp_pt"           ,"",18,20,200);
TH1D *H_lp_pt_fine    =new TH1D("H_lp_pt_fine"      ,"",7,jet_Pt_bin);
TH1D *H_lp_eta        =new TH1D("H_lp_eta"          ,"",40,-4,4 );
TH1D *H_lp_phi        =new TH1D("H_lp_phi"          ,"",40,-4,4 );
TH1D *H_lp_Rap        =new TH1D("H_lp_Rap"          ,"",24,0,2.4  );
TH1D *H_lp_Rap_fine   =new TH1D("H_lp_Rap_fine"     ,"",4,jet_rapid_bin);
TH1D *H_lm_pt         =new TH1D("H_lm_pt"           ,"",18,20,200);
TH1D *H_lm_pt_fine    =new TH1D("H_lm_pt_fine"      ,"",7,jet_Pt_bin);
TH1D *H_lm_eta        =new TH1D("H_lm_eta"          ,"",40,-4,4 );
TH1D *H_lm_phi        =new TH1D("H_lm_phi"          ,"",40,-4,4 );
TH1D *H_lm_Rap        =new TH1D("H_lm_Rap"          ,"",24,0,2.4  );
TH1D *H_lm_Rap_fine   =new TH1D("H_lm_Rap_fine"     ,"",4,jet_rapid_bin);
TH1D *H_bjet_pt       =new TH1D("H_bjet_pt"         ,"",18,20,200);
TH1D *H_bjet_pt_fine  =new TH1D("H_bjet_pt_fine"    ,"",7,jet_Pt_bin);
TH1D *H_bjet_eta      =new TH1D("H_bjet_eta"        ,"",40,-4,4 );
TH1D *H_bjet_phi      =new TH1D("H_bjet_phi"        ,"",40,-4,4 );
TH1D *H_bjet_Rap      =new TH1D("H_bjet_Rap"        ,"",24,0,2.4  );
TH1D *H_bjet_Rap_fine =new TH1D("H_bjet_Rap_fine"   ,"",4,jet_rapid_bin);
TH1D *H_MET_pt        =new TH1D("H_MET_pt"          ,"",30,0,300);
TH1D *H_MET_phi       =new TH1D("H_MET_phi"         ,"",40,-4,4 );
TH1D *H_DR_ll         =new TH1D("H_DR_ll"           ,"",40,0 ,4 );




std::cout<<"total:"<<t->GetEntries()<<std::endl;
long N_event_no_nu=0;
float N_final=0;
for(int i=0;i<t->GetEntries();i++){
if(i%100000==0)std::cout<<"processed:"<<100*i/t->GetEntries()<<"%"<<std::endl;
t->GetEntry(i);
long N_lp=0;
long N_lm=0;
long N_Nup=0;
long N_Num=0;
long N_bjet=0;

TLorentzVector lp(0,0,0,0);
TLorentzVector lm(0,0,0,0);
TLorentzVector Nup(0,0,0,0);
TLorentzVector Num(0,0,0,0);
TLorentzVector bjet(0,0,0,0);
//----------------- usinf LHE info---------------------------------------

for(unsigned int il=0;il<LHE_Pt->size();il++){
if(LHE_Pt->at(il)<20 || fabs(LHE_Eta->at(il))>2.4) continue;
if( LHE_pdgid->at(il)==11 || LHE_pdgid->at(il)==13 || LHE_pdgid->at(il)==15 ){
lm.SetPtEtaPhiE(LHE_Pt->at(il),LHE_Eta->at(il),LHE_Phi->at(il),LHE_E->at(il));
N_lm++;
}
else if( LHE_pdgid->at(il)==12 || LHE_pdgid->at(il)==14 || LHE_pdgid->at(il)==16 ){
Nup.SetPtEtaPhiE(LHE_Pt->at(il),LHE_Eta->at(il),LHE_Phi->at(il),LHE_E->at(il));
N_Nup++;
}
else if( LHE_pdgid->at(il)==-11 || LHE_pdgid->at(il)==-13 || LHE_pdgid->at(il)==-15 ){
lp.SetPtEtaPhiE(LHE_Pt->at(il),LHE_Eta->at(il),LHE_Phi->at(il),LHE_E->at(il));
N_lp++;
}
else if( LHE_pdgid->at(il)==-12 || LHE_pdgid->at(il)==-14 || LHE_pdgid->at(il)==-16 ){
Num.SetPtEtaPhiE(LHE_Pt->at(il),LHE_Eta->at(il),LHE_Phi->at(il),LHE_E->at(il));
N_Num++;
}
else if( (LHE_pdgid->at(il)==5 || LHE_pdgid->at(il)==-5) && LHE_status->at(il)>0){
bjet.SetPtEtaPhiE(LHE_Pt->at(il),LHE_Eta->at(il),LHE_Phi->at(il),LHE_E->at(il));
N_bjet++;
}
}//
TLorentzVector MET(0,0,0,0);
MET=Num+Nup;
//if(N_lm!=1 || N_lp!=1 || N_Nup!=1 || N_Num!=1 || N_bjet!=1){std::cout<<"N_lm="<<N_lm<<",N_lp="<<N_lp<<",N_Num="<<N_Num<<",N_Nup="<<N_Nup<<",N_bjet="<<N_bjet<<std::endl;}
//------------------- Fill histograms--------------------------------------
if(true){
if(lp.E()!=0){
fill( H_lp_pt          ,lp.Pt()               ,1.0); 
fill( H_lp_pt_fine     ,lp.Pt()               ,1.0); 
fill( H_lp_eta         ,lp.Eta()              ,1.0); 
fill( H_lp_phi         ,lp.Phi()              ,1.0); 
fill( H_lp_Rap         ,fabs(lp.Rapidity())   ,1.0); 
fill( H_lp_Rap_fine    ,fabs(lp.Rapidity())   ,1.0); 
}
if(lm.E()!=0){
fill( H_lp_pt          ,lp.Pt()               ,1.0); 
fill( H_lm_pt          ,lm.Pt()               ,1.0); 
fill( H_lm_pt_fine     ,lm.Pt()               ,1.0); 
fill( H_lm_eta         ,lm.Eta()              ,1.0); 
fill( H_lm_phi         ,lm.Phi()              ,1.0); 
fill( H_lm_Rap         ,fabs(lm.Rapidity())   ,1.0); 
fill( H_lm_Rap_fine    ,fabs(lm.Rapidity())   ,1.0); 
}
if(bjet.E()!=0){
fill( H_bjet_pt        ,bjet.Pt()             ,1.0); 
fill( H_bjet_pt_fine   ,bjet.Pt()             ,1.0); 
fill( H_bjet_eta       ,bjet.Eta()            ,1.0); 
fill( H_bjet_phi       ,bjet.Phi()            ,1.0); 
fill( H_bjet_Rap       ,fabs(bjet.Rapidity()) ,1.0); 
fill( H_bjet_Rap_fine  ,fabs(bjet.Rapidity()) ,1.0); 
}
fill( H_MET_pt         ,MET.Pt()              ,1.0); 
fill( H_MET_phi        ,MET.Phi()             ,1.0); 
if(lp.E()!=0 && lm.E()!=0){
fill( H_DR_ll          ,lp.DeltaR(lm)         ,1.0); 
}
}
}
//-----------------save histograms-------------------------

TFile *f = new TFile(output_file,"RECREATE");
f->cd();

H_lp_pt          ->Write("",TObject::kOverwrite); 
H_lp_pt_fine     ->Write("",TObject::kOverwrite); 
H_lp_eta         ->Write("",TObject::kOverwrite); 
H_lp_phi         ->Write("",TObject::kOverwrite); 
H_lp_Rap         ->Write("",TObject::kOverwrite); 
H_lp_Rap_fine    ->Write("",TObject::kOverwrite); 
H_lm_pt          ->Write("",TObject::kOverwrite); 
H_lm_pt_fine     ->Write("",TObject::kOverwrite); 
H_lm_eta         ->Write("",TObject::kOverwrite); 
H_lm_phi         ->Write("",TObject::kOverwrite); 
H_lm_Rap         ->Write("",TObject::kOverwrite); 
H_lm_Rap_fine    ->Write("",TObject::kOverwrite); 
H_bjet_pt        ->Write("",TObject::kOverwrite);
H_bjet_pt_fine   ->Write("",TObject::kOverwrite);
H_bjet_eta       ->Write("",TObject::kOverwrite);
H_bjet_phi       ->Write("",TObject::kOverwrite);
H_bjet_Rap       ->Write("",TObject::kOverwrite);
H_bjet_Rap_fine  ->Write("",TObject::kOverwrite);
H_MET_pt         ->Write("",TObject::kOverwrite); 
H_MET_phi        ->Write("",TObject::kOverwrite); 
H_DR_ll          ->Write("",TObject::kOverwrite); 



f->Close();
H_lp_pt          ->Delete();
H_lp_pt_fine     ->Delete();
H_lp_eta         ->Delete();
H_lp_phi         ->Delete();
H_lp_Rap         ->Delete();
H_lp_Rap_fine    ->Delete();
H_lm_pt          ->Delete();
H_lm_pt_fine     ->Delete();
H_lm_eta         ->Delete();
H_lm_phi         ->Delete();
H_lm_Rap         ->Delete();
H_lm_Rap_fine    ->Delete();
H_bjet_pt        ->Delete();
H_bjet_pt_fine   ->Delete();
H_bjet_eta       ->Delete();
H_bjet_phi       ->Delete();
H_bjet_Rap       ->Delete();
H_bjet_Rap_fine  ->Delete();
H_MET_pt         ->Delete();
H_MET_phi        ->Delete();
H_DR_ll          ->Delete();

t                 ->Delete();
std::cout<<output_file<<" is saved"<<std::endl;
}
/////////////////////////////////////////////////////////////////////////////
double Nu_pz( TLorentzVector lepton, TLorentzVector met, TString soultion, bool &isNegative){
double  mW = 80.38;
double MisET2 = (met.Px()*met.Px() + met.Py()*met.Py());
double mu  =(mW*mW)/2 + met.Px()*lepton.Px() + met.Py()*lepton.Py();
double a =  (mu*lepton.Pz())/(lepton.E()*lepton.E() - lepton.Pz()*lepton.Pz());
double a2 = TMath::Power(a,2);
double b = (TMath::Power(lepton.E(),2)*(MisET2) - TMath::Power(mu,2))/(TMath::Power(lepton.E(),2) - TMath::Power(lepton.Pz(),2));
if(a2>b){
isNegative=false;
double root = sqrt(a2-b);
double x1=a+root;
double x2=a-root;
if(soultion=="min") {if(fabs(x1)>fabs(x2))return x2;else return x1;}
else if(soultion=="plus") return x1;
else if(soultion=="minus") return x2;
else return 0;
}
else{isNegative=true;return a;}
}

void fill(TH1D* &hist , float value, float weight){
float max=hist->GetBinLowEdge(hist->GetNbinsX())+hist->GetBinWidth(hist->GetNbinsX());
float min=hist->GetBinLowEdge(1);
if(max<=value) value=( max+hist->GetBinLowEdge(hist->GetNbinsX()) )/2;
else if(value<=min) value=(min+hist->GetBinLowEdge(1)+hist->GetBinWidth(1))/2;
hist->Fill(value,weight);
}
