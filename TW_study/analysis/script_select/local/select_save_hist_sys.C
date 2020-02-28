#include <TH1.h>
#include <TH1F.h>
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
#include <TGraphAsymmErrors.h>
#include <time.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include "../MC_pileup_weight.C"

const float PI_F=3.14159265358979;
const int Data_range=1; // 1 for all,2 for B-F, 3 for GH
const int Regress=80;//80 or 74 regression
const int Rchest=1;// 1 for muon rchest correction , other is not

long double deltaPhi(long double phi1, long double phi2);
int find_max_pt(vector<float> *pt);
int find_second_pt(vector<float> *pt);
int find_led_jet(vector<float> *pt, vector<float> *eta, vector<float> *phi, vector<float> *mass, vector<int> *loose_ID, TLorentzVector lepton_led, TLorentzVector lepton_sub);
int find_low_led_jet(vector<float> *pt, vector<float> *eta, vector<float> *phi, vector<float> *mass, vector<int> *loose_ID, TLorentzVector lepton_led, TLorentzVector lepton_sub);
int find_forward_led_jet(vector<float> *pt, vector<float> *eta, vector<float> *phi, vector<float> *mass, vector<int> *loose_ID, TLorentzVector lepton_led, TLorentzVector lepton_sub);
int find_sub_jet(vector<float> *pt, vector<float> *eta, vector<float> *phi, vector<float> *mass, vector<int> *loose_ID, TLorentzVector lepton_led, TLorentzVector lepton_sub);
float scale_factor( TH2F* h, float pt, float eta);
float weight_1D( TH1D* h, float value);
float scale_factor_graph( TGraphAsymmErrors* gr, float eta);
void fill_2D(TH2D* &hist , float value1, float value2, float weight);
void fill(TH1D* &hist , float value, float weight);
void fill_hist(TString input_file, TString output_file, TString sample_name, bool is_data=false, bool is_single_ele_data=false, bool is_single_muon_data=false, TString uncert="", int chan=0, bool is_ttbar=false, bool do_trigger_study=false);

void select_save_hist_sys(TString chan, TString s_uncert){
TString input_dir="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/reskim_script/reskim_out/for_plots/";
TString output_dir="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/ntuples/saved_hist/Step2_Final/";
TString str_uncert="";
TString uncertainty="";
int channel=1;//ee is 1, emu is 2, mumu is 3 

////////////////////////////////// trigger ///////////////////////////////////////////////
/*
fill_hist(input_dir+"MET_RunBCDEFGH.root"                        ,output_dir+"ee_"  +"trig_hist_addtrig.root"   ,"RunBCDEFGH"        ,true ,false,false, "trig",1,false,true);
fill_hist(input_dir+"TTTo2L2Nu.root"                             ,output_dir+"ee_"  +"trig_hist_addtrig.root"   ,"TTTo2L2Nu"         ,false,false,false, "trig",1,true ,true);
fill_hist(input_dir+"MET_RunBCDEFGH.root"                        ,output_dir+"emu_" +"trig_hist_addtrig.root"   ,"RunBCDEFGH"        ,true ,false,false, "trig",2,false,true);
fill_hist(input_dir+"TTTo2L2Nu.root"                             ,output_dir+"emu_" +"trig_hist_addtrig.root"   ,"TTTo2L2Nu"         ,false,false,false, "trig",2,true ,true);
fill_hist(input_dir+"MET_RunBCDEFGH.root"                        ,output_dir+"mumu_"+"trig_hist_addtrig.root"   ,"RunBCDEFGH"        ,true ,false,false, "trig",3,false,true);
fill_hist(input_dir+"MET_RunBCDE.root"                           ,output_dir+"mumu_"+"trig_hist_addtrig.root"   ,"RunBCDE"           ,true ,false,false, "trig",3,false,true);
fill_hist(input_dir+"MET_RunFGH.root"                            ,output_dir+"mumu_"+"trig_hist_addtrig.root"   ,"RunFGH"            ,true ,false,false, "trig",3,false,true);
fill_hist(input_dir+"TTTo2L2Nu.root"                             ,output_dir+"mumu_"+"trig_hist_addtrig.root"   ,"TTTo2L2Nu"         ,false,false,false, "trig",3,true ,true);
*/
////////////////////////////////// system uncertainty ///////////////////////////////////////////////


//fill_hist(input_dir+"MuonEG_RunBCDEFGH.root"                     ,output_dir+"emu_" +"sys_hist.root" ,"data"       ,true ,false,false,"nominal",2,false,false);
//fill_hist(input_dir+"TTTo2L2Nu.root"                             ,output_dir+"emu_" +"test.root"     , "TTTo2L2Nu" ,false,false,false,"nominal",2,true,false);
//fill_hist(input_dir+"ST_tW_top_5f_NoFullyHadronicDecays.root"    ,output_dir+"ee_"  +"test.root"     , "TW_top"    ,false,false,false,uncertainty,1,false,false);
vector<TString> v_uncert;
v_uncert.push_back(s_uncert);
//v_uncert.push_back("nominal")             ;
//v_uncert.push_back("PU_scale_up")         ;
//v_uncert.push_back("PU_scale_down")       ;
//v_uncert.push_back("SmearedJetResUp")     ;
//v_uncert.push_back("SmearedJetResDown")   ;
//v_uncert.push_back("JetEnUp")             ;
//v_uncert.push_back("JetEnDown")           ;
//v_uncert.push_back("BtagSFbcUp")          ;
//v_uncert.push_back("BtagSFbcDown")        ;
//v_uncert.push_back("BtagSFudsgUp")        ;
//v_uncert.push_back("BtagSFudsgDown")      ;
//v_uncert.push_back("T1JetEnUp")           ;
//v_uncert.push_back("T1JetEnDown")         ;
//v_uncert.push_back("EleSFReco_up")        ;
//v_uncert.push_back("EleSFReco_down")      ;
//v_uncert.push_back("EleSFID_up")          ;
//v_uncert.push_back("EleSFID_down")        ;
//v_uncert.push_back("MuonSFID_up")         ;
//v_uncert.push_back("MuonSFID_down")       ;
//v_uncert.push_back("MuonSFIso_up")        ;
//v_uncert.push_back("MuonSFIso_down")      ;
//v_uncert.push_back("MuonSFtrack_up")      ;
//v_uncert.push_back("MuonSFtrack_down")    ;
for( unsigned int iv=0;iv<v_uncert.size();iv++){
uncertainty = v_uncert.at(iv);

//////////////////////////////////e e ///////////////////////////////////////////////
if(chan=="ee"){
fill_hist(input_dir+"TT_hdampUP.root"                            ,output_dir+"ee_"  +uncertainty+"_.root", "TT_hdampUP"            ,false,false,false,uncertainty,1,false,false);
/*
if(s_uncert=="nominal"){
fill_hist(input_dir+"DoubleEG_RunBCDEFGH.root"                   ,output_dir+"ee_"  +uncertainty+"_.root","data"                   ,true ,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"SingleElectron_BCDEFGH.root"                ,output_dir+"ee_"  +uncertainty+"_singleEle.root","data"          ,true ,true ,false,uncertainty,1,false,false);
}
fill_hist(input_dir+"DYJetsToLL_M10to50_amc.root"                ,output_dir+"ee_"  +uncertainty+"_.root", "DYJetsToLL_M10to50_amc",false,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"DYJetsToLL_M50_amc.root"                    ,output_dir+"ee_"  +uncertainty+"_.root", "DYJetsToLL_M50_amc"    ,false,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"ST_tW_top_5f_NoFullyHadronicDecays.root"    ,output_dir+"ee_"  +uncertainty+"_.root", "TW_top"                ,false,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"ST_tW_antitop_5f_NoFullyHadronicDecays.root",output_dir+"ee_"  +uncertainty+"_.root", "TW_antitop"            ,false,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"TTTo2L2Nu.root"                             ,output_dir+"ee_"  +uncertainty+"_.root", "TTTo2L2Nu"             ,false,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"TTWJetsToQQ.root"                           ,output_dir+"ee_"  +uncertainty+"_.root", "TTWJetsToQQ"           ,false,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"TTWJetsToLNu.root"                          ,output_dir+"ee_"  +uncertainty+"_.root", "TTWJetsToLNu"          ,false,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"TTZToLLNuNu.root"                           ,output_dir+"ee_"  +uncertainty+"_.root", "TTZToLLNuNu"           ,false,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"TTZToQQ.root"                               ,output_dir+"ee_"  +uncertainty+"_.root", "TTZToQQ"               ,false,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"TTGJets.root"                               ,output_dir+"ee_"  +uncertainty+"_.root", "TTGJets"               ,false,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"WJet_mad.root"                              ,output_dir+"ee_"  +uncertainty+"_.root", "WJet_mad"              ,false,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"WG_LNuG.root"                               ,output_dir+"ee_"  +uncertainty+"_.root", "WG_LNuG"               ,false,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"WWTo2L2Nu.root"                             ,output_dir+"ee_"  +uncertainty+"_.root", "WWTo2L2Nu"             ,false,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"WZ_2L2Q.root"                               ,output_dir+"ee_"  +uncertainty+"_.root", "WZ_2L2Q"               ,false,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"WZ_3LNu.root"                               ,output_dir+"ee_"  +uncertainty+"_.root", "WZ_3LNu"               ,false,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"ZZ_2L2Nu.root"                              ,output_dir+"ee_"  +uncertainty+"_.root", "ZZ_2L2Nu"              ,false,false,false,uncertainty,1,false,false);
fill_hist(input_dir+"ZZ_4L.root"                                 ,output_dir+"ee_"  +uncertainty+"_.root", "ZZ_4L"                 ,false,false,false,uncertainty,1,false,false);
*/
}

//////////////////////////////////e  mu /////////////////////////////////////////////uncertainty+/_
if(chan=="emu"){
fill_hist(input_dir+"TT_hdampUP.root"                            ,output_dir+"emu_" +uncertainty+"_.root", "TT_hdampUP"            ,false,false,false,uncertainty,2,false,false);
/*
if(s_uncert=="nominal"){
fill_hist(input_dir+"MuonEG_RunBCDEFGH.root"                     ,output_dir+"emu_" +uncertainty+"_.root", "data"                  ,true ,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"SingleElectron_BCDEFGH.root"                ,output_dir+"emu_" +uncertainty+"_singleEle.root","data"          ,true ,true ,false,uncertainty,2,false,false);
fill_hist(input_dir+"SingleMuon_BCDEFGH.root"                    ,output_dir+"emu_" +uncertainty+"_singleMuon.root","data"         ,true ,false,true ,uncertainty,2,false,false);
}
fill_hist(input_dir+"DYJetsToLL_M10to50_amc.root"                ,output_dir+"emu_" +uncertainty+"_.root", "DYJetsToLL_M10to50_amc",false,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"DYJetsToLL_M50_amc.root"                    ,output_dir+"emu_" +uncertainty+"_.root", "DYJetsToLL_M50_amc"    ,false,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"ST_tW_top_5f_NoFullyHadronicDecays.root"    ,output_dir+"emu_" +uncertainty+"_.root", "TW_top"                ,false,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"ST_tW_antitop_5f_NoFullyHadronicDecays.root",output_dir+"emu_" +uncertainty+"_.root", "TW_antitop"            ,false,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"TTTo2L2Nu.root"                             ,output_dir+"emu_" +uncertainty+"_.root", "TTTo2L2Nu"             ,false,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"TTWJetsToQQ.root"                           ,output_dir+"emu_" +uncertainty+"_.root", "TTWJetsToQQ"           ,false,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"TTWJetsToLNu.root"                          ,output_dir+"emu_" +uncertainty+"_.root", "TTWJetsToLNu"          ,false,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"TTZToLLNuNu.root"                           ,output_dir+"emu_" +uncertainty+"_.root", "TTZToLLNuNu"           ,false,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"TTZToQQ.root"                               ,output_dir+"emu_" +uncertainty+"_.root", "TTZToQQ"               ,false,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"TTGJets.root"                               ,output_dir+"emu_" +uncertainty+"_.root", "TTGJets"               ,false,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"WJet_mad.root"                              ,output_dir+"emu_" +uncertainty+"_.root", "WJet_mad"              ,false,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"WG_LNuG.root"                               ,output_dir+"emu_" +uncertainty+"_.root", "WG_LNuG"               ,false,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"WWTo2L2Nu.root"                             ,output_dir+"emu_" +uncertainty+"_.root", "WWTo2L2Nu"             ,false,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"WZ_2L2Q.root"                               ,output_dir+"emu_" +uncertainty+"_.root", "WZ_2L2Q"               ,false,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"WZ_3LNu.root"                               ,output_dir+"emu_" +uncertainty+"_.root", "WZ_3LNu"               ,false,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"ZZ_2L2Nu.root"                              ,output_dir+"emu_" +uncertainty+"_.root", "ZZ_2L2Nu"              ,false,false,false,uncertainty,2,false,false);
fill_hist(input_dir+"ZZ_4L.root"                                 ,output_dir+"emu_" +uncertainty+"_.root", "ZZ_4L"                 ,false,false,false,uncertainty,2,false,false);
*/
}

//////////////////////////////////mu mu /////////////////////////////////////////////uncertainty+/_
if(chan=="mumu"){
fill_hist(input_dir+"TT_hdampUP.root"                            ,output_dir+"mumu_"  +uncertainty+"_.root", "TT_hdampUP"          ,false,false,false,uncertainty,3,false,false);
/*
if(s_uncert=="nominal"){
fill_hist(input_dir+"DoubleMuon_RunBCDEFGH.root"                 ,output_dir+"mumu_"+uncertainty+"_.root", "data"                  ,true ,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"SingleMuon_BCDEFGH.root"                    ,output_dir+"mumu_"+uncertainty+"_singleMuon.root","data"         ,true ,false,true ,uncertainty,3,false,false);
}
fill_hist(input_dir+"DYJetsToLL_M10to50_amc.root"                ,output_dir+"mumu_"+uncertainty+"_.root", "DYJetsToLL_M10to50_amc",false,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"DYJetsToLL_M50_amc.root"                    ,output_dir+"mumu_"+uncertainty+"_.root", "DYJetsToLL_M50_amc"    ,false,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"ST_tW_top_5f_NoFullyHadronicDecays.root"    ,output_dir+"mumu_"+uncertainty+"_.root", "TW_top"                ,false,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"ST_tW_antitop_5f_NoFullyHadronicDecays.root",output_dir+"mumu_"+uncertainty+"_.root", "TW_antitop"            ,false,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"TTTo2L2Nu.root"                             ,output_dir+"mumu_"+uncertainty+"_.root", "TTTo2L2Nu"             ,false,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"TTWJetsToQQ.root"                           ,output_dir+"mumu_"+uncertainty+"_.root", "TTWJetsToQQ"           ,false,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"TTWJetsToLNu.root"                          ,output_dir+"mumu_"+uncertainty+"_.root", "TTWJetsToLNu"          ,false,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"TTZToLLNuNu.root"                           ,output_dir+"mumu_"+uncertainty+"_.root", "TTZToLLNuNu"           ,false,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"TTZToQQ.root"                               ,output_dir+"mumu_"+uncertainty+"_.root", "TTZToQQ"               ,false,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"TTGJets.root"                               ,output_dir+"mumu_"+uncertainty+"_.root", "TTGJets"               ,false,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"WJet_mad.root"                              ,output_dir+"mumu_"+uncertainty+"_.root", "WJet_mad"              ,false,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"WG_LNuG.root"                               ,output_dir+"mumu_"+uncertainty+"_.root", "WG_LNuG"               ,false,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"WWTo2L2Nu.root"                             ,output_dir+"mumu_"+uncertainty+"_.root", "WWTo2L2Nu"             ,false,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"WZ_2L2Q.root"                               ,output_dir+"mumu_"+uncertainty+"_.root", "WZ_2L2Q"               ,false,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"WZ_3LNu.root"                               ,output_dir+"mumu_"+uncertainty+"_.root", "WZ_3LNu"               ,false,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"ZZ_2L2Nu.root"                              ,output_dir+"mumu_"+uncertainty+"_.root", "ZZ_2L2Nu"              ,false,false,false,uncertainty,3,false,false);
fill_hist(input_dir+"ZZ_4L.root"                                 ,output_dir+"mumu_"+uncertainty+"_.root", "ZZ_4L"                 ,false,false,false,uncertainty,3,false,false);
*/
}

}


}

