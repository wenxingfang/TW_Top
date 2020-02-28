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
void fill_hist(TString input_file, TString output_file, bool is_top);
void select_save(){
TString dir_in ="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/";
TString dir_out="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/ntuple/";
//TString dir_out="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/ntuple/noNegative/";
//fill_hist(dir_in+"outfile_Vtb.root", dir_out+"hist_Vtb.root");
//fill_hist(dir_in+"outfile_Vts.root", dir_out+"hist_Vts.root");
//fill_hist(dir_in+"outfile_Vtd.root", dir_out+"hist_Vtd.root");
fill_hist(dir_in+"outfile_Vtb_antitop.root", dir_out+"hist_Vtb_antitop.root", false);
fill_hist(dir_in+"outfile_Vtb_top.root"    , dir_out+"hist_Vtb_top.root",     true );
//fill_hist(dir_in+"outfile_Vtb_top_CT10.root"    , dir_out+"hist_Vtb_top_CT10.root");
//fill_hist("/pnfs/iihe/cms/store/user/wenxing/ST_t-channel_top_4f_inclusiveDecays_TuneCUETP8M2T4_13TeV-powhegV2-madspin/crab_ST_t-channel_top_4f_inclusiveDecays_13TeV-powheg/170901_221215/0000/outfile*.root"    , dir_out+"hist_Vtb_top_13TeV_powheg_inclusive_mclep.root");
//fill_hist("/pnfs/iihe/cms/store/user/wenxing/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/crab_ST_t-channel_4f_leptonDecays_13TeV-amcatnlo/170901_221350/0000/outfile_1*.root"    , dir_out+"hist_Vtb_top_13TeV_amcatnlo_PL.root");
}