void fill_hist(TString input_file, TString output_file, TString sample_name, bool is_data, bool is_single_ele_data, bool is_single_muon_data, TString uncert , int chan, bool is_ttbar, bool do_trigger_study){

std::cout<<"For "<<uncert<<std::endl;

TH1::SetDefaultSumw2(kTRUE);
TString t_name="LL";
TChain *t = new TChain(t_name);
t->Add(input_file);

TString name=uncert+"__"+sample_name+"__";

   int           pv_n         = 0 ;
   vector<int>   *pv_isValid       =0;
   vector<int>   *pv_ndof          =0;
   vector<int>   *pv_nTracks       =0;
   vector<int>   *pv_totTrackSize  =0;
   vector<float> *pv_normalizedChi2=0;


   int   PU_true     = 0 ;
   int   event_sign  = 0 ;
   
   float rho         = 0 ;

   float Met_et      = 0 ; 
   float Met_phi     = 0 ;
   float MET_T1Txy_et          =0; 
   float MET_T1Txy_phi         =0; 
   float MET_T1Txy_significance=0; 
 

   int trig_Ele23_Ele12  =0; 
   int trig_DEle33       =0; 
   int trig_DEle33_MW    =0; 
   int trig_DEle33_CaloId=0; 
   int trig_Ele27_WPTight=0; 
   int trig_Mu8_Ele23    =0; 
   int trig_Mu23_Ele12   =0; 
   int trig_Mu8_Ele23_DZ =0; 
   int trig_Mu23_Ele12_DZ=0; 
   int trig_Mu30_Ele30   =0; 
   int trig_Mu33_Ele33   =0; 
   int trig_Mu17_TkMu8   =0; 
   int trig_Mu17_Mu8     =0; 
   int trig_Mu17_TkMu8_DZ=0; 
   int trig_Mu17_Mu8_DZ  =0; 
   int trig_Mu30_TkMu11  =0; 
   int trig_IsoMu24      =0; 
   int trig_IsoTkMu24    =0; 
   int trig_HLT_PFHT300_PFMET110         =0; 
   int trig_HLT_MET200                   =0; 
   int trig_HLT_PFMET300                 =0; 
   int trig_HLT_PFMET120_PFMHT120_IDTight=0; 
   int trig_HLT_PFMET170_HBHECleaned     =0; 
   int trig_HLT_MET75_IsoTrk50           =0; 


   vector<float> *electrons_pt      =0; 
   vector<float> *electrons_eta     =0; 
   vector<float> *electrons_sc_eta  =0; 
   vector<float> *electrons_phi     =0; 
   vector<int>   *electrons_charge  =0; 
   vector<int>   *electrons_tight_ID=0; 
   vector<float> *muons_pt          =0; 
   vector<float> *muons_eta         =0; 
   vector<float> *muons_phi         =0; 
   vector<int>   *muons_charge      =0; 
   vector<int>   *muons_tight_ID    =0; 
   vector<int>   *muons_pfIso       =0; 
   vector<float> *muons_rochester_sf=0; 


   vector<float> *jets_pt      =0;
   vector<float> *jets_eta     =0;
   vector<float> *jets_phi     =0;
   vector<float> *jets_mass    =0;
   vector<float> *jets_energy  =0;
   vector<float> *jets_CSV     =0;
   vector<int>   *jets_loose_ID=0;
   vector<float> *jets_BtagSF  =0; 


 
   int trig_Flag_HBHENoiseFilter                   =0; 
   int trig_Flag_HBHENoiseIsoFilter                =0; 
   int trig_Flag_CSCTightHaloFilter                =0; 
   int trig_Flag_CSCTightHaloTrkMuUnvetoFilter     =0; 
   int trig_Flag_CSCTightHalo2015Filter            =0; 
   int trig_Flag_globalTightHalo2016Filter         =0; 
   int trig_Flag_globalSuperTightHalo2016Filter    =0; 
   int trig_Flag_goodVertices                      =0; 
   int trig_Flag_BadPFMuonFilter                   =0; 
   int trig_Flag_BadChargedCandidateFilter         =0; 
   int trig_Flag_eeBadScFilter                     =0; 
   int trig_Flag_HcalStripHaloFilter               =0; 
   int trig_Flag_hcalLaserEventFilter              =0; 
   int trig_Flag_EcalDeadCellTriggerPrimitiveFilter=0; 
   int trig_Flag_EcalDeadCellBoundaryEnergyFilter  =0; 
   int trig_Flag_ecalLaserCorrFilter               =0; 
   int trig_Flag_chargedHadronTrackResolutionFilter=0; 
   int trig_Flag_muonBadTrackFilter                =0; 
   int trig_Flag_trkPOG_manystripclus53X           =0; 
   int trig_Flag_trkPOG_toomanystripclus53X        =0; 
   int trig_Flag_trkPOG_logErrorTooManyClusters    =0; 
   int trig_Flag_METFilters                        =0;

   float w_LHE            = 0 ;
   float w_PU_combined    = 0 ;
   float w_PU_silver_down = 0 ; 
   float w_PU_silver_up   = 0 ;

   ULong_t ev_run=0;
   ULong_t ev_event=0;
   ULong_t ev_luminosityBlock=0;
 
   t->SetBranchAddress("ev_run"                     , &ev_run                ) ;
   t->SetBranchAddress("ev_event"                   , &ev_event              ) ;
   t->SetBranchAddress("ev_luminosityBlock"         , &ev_luminosityBlock    ) ;
   t->SetBranchAddress("pv_n"                       , &pv_n                  ) ;
   t->SetBranchAddress("pv_isValid"                 , &pv_isValid            ) ;
   t->SetBranchAddress("pv_ndof"                    , &pv_ndof               ) ;
   t->SetBranchAddress("pv_nTracks"                 , &pv_nTracks            ) ;
   t->SetBranchAddress("pv_totTrackSize"            , &pv_totTrackSize       ) ;
   t->SetBranchAddress("pv_normalizedChi2"          , &pv_normalizedChi2     ) ;
   t->SetBranchAddress("PU_true"                    , &PU_true               ) ;
   t->SetBranchAddress("event_sign"                 , &event_sign            ) ;
   t->SetBranchAddress("trig_Flag_HBHENoiseFilter_accept"                   , &trig_Flag_HBHENoiseFilter                     ) ;
   t->SetBranchAddress("trig_Flag_HBHENoiseIsoFilter_accept"                , &trig_Flag_HBHENoiseIsoFilter                  ) ;
   t->SetBranchAddress("trig_Flag_CSCTightHaloFilter_accept"                , &trig_Flag_CSCTightHaloFilter                  ) ;
   t->SetBranchAddress("trig_Flag_CSCTightHaloTrkMuUnvetoFilter_accept"     , &trig_Flag_CSCTightHaloTrkMuUnvetoFilter       ) ;
   t->SetBranchAddress("trig_Flag_CSCTightHalo2015Filter_accept"            , &trig_Flag_CSCTightHalo2015Filter              ) ;
   t->SetBranchAddress("trig_Flag_globalTightHalo2016Filter_accept"         , &trig_Flag_globalTightHalo2016Filter           ) ;
   t->SetBranchAddress("trig_Flag_globalSuperTightHalo2016Filter_accept"    , &trig_Flag_globalSuperTightHalo2016Filter      ) ;
   t->SetBranchAddress("trig_Flag_goodVertices_accept"                      , &trig_Flag_goodVertices                        ) ;
   t->SetBranchAddress("trig_Flag_BadPFMuonFilter_accept"                   , &trig_Flag_BadPFMuonFilter                     ) ;
   t->SetBranchAddress("trig_Flag_BadChargedCandidateFilter_accept"         , &trig_Flag_BadChargedCandidateFilter           ) ;
   t->SetBranchAddress("trig_Flag_eeBadScFilter_accept"                     , &trig_Flag_eeBadScFilter                       ) ;
   t->SetBranchAddress("trig_Flag_HcalStripHaloFilter_accept"               , &trig_Flag_HcalStripHaloFilter                 ) ;
   t->SetBranchAddress("trig_Flag_hcalLaserEventFilter_accept"              , &trig_Flag_hcalLaserEventFilter                ) ;
   t->SetBranchAddress("trig_Flag_EcalDeadCellTriggerPrimitiveFilter_accept", &trig_Flag_EcalDeadCellTriggerPrimitiveFilter  ) ;
   t->SetBranchAddress("trig_Flag_EcalDeadCellBoundaryEnergyFilter_accept"  , &trig_Flag_EcalDeadCellBoundaryEnergyFilter    ) ;
   t->SetBranchAddress("trig_Flag_ecalLaserCorrFilter_accept"               , &trig_Flag_ecalLaserCorrFilter                 ) ;
   t->SetBranchAddress("trig_Flag_chargedHadronTrackResolutionFilter_accept", &trig_Flag_chargedHadronTrackResolutionFilter  ) ;
   t->SetBranchAddress("trig_Flag_muonBadTrackFilter_accept"                , &trig_Flag_muonBadTrackFilter                  ) ;
   t->SetBranchAddress("trig_Flag_trkPOG_manystripclus53X_accept"           , &trig_Flag_trkPOG_manystripclus53X             ) ;
   t->SetBranchAddress("trig_Flag_trkPOG_toomanystripclus53X_accept"        , &trig_Flag_trkPOG_toomanystripclus53X          ) ;
   t->SetBranchAddress("trig_Flag_trkPOG_logErrorTooManyClusters_accept"    , &trig_Flag_trkPOG_logErrorTooManyClusters      ) ;
   t->SetBranchAddress("trig_Flag_METFilters_accept"                        , &trig_Flag_METFilters                          ) ;
   t->SetBranchAddress("rho"        , &rho           ) ;

   t->SetBranchAddress("trig_Ele23_Ele12"    , &trig_Ele23_Ele12   ) ;
   t->SetBranchAddress("trig_DEle33"         , &trig_DEle33        ) ;
   t->SetBranchAddress("trig_DEle33_MW"      , &trig_DEle33_MW     ) ;
   t->SetBranchAddress("trig_DEle33_CaloId"  , &trig_DEle33_CaloId ) ;
   t->SetBranchAddress("trig_Ele27"          , &trig_Ele27_WPTight ) ;
   t->SetBranchAddress("trig_Mu8_Ele23"      , &trig_Mu8_Ele23     ) ;
   t->SetBranchAddress("trig_Mu23_Ele12"     , &trig_Mu23_Ele12    ) ;
   t->SetBranchAddress("trig_Mu8_Ele23_DZ"   , &trig_Mu8_Ele23_DZ  ) ;
   t->SetBranchAddress("trig_Mu23_Ele12_DZ"  , &trig_Mu23_Ele12_DZ ) ;
   t->SetBranchAddress("trig_Mu30_Ele30"     , &trig_Mu30_Ele30    ) ;
   t->SetBranchAddress("trig_Mu33_Ele33"     , &trig_Mu33_Ele33    ) ;
   t->SetBranchAddress("trig_Mu17_TkMu8"     , &trig_Mu17_TkMu8    ) ;
   t->SetBranchAddress("trig_Mu17_Mu8"       , &trig_Mu17_Mu8      ) ;
   t->SetBranchAddress("trig_Mu17_TkMu8_DZ"  , &trig_Mu17_TkMu8_DZ ) ;
   t->SetBranchAddress("trig_Mu17_Mu8_DZ"    , &trig_Mu17_Mu8_DZ   ) ;
   t->SetBranchAddress("trig_Mu30_TkMu11"    , &trig_Mu30_TkMu11   ) ;
   t->SetBranchAddress("trig_IsoMu24"        , &trig_IsoMu24       ) ;
   t->SetBranchAddress("trig_IsoTkMu24"      , &trig_IsoTkMu24     ) ;
   t->SetBranchAddress("trig_HLT_PFHT300_PFMET110"          , &trig_HLT_PFHT300_PFMET110           ) ;
   t->SetBranchAddress("trig_HLT_MET200"                    , &trig_HLT_MET200                     ) ;
   t->SetBranchAddress("trig_HLT_PFMET300"                  , &trig_HLT_PFMET300                   ) ;
   t->SetBranchAddress("trig_HLT_PFMET120_PFMHT120_IDTight" , &trig_HLT_PFMET120_PFMHT120_IDTight  ) ;
   t->SetBranchAddress("trig_HLT_PFMET170_HBHECleaned"      , &trig_HLT_PFMET170_HBHECleaned       ) ;
   t->SetBranchAddress("trig_HLT_MET75_IsoTrk50"            , &trig_HLT_MET75_IsoTrk50             ) ;
   if(Regress==80){
   t->SetBranchAddress("electrons_pt"        , &electrons_pt                ) ;
   t->SetBranchAddress("electrons_eta"       , &electrons_eta               ) ;
   t->SetBranchAddress("electrons_sc_eta"    , &electrons_sc_eta            ) ;
   t->SetBranchAddress("electrons_phi"       , &electrons_phi               ) ;
   t->SetBranchAddress("electrons_charge"    , &electrons_charge            ) ;
   t->SetBranchAddress("electrons_tight_ID"  , &electrons_tight_ID          ) ;
   }
   else{
   t->SetBranchAddress("electrons_74_pt"        , &electrons_pt             ) ;
   t->SetBranchAddress("electrons_74_eta"       , &electrons_eta            ) ;
   t->SetBranchAddress("electrons_74_sc_eta"    , &electrons_sc_eta         ) ;
   t->SetBranchAddress("electrons_74_phi"       , &electrons_phi            ) ;
   t->SetBranchAddress("electrons_74_charge"    , &electrons_charge         ) ;
   t->SetBranchAddress("electrons_74_tight_ID"  , &electrons_tight_ID       ) ;
   }
   if(Rchest==1){
   t->SetBranchAddress("muons_pt_rochest"    , &muons_pt                    ) ;
   }
   else{
   t->SetBranchAddress("muons_pt"            , &muons_pt                    ) ;
   }
   t->SetBranchAddress("muons_eta"           , &muons_eta                   ) ;
   t->SetBranchAddress("muons_phi"           , &muons_phi                   ) ;
   t->SetBranchAddress("muons_charge"        , &muons_charge                ) ;
   t->SetBranchAddress("muons_tight_ID"      , &muons_tight_ID              ) ;
   t->SetBranchAddress("muons_pfIso"         , &muons_pfIso                 ) ;
   t->SetBranchAddress("muons_rochester_sf"  , &muons_rochester_sf          ) ;
   t->SetBranchAddress("jets_eta"            , &jets_eta                    ) ;
   t->SetBranchAddress("jets_phi"            , &jets_phi                    ) ;
   t->SetBranchAddress("jets_mass"           , &jets_mass                   ) ;
   t->SetBranchAddress("jets_CSV"            , &jets_CSV                    ) ;
   t->SetBranchAddress("jets_loose_ID"       , &jets_loose_ID               ) ;
   /////////// jet scale and smear ///////////////////
   if(uncert=="SmearedJetResUp"){
   t->SetBranchAddress("jets_SmearedJetResUp_pt"       , &jets_pt           ) ;
   t->SetBranchAddress("jets_SmearedJetResUp_energy"   , &jets_energy       ) ;
   }
   else if(uncert=="SmearedJetResDown"){
   t->SetBranchAddress("jets_SmearedJetResDown_pt"     , &jets_pt           ) ;
   t->SetBranchAddress("jets_SmearedJetResDown_energy" , &jets_energy       ) ;
   }
   else if(uncert=="JetEnUp"){
   t->SetBranchAddress("jets_EnUp_pt"                  , &jets_pt           ) ;
   t->SetBranchAddress("jets_EnUp_energy"              , &jets_energy       ) ;
   }
   else if(uncert=="JetEnDown"){
   t->SetBranchAddress("jets_EnDown_pt"                , &jets_pt           ) ;
   t->SetBranchAddress("jets_EnDown_energy"            , &jets_energy       ) ;
   }
   else{
   t->SetBranchAddress("jets_pt"                       , &jets_pt           ) ;
   t->SetBranchAddress("jets_energy"                   , &jets_energy       ) ;
   }
   /////////// Btag sf ///////////////////
   if(uncert=="BtagSFbcUp"){
   t->SetBranchAddress("jets_BtagSFbcUp_medium"        , &jets_BtagSF       ) ;
   }
   else if(uncert=="BtagSFbcDown"){
   t->SetBranchAddress("jets_BtagSFbcDown_medium"      , &jets_BtagSF       ) ;
   }
   else if(uncert=="BtagSFudsgUp"){
   t->SetBranchAddress("jets_BtagSFudsgUp_medium"      , &jets_BtagSF       ) ;
   }
   else if(uncert=="BtagSFudsgDown"){
   t->SetBranchAddress("jets_BtagSFudsgDown_medium"    , &jets_BtagSF       ) ;
   }
   else{
   t->SetBranchAddress("jets_BtagSF_medium"            , &jets_BtagSF       ) ;
   }
   /////////// MET   ///////////////////
   t->SetBranchAddress("Met_et"                , &Met_et                 ) ;
   t->SetBranchAddress("Met_phi"               , &Met_phi                ) ;
   t->SetBranchAddress("MET_T1Txy_significance", &MET_T1Txy_significance ) ;
   if(uncert=="T1JetEnUp"){
   t->SetBranchAddress("MET_T1JetEnUp_Pt_out"   , &MET_T1Txy_et          ) ;
   t->SetBranchAddress("MET_T1JetEnUp_phi_out"  , &MET_T1Txy_phi         ) ;
   }
   else if(uncert=="T1JetEnDown"){
   t->SetBranchAddress("MET_T1JetEnDown_Pt_out" , &MET_T1Txy_et          ) ;
   t->SetBranchAddress("MET_T1JetEnDown_phi_out", &MET_T1Txy_phi         ) ;
   }
   else{
   t->SetBranchAddress("MET_T1Txy_et"          , &MET_T1Txy_et           ) ;
   t->SetBranchAddress("MET_T1Txy_phi"         , &MET_T1Txy_phi          ) ;
   }

   t->SetBranchAddress("w_LHE"           , &w_LHE             ) ;
   t->SetBranchAddress("w_PU_combined"   , &w_PU_combined     ) ;
   t->SetBranchAddress("w_PU_silver_up"  , &w_PU_silver_up    ) ;
   t->SetBranchAddress("w_PU_silver_down", &w_PU_silver_down  ) ;

////// for trigger sf ////////////
const float ele_eta_bin[4]={0,1.4442,1.566,2.5};
const float mu_eta_bin[3] ={0,1.2,2.4};
const float pt_led_bin[18]={25,35,45,55,65,75,85,95,105,115,125,135,145,165,185,205,255,305}; 
const float pt_sub_bin[18]={20,30,40,50,60,70,80,90,100,110,120,130,140,160,180,200,250,300}; 
const float MET_bin[11] ={0,10,20,30,40,60,80,100,150,200,300};
const float Nvtx_bin[13] ={0,5,10,15,20,25,30,35,40,45,50,55,60};
TH2D *H2_pt1_pt2             =new TH2D(name+"H2_pt1_pt2"             ,"",17,pt_led_bin,17,pt_sub_bin);
TH2D *H2_pt1_pt2_pass        =new TH2D(name+"H2_pt1_pt2_pass"        ,"",17,pt_led_bin,17,pt_sub_bin);
TH2D *H2_ee_eta1_eta2        =new TH2D(name+"H2_ee_eta1_eta2"        ,"",10,-2.5,2.5,10,-2.5,2.5);
TH2D *H2_emu_eta1_eta2       =new TH2D(name+"H2_emu_eta1_eta2"       ,"",10,-2.5,2.5,10,-2.5,2.5);
TH2D *H2_mumu_eta1_eta2      =new TH2D(name+"H2_mumu_eta1_eta2"      ,"",10,-2.5,2.5,10,-2.5,2.5);
TH2D *H2_ee_eta1_eta2_pass   =new TH2D(name+"H2_ee_eta1_eta2_pass"   ,"",10,-2.5,2.5,10,-2.5,2.5);
TH2D *H2_emu_eta1_eta2_pass  =new TH2D(name+"H2_emu_eta1_eta2_pass"  ,"",10,-2.5,2.5,10,-2.5,2.5);
TH2D *H2_mumu_eta1_eta2_pass =new TH2D(name+"H2_mumu_eta1_eta2_pass" ,"",10,-2.5,2.5,10,-2.5,2.5);
TH2D *H2_MET_Nvtx            =new TH2D(name+"H2_MET_Nvtx"            ,"",10,MET_bin,12,Nvtx_bin);
TH2D *H2_MET_Nvtx_pass       =new TH2D(name+"H2_MET_Nvtx_pass"       ,"",10,MET_bin,12,Nvtx_bin);
TH2D *H2_Njet_Nbjet          =new TH2D(name+"H2_Njet_Nbjet"          ,"",7,0,7,4,0,4);
TH2D *H2_Njet_Nbjet_pass     =new TH2D(name+"H2_Njet_Nbjet_pass"     ,"",7,0,7,4,0,4);

TH1D *H_ee_region            =new TH1D(name+"H_ee_region"        ,"",4,0,4);
TH1D *H_ee_region_pass       =new TH1D(name+"H_ee_region_pass"   ,"",4,0,4);
TH1D *H_emu_region           =new TH1D(name+"H_emu_region"       ,"",4,0,4);
TH1D *H_emu_region_pass      =new TH1D(name+"H_emu_region_pass"  ,"",4,0,4);
TH1D *H_mumu_region          =new TH1D(name+"H_mumu_region"      ,"",4,0,4);
TH1D *H_mumu_region_pass     =new TH1D(name+"H_mumu_region_pass" ,"",4,0,4);
///////////////////////////////////////////
TH2D *H2_Mll_MET        =new TH2D("H2_Mll_MET"        ,"",140,20,300,60,0,300);
TH2D *H2_Ptll_MET       =new TH2D("H2_Ptll_MET"       ,"",100,0,200 ,60,0,300);
TH2D *H2_Mll_METSF      =new TH2D("H2_Mll_METSF"      ,"",140,20,300,20,0,20 );
TH2D *H2_Ptll_Dphi      =new TH2D("H2_Ptll_Dphi"      ,"",100,0,200 ,40,0,4);
TH2D *H2_MET_Dphi       =new TH2D("H2_MET_Dphi"       ,"",60 ,0,300 ,40,0,4);
TH2D *H2_Txy_MET_phi    =new TH2D("H2_Txy_MET_phi"    ,"",50 ,0,100 ,80,-4,4);

TH1D *H_Mll                =new TH1D(name+"H_Mll"             ,"",60 ,0 ,300);
TH1D *H_Mll_Zpeak          =new TH1D(name+"H_Mll_Zpeak"       ,"",60 ,60,120);
TH1D *H_Ptll               =new TH1D(name+"H_Ptll"            ,"",40 ,0 ,200);
TH1D *H_Rll                =new TH1D(name+"H_Rll"             ,"",60,-3 ,3  );
TH1D *H_Ptll_phi           =new TH1D(name+"H_Ptll_phi"        ,"",35 ,-3.5,3.5);
TH1D *H_ll_Dphi            =new TH1D(name+"H_ll_Dphi"         ,"",40 ,0 ,4  );
TH1D *H_ll_DR              =new TH1D(name+"H_ll_DR"           ,"",120,0 ,6  );
TH1D *H_lepton_led_pt      =new TH1D(name+"H_lepton_led_pt"   ,"",30 ,0 ,150);
TH1D *H_lepton_led_eta     =new TH1D(name+"H_lepton_led_eta"  ,"",51 ,-2.55,2.55);
TH1D *H_lepton_led_phi     =new TH1D(name+"H_lepton_led_phi"  ,"",35 ,-3.5 ,3.5 );
TH1D *H_lepton_sub_pt      =new TH1D(name+"H_lepton_sub_pt"   ,"",30 ,0 ,150);
TH1D *H_lepton_sub_eta     =new TH1D(name+"H_lepton_sub_eta"  ,"",51 ,-2.55,2.55);
TH1D *H_lepton_sub_phi     =new TH1D(name+"H_lepton_sub_phi"  ,"",35 ,-3.5,3.5);
TH1D *H_jet_led_pt         =new TH1D(name+"H_jet_led_pt"      ,"",140 ,20,300);
TH1D *H_jet_led_eta        =new TH1D(name+"H_jet_led_eta"     ,"",60 ,-3,3  );
TH1D *H_jet_led_phi        =new TH1D(name+"H_jet_led_phi"     ,"",100,-5,5  );
TH1D *H_jet_sub_pt         =new TH1D(name+"H_jet_sub_pt"      ,"",140 ,20,300);
TH1D *H_jet_sub_eta        =new TH1D(name+"H_jet_sub_eta"     ,"",60 ,-3,3  );
TH1D *H_jet_sub_phi        =new TH1D(name+"H_jet_sub_phi"     ,"",100,-5,5  );
TH1D *H_jet_forward_led_pt =new TH1D(name+"H_jet_forward_led_pt"  ,"",150 ,0,300);
TH1D *H_jet_forward_led_eta=new TH1D(name+"H_jet_forward_led_eta" ,"",60 ,-3,3  );
TH1D *H_jet_low_led_CSV    =new TH1D(name+"H_jet_low_led_CSV"  ,"",100 ,-1,1);
TH1D *H_jet_Bmissed_CSV    =new TH1D(name+"H_jet_Bmissed_CSV"  ,"",100 ,-1,1);

TH1D *H_N_loose_jets       =new TH1D(name+"H_N_loose_jets"    ,"",10 ,0 ,10 );
TH1D *H_N_loose_jets_low   =new TH1D(name+"H_N_loose_jets_low","",10 ,0 ,10 );
TH1D *H_N_b_jets           =new TH1D(name+"H_N_b_jets"        ,"",6  ,0 ,6  );
TH1D *H_N_b_jets_low       =new TH1D(name+"H_N_b_jets_low"    ,"",6  ,0 ,6  );
TH1D *H_N_eta2p4_30_jets   =new TH1D(name+"H_N_eta2p4_30_jets","",6  ,0 ,6  );
TH1D *H_N_eta2p4_40_jets   =new TH1D(name+"H_N_eta2p4_40_jets","",6  ,0 ,6  );
TH1D *H_MET_Et             =new TH1D(name+"H_MET_Et"          ,"",20 ,0 ,200);
TH1D *H_MET_phi            =new TH1D(name+"H_MET_phi"         ,"",35 ,-3.5,3.5);
TH1D *H_MET_Z_phi          =new TH1D(name+"H_MET_Z_phi"       ,"",35 ,0,3.5  );
TH1D *H_MET_T1Txy_et       =new TH1D(name+"H_MET_T1Txy_et"    ,"",20 ,0 ,200 );
TH1D *H_MET_T1Txy_phi      =new TH1D(name+"H_MET_T1Txy_phi"   ,"",35 ,-3.5,3.5);
TH1D *H_MET_Z_T1Txy_phi    =new TH1D(name+"H_MET_Z_T1Txy_phi" ,"",35 ,0,3.5  );
TH1D *H_MET_T1Txy_sf       =new TH1D(name+"H_MET_T1Txy_sf"    ,"",40 ,0 ,20  );
TH1D *H_HT                 =new TH1D(name+"H_HT"              ,"",50 ,0 ,500);
TH1D *H_HT_sys             =new TH1D(name+"H_HT_sys"          ,"",50 ,0 ,500);
TH1D *H_Pt_sys             =new TH1D(name+"H_Pt_sys"          ,"",50 ,0 ,500);
TH1D *H_MT_sys             =new TH1D(name+"H_MT_sys"          ,"",50 ,0 ,500);
TH1D *H_pv_n               =new TH1D(name+"H_pv_n"            ,"",50 ,0 ,50 );
TH1D *H_rho                =new TH1D(name+"H_rho"             ,"",100,0 ,50 );

const Int_t nx = 5;
const char *steps[nx] ={"Dilepton","Z veto","MET",">=2 jets",">=1 b jet"};
TH1D *H_steps           =new TH1D("H_steps","",nx,0,nx);
for (int i=1;i<=nx;i++) H_steps->GetXaxis()->SetBinLabel(i,steps[i-1]);
const Int_t njet = 15;
const char *str_njet[njet] ={"(0,0)","(1,0)","(1,1)","(2,0)","(2,1)","(2,2)","(3,0)","(3,1)","(3,2)","(3,3)","(4,0)","(4,1)","(4,2)","(4,3)","(4,4)"};
TH1D *H_njet_bjet           =new TH1D(name+"H_njet_bjet","",15,0,15);
for (int i=1;i<=njet;i++) H_njet_bjet->GetXaxis()->SetBinLabel(i,str_njet[i-1]);
int N_step_1=0;
int N_step_2=0;
int N_step_3=0;
int N_step_4_1_1=0;
int N_step_4_1_2=0;
int N_step_4_2_1=0;
int N_step_4_2_2=0;
int N_step_4_3=0;
int N_step_5=0;

const float M_Z_PDG=91.188    ;
const float m_el   = 0.000511 ;
const float m_mu   = 0.10566  ;
const float lumi_B2F=19720.82 ;
const float lumi_GH =16146.18 ;
const int RunH=281207;

const float led_pt_threshold=25;
const float sub_pt_threshold=20;
const float jet_pt_threshold=30;
const float MET_cut=40;
const float MET_SF_cut=4;
const float Mass_cut_low=20;
const float Z_cut_low=81;
const float Z_cut_high=101;
const float Btag_WP=0.8484;

bool combine_channel=false;
bool ee_channel  =false;
bool emu_channel =false;
bool mumu_channel=false;
if(chan==0)      combine_channel  =true;
else if(chan==1)      ee_channel  =true;
else if(chan==2) emu_channel =true;
else if(chan==3) mumu_channel=true;

double event_weight=1;
double sf_Ele_reco=1;
double sf_Ele_ID=1;
double sf_Muon_track=1;
double sf_Muon_ID=1;
double sf_Muon_Iso=1;
double sf_Btag    =1;
double sf_trigger =1;
bool do_PU_weight=true;
bool do_Nvtx_reweight=true;
bool use_trigger =true;
bool trigger_study=do_trigger_study;
if (trigger_study) use_trigger =false;
bool use_met_filter=true;
bool apply_sf_Ele_reco  =true;
bool apply_sf_Ele_ID    =true; 
bool apply_sf_Muon_track=true;
bool apply_sf_Muon_ID   =true; 
bool apply_sf_Muon_Iso  =true; 
bool apply_sf_Btag      =true; 
bool apply_sf_trigger   =true;
if(is_data==true || do_trigger_study){
                  do_PU_weight       =false;
                  do_Nvtx_reweight   =false;
                  apply_sf_Ele_reco  =false;
                  apply_sf_Ele_ID    =false;
                  apply_sf_Muon_track=false;
                  apply_sf_Muon_ID   =false;
                  apply_sf_Muon_Iso  =false; 
                  apply_sf_Btag      =false; 
                  apply_sf_trigger   =false;
                 }

//if(is_data==false)do_data_mass_scale=false;
///// fewz /////
//TF1 *fewzKFactor = new TF1("fit","pol3",120,6000);
//fewzKFactor->SetParameters(1.06780e+00,-1.20666e-04,3.22646e-08,-3.94886e-12);
////////
TFile *f_Ele_Reco_Map = new TFile("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/Scale_Factor/egammaEffi.txt_EGM2D_reco.root");
TH2F  *sf_Ele_Reco_Map= (TH2F*)f_Ele_Reco_Map->Get("EGamma_SF2D");
TFile *f_Ele_ID_Map   = new TFile("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/Scale_Factor/egammaEffi.txt_EGM2D_tightID.root");
TH2F  *sf_Ele_ID_Map  = (TH2F*)f_Ele_ID_Map->Get("EGamma_SF2D");

TFile *f_Muon_track   = new TFile("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/Scale_Factor/Tracking_EfficienciesAndSF_BCDEFGH.root");
TGraphAsymmErrors  *sf_Muon_track_gr  = (TGraphAsymmErrors*)f_Muon_track->Get("ratio_eff_eta3_dr030e030_corr");

TFile *f_Muon_ID_B2F_Map   = new TFile("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/Scale_Factor/EfficienciesAndSF_ID_BCDEF.root");
TH2F  *sf_Muon_ID_B2F_Map  = (TH2F*)f_Muon_ID_B2F_Map->Get("MC_NUM_TightID_DEN_genTracks_PAR_pt_eta/abseta_pt_ratio");
TFile *f_Muon_ID_GH_Map   = new TFile("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/Scale_Factor/EfficienciesAndSF_ID_GH.root");
TH2F  *sf_Muon_ID_GH_Map  = (TH2F*)f_Muon_ID_GH_Map->Get("MC_NUM_TightID_DEN_genTracks_PAR_pt_eta/abseta_pt_ratio");
TFile *f_Muon_Iso_B2F_Map   = new TFile("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/Scale_Factor/EfficienciesAndSF_Iso_BCDEF.root");
TH2F  *sf_Muon_Iso_B2F_Map  = (TH2F*)f_Muon_Iso_B2F_Map->Get("TightISO_TightID_pt_eta/abseta_pt_ratio");
TFile *f_Muon_Iso_GH_Map   = new TFile("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/Scale_Factor/EfficienciesAndSF_Iso_GH.root");
TH2F  *sf_Muon_Iso_GH_Map  = (TH2F*)f_Muon_Iso_GH_Map->Get("TightISO_TightID_pt_eta/abseta_pt_ratio");

TFile *Nvtx_Map_ee   = new TFile("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/ee_Nvtx_ratio.root");
TH1D  *w_Nvtx_ee  = (TH1D*)Nvtx_Map_ee->Get("H_pv_n");
TFile *Nvtx_Map_emu  = new TFile("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/emu_Nvtx_ratio.root");
TH1D  *w_Nvtx_emu  = (TH1D*)Nvtx_Map_emu->Get("H_pv_n");
TFile *Nvtx_Map_mumu  = new TFile("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/mumu_Nvtx_ratio.root");
TH1D  *w_Nvtx_mumu  = (TH1D*)Nvtx_Map_mumu->Get("H_pv_n");
ofstream fout("Wx_tw.txt");
std::cout<<"sample:"<<sample_name<<",total event="<<t->GetEntries()<<std::endl;
for(long long i=0;i<t->GetEntries();i++){
t->GetEntry(i);
//if(ev_event!=2607988 && ev_event!=2607991  && ev_event!=2607998  && ev_event!=2608004  && ev_event!=2608002  && ev_event!=2608012  && ev_event!=2608017  && ev_event!=2608028  && ev_event!=2608032  && ev_event!=2608036)continue;
if( trigger_study && (trig_HLT_PFHT300_PFMET110==0 && trig_HLT_MET200==0 && trig_HLT_PFMET300==0 && trig_HLT_PFMET120_PFMHT120_IDTight==0 && trig_HLT_PFMET170_HBHECleaned==0 && trig_HLT_MET75_IsoTrk50==0)) continue;
//if( trigger_study && (trig_HLT_PFHT300_PFMET110==0 && trig_HLT_MET200==0 && trig_HLT_PFMET300==0 && trig_HLT_PFMET120_PFMHT120_IDTight==0 && trig_HLT_PFMET170_HBHECleaned==0 )) continue;
bool pass_1    =false;
bool pass_2    =false;
bool pass_3    =false;
bool pass_4_1_1=false;
bool pass_4_1_2=false;
bool pass_4_2_1=false;
bool pass_4_2_2=false;
bool pass_5    =false;

event_weight =1;
sf_Ele_reco  =1;
sf_Ele_ID    =1;
sf_Muon_track=1;
sf_Muon_ID   =1;
sf_Muon_Iso  =1;
sf_Btag      =1;
sf_trigger   =1;
if(i%1000000==0)std::cout<<"processing: "<<float(100*i/t->GetEntries())<<"%"<<std::endl;
if(do_PU_weight==true) {
                        event_weight=w_PU_combined;
                        //event_weight=event_sign*PU_reReco_Morind17::MC_pileup_weight(PU_true, 0, "B2D");
                        //event_weight=event_sign*PU_reReco_Morind17::MC_pileup_weight(PU_true, 0, "EF");
                        //event_weight=event_sign*PU_reReco_Morind17::MC_pileup_weight(PU_true, 0, "GH");
                        if(uncert=="PU_scale_up") event_weight=w_PU_silver_up;
                        else if(uncert=="PU_scale_down") event_weight=w_PU_silver_down;
                       }
else event_weight=event_sign;
if(do_Nvtx_reweight==true){
if(ee_channel)event_weight=event_weight*weight_1D(w_Nvtx_ee, float(pv_n));
else if(emu_channel)event_weight=event_weight*weight_1D(w_Nvtx_emu, float(pv_n));
else if(mumu_channel)event_weight=event_weight*weight_1D(w_Nvtx_mumu, float(pv_n));
}
if(is_ttbar) event_weight=event_weight*w_LHE;


///////// MET Filter ///////////////
//if(trig_Flag_METFilters==0) continue;
if(use_met_filter){
if(trig_Flag_HBHENoiseFilter==0 || trig_Flag_HBHENoiseIsoFilter==0 || trig_Flag_globalTightHalo2016Filter==0 || trig_Flag_goodVertices==0 || trig_Flag_EcalDeadCellTriggerPrimitiveFilter==0 || trig_Flag_BadChargedCandidateFilter==0 || trig_Flag_BadPFMuonFilter==0 || (is_data && trig_Flag_eeBadScFilter==0)) continue;
}
//////////////////////////////
int ele_max    =-1;
int ele_second =-1;
int muon_max   =-1;
int muon_second=-1;
ele_max     = find_max_pt(electrons_pt)   ;
ele_second  = find_second_pt(electrons_pt);
muon_max    = find_max_pt(muons_pt)       ;
muon_second = find_second_pt(muons_pt)    ;
TLorentzVector lepton_led(0,0,0,0);
TLorentzVector lepton_sub(0,0,0,0);
TLorentzVector llp4;
//############## combine ##########################################
bool use_ee  =false;
bool use_emu =false;
bool use_mumu=false;
bool Skip_mumu=false;
if(combine_channel){

if(ele_max!=-1 && ele_second!=-1){if(muon_max==-1) use_ee=true; 
                                  else if(muon_max!=-1 && electrons_pt->at(ele_second) >= muons_pt->at(muon_max)) use_ee=true;
                                 }

if(muon_max!=-1 && muon_second!=-1){if(ele_max==-1)use_mumu=true;
                                  else if(ele_max!=-1 && muons_pt->at(muon_second) >= electrons_pt->at(ele_max)) use_mumu=true;
                                 }
if(use_ee==false && use_mumu==false) use_emu=true;
}
//############## ee ##########################################
if(ee_channel || use_ee ){
if(is_data){if(is_single_ele_data==false){if(use_trigger && trig_Ele23_Ele12 ==0)continue;}
            else{if(use_trigger && (trig_Ele27_WPTight==0||trig_Ele23_Ele12==1))continue;}
           }
else{if(use_trigger && trig_Ele23_Ele12 ==0 &&trig_Ele27_WPTight==0 ) continue;}//trigger
if(ele_max ==-1 || ele_second==-1) continue;//two electrons with pt>15
if(electrons_charge->at(ele_max) == electrons_charge->at(ele_second)) continue;//OS
if(electrons_pt->at(ele_second) < sub_pt_threshold || electrons_pt->at(ele_max) < led_pt_threshold) continue; // led>25 && sub>20
if(muon_max!=-1 && (muons_pt->at(muon_max) > electrons_pt->at(ele_second))) continue;//if muons max pt > second pt of electron
lepton_led.SetPtEtaPhiM(electrons_pt->at(ele_max)   , electrons_eta->at(ele_max)   , electrons_phi->at(ele_max)   , m_el);
lepton_sub.SetPtEtaPhiM(electrons_pt->at(ele_second), electrons_eta->at(ele_second), electrons_phi->at(ele_second), m_el);
llp4=lepton_led + lepton_sub;

if(llp4.M()<Mass_cut_low) continue;
pass_1=true;
/////////////////////////for trigger study part1/////////////////
if(trigger_study){
float region=-1;
if     (fabs(electrons_sc_eta->at(ele_max))<1.4442 && fabs(electrons_sc_eta->at(ele_second))<1.4442) region=0.5;
else if( (fabs(electrons_sc_eta->at(ele_max))<1.4442 && fabs(electrons_sc_eta->at(ele_second))>1.566 && fabs(electrons_sc_eta->at(ele_second))<2.5) || (fabs(electrons_sc_eta->at(ele_second))<1.4442 && fabs(electrons_sc_eta->at(ele_max))>1.566 && fabs(electrons_sc_eta->at(ele_max))<2.5) ) region=1.5;
else if( (fabs(electrons_sc_eta->at(ele_second))>1.566 && fabs(electrons_sc_eta->at(ele_second))<2.5) && (fabs(electrons_sc_eta->at(ele_max))>1.566 && fabs(electrons_sc_eta->at(ele_max))<2.5) ) region=2.5;
H_ee_region->Fill(region, event_sign);
H_ee_region->Fill(3.5   , event_sign);//BB+BE+EE
fill_2D(H2_pt1_pt2 , lepton_led.Pt(),lepton_sub.Pt(), event_sign);
fill_2D(H2_ee_eta1_eta2, electrons_sc_eta->at(ele_max),electrons_sc_eta->at(ele_second), event_sign);
if(trig_Ele23_Ele12==1 || trig_Ele27_WPTight==1) {fill_2D(H2_pt1_pt2_pass, lepton_led.Pt(),lepton_sub.Pt(), event_sign);
                         fill_2D(H2_ee_eta1_eta2_pass, electrons_sc_eta->at(ele_max),electrons_sc_eta->at(ele_second), event_sign);
                         H_ee_region_pass->Fill(region, event_sign);
                         H_ee_region_pass->Fill(3.5   , event_sign);//BB+BE+EE
                        }
                 }
/////////////////////////////////////////
if((llp4.M()<Z_cut_low || llp4.M()>Z_cut_high) && (MET_T1Txy_et>50)) pass_2=true;//not in Zpeak && MET_SF>4
//if(Met_et>MET_cut) pass_3=true; //MET>40
pass_3=true; 
////////////// For Ele reco sf /////////////
if(apply_sf_Ele_reco==true){
sf_Ele_reco=scale_factor(sf_Ele_Reco_Map ,electrons_pt->at(ele_max) ,electrons_sc_eta->at(ele_max));
sf_Ele_reco=sf_Ele_reco*scale_factor(sf_Ele_Reco_Map ,electrons_pt->at(ele_second) ,electrons_sc_eta->at(ele_second) );
}
else sf_Ele_reco=1;
////////////// For Ele ID sf ///////////
if(apply_sf_Ele_ID==true){
sf_Ele_ID=scale_factor(sf_Ele_ID_Map ,electrons_pt->at(ele_max) ,electrons_sc_eta->at(ele_max));
sf_Ele_ID=sf_Ele_ID*scale_factor(sf_Ele_ID_Map ,electrons_pt->at(ele_second) ,electrons_sc_eta->at(ele_second));

}
else sf_Ele_ID=1;
///////////////////////////////////////
////////////// For trigger sf ///////////
sf_trigger=0.989;

}
//############## emu ##########################################
else if(emu_channel || use_emu){
if(is_data){if(ev_run>=RunH){trig_Mu8_Ele23=trig_Mu8_Ele23_DZ;
                        trig_Mu23_Ele12=trig_Mu23_Ele12_DZ;} 
           }
if(is_data){
            if(is_single_ele_data==true){if(use_trigger && (trig_Ele27_WPTight==0 || (trig_Mu8_Ele23 ==1 || trig_Mu23_Ele12==1 || trig_IsoMu24==1 || trig_IsoTkMu24==1)))continue;}
            else if(is_single_muon_data==true){if(use_trigger && ((trig_IsoMu24==0 && trig_IsoTkMu24==0)||(trig_Mu8_Ele23 ==1 || trig_Mu23_Ele12==1)))continue;}
            else{if(use_trigger && trig_Mu8_Ele23 ==0 && trig_Mu23_Ele12==0)continue;}
           }
else{if(use_trigger && trig_Mu8_Ele23 ==0 && trig_Mu23_Ele12==0 && trig_IsoMu24==0 && trig_IsoTkMu24==0 && trig_Ele27_WPTight==0) continue;}//trigger
if(ele_max ==-1 || muon_max==-1) continue;//one electrons and one muon both pt>15
if(electrons_charge->at(ele_max) == muons_charge->at(muon_max)) continue;//OS
if(electrons_pt->at(ele_max) < sub_pt_threshold || muons_pt->at(muon_max) < sub_pt_threshold) continue; //  sub>20
if(electrons_pt->at(ele_max) < led_pt_threshold && muons_pt->at(muon_max) < led_pt_threshold) continue; //  led>25
if(muon_second!=-1 && (muons_pt->at(muon_second) > electrons_pt->at(ele_max))) continue;//if muons second pt > max pt of electrons
if(ele_second !=-1 && (electrons_pt->at(ele_second) > muons_pt->at(muon_max))) continue;//if electrons second pt > max pt of muons
if(electrons_pt->at(ele_max) > muons_pt->at(muon_max)){
lepton_led.SetPtEtaPhiM(electrons_pt->at(ele_max)   , electrons_eta->at(ele_max)   , electrons_phi->at(ele_max)   , m_el);
lepton_sub.SetPtEtaPhiM(muons_pt->at(muon_max)      , muons_eta->at(muon_max)      , muons_phi->at(muon_max)      , m_mu);
}
else{
lepton_sub.SetPtEtaPhiM(electrons_pt->at(ele_max)   , electrons_eta->at(ele_max)   , electrons_phi->at(ele_max)   , m_el);
lepton_led.SetPtEtaPhiM(muons_pt->at(muon_max)      , muons_eta->at(muon_max)      , muons_phi->at(muon_max)      , m_mu);
}
llp4=lepton_led + lepton_sub;
if(llp4.M()<Mass_cut_low) continue;//
pass_1=true;
/////////////////////////for trigger study part1 /////////////////
if(trigger_study){
float region=-1;
if     (fabs(electrons_sc_eta->at(ele_max))<1.4442 && fabs(muons_eta->at(muon_max))<1.2) region=0.5;
else if( (fabs(electrons_sc_eta->at(ele_max))<1.4442 && fabs(muons_eta->at(muon_max))>1.2 && fabs(muons_eta->at(muon_max))<2.4) || (fabs(muons_eta->at(muon_max))<1.2 && fabs(electrons_sc_eta->at(ele_max))>1.566 && fabs(electrons_sc_eta->at(ele_max))<2.5) ) region=1.5;
else if( (fabs(muons_eta->at(muon_max))>1.2 && fabs(muons_eta->at(muon_max))<2.4) && (fabs(electrons_sc_eta->at(ele_max))>1.566 && fabs(electrons_sc_eta->at(ele_max))<2.5) ) region=2.5;
H_emu_region->Fill(region, event_sign);
H_emu_region->Fill(3.5   , event_sign);
fill_2D(H2_pt1_pt2      , lepton_led.Pt() ,lepton_sub.Pt() , event_sign);
if(fabs(lepton_led.M()-m_el)<0.01) fill_2D(H2_emu_eta1_eta2, electrons_sc_eta->at(ele_max),lepton_sub.Eta()             , event_sign);
else                               fill_2D(H2_emu_eta1_eta2, lepton_led.Eta()             ,electrons_sc_eta->at(ele_max), event_sign);
if(trig_Mu8_Ele23==1 || trig_Mu23_Ele12==1 || trig_Ele27_WPTight==1 ||trig_IsoMu24==1 || trig_IsoTkMu24==1) {
                         fill_2D(H2_pt1_pt2_pass,lepton_led.Pt() ,lepton_sub.Pt(), event_sign);
                         if(fabs(lepton_led.M()-m_el)<0.01) fill_2D(H2_emu_eta1_eta2_pass, electrons_sc_eta->at(ele_max),lepton_sub.Eta()             , event_sign);
                         else                               fill_2D(H2_emu_eta1_eta2_pass, lepton_led.Eta()             ,electrons_sc_eta->at(ele_max), event_sign);
                         H_emu_region_pass->Fill(region, event_sign);
                         H_emu_region_pass->Fill(3.5   , event_sign);
                         }
                 }
///////////////////////////////////////////////////////////
//if(llp4.M()>80 || MET_T1Txy_et>40) pass_2=true;//
pass_2=true;//
pass_3=true; //MET SF>40

////////////// For Ele reco sf /////////////
if(apply_sf_Ele_reco==true){
sf_Ele_reco=scale_factor(sf_Ele_Reco_Map ,electrons_pt->at(ele_max) ,electrons_sc_eta->at(ele_max));
}
else sf_Ele_reco=1;
////////////// For Ele ID sf ///////////
if(apply_sf_Ele_ID==true){
sf_Ele_ID=scale_factor(sf_Ele_ID_Map ,electrons_pt->at(ele_max) ,electrons_sc_eta->at(ele_max));
}
else sf_Ele_ID=1;
////////////////For Muon tracking ///////////////////////
if(apply_sf_Muon_track==true){
sf_Muon_track=scale_factor_graph(sf_Muon_track_gr ,muons_eta->at(muon_max));
}
else sf_Muon_track=1;
////////////////For Muon ID  ///////////////////////
if(apply_sf_Muon_ID==true){
if(Data_range==1) sf_Muon_ID=(lumi_B2F/(lumi_B2F+lumi_GH))*scale_factor(sf_Muon_ID_B2F_Map ,muons_pt->at(muon_max) ,fabs(muons_eta->at(muon_max))) + (lumi_GH/(lumi_B2F+lumi_GH))*scale_factor(sf_Muon_ID_GH_Map ,muons_pt->at(muon_max) ,fabs(muons_eta->at(muon_max)));
else if(Data_range==2) sf_Muon_ID=scale_factor(sf_Muon_ID_B2F_Map ,muons_pt->at(muon_max),fabs(muons_eta->at(muon_max))) ;
else if(Data_range==3) sf_Muon_ID=scale_factor(sf_Muon_ID_GH_Map ,muons_pt->at(muon_max) ,fabs(muons_eta->at(muon_max))) ;
else {std::cout<<"wrong data range"<<std::endl;}
}
else sf_Muon_ID=1;
////////////////For Muon Iso  ///////////////////////
if(apply_sf_Muon_Iso==true){
if(Data_range==1) sf_Muon_Iso=(lumi_B2F/(lumi_B2F+lumi_GH))*scale_factor(sf_Muon_Iso_B2F_Map ,muons_pt->at(muon_max) ,fabs(muons_eta->at(muon_max))) + (lumi_GH/(lumi_B2F+lumi_GH))*scale_factor(sf_Muon_Iso_GH_Map ,muons_pt->at(muon_max) ,fabs(muons_eta->at(muon_max)));
else if(Data_range==2) sf_Muon_Iso=scale_factor(sf_Muon_Iso_B2F_Map ,muons_pt->at(muon_max) ,fabs(muons_eta->at(muon_max))) ;
else if(Data_range==3) sf_Muon_Iso=scale_factor(sf_Muon_Iso_GH_Map ,muons_pt->at(muon_max)  ,fabs(muons_eta->at(muon_max))) ;
else {std::cout<<"wrong data range"<<std::endl;}
}
else sf_Muon_Iso=1;
////////////////////////////////////////////////////
////////////// For trigger sf ///////////
sf_trigger=0.996;
//std::cout<<"event:"<<ev_event<<std::endl;
}
//############## mumu ##########################################
else if(mumu_channel || use_mumu){
if(is_data){if(ev_run>=RunH){trig_Mu17_TkMu8=trig_Mu17_TkMu8_DZ;
                             trig_Mu17_Mu8  =trig_Mu17_Mu8_DZ;} 
           }
if(is_data){if(is_single_muon_data==false){if(use_trigger && trig_Mu17_TkMu8 ==0 && trig_Mu17_Mu8==0)continue;}
            else{if(use_trigger && ((trig_IsoMu24==0 && trig_IsoTkMu24==0)||(trig_Mu17_TkMu8 ==1 || trig_Mu17_Mu8==1)))continue;}
           }
else{if(use_trigger && trig_Mu17_TkMu8 ==0 && trig_Mu17_Mu8==0 && trig_IsoMu24==0 && trig_IsoTkMu24==0 ) continue;}//trigger
if(muon_max ==-1 || muon_second==-1) continue;//two muons with pt>15
if(muons_charge->at(muon_max) == muons_charge->at(muon_second)) continue;//OS
if(muons_pt->at(muon_second) < sub_pt_threshold || muons_pt->at(muon_max) < led_pt_threshold) continue; // led>25 && sub>20
if(ele_max!=-1 && (electrons_pt->at(ele_max) > muons_pt->at(muon_second))) continue;//if electrons max pt > second pt of muons
lepton_led.SetPtEtaPhiM(muons_pt->at(muon_max)   , muons_eta->at(muon_max)   , muons_phi->at(muon_max)   , m_mu);
lepton_sub.SetPtEtaPhiM(muons_pt->at(muon_second), muons_eta->at(muon_second), muons_phi->at(muon_second), m_mu);
llp4=lepton_led + lepton_sub;

if(llp4.M()<Mass_cut_low) continue;
if(deltaPhi(lepton_led.Phi(),lepton_sub.Phi())<(PI_F*70/180) && ( (muons_eta->at(muon_max)>0.9 && muons_eta->at(muon_second)>0.9) || (muons_eta->at(muon_max)<-0.9 && muons_eta->at(muon_second)<-0.9) ) ) Skip_mumu=true;
if(Skip_mumu && trigger_study==false)continue;// remove very close muons event
pass_1=true;
/////////////////////////for trigger study part 1/////////////////
if(trigger_study){
if(Skip_mumu==false){
float region=-1;
if     (fabs(muons_eta->at(muon_max))<1.2 && fabs(muons_eta->at(muon_second))<1.2) region=0.5;
else if( (fabs(muons_eta->at(muon_max))<1.2 && fabs(muons_eta->at(muon_second))>1.2 && fabs(muons_eta->at(muon_second))<2.4) || (fabs(muons_eta->at(muon_second))<1.2 && fabs(muons_eta->at(muon_max))>1.2 && fabs(muons_eta->at(muon_max))<2.4) ) region=1.5;
else if( (fabs(muons_eta->at(muon_second))>1.2 && fabs(muons_eta->at(muon_second))<2.4) && (fabs(muons_eta->at(muon_max))>1.2 && fabs(muons_eta->at(muon_max))<2.4) ) region=2.5;
H_mumu_region->Fill(region, event_sign);
H_mumu_region->Fill(3.5   , event_sign);
fill_2D(H2_pt1_pt2, lepton_led.Pt(),lepton_sub.Pt(), event_sign);
fill_2D(H2_mumu_eta1_eta2, lepton_led.Eta(),lepton_sub.Eta(), event_sign);
if(trig_Mu17_TkMu8 ==1 || trig_Mu17_Mu8==1 || trig_IsoMu24==1 || trig_IsoTkMu24==1 ) {fill_2D(H2_pt1_pt2_pass, lepton_led.Pt(),lepton_sub.Pt(), event_sign);
                         fill_2D(H2_mumu_eta1_eta2_pass, lepton_led.Eta(),lepton_sub.Eta(), event_sign);
                         H_mumu_region_pass->Fill(region, event_sign);
                         H_mumu_region_pass->Fill(3.5   , event_sign);
                        }
               }
                  }

////////////////////////////////////////
if((llp4.M()<Z_cut_low || llp4.M()>Z_cut_high) && (MET_T1Txy_et>50) ) pass_2=true;//not in Zpeak && MET_SF>4
//if(Met_et>MET_cut) pass_3=true; //MET>40
pass_3=true; //
////////////////For Muon tracking ///////////////////////
if(apply_sf_Muon_track==true){
sf_Muon_track=scale_factor_graph(sf_Muon_track_gr ,muons_eta->at(muon_max));
sf_Muon_track=sf_Muon_track * scale_factor_graph(sf_Muon_track_gr ,muons_eta->at(muon_second));
}
else sf_Muon_track=1;
////////////////For Muon ID  ///////////////////////
if(apply_sf_Muon_ID==true){
double tmp_sf_1=1;
double tmp_sf_2=1;
if(Data_range==1) {tmp_sf_1=(lumi_B2F/(lumi_B2F+lumi_GH))*scale_factor(sf_Muon_ID_B2F_Map ,muons_pt->at(muon_max) ,fabs(muons_eta->at(muon_max))) + (lumi_GH/(lumi_B2F+lumi_GH))*scale_factor(sf_Muon_ID_GH_Map ,muons_pt->at(muon_max) ,fabs(muons_eta->at(muon_max)));
                   tmp_sf_2=(lumi_B2F/(lumi_B2F+lumi_GH))*scale_factor(sf_Muon_ID_B2F_Map ,muons_pt->at(muon_second) ,fabs(muons_eta->at(muon_second))) + (lumi_GH/(lumi_B2F+lumi_GH))*scale_factor(sf_Muon_ID_GH_Map ,muons_pt->at(muon_second) ,fabs(muons_eta->at(muon_second))) ;}
else if(Data_range==2) {tmp_sf_1=scale_factor(sf_Muon_ID_B2F_Map ,muons_pt->at(muon_max)    ,fabs(muons_eta->at(muon_max))) ;
                        tmp_sf_2=scale_factor(sf_Muon_ID_B2F_Map ,muons_pt->at(muon_second) ,fabs(muons_eta->at(muon_second))) ; }
else if(Data_range==3) {tmp_sf_1=scale_factor(sf_Muon_ID_GH_Map ,muons_pt->at(muon_max)     ,fabs(muons_eta->at(muon_max))) ;
                        tmp_sf_2=scale_factor(sf_Muon_ID_GH_Map ,muons_pt->at(muon_second)  ,fabs(muons_eta->at(muon_second))) ; }
sf_Muon_ID=tmp_sf_1*tmp_sf_2;
}
else sf_Muon_ID=1;
////////////////For Muon Iso  ///////////////////////
if(apply_sf_Muon_Iso==true){
double tmp_sf_1=1;
double tmp_sf_2=1;
if(Data_range==1) {tmp_sf_1=(lumi_B2F/(lumi_B2F+lumi_GH))*scale_factor(sf_Muon_Iso_B2F_Map ,muons_pt->at(muon_max)    ,fabs(muons_eta->at(muon_max))) + (lumi_GH/(lumi_B2F+lumi_GH))*scale_factor(sf_Muon_Iso_GH_Map ,muons_pt->at(muon_max)       ,fabs(muons_eta->at(muon_max)));
                   tmp_sf_2=(lumi_B2F/(lumi_B2F+lumi_GH))*scale_factor(sf_Muon_Iso_B2F_Map ,muons_pt->at(muon_second) ,fabs(muons_eta->at(muon_second))) + (lumi_GH/(lumi_B2F+lumi_GH))*scale_factor(sf_Muon_Iso_GH_Map ,muons_pt->at(muon_second) ,fabs(muons_eta->at(muon_second))) ;}
else if(Data_range==2) {tmp_sf_1=scale_factor(sf_Muon_Iso_B2F_Map ,muons_pt->at(muon_max)    ,fabs(muons_eta->at(muon_max))) ;
                        tmp_sf_2=scale_factor(sf_Muon_Iso_B2F_Map ,muons_pt->at(muon_second) ,fabs(muons_eta->at(muon_second))) ; }
else if(Data_range==3) {tmp_sf_1=scale_factor(sf_Muon_Iso_GH_Map ,muons_pt->at(muon_max)     ,fabs(muons_eta->at(muon_max))) ;
                        tmp_sf_2=scale_factor(sf_Muon_Iso_GH_Map ,muons_pt->at(muon_second)  ,fabs(muons_eta->at(muon_second))) ; }
sf_Muon_Iso=tmp_sf_1*tmp_sf_2;
}
else sf_Muon_Iso=1;
////////////////////////////////////////////////////
////////////// For trigger sf ///////////
sf_trigger=0.994;
}
else{continue;}
////////////////////For Reco ID Iso uncertainty//////////////////////
if(uncert=="EleSFReco_up"){ 
if(ee_channel || use_ee) sf_Ele_reco=1.01*1.01*sf_Ele_reco; 
else if(emu_channel || use_emu) sf_Ele_reco=1.01*sf_Ele_reco;                               
}
else if(uncert=="EleSFReco_down") {
if(ee_channel || use_ee) sf_Ele_reco=0.99*0.99*sf_Ele_reco;
else if(emu_channel || use_emu) sf_Ele_reco=0.99*sf_Ele_reco;                                
}
else if(uncert=="EleSFID_up"){ 
if(ee_channel || use_ee) sf_Ele_ID=1.01*1.01*sf_Ele_ID; 
else if(emu_channel || use_emu) sf_Ele_ID=1.01*sf_Ele_ID;                               
}
else if(uncert=="EleSFID_down") {
if(ee_channel || use_ee) sf_Ele_ID=0.99*0.99*sf_Ele_ID;
else if(emu_channel || use_emu) sf_Ele_ID=0.99*sf_Ele_ID;                                
}
else if(uncert=="MuonSFID_up"){ 
if(mumu_channel || use_mumu) sf_Muon_ID=1.01*1.01*sf_Muon_ID; 
else if(emu_channel || use_emu) sf_Muon_ID=1.01*sf_Muon_ID;                               
}
else if(uncert=="MuonSFID_down") {
if(mumu_channel || use_mumu) sf_Muon_ID=0.99*0.99*sf_Muon_ID;
else if(emu_channel || use_emu) sf_Muon_ID=0.99*sf_Muon_ID;                                
}
else if(uncert=="MuonSFIso_up"){ 
if(mumu_channel || use_mumu) sf_Muon_Iso=1.01*1.01*sf_Muon_Iso; 
else if(emu_channel || use_emu) sf_Muon_Iso=1.01*sf_Muon_Iso;                               
}
else if(uncert=="MuonSFIso_down") {
if(mumu_channel || use_mumu) sf_Muon_Iso=0.99*0.99*sf_Muon_Iso;
else if(emu_channel || use_emu) sf_Muon_Iso=0.99*sf_Muon_Iso;                                
}
else if(uncert=="MuonSFtrack_up"){ 
if(mumu_channel || use_mumu) sf_Muon_track=1.01*1.01*sf_Muon_track; 
else if(emu_channel || use_emu) sf_Muon_track=1.01*sf_Muon_track;                               
}
else if(uncert=="MuonSFtrack_down") {
if(mumu_channel || use_mumu) sf_Muon_track=0.99*0.99*sf_Muon_track;
else if(emu_channel || use_emu) sf_Muon_track=0.99*sf_Muon_track;                                
}
//////////////////////////////////////////////////////////////////
float HT_sys=0;
float Pt_sys=0;
float MT_sys=0;
TLorentzVector sum_p4(0,0,0,0);
TLorentzVector tmp_p4(0,0,0,0);

int Num_jet =0;
int Num_loose_jet =0;
int Num_loose_jet_low =0;
int Num_b_jet     =0;
int Num_b_jet_low =0;
int Num_eta2p4_30_jet=0;
int Num_eta2p4_40_jet=0;
vector<int> loose_jet_index;
vector<int> b_jet_index;
for(unsigned int ij=0;ij<jets_pt->size();ij++){
tmp_p4.SetPtEtaPhiM(jets_pt->at(ij), jets_eta->at(ij), jets_phi->at(ij), jets_mass->at(ij));
if(tmp_p4.DeltaR(lepton_led)<0.4 || tmp_p4.DeltaR(lepton_sub)<0.4) continue;
if(fabs(jets_eta->at(ij))<2.4 && jets_pt->at(ij) > jet_pt_threshold && jets_loose_ID->at(ij)==1) {Num_loose_jet++;
                                                                                    HT_sys=HT_sys+jets_pt->at(ij);
                                                                                    sum_p4=sum_p4+tmp_p4;
                                                                                    loose_jet_index.push_back(ij);
                                                                                    if(apply_sf_Btag) sf_Btag=sf_Btag*jets_BtagSF->at(ij);
                                                                                   }
if(fabs(jets_eta->at(ij))<2.4 && jets_pt->at(ij) > 20 && jets_pt->at(ij) <30 && jets_loose_ID->at(ij)==1 ) Num_loose_jet_low++;
if(fabs(jets_eta->at(ij))<2.4 && jets_pt->at(ij) > jet_pt_threshold && jets_loose_ID->at(ij)==1 && jets_CSV->at(ij)>Btag_WP) {Num_b_jet++;b_jet_index.push_back(ij);
                                                                                                                             }
if(fabs(jets_eta->at(ij))<2.4 && jets_pt->at(ij) > 20 && jets_pt->at(ij) <30 && jets_loose_ID->at(ij)==1 && jets_CSV->at(ij)>Btag_WP) Num_b_jet_low++;
if(fabs(jets_eta->at(ij))>=2.4 && fabs(jets_eta->at(ij))< 5.2 && jets_pt->at(ij) > 30 && jets_loose_ID->at(ij)==1) Num_eta2p4_30_jet++;
if(fabs(jets_eta->at(ij))>=2.4 && fabs(jets_eta->at(ij))< 5.2 && jets_pt->at(ij) > 40 && jets_loose_ID->at(ij)==1) Num_eta2p4_40_jet++;
}
//////////////// event weight ////////////////////
event_weight=event_weight*sf_Ele_reco*sf_Ele_ID*sf_Muon_track*sf_Muon_ID*sf_Muon_Iso*sf_Btag*sf_trigger;
//if(ev_event==10083162 || ev_event==10129618) std::cout<<"event:"<<ev_event<<",b sf="<<sf_Btag<<", w nvtx="<<weight_1D(w_Nvtx_emu, float(pv_n))<<",pu="<<w_PU_combined<<",muon trk="<<sf_Muon_track<<", muon ID="<<sf_Muon_ID<<",muon iso="<<sf_Muon_Iso<<",ele reco="<<sf_Ele_reco<<",ele ID="<<sf_Ele_ID<<", led pt="<<lepton_led.Pt()<<",led eta="<<lepton_led.Eta()<<", sub pt="<<lepton_sub.Pt()<<", sub eta="<<lepton_sub.Eta()<<",ele sc eta="<<electrons_sc_eta->at(ele_max)<<",Nvtx="<<pv_n<<",top="<<w_LHE<<",total="<<event_weight<<std::endl;
//std::cout<<"event:"<<ev_event<<",b sf="<<sf_Btag<<", w nvtx="<<weight_1D(w_Nvtx_emu, pv_n)<<",pu="<<w_PU_combined<<",muon trk="<<sf_Muon_track<<", muon ID="<<sf_Muon_ID<<",muon iso="<<sf_Muon_Iso<<",ele reco="<<sf_Ele_reco<<",ele ID="<<sf_Ele_ID<<", led pt="<<lepton_led.Pt()<<",led eta="<<lepton_led.Eta()<<", sub pt="<<lepton_sub.Pt()<<", sub eta="<<lepton_sub.Eta()<<",ele sc eta="<<electrons_sc_eta->at(ele_max)<<",top="<<w_LHE<<",total="<<event_weight<<std::endl;
///////////////////////////
int jet_led_index=-1;
int jet_sub_index=-1;
int jet_forward_led_index=-1;
int jet_low_led_index=-1;
jet_led_index = find_led_jet(jets_pt, jets_eta, jets_phi, jets_mass, jets_loose_ID, lepton_led, lepton_sub);
jet_sub_index = find_sub_jet(jets_pt, jets_eta, jets_phi, jets_mass, jets_loose_ID, lepton_led, lepton_sub);
jet_forward_led_index = find_forward_led_jet(jets_pt, jets_eta, jets_phi, jets_mass, jets_loose_ID, lepton_led, lepton_sub);
jet_low_led_index = find_low_led_jet(jets_pt, jets_eta, jets_phi, jets_mass, jets_loose_ID, lepton_led, lepton_sub);
int missed_b_index=-1;
if(loose_jet_index.size()==2 && b_jet_index.size()==1){
for(unsigned int ib=0;ib<loose_jet_index.size();ib++){
if(loose_jet_index.at(ib) != b_jet_index.at(0)){missed_b_index=loose_jet_index.at(ib);break;}
}
//if(jets_CSV->at(missed_b_index)<0)std::cout<<"csv="<<jets_CSV->at(missed_b_index)<<std::endl;
}
//if(Num_b_jet==0) pass_4_1_1=true;
//else if(Num_b_jet==1) pass_4_1_2=true;
//else if(Num_b_jet>1) pass_4_2_1=true;

//if(Num_loose_jet>=2) pass_4_1_1=true;
if(Num_loose_jet ==1 && Num_b_jet ==1 ) pass_4_2_1=true;
if(Num_loose_jet >1  && Num_b_jet ==1 ) pass_4_2_2=true;
//if(Num_loose_jet==0 || (Num_loose_jet==1 && Num_b_jet==0))   pass_5=true;
////////////////// trigger study part2///////////////////
if(trigger_study){
if(ee_channel || use_ee){
fill_2D(H2_MET_Nvtx  , pv_n           ,MET_T1Txy_et , event_sign);
fill_2D(H2_Njet_Nbjet, Num_loose_jet  ,Num_b_jet    , event_sign);
if(trig_Ele23_Ele12==1 || trig_Ele27_WPTight==1) {
fill_2D(H2_MET_Nvtx_pass  , pv_n           ,MET_T1Txy_et , event_sign);
fill_2D(H2_Njet_Nbjet_pass, Num_loose_jet  ,Num_b_jet    , event_sign);
}
}
else if(emu_channel || use_emu){  
fill_2D(H2_MET_Nvtx  , pv_n           ,MET_T1Txy_et , event_sign);
fill_2D(H2_Njet_Nbjet, Num_loose_jet  ,Num_b_jet    , event_sign);
if(trig_Mu8_Ele23==1 || trig_Mu23_Ele12==1 || trig_Ele27_WPTight==1 ||trig_IsoMu24==1 || trig_IsoTkMu24==1) {
fill_2D(H2_MET_Nvtx_pass  , pv_n           ,MET_T1Txy_et , event_sign);
fill_2D(H2_Njet_Nbjet_pass, Num_loose_jet  ,Num_b_jet    , event_sign);
}
}
else if(mumu_channel || use_mumu){
if(Skip_mumu==false){
fill_2D(H2_MET_Nvtx  , pv_n           ,MET_T1Txy_et , event_sign);
fill_2D(H2_Njet_Nbjet, Num_loose_jet  ,Num_b_jet    , event_sign);
if(trig_Mu17_TkMu8 ==1 || trig_Mu17_Mu8==1 || trig_IsoMu24==1 || trig_IsoTkMu24==1) {
fill_2D(H2_MET_Nvtx_pass  , pv_n           ,MET_T1Txy_et , event_sign);
fill_2D(H2_Njet_Nbjet_pass, Num_loose_jet  ,Num_b_jet    , event_sign);
}
}
}
}//trigger study part2
////////////////////////////////////////////////////////

float HT_jet=0;
HT_jet=HT_sys;
sum_p4=sum_p4+lepton_led;
HT_sys=HT_sys+lepton_led.Pt();
sum_p4=sum_p4+lepton_sub;
HT_sys=HT_sys+lepton_sub.Pt();
TLorentzVector Met_p4(0,0,0,0);
Pt_sys=sum_p4.Pt();
MT_sys=sum_p4.Mt();

//Met_p4.SetPtEtaPhiM(Met_et,0,Met_phi,0);
//HT_sys=HT_sys+Met_p4.Pt();
////////////////////////////////////////////////////////
int njet_bjet=-1;
if(Num_loose_jet==0) njet_bjet=0;
else if(Num_loose_jet==1){if(Num_b_jet==0)njet_bjet=1;
                          else njet_bjet=2;
                         }
else if(Num_loose_jet==2){if(Num_b_jet==0)njet_bjet=3;
                          else if(Num_b_jet==1)njet_bjet=4;
                          else njet_bjet=5;
}
else if(Num_loose_jet==3){if(Num_b_jet==0)njet_bjet=6;
                          else if(Num_b_jet==1)njet_bjet=7;
                          else if(Num_b_jet==2)njet_bjet=8;
                          else njet_bjet=9;
}
else if(Num_loose_jet==4){if(Num_b_jet==0)njet_bjet=10;
                          else if(Num_b_jet==1)njet_bjet=11;
                          else if(Num_b_jet==2)njet_bjet=12;
                          else if(Num_b_jet==3)njet_bjet=13;
                          else njet_bjet=14;
}
else{njet_bjet=14;}
////////////////////////////////////////
if(pass_1){N_step_1++;
          H_steps->Fill(0.1, event_weight);
          //fout<<ev_run<<" "<<ev_luminosityBlock<<" "<<ev_event<<"\n";
          //fout<<ev_event<<" "<<event_weight<<"\n";
          fout<<ev_event<<"\n";
          }
if(pass_1 && pass_2){N_step_2++;
                     H_steps->Fill(1.1, event_weight);
                    }
/////////////////////////////////////////////////////////////
if(pass_1 && pass_2){

float Dphi=fabs(MET_T1Txy_phi-llp4.Phi()) < PI_F ? fabs(MET_T1Txy_phi-llp4.Phi()) : (2*PI_F - fabs(MET_T1Txy_phi-llp4.Phi())) ;
float ll_Dphi=fabs(lepton_led.Phi()-lepton_sub.Phi()) < PI_F ? fabs(lepton_led.Phi()-lepton_sub.Phi()) : (2*PI_F - fabs(lepton_led.Phi()-lepton_sub.Phi())) ;
float ll_DR  =lepton_led.DeltaR(lepton_sub);
 
H2_Mll_MET  ->Fill(llp4.M(),  Met_et               , event_weight);
H2_Ptll_MET ->Fill(llp4.Pt(), Met_et               , event_weight);
H2_Mll_METSF->Fill(llp4.M(), MET_T1Txy_significance, event_weight);
H2_MET_Dphi ->Fill(Met_et   , Dphi                 , event_weight);
H2_Ptll_Dphi->Fill(llp4.Pt(), Dphi                 , event_weight);
H2_Txy_MET_phi->Fill(MET_T1Txy_et, MET_T1Txy_phi   , event_weight);

H_njet_bjet->Fill(njet_bjet+0.1, event_weight);
if(jet_led_index!=-1){
fill( H_jet_led_pt   ,jets_pt ->at(jet_led_index)  ,event_weight);
fill( H_jet_led_eta  ,jets_eta->at(jet_led_index)  ,event_weight);
fill( H_jet_led_phi  ,jets_phi->at(jet_led_index)  ,event_weight);
}
if(jet_sub_index!=-1){
fill( H_jet_sub_pt   ,jets_pt ->at(jet_sub_index)  ,event_weight);
fill( H_jet_sub_eta  ,jets_eta->at(jet_sub_index)  ,event_weight);
fill( H_jet_sub_phi  ,jets_phi->at(jet_sub_index)  ,event_weight);
}
if(jet_forward_led_index!=-1){
fill( H_jet_forward_led_pt   ,jets_pt ->at(jet_forward_led_index)  ,event_weight);
fill( H_jet_forward_led_eta  ,jets_eta->at(jet_forward_led_index)  ,event_weight);
}
else fill( H_jet_forward_led_pt   ,0  ,event_weight);
if(jet_low_led_index!=-1){
fill( H_jet_low_led_CSV   ,jets_CSV ->at(jet_low_led_index)  ,event_weight);
}
else fill( H_jet_low_led_CSV   ,-1  ,event_weight);
if(missed_b_index!=-1){
fill( H_jet_Bmissed_CSV   ,jets_CSV ->at(missed_b_index)  ,event_weight);
}
else fill( H_jet_Bmissed_CSV   ,-1  ,event_weight);

fill( H_Mll             ,llp4.M()          ,event_weight);
fill( H_Mll_Zpeak       ,llp4.M()          ,event_weight);
fill( H_Ptll            ,llp4.Pt()         ,event_weight);
fill( H_Rll             ,llp4.Rapidity()   ,event_weight);
fill( H_Ptll_phi        ,llp4.Phi()        ,event_weight);
fill( H_ll_Dphi         ,ll_Dphi           ,event_weight);
fill( H_ll_DR           ,ll_DR             ,event_weight);
fill( H_lepton_led_pt   ,lepton_led.Pt()   ,event_weight);
fill( H_lepton_led_eta  ,lepton_led.Eta()  ,event_weight);
fill( H_lepton_led_phi  ,lepton_led.Phi()  ,event_weight);
fill( H_lepton_sub_pt   ,lepton_sub.Pt()   ,event_weight);
fill( H_lepton_sub_eta  ,lepton_sub.Eta()  ,event_weight);
fill( H_lepton_sub_phi  ,lepton_sub.Phi()  ,event_weight);
fill( H_N_loose_jets    ,float(Num_loose_jet+0.1)     ,event_weight);
fill( H_N_loose_jets_low,float(Num_loose_jet_low+0.1) ,event_weight);
fill( H_N_b_jets        ,float(Num_b_jet+0.1)         ,event_weight);
fill( H_N_b_jets_low    ,float(Num_b_jet_low+0.1)     ,event_weight);
fill( H_N_eta2p4_30_jets,float(Num_eta2p4_30_jet+0.1) ,event_weight);
fill( H_N_eta2p4_40_jets,float(Num_eta2p4_40_jet+0.1) ,event_weight);
fill( H_MET_Et          ,Met_et              ,event_weight);
fill( H_MET_phi         ,Met_phi             ,event_weight);
fill( H_MET_Z_phi       ,fabs(Met_phi-llp4.Phi()),event_weight);
fill( H_MET_T1Txy_et    ,MET_T1Txy_et           ,event_weight);
fill( H_MET_T1Txy_phi   ,MET_T1Txy_phi          ,event_weight);
fill( H_MET_Z_T1Txy_phi ,Dphi ,event_weight);
fill( H_MET_T1Txy_sf    ,MET_T1Txy_significance ,event_weight);
fill( H_HT              ,HT_jet            ,event_weight);
fill( H_HT_sys          ,HT_sys            ,event_weight);
fill( H_Pt_sys          ,Pt_sys            ,event_weight);
fill( H_MT_sys          ,MT_sys            ,event_weight);
fill( H_pv_n            ,float(pv_n)       ,event_weight);
fill( H_rho             ,rho               ,event_weight);
}

}
std::cout<<left<<setw(5)<<"N1="<<setw(5)<<N_step_1<<setw(5)<<",N2="<<setw(5)<<N_step_2<<setw(5)<<",N3="<<setw(5)<<N_step_3<<setw(5)<<",N4_1_1="<<setw(5)<<N_step_4_1_1<<setw(5)<<",N4_1_2="<<setw(5)<<N_step_4_1_2<<setw(5)<<",N4_2_1="<<setw(5)<<N_step_4_2_1<<setw(5)<<",N4_2_2="<<setw(5)<<N_step_4_2_2<<setw(5)<<",N4_3="<<setw(5)<<N_step_4_3<<setw(5)<<",N5="<<setw(5)<<N_step_5<<std::endl;

fout << flush;
fout.close();

///////////////////////// save hist //////////////////////////////

TFile *f = new TFile(output_file,"UPDATE");
f->cd();
//////////////////// trigger/////////////////
H2_pt1_pt2            ->Write("",TObject::kOverwrite); 
H2_ee_eta1_eta2       ->Write("",TObject::kOverwrite); 
H2_emu_eta1_eta2      ->Write("",TObject::kOverwrite); 
H2_mumu_eta1_eta2     ->Write("",TObject::kOverwrite); 
H2_pt1_pt2_pass       ->Write("",TObject::kOverwrite); 
H2_ee_eta1_eta2_pass  ->Write("",TObject::kOverwrite); 
H2_emu_eta1_eta2_pass ->Write("",TObject::kOverwrite); 
H2_mumu_eta1_eta2_pass->Write("",TObject::kOverwrite); 
H2_MET_Nvtx           ->Write("",TObject::kOverwrite); 
H2_MET_Nvtx_pass      ->Write("",TObject::kOverwrite); 
H2_Njet_Nbjet         ->Write("",TObject::kOverwrite); 
H2_Njet_Nbjet_pass    ->Write("",TObject::kOverwrite); 
H_ee_region           ->Write("",TObject::kOverwrite); 
H_ee_region_pass      ->Write("",TObject::kOverwrite); 
H_emu_region          ->Write("",TObject::kOverwrite); 
H_emu_region_pass     ->Write("",TObject::kOverwrite); 
H_mumu_region         ->Write("",TObject::kOverwrite); 
H_mumu_region_pass    ->Write("",TObject::kOverwrite); 
///////////////////
H2_Mll_MET            ->Write("",TObject::kOverwrite);
H2_Ptll_MET           ->Write("",TObject::kOverwrite);
H2_Mll_METSF          ->Write("",TObject::kOverwrite);
H2_Ptll_Dphi          ->Write("",TObject::kOverwrite);
H2_Txy_MET_phi        ->Write("",TObject::kOverwrite);
H2_MET_Dphi           ->Write("",TObject::kOverwrite);
H_Mll                 ->Write("",TObject::kOverwrite);
H_Mll_Zpeak           ->Write("",TObject::kOverwrite);
H_Ptll                ->Write("",TObject::kOverwrite);
H_Rll                 ->Write("",TObject::kOverwrite);
H_Ptll_phi            ->Write("",TObject::kOverwrite);
H_ll_Dphi             ->Write("",TObject::kOverwrite);
H_ll_DR               ->Write("",TObject::kOverwrite);
H_lepton_led_pt       ->Write("",TObject::kOverwrite);
H_lepton_led_eta      ->Write("",TObject::kOverwrite);
H_lepton_led_phi      ->Write("",TObject::kOverwrite);
H_lepton_sub_pt       ->Write("",TObject::kOverwrite);
H_lepton_sub_eta      ->Write("",TObject::kOverwrite);
H_lepton_sub_phi      ->Write("",TObject::kOverwrite);
H_N_loose_jets        ->Write("",TObject::kOverwrite);
H_N_loose_jets_low    ->Write("",TObject::kOverwrite);
H_N_b_jets            ->Write("",TObject::kOverwrite);
H_N_b_jets_low        ->Write("",TObject::kOverwrite);
H_N_eta2p4_30_jets    ->Write("",TObject::kOverwrite);
H_N_eta2p4_40_jets    ->Write("",TObject::kOverwrite);
H_MET_Et              ->Write("",TObject::kOverwrite);
H_MET_phi             ->Write("",TObject::kOverwrite);
H_MET_Z_phi           ->Write("",TObject::kOverwrite);
H_MET_T1Txy_et        ->Write("",TObject::kOverwrite); 
H_MET_T1Txy_phi       ->Write("",TObject::kOverwrite); 
H_MET_Z_T1Txy_phi     ->Write("",TObject::kOverwrite); 
H_MET_T1Txy_sf        ->Write("",TObject::kOverwrite); 
H_HT                  ->Write("",TObject::kOverwrite);
H_HT_sys              ->Write("",TObject::kOverwrite);
H_Pt_sys              ->Write("",TObject::kOverwrite);
H_MT_sys              ->Write("",TObject::kOverwrite);
H_pv_n                ->Write("",TObject::kOverwrite);
H_rho                 ->Write("",TObject::kOverwrite);

H_steps               ->Write("",TObject::kOverwrite);
H_njet_bjet           ->Write("",TObject::kOverwrite);
H_jet_led_pt          ->Write("",TObject::kOverwrite);
H_jet_led_eta         ->Write("",TObject::kOverwrite);
H_jet_led_phi         ->Write("",TObject::kOverwrite);
H_jet_sub_pt          ->Write("",TObject::kOverwrite);
H_jet_sub_eta         ->Write("",TObject::kOverwrite);
H_jet_sub_phi         ->Write("",TObject::kOverwrite);
H_jet_forward_led_pt  ->Write("",TObject::kOverwrite);
H_jet_forward_led_eta ->Write("",TObject::kOverwrite);
H_jet_low_led_CSV     ->Write("",TObject::kOverwrite);
H_jet_Bmissed_CSV     ->Write("",TObject::kOverwrite);

f->Close();
//f_L1Map->Close();
H2_pt1_pt2            ->Delete(); 
H2_ee_eta1_eta2       ->Delete(); 
H2_emu_eta1_eta2      ->Delete(); 
H2_mumu_eta1_eta2     ->Delete(); 
H2_pt1_pt2_pass       ->Delete(); 
H2_ee_eta1_eta2_pass  ->Delete(); 
H2_emu_eta1_eta2_pass ->Delete(); 
H2_mumu_eta1_eta2_pass->Delete(); 
H2_MET_Nvtx           ->Delete(); 
H2_MET_Nvtx_pass      ->Delete(); 
H2_Njet_Nbjet         ->Delete(); 
H2_Njet_Nbjet_pass    ->Delete(); 
H_ee_region           ->Delete(); 
H_ee_region_pass      ->Delete(); 
H_emu_region          ->Delete(); 
H_emu_region_pass     ->Delete(); 
H_mumu_region         ->Delete(); 
H_mumu_region_pass    ->Delete(); 


H2_Mll_MET      ->Delete();
H2_Ptll_MET     ->Delete();
H2_Mll_METSF    ->Delete();
H2_Ptll_Dphi    ->Delete();
H2_Txy_MET_phi  ->Delete();
H2_MET_Dphi     ->Delete();
H_Mll           ->Delete();
H_Mll_Zpeak     ->Delete();
H_Ptll          ->Delete();
H_Rll           ->Delete();
H_Ptll_phi      ->Delete();
H_ll_Dphi       ->Delete();
H_ll_DR         ->Delete();
H_lepton_led_pt ->Delete();
H_lepton_led_eta->Delete();
H_lepton_led_phi->Delete();
H_lepton_sub_pt ->Delete();
H_lepton_sub_eta->Delete();
H_lepton_sub_phi->Delete();
H_N_loose_jets  ->Delete();
H_N_loose_jets_low->Delete();
H_N_b_jets      ->Delete();
H_N_b_jets_low  ->Delete();
H_N_eta2p4_30_jets ->Delete();
H_N_eta2p4_40_jets ->Delete();
H_MET_Et      ->Delete();
H_MET_phi     ->Delete();
H_MET_Z_phi   ->Delete();
H_MET_T1Txy_et ->Delete(); 
H_MET_T1Txy_phi->Delete(); 
H_MET_Z_T1Txy_phi->Delete(); 
H_MET_T1Txy_sf ->Delete(); 
H_HT          ->Delete();
H_HT_sys      ->Delete();
H_Pt_sys      ->Delete();
H_MT_sys      ->Delete();
H_pv_n        ->Delete();
H_rho         ->Delete();

H_steps       ->Delete();
H_njet_bjet   ->Delete();
H_jet_led_pt  ->Delete();
H_jet_led_eta ->Delete();
H_jet_led_phi ->Delete();
H_jet_sub_pt  ->Delete();
H_jet_sub_eta ->Delete();
H_jet_sub_phi ->Delete();
H_jet_forward_led_pt ->Delete();
H_jet_forward_led_eta ->Delete();
H_jet_low_led_CSV ->Delete();
H_jet_Bmissed_CSV ->Delete();
std::cout<<output_file<<" is saved"<<std::endl;
f_Ele_Reco_Map->Close();
f_Ele_ID_Map->Close();
f_Muon_track->Close();
f_Muon_ID_B2F_Map->Close();
f_Muon_ID_GH_Map->Close();
f_Muon_Iso_B2F_Map->Close();
f_Muon_Iso_GH_Map->Close();
Nvtx_Map_ee->Close();
Nvtx_Map_emu->Close();
Nvtx_Map_mumu->Close();
}