void fill_hist(TString input_file, TString output_file, bool is_top){

TH1::SetDefaultSumw2(kTRUE);
TString t_name="IIHEAnalysis";
TChain *t = new TChain(t_name);
t->Add(input_file);

float mc_w_sign            =0; 
vector<float> *pl_jet_pt   =0; 
vector<float> *pl_jet_eta  =0; 
vector<float> *pl_jet_phi  =0; 
vector<float> *pl_lep_pt   =0; 
vector<float> *pl_lep_eta  =0; 
vector<float> *pl_lep_phi  =0; 
vector<float> *pl_MET_pt   =0; 
vector<float> *pl_MET_phi  =0; 
vector<int  > *pl_jet_pdgid=0; 
vector<int  > *pl_lep_pdgid=0; 

vector<int>   *mc_status  =0; 
vector<float> *mc_pt      =0; 
vector<float> *mc_eta     =0; 
vector<float> *mc_phi     =0; 
vector<float> *mc_energy  =0; 
vector<int>   *mc_pdgId   =0; 

vector<int>   *LHE_status =0; 
vector<float> *LHE_Pt     =0; 
vector<float> *LHE_Eta    =0; 
vector<float> *LHE_Phi    =0; 
vector<float> *LHE_E      =0; 
vector<int>   *LHE_pdgid  =0; 


t->SetBranchAddress("mc_w_sign"    , &mc_w_sign    ) ;
t->SetBranchAddress("pl_jet_pt"    , &pl_jet_pt    ) ;
t->SetBranchAddress("pl_jet_eta"   , &pl_jet_eta   ) ;
t->SetBranchAddress("pl_jet_phi"   , &pl_jet_phi   ) ;
t->SetBranchAddress("pl_lep_pt"    , &pl_lep_pt    ) ;
t->SetBranchAddress("pl_lep_eta"   , &pl_lep_eta   ) ;
t->SetBranchAddress("pl_lep_phi"   , &pl_lep_phi   ) ;
t->SetBranchAddress("pl_MET_pt"    , &pl_MET_pt    ) ;
t->SetBranchAddress("pl_MET_phi"   , &pl_MET_phi   ) ;
t->SetBranchAddress("pl_jet_pdgid" , &pl_jet_pdgid ) ;
t->SetBranchAddress("pl_lep_pdgid" , &pl_lep_pdgid ) ;
t->SetBranchAddress("mc_status"    , &mc_status    ) ;
t->SetBranchAddress("mc_pt"        , &mc_pt        ) ;
t->SetBranchAddress("mc_eta"       , &mc_eta       ) ;
t->SetBranchAddress("mc_phi"       , &mc_phi       ) ;
t->SetBranchAddress("mc_energy"    , &mc_energy    ) ;
t->SetBranchAddress("mc_pdgId"     , &mc_pdgId     ) ;
t->SetBranchAddress("LHE_status"   , &LHE_status   ) ;
t->SetBranchAddress("LHE_Pt"       , &LHE_Pt       ) ;
t->SetBranchAddress("LHE_Eta"      , &LHE_Eta      ) ;
t->SetBranchAddress("LHE_Phi"      , &LHE_Phi      ) ;
t->SetBranchAddress("LHE_E"        , &LHE_E        ) ;
t->SetBranchAddress("LHE_pdgid"    , &LHE_pdgid    ) ;

double Top_Pt_bin[8]={0,35,50,75,100,150,200,300};
double antiTop_Pt_bin[7]={0,35,50,75,100,150,300};
double rapid_bin[8]={0,0.15,0.30,0.45,0.70,1.00,1.30,2.20};
double jet_Pt_bin[7]={30,45,60,75,100,150,300};
double jet_rapid_bin[7]={0,1.2,1.7,2.2,2.7,3.3,4.5};
TH1D *H_lep_pt           =new TH1D("H_lep_pt"          ,"",30,0,300);
TH1D *H_lep_eta          =new TH1D("H_lep_eta"         ,"",40,-4,4 );
TH1D *H_lep_phi          =new TH1D("H_lep_phi"         ,"",40,-4,4 );
TH1D *H_lep_Rap          =new TH1D("H_lep_Rap"         ,"",40,0,4  );
TH1D *H_bjet_pt          =new TH1D("H_bjet_pt"         ,"",30,0,300);
TH1D *H_bjet_eta         =new TH1D("H_bjet_eta"        ,"",40,-4,4 );
TH1D *H_bjet_phi         =new TH1D("H_bjet_phi"        ,"",40,-4,4 );
TH1D *H_bjet_Rap         =new TH1D("H_bjet_Rap"        ,"",40,0,4  );
TH1D *H_Nu_pt            =new TH1D("H_Nu_pt"           ,"",30,0,300);
TH1D *H_Nu_eta           =new TH1D("H_Nu_eta"          ,"",40,-4,4 );
TH1D *H_Nu_phi           =new TH1D("H_Nu_phi"          ,"",40,-4,4 );
TH1D *H_Nu_Rap           =new TH1D("H_Nu_Rap"          ,"",40,0,4  );
TH1D *H_W_pt             =new TH1D("H_W_pt"            ,"",30,0,300);
TH1D *H_W_eta            =new TH1D("H_W_eta"           ,"",40,-4,4 );
TH1D *H_W_phi            =new TH1D("H_W_phi"           ,"",40,-4,4 );
TH1D *H_W_Rap            =new TH1D("H_W_Rap"           ,"",40,0,4  );
TH1D *H_W_mass           =new TH1D("H_W_mass"          ,"",20,70,90);
TH1D *H_top_pt           =new TH1D("H_top_pt"          ,"",30,0,300);
TH1D *H_top_pt_fine      =new TH1D("H_top_pt_fine"     ,"",7,Top_Pt_bin);
TH1D *H_top_eta          =new TH1D("H_top_eta"         ,"",40,-4,4 );
TH1D *H_top_phi          =new TH1D("H_top_phi"         ,"",40,-4,4 );
TH1D *H_top_Rap          =new TH1D("H_top_Rap"         ,"",40,0,4  );
TH1D *H_top_Rap_fine     =new TH1D("H_top_Rap_fine"    ,"",7,rapid_bin);
TH1D *H_top_mass         =new TH1D("H_top_mass"        ,"",50,100,200);
TH1D *H_atop_pt       =new TH1D("H_atop_pt"            ,"",30,0,300);
TH1D *H_atop_pt_fine  =new TH1D("H_atop_pt_fine"       ,"",6,antiTop_Pt_bin);
TH1D *H_atop_eta      =new TH1D("H_atop_eta"           ,"",40,-4,4 );
TH1D *H_atop_phi      =new TH1D("H_atop_phi"           ,"",40,-4,4 );
TH1D *H_atop_Rap      =new TH1D("H_atop_Rap"           ,"",40,0,4  );
TH1D *H_atop_Rap_fine =new TH1D("H_atop_Rap_fine"      ,"",7,rapid_bin);
TH1D *H_atop_mass     =new TH1D("H_atop_mass"          ,"",50,100,200);
TH1D *H_top_jet_pt       =new TH1D("H_top_jet_pt"      ,"",30,0,300);
TH1D *H_top_jet_pt_fine  =new TH1D("H_top_jet_pt_fine" ,"",6,jet_Pt_bin);
TH1D *H_top_jet_eta      =new TH1D("H_top_jet_eta"     ,"",40,-4,4 );
TH1D *H_top_jet_phi      =new TH1D("H_top_jet_phi"     ,"",40,-4,4 );
TH1D *H_top_jet_Rap      =new TH1D("H_top_jet_Rap"     ,"",40,0,4  );
TH1D *H_top_jet_Rap_fine =new TH1D("H_top_jet_Rap_fine","",6,jet_rapid_bin);
TH1D *H_atop_jet_pt      =new TH1D("H_atop_jet_pt"     ,"",30,0,300);
TH1D *H_atop_jet_pt_fine =new TH1D("H_atop_jet_pt_fine","",6,jet_Pt_bin);
TH1D *H_atop_jet_eta     =new TH1D("H_atop_jet_eta"    ,"",40,-4,4 );
TH1D *H_atop_jet_phi     =new TH1D("H_atop_jet_phi"    ,"",40,-4,4 );
TH1D *H_atop_jet_Rap     =new TH1D("H_atop_jet_Rap"    ,"",40,0,4  );
TH1D *H_atop_jet_Rap_fine=new TH1D("H_atop_jet_Rap_fine","",6,jet_rapid_bin);
TH1D *H_MET_pt           =new TH1D("H_MET_pt"          ,"",30,0,300);
TH1D *H_MET_phi          =new TH1D("H_MET_phi"         ,"",40,-4,4 );
TH1D *H_DR_lep_Nu        =new TH1D("H_DR_lep_Nu"       ,"",40,0 ,4 );
TH1D *H_DR_W_bjet        =new TH1D("H_DR_W_bjet"       ,"",40,0 ,4 );
TH1D *H_DPz_Nu_mc        =new TH1D("H_DPz_Nu_mc"       ,"",50,0 ,500 );
TH1D *H_DPx_Nu_mc        =new TH1D("H_DPx_Nu_mc"       ,"",50,0 ,500 );
TH1D *H_DPy_Nu_mc        =new TH1D("H_DPy_Nu_mc"       ,"",50,0 ,500 );

TH1D *H_Steps            =new TH1D("H_Steps"           ,"",10,0 ,10);
bool pass_1=false;
bool pass_2=false;
bool pass_3=false;
bool pass_4=false;
bool pass_5=false;


TH1D *H_S1_lep_pt           =new TH1D("H_S1_lep_pt"          ,"",60,0,300);
TH1D *H_S1_lep_eta          =new TH1D("H_S1_lep_eta"         ,"",40,-4,4 );
TH1D *H_S1_lep_phi          =new TH1D("H_S1_lep_phi"         ,"",40,-4,4 );
TH1D *H_S1_lep_id           =new TH1D("H_S1_lep_id"          ,"",120,-30,30 );
TH1D *H_N_lep               =new TH1D("H_N_lep"              ,"",40,0,4 );

TH1D *H_S1_jet_pt           =new TH1D("H_S1_jet_pt"          ,"",60,0,300);
TH1D *H_S1_jet_eta          =new TH1D("H_S1_jet_eta"         ,"",40,-4,4 );
TH1D *H_S1_jet_phi          =new TH1D("H_S1_jet_phi"         ,"",40,-4,4 );
TH1D *H_S1_jet_id           =new TH1D("H_S1_jet_id"          ,"",120,-30,30 );
TH1D *H_N_jet               =new TH1D("H_N_jet"              ,"",100,0,10 );

std::cout<<"total:"<<t->GetEntries()<<std::endl;
for(int i=0;i<t->GetEntries();i++){
if(i%100000==0)std::cout<<"processed:"<<100*i/t->GetEntries()<<"%"<<std::endl;
t->GetEntry(i);

pass_1=false;
pass_2=false;
pass_3=false;
pass_4=false;
pass_5=false;

//+++++++++++++++++ For lepton +++++++++++++++++++++++++++++++++++++++++++++++
int N_lep=0;
int S1_N_lep=0;
TLorentzVector lep(0,0,0,0);
//----------------- particle level info---------------------------------------

for(unsigned int il=0;il<pl_lep_pt->size();il++){
fill( H_S1_lep_pt          ,pl_lep_pt->at(il)                 ,mc_w_sign); 
fill( H_S1_lep_eta         ,pl_lep_eta->at(il)                ,mc_w_sign); 
fill( H_S1_lep_phi         ,pl_lep_phi->at(il)                ,mc_w_sign); 
fill( H_S1_lep_id          ,pl_lep_pdgid->at(il)              ,mc_w_sign); 
S1_N_lep++;
if(pl_lep_pt->at(il)>25 && fabs(pl_lep_eta->at(il))<2.5 && (abs(pl_lep_pdgid->at(il))==11 || abs(pl_lep_pdgid->at(il))==13)){
N_lep++;
double m_lep=0;
if(abs(pl_lep_pdgid->at(il))==11 ) m_lep=m_el;
else if(abs(pl_lep_pdgid->at(il))==13 ) m_lep=m_mu;
lep.SetPtEtaPhiM(pl_lep_pt->at(il),pl_lep_eta->at(il),pl_lep_phi->at(il),m_lep);
}
}

//----------------- usinf LHE info---------------------------------------
/*
for(unsigned int il=0;il<LHE_Pt->size();il++){
if(abs(LHE_pdgid->at(il))!=11 && abs(LHE_pdgid->at(il))!=13)continue;
fill( H_S1_lep_pt          ,LHE_Pt->at(il)                 ,mc_w_sign); 
fill( H_S1_lep_eta         ,LHE_Eta->at(il)                ,mc_w_sign); 
fill( H_S1_lep_phi         ,LHE_Phi->at(il)                ,mc_w_sign); 
fill( H_S1_lep_id          ,LHE_pdgid->at(il)              ,mc_w_sign); 
S1_N_lep++;
if(LHE_Pt->at(il)>25 && fabs(LHE_Eta->at(il))<2.5){
N_lep++;
double m_lep=0;
lep.SetPtEtaPhiE(LHE_Pt->at(il),LHE_Eta->at(il),LHE_Phi->at(il),LHE_E->at(il));
}
}
*/
//----------------- usinf MC info---------------------------------------
/*
int status=1;
for(unsigned int ij=0;ij<mc_pdgId->size();ij++){
if((abs(mc_pdgId->at(ij))==11 || abs(mc_pdgId->at(ij))==13) && mc_status->at(ij)==23 )status=23;
}
//status=23;
for(unsigned int ij=0;ij<mc_pdgId->size();ij++){
if((abs(mc_pdgId->at(ij))==11 || abs(mc_pdgId->at(ij))==13) && mc_status->at(ij)==status ){
fill( H_S1_lep_pt          ,mc_pt   ->at(ij)                ,mc_w_sign); 
fill( H_S1_lep_eta         ,mc_eta  ->at(ij)                ,mc_w_sign); 
fill( H_S1_lep_phi         ,mc_phi  ->at(ij)                ,mc_w_sign); 
fill( H_S1_lep_id          ,mc_pdgId->at(ij)                ,mc_w_sign); 
S1_N_lep++;
}
if((abs(mc_pdgId->at(ij))==11 || abs(mc_pdgId->at(ij))==13) && mc_status->at(ij)==status && mc_pt->at(ij)>25 && fabs(mc_eta->at(ij))<2.5 ){
                                                                                      N_lep++;
                                                                                      lep.SetPtEtaPhiM(mc_pt->at(ij),mc_eta->at(ij),mc_phi->at(ij),mc_energy->at(ij));
                                                                                                                                      }
                                               }
*/
if(N_lep==1) pass_1=true;//ask for exactly one lepton
fill( H_N_lep         ,S1_N_lep                ,mc_w_sign); 
//+++++++++++++++++ For jets +++++++++++++++++++++++++++++++++++++++++++++++
int N_jet=0;
int N_S1_jet=0;
int N_bjet=0;
float jet_max_pt=0;
vector<TLorentzVector> v_jet;
TLorentzVector jet(0,0,0,0);
TLorentzVector b_jet(0,0,0,0);
TLorentzVector led_jet(0,0,0,0);
for(unsigned int ij=0;ij<pl_jet_pt->size();ij++){
if(pass_1){
N_S1_jet++;
fill( H_S1_jet_pt          ,pl_jet_pt   ->at(ij)              ,mc_w_sign); 
fill( H_S1_jet_eta         ,pl_jet_eta  ->at(ij)              ,mc_w_sign); 
fill( H_S1_jet_phi         ,pl_jet_phi  ->at(ij)              ,mc_w_sign); 
fill( H_S1_jet_id          ,pl_jet_pdgid->at(ij)              ,mc_w_sign); 
}
if(pl_jet_pt->at(ij)>30 && fabs(pl_jet_eta->at(ij))<4.5){
N_jet++;
jet.SetPtEtaPhiM(pl_jet_pt->at(ij),pl_jet_eta->at(ij),pl_jet_phi->at(ij),0);//M is 0?
v_jet.push_back(jet);
if(fabs(pl_jet_eta->at(ij))<2.5 && abs(pl_jet_pdgid->at(ij))==5){N_bjet++;b_jet.SetPtEtaPhiM(pl_jet_pt->at(ij),pl_jet_eta->at(ij),pl_jet_phi->at(ij),0);}//for b jet 
else if(pl_jet_pt->at(ij)>jet_max_pt){led_jet.SetPtEtaPhiM(pl_jet_pt->at(ij),pl_jet_eta->at(ij),pl_jet_phi->at(ij),0);jet_max_pt=pl_jet_pt->at(ij);}
}
}
if(N_bjet==1) pass_2=true; //ask for N_jet>=2 and N_bjet==1
if(N_jet>=2)  pass_3=true;
if(pass_1) fill( H_N_jet         ,N_S1_jet                ,mc_w_sign); 

bool reject_event=false;
for(unsigned int ij=0;ij<v_jet.size();ij++){if(lep.DeltaR(v_jet.at(ij))<0.4){reject_event=true;break;}}// for DeltaR between lepton and jets > 0.4
if(reject_event==false) pass_4=true;
if((lep+b_jet).M()<160) pass_5=true;//m(lb)<160
//+++++++++++++++++ For MET +++++++++++++++++++++++++++++++++++++++++++++++
TLorentzVector MET(0,0,0,0);
MET.SetPtEtaPhiM(pl_MET_pt->at(0),0,pl_MET_phi->at(0),0);
//+++++++++++++++++ For Neutrion +++++++++++++++++++++++++++++++++++++++++++++++
TLorentzVector Nu(0,0,0,0);
TLorentzVector mc_Nu(0,0,0,0);

bool negative_s=false;
double Nu_Pz = Nu_pz( lep, MET, "min",negative_s);
//if(negative_s)continue;
double Nu_E  = sqrt( MET.Px()*MET.Px() + MET.Py()*MET.Py() + Nu_Pz*Nu_Pz );
Nu.SetPxPyPzE(MET.Px(),MET.Py(),Nu_Pz,Nu_E);


for(unsigned int ij=0;ij<mc_pdgId->size();ij++){
if((abs(mc_pdgId->at(ij))==12 || abs(mc_pdgId->at(ij))==14) && mc_status->at(ij)==23){
                                                                                      //std::cout<<"find"<<std::endl;
                                                                                      mc_Nu.SetPtEtaPhiM(mc_pt->at(ij),mc_eta->at(ij),mc_phi->at(ij),0);break;
                                                                                     }
}

//if(Nu.E()==0)continue;

//+++++++++++++++++ For Top +++++++++++++++++++++++++++++++++++++++++++++++
TLorentzVector Top(0,0,0,0);
Top=lep+Nu+b_jet;
//------------------- Fill histograms--------------------------------------
float weight=mc_w_sign;
//if(weight>0)continue;
//weight=-weight;
fill( H_Steps           ,0.5                      ,weight); 
if(pass_1){
fill( H_Steps           ,1.5                      ,weight); 
}
if(pass_1 && pass_2){
fill( H_Steps           ,2.5                      ,weight); 
}
if(pass_1 && pass_2 && pass_3){
fill( H_Steps           ,3.5                      ,weight); 
}
if(pass_1 && pass_2 && pass_3 && pass_4){
fill( H_Steps           ,4.5                      ,weight); 
}
if(pass_1 && pass_2 && pass_3 && pass_4 && pass_5){
fill( H_Steps           ,5.5                      ,weight); 
}
if(pass_1 && pass_2 && pass_3 && pass_4 && pass_5){
fill( H_lep_pt          ,lep.Pt()                 ,weight); 
fill( H_lep_eta         ,lep.Eta()                ,weight); 
fill( H_lep_phi         ,lep.Phi()                ,weight); 
fill( H_lep_Rap         ,fabs(lep.Rapidity())     ,weight); 
fill( H_bjet_pt         ,b_jet.Pt()               ,weight); 
fill( H_bjet_eta        ,b_jet.Eta()              ,weight); 
fill( H_bjet_phi        ,b_jet.Phi()              ,weight); 
fill( H_bjet_Rap        ,fabs(b_jet.Rapidity())   ,weight); 
fill( H_Nu_pt           ,Nu.Pt()                  ,weight); 
fill( H_Nu_eta          ,Nu.Eta()                 ,weight); 
fill( H_Nu_phi          ,Nu.Phi()                 ,weight); 
fill( H_Nu_Rap          ,fabs(Nu.Rapidity())      ,weight); 
fill( H_W_pt            ,(lep+Nu).Pt()            ,weight); 
fill( H_W_eta           ,(lep+Nu).Eta()           ,weight); 
fill( H_W_phi           ,(lep+Nu).Phi()           ,weight); 
fill( H_W_Rap           ,fabs((lep+Nu).Rapidity()),weight); 
fill( H_W_mass          ,(lep+Nu).M()             ,weight); 
fill( H_top_pt          ,Top.Pt()                 ,weight); 
fill( H_top_pt_fine     ,Top.Pt()                 ,weight); 
fill( H_top_eta         ,Top.Eta()                ,weight); 
fill( H_top_phi         ,Top.Phi()                ,weight); 
fill( H_top_Rap         ,fabs(Top.Rapidity())     ,weight); 
fill( H_top_Rap_fine    ,fabs(Top.Rapidity())     ,weight); 
fill( H_top_mass        ,Top.M()                  ,weight); 
fill( H_top_jet_pt      ,led_jet.Pt()             ,weight); 
fill( H_top_jet_pt_fine ,led_jet.Pt()             ,weight); 
fill( H_top_jet_eta     ,led_jet.Eta()            ,weight); 
fill( H_top_jet_phi     ,led_jet.Phi()            ,weight); 
fill( H_top_jet_Rap     ,fabs(led_jet.Rapidity()) ,weight); 
fill( H_top_jet_Rap_fine,fabs(led_jet.Rapidity()) ,weight); 

fill( H_atop_pt          ,Top.Pt()                ,weight); 
fill( H_atop_pt_fine     ,Top.Pt()                ,weight); 
fill( H_atop_eta         ,Top.Eta()               ,weight); 
fill( H_atop_phi         ,Top.Phi()               ,weight); 
fill( H_atop_Rap         ,fabs(Top.Rapidity())    ,weight); 
fill( H_atop_Rap_fine    ,fabs(Top.Rapidity())    ,weight); 
fill( H_atop_mass        ,Top.M()                 ,weight); 
fill( H_atop_jet_pt      ,led_jet.Pt()            ,weight); 
fill( H_atop_jet_pt_fine ,led_jet.Pt()            ,weight); 
fill( H_atop_jet_eta     ,led_jet.Eta()           ,weight); 
fill( H_atop_jet_phi     ,led_jet.Phi()           ,weight); 
fill( H_atop_jet_Rap     ,fabs(led_jet.Rapidity()),weight); 
fill( H_atop_jet_Rap_fine,fabs(led_jet.Rapidity()),weight); 

fill( H_MET_pt          ,MET.Pt()              ,weight); 
fill( H_MET_phi         ,MET.Phi()             ,weight); 
fill( H_DR_lep_Nu       ,lep.DeltaR(Nu)        ,weight); 
fill( H_DR_W_bjet       ,(lep+Nu).DeltaR(b_jet),weight); 
fill( H_DPz_Nu_mc       ,fabs(Nu.Pz()-mc_Nu.Pz())  ,weight); 
fill( H_DPx_Nu_mc       ,fabs(Nu.Px()-mc_Nu.Px())  ,weight); 
fill( H_DPy_Nu_mc       ,fabs(Nu.Py()-mc_Nu.Py())  ,weight); 
}
}

//-----------------save histograms-------------------------

TFile *f = new TFile(output_file,"RECREATE");
f->cd();

H_lep_pt          ->Write("",TObject::kOverwrite); 
H_lep_eta         ->Write("",TObject::kOverwrite); 
H_lep_phi         ->Write("",TObject::kOverwrite); 
H_lep_Rap         ->Write("",TObject::kOverwrite); 
H_bjet_pt         ->Write("",TObject::kOverwrite); 
H_bjet_eta        ->Write("",TObject::kOverwrite); 
H_bjet_phi        ->Write("",TObject::kOverwrite); 
H_bjet_Rap        ->Write("",TObject::kOverwrite); 
H_Nu_pt           ->Write("",TObject::kOverwrite); 
H_Nu_eta          ->Write("",TObject::kOverwrite); 
H_Nu_phi          ->Write("",TObject::kOverwrite); 
H_Nu_Rap          ->Write("",TObject::kOverwrite); 
H_W_pt            ->Write("",TObject::kOverwrite); 
H_W_eta           ->Write("",TObject::kOverwrite); 
H_W_phi           ->Write("",TObject::kOverwrite); 
H_W_Rap           ->Write("",TObject::kOverwrite); 
H_W_mass          ->Write("",TObject::kOverwrite); 
H_top_pt          ->Write("",TObject::kOverwrite); 
H_top_pt_fine     ->Write("",TObject::kOverwrite); 
H_top_eta         ->Write("",TObject::kOverwrite); 
H_top_phi         ->Write("",TObject::kOverwrite); 
H_top_Rap         ->Write("",TObject::kOverwrite); 
H_top_Rap_fine    ->Write("",TObject::kOverwrite); 
H_top_mass        ->Write("",TObject::kOverwrite); 
H_atop_pt      ->Write("",TObject::kOverwrite); 
H_atop_pt_fine ->Write("",TObject::kOverwrite); 
H_atop_eta     ->Write("",TObject::kOverwrite); 
H_atop_phi     ->Write("",TObject::kOverwrite); 
H_atop_Rap     ->Write("",TObject::kOverwrite); 
H_atop_Rap_fine->Write("",TObject::kOverwrite); 
H_atop_mass    ->Write("",TObject::kOverwrite); 
H_top_jet_pt       ->Write("",TObject::kOverwrite);
H_top_jet_pt_fine  ->Write("",TObject::kOverwrite);
H_top_jet_eta      ->Write("",TObject::kOverwrite);
H_top_jet_phi      ->Write("",TObject::kOverwrite);
H_top_jet_Rap      ->Write("",TObject::kOverwrite);
H_top_jet_Rap_fine ->Write("",TObject::kOverwrite);
H_atop_jet_pt      ->Write("",TObject::kOverwrite);
H_atop_jet_pt_fine ->Write("",TObject::kOverwrite);
H_atop_jet_eta     ->Write("",TObject::kOverwrite);
H_atop_jet_phi     ->Write("",TObject::kOverwrite);
H_atop_jet_Rap     ->Write("",TObject::kOverwrite);
H_atop_jet_Rap_fine->Write("",TObject::kOverwrite);
H_MET_pt          ->Write("",TObject::kOverwrite); 
H_MET_phi         ->Write("",TObject::kOverwrite); 
H_DR_lep_Nu       ->Write("",TObject::kOverwrite); 
H_DR_W_bjet       ->Write("",TObject::kOverwrite); 
H_DPz_Nu_mc       ->Write("",TObject::kOverwrite); 
H_DPx_Nu_mc       ->Write("",TObject::kOverwrite); 
H_DPy_Nu_mc       ->Write("",TObject::kOverwrite); 
H_Steps           ->Write("",TObject::kOverwrite); 

H_S1_lep_pt       ->Write("",TObject::kOverwrite); 
H_S1_lep_eta      ->Write("",TObject::kOverwrite); 
H_S1_lep_phi      ->Write("",TObject::kOverwrite); 
H_S1_lep_id       ->Write("",TObject::kOverwrite); 
H_N_lep           ->Write("",TObject::kOverwrite); 
H_S1_jet_pt       ->Write("",TObject::kOverwrite); 
H_S1_jet_eta      ->Write("",TObject::kOverwrite); 
H_S1_jet_phi      ->Write("",TObject::kOverwrite); 
H_S1_jet_id       ->Write("",TObject::kOverwrite); 
H_N_jet           ->Write("",TObject::kOverwrite); 


f->Close();
H_lep_pt          ->Delete();
H_lep_eta         ->Delete();
H_lep_phi         ->Delete();
H_lep_Rap         ->Delete();
H_bjet_pt         ->Delete();
H_bjet_eta        ->Delete();
H_bjet_phi        ->Delete();
H_bjet_Rap        ->Delete();
H_Nu_pt           ->Delete();
H_Nu_eta          ->Delete();
H_Nu_phi          ->Delete();
H_Nu_Rap          ->Delete();
H_W_pt            ->Delete();
H_W_eta           ->Delete();
H_W_phi           ->Delete();
H_W_Rap           ->Delete();
H_W_mass          ->Delete();
H_top_pt          ->Delete();
H_top_pt_fine     ->Delete();
H_top_eta         ->Delete();
H_top_phi         ->Delete();
H_top_Rap         ->Delete();
H_top_Rap_fine    ->Delete();
H_top_mass        ->Delete();
H_atop_pt      ->Delete();
H_atop_pt_fine ->Delete();
H_atop_eta     ->Delete();
H_atop_phi     ->Delete();
H_atop_Rap     ->Delete();
H_atop_Rap_fine->Delete();
H_atop_mass    ->Delete();
H_top_jet_pt       ->Delete();
H_top_jet_pt_fine  ->Delete();
H_top_jet_eta      ->Delete();
H_top_jet_phi      ->Delete();
H_top_jet_Rap      ->Delete();
H_top_jet_Rap_fine ->Delete();
H_atop_jet_pt      ->Delete();
H_atop_jet_pt_fine ->Delete();
H_atop_jet_eta     ->Delete();
H_atop_jet_phi     ->Delete();
H_atop_jet_Rap     ->Delete();
H_atop_jet_Rap_fine->Delete();
H_MET_pt          ->Delete();
H_MET_phi         ->Delete();
H_DR_lep_Nu       ->Delete();
H_DR_W_bjet       ->Delete();
H_DPz_Nu_mc       ->Delete();
H_DPx_Nu_mc       ->Delete();
H_DPy_Nu_mc       ->Delete();
H_Steps           ->Delete();


H_S1_lep_pt       ->Delete(); 
H_S1_lep_eta      ->Delete(); 
H_S1_lep_phi      ->Delete(); 
H_S1_lep_id       ->Delete(); 
H_N_lep           ->Delete(); 
H_S1_jet_pt       ->Delete(); 
H_S1_jet_eta      ->Delete(); 
H_S1_jet_phi      ->Delete(); 
H_S1_jet_id       ->Delete(); 
H_N_jet           ->Delete(); 

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