void fill(TH1D* &hist , float value, float weight){
float max=hist->GetBinLowEdge(hist->GetNbinsX())+hist->GetBinWidth(hist->GetNbinsX());
float min=hist->GetBinLowEdge(1);
if(max<=value) value=( max+hist->GetBinLowEdge(hist->GetNbinsX()) )/2;
else if(value<=min) value=(min+hist->GetBinLowEdge(1)+hist->GetBinWidth(1))/2;
hist->Fill(value,weight);
}

void fill_2D(TH2D* &hist , float value1, float value2, float weight){
float x_max=hist->GetXaxis()->GetXmax();
float x_min=hist->GetXaxis()->GetXmin();
float y_max=hist->GetYaxis()->GetXmax();
float y_min=hist->GetYaxis()->GetXmin();
if(x_max<=value1) value1=x_max-0.5*hist->GetXaxis()->GetBinWidth(hist->GetXaxis()->GetNbins());
else if(value1<=x_min) value1=x_min+0.5*hist->GetXaxis()->GetBinWidth(1);
if(y_max<=value2) value2=y_max-0.5*hist->GetYaxis()->GetBinWidth(hist->GetYaxis()->GetNbins());
else if(value1<=y_min) value2=y_min+0.5*hist->GetYaxis()->GetBinWidth(1);
hist->Fill(value1,value2,weight);
}

float scale_factor( TH2F* h, float pt, float eta){
int NbinsX=h->GetXaxis()->GetNbins();
int NbinsY=h->GetYaxis()->GetNbins();
float x_min=h->GetXaxis()->GetBinLowEdge(1);
float x_max=h->GetXaxis()->GetBinLowEdge(NbinsX)+h->GetXaxis()->GetBinWidth(NbinsX);
float y_min=h->GetYaxis()->GetBinLowEdge(1);
float y_max=h->GetYaxis()->GetBinLowEdge(NbinsY)+h->GetYaxis()->GetBinWidth(NbinsY);
TAxis *Xaxis = h->GetXaxis();
TAxis *Yaxis = h->GetYaxis();
Int_t binx=1;
Int_t biny=1;
if(x_min < eta && eta < x_max) binx = Xaxis->FindBin(eta);
else binx= (eta<=x_min) ? 1 : NbinsX ;
if(y_min < pt && pt < y_max) biny = Yaxis->FindBin(pt);
else biny= (pt<=y_min) ? 1 : NbinsY ;
//std::cout<<h->GetName()<<",value="<<h->GetBinContent(binx, biny)<<std::endl;
return h->GetBinContent(binx, biny);
}
float weight_1D( TH1D* h, float value){
int NbinsX=h->GetXaxis()->GetNbins();
float x_min=h->GetXaxis()->GetBinLowEdge(1);
float x_max=h->GetXaxis()->GetBinLowEdge(NbinsX)+h->GetXaxis()->GetBinWidth(NbinsX);
TAxis *Xaxis = h->GetXaxis();
Int_t binx=1;
if(x_min <= value && value < x_max) binx = Xaxis->FindBin(value);
else return 1 ;
return h->GetBinContent(binx);
}

float scale_factor_graph( TGraphAsymmErrors* gr, float eta){
float x_min=gr->GetX()[0] - gr->GetErrorXlow(0);
float x_max=gr->GetX()[gr->GetN()-1] + gr->GetErrorXhigh(gr->GetN()-1);
//std::cout<<"x_min:"<<x_min<<",x_max="<<x_max<<std::endl;
if(eta<x_min){return gr->GetY()[0];}
else if(x_min<=eta && eta<=x_max){float sf=1;
                                  for(int ig=0; ig<gr->GetN(); ig++){
                                  if( (eta >= gr->GetX()[ig] - gr->GetErrorXlow(ig)) && (eta <= gr->GetX()[ig] + gr->GetErrorXhigh(ig)) ) {sf=gr->GetY()[ig];break;}
                                 }
                                 //std::cout<<"eta="<<eta<<",sf="<<sf<<std::endl;
                                 return sf;
                                 }
else{return gr->GetY()[gr->GetN()-1];}

}
int find_max_pt(vector<float> *pt){
    if (pt->size()==0) return -1;
    float max=0;
    int index=-1;
    for(unsigned int ip=0; ip<pt->size(); ip++){
    if(pt->at(ip)>max){max=pt->at(ip);index=ip;}   
    }
    return index;
}

int find_second_pt(vector<float> *pt){
    if (pt->size()<2) return -1;
    unsigned int index   =find_max_pt(pt);
    float second= 0;
    int index_se=-1;
    for(unsigned int ip=0; ip<pt->size(); ip++){
    if(ip!=index && pt->at(ip)>second){second=pt->at(ip);index_se=ip;}   
    }
    return index_se;
}

int find_led_jet(vector<float> *pt, vector<float> *eta, vector<float> *phi, vector<float> *mass, vector<int> *loose_ID, TLorentzVector lepton_led, TLorentzVector lepton_sub){
    if (pt->size()==0) return -1;
    float max=0;
    int index=-1;

    TLorentzVector tmp_p4;
    for(unsigned int ip=0; ip<pt->size(); ip++){
    if(fabs(eta->at(ip))>2.4 || pt->at(ip) < 30 || loose_ID->at(ip)!=1) continue;
    tmp_p4.SetPtEtaPhiM(pt->at(ip), eta->at(ip), phi->at(ip), mass->at(ip));
    if(tmp_p4.DeltaR(lepton_led)<0.4 || tmp_p4.DeltaR(lepton_sub)<0.4) continue;
    if(pt->at(ip)>max){max=pt->at(ip);index=ip;}   
    }
    return index;
}

int find_low_led_jet(vector<float> *pt, vector<float> *eta, vector<float> *phi, vector<float> *mass, vector<int> *loose_ID, TLorentzVector lepton_led, TLorentzVector lepton_sub){
    if (pt->size()==0) return -1;
    float max=0;
    int index=-1;

    TLorentzVector tmp_p4;
    for(unsigned int ip=0; ip<pt->size(); ip++){
    if(fabs(eta->at(ip))>2.4 || pt->at(ip) < 20 || pt->at(ip) > 30 || loose_ID->at(ip)!=1) continue;
    tmp_p4.SetPtEtaPhiM(pt->at(ip), eta->at(ip), phi->at(ip), mass->at(ip));
    if(tmp_p4.DeltaR(lepton_led)<0.4 || tmp_p4.DeltaR(lepton_sub)<0.4) continue;
    if(pt->at(ip)>max){max=pt->at(ip);index=ip;}   
    }
    return index;
}

int find_forward_led_jet(vector<float> *pt, vector<float> *eta, vector<float> *phi, vector<float> *mass, vector<int> *loose_ID, TLorentzVector lepton_led, TLorentzVector lepton_sub){
    if (pt->size()==0) return -1;
    float max=0;
    int index=-1;

    TLorentzVector tmp_p4;
    for(unsigned int ip=0; ip<pt->size(); ip++){
    if(fabs(eta->at(ip))<2.4 || fabs(eta->at(ip))>5.2 || pt->at(ip) < 30 || loose_ID->at(ip)!=1) continue;
    tmp_p4.SetPtEtaPhiM(pt->at(ip), eta->at(ip), phi->at(ip), mass->at(ip));
    if(tmp_p4.DeltaR(lepton_led)<0.4 || tmp_p4.DeltaR(lepton_sub)<0.4) continue;
    if(pt->at(ip)>max){max=pt->at(ip);index=ip;}   
    }
    return index;
}

int find_sub_jet(vector<float> *pt, vector<float> *eta, vector<float> *phi, vector<float> *mass, vector<int> *loose_ID, TLorentzVector lepton_led, TLorentzVector lepton_sub){
    if (pt->size()<2) return -1;
    unsigned int index   =find_led_jet(pt, eta, phi, mass, loose_ID, lepton_led, lepton_sub);
    float second= 0;
    int index_se=-1;
    TLorentzVector tmp_p4;
    for(unsigned int ip=0; ip<pt->size(); ip++){
    if(fabs(eta->at(ip))>2.4 || pt->at(ip) < 30 || loose_ID->at(ip)!=1) continue;
    tmp_p4.SetPtEtaPhiM(pt->at(ip), eta->at(ip), phi->at(ip), mass->at(ip));
    if(tmp_p4.DeltaR(lepton_led)<0.4 || tmp_p4.DeltaR(lepton_sub)<0.4) continue;
    if(ip!=index && pt->at(ip)>second){second=pt->at(ip);index_se=ip;}   
    }
    return index_se;
}

long double deltaPhi(long double phi1, long double phi2){
  long double dphi = fmod(fabs(phi2-phi1), 2.L*PI_F);
  return dphi>PI_F ? 2.L*PI_F-dphi : dphi;
}
