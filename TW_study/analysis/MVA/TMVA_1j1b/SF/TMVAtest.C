#include <cstdlib>
#include <iostream>
#include <map>
#include <string>

#include "TChain.h"
#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TObjString.h"
#include "TSystem.h"
#include "TROOT.h"

//#include "tmva/test/TMVAGui.C"

//#if not defined(__CINT__) || defined(__MAKECINT__)
//// needs to be included when makecint runs (ACLIC)
//#include "TMVA/Factory.h"
//#include "TMVA/Tools.h"
//#endif

void TMVAtest()
{

  // ---------------------------------------------------------------
  std::cout << std::endl;
  std::cout << "==> Start TMVAClassification" << std::endl;
  // --------------------------------------------------------------------------------------------------
  
  // --- Here the preparation phase begins
  
  // Create a ROOT output file where TMVA will store ntuples, histograms, etc.
  TString TrainName = "TMVA";
  
  TString outfileName( TrainName+".root" );
  TFile* outputFile = TFile::Open( outfileName, "RECREATE" );
  
  // Create the factory object. Later you can choose the methods
  // whose performance you'd like to investigate. The factory is 
  // the only TMVA object you have to interact with
  //
  // The first argument is the base of the name of all the
  // weightfiles in the directory weight/
  //
  // The second argument is the output file for the training results
  // All TMVA output can be suppressed by removing the "!" (not) in
  // front of the "Silent" argument in the option string
  TMVA::Factory *factory = new TMVA::Factory( TrainName, outputFile, "!V:!Silent:Color:DrawProgressBar:Transformations=I;D;P;G,D:AnalysisType=Classification" );
  
  // If you wish to modify default settings
  // (please check "src/Config.h" to see all available global options)
  //    (TMVA::gConfig().GetVariablePlotting()).fTimesRMS = 8.0;
  //    (TMVA::gConfig().GetIONames()).fWeightFileDir = "myWeightDirectory";
  
  // Define the input variables that shall be used for the MVA training
  // note that you may also use variable expressions, such as: "3*var1/var2*abs(var3)"
  // [all types of expressions that can also be parsed by TTree::Draw( "expression" )]
  
  //factory->AddVariable("leading_pt", 'F');
  //factory->AddVariable("leading_eta", 'F');
  //factory->AddVariable("sub_leading_pt", 'F');
  //factory->AddVariable("sub_leading_eta", 'F');
  //factory->AddVariable("MET_Et", 'F');

  //factory->AddVariable("PT_F_jet", 'F');
  //factory->AddVariable("n_F_jet", 'I');
  factory->AddVariable("PT_Loose_jet", 'F');
  //factory->AddVariable("n_Loose_jet", 'I');
  factory->AddVariable("n_Loose_bjet", 'I');
  factory->AddVariable("PT_ll_j1", 'F');
  factory->AddVariable("deltaR_l1_j1", 'F');
  factory->AddVariable("deltaR_ll", 'F');
  factory->AddVariable("delta_phi_ll_j1", 'F');
  //factory->AddVariable("C_ll", 'F');
  factory->AddVariable("C_ll_j1", 'F');
  factory->AddVariable("PT_ll_MET_j1", 'F');
  //factory->AddVariable("PT_ll", 'F');
  //factory->AddVariable("PT_j1j2", 'F');
  //factory->AddVariable("PT_ll_MET", 'F');
  //factory->AddVariable("PT_ll_MET_j1j2", 'F');
  factory->AddVariable("PT_l1j1", 'F');
  //factory->AddVariable("ratio_PT_ll_MET_j1", 'F');
  //factory->AddVariable("PT_j2", 'F');
  //factory->AddVariable("delta_PT_ll", 'F');
  //factory->AddVariable("delta_PT_llj1_MET", 'F');
  //factory->AddVariable("delta_PT_MET_j1", 'F');
  //factory->AddVariable("delta_PT_llMET_j1", 'F');
  //factory->AddVariable("delta_PT_l2_j2", 'F');
  //factory->AddVariable("deltaR_l2_j1", 'F');
  //factory->AddVariable("deltaR_l1_j2", 'F');
  //factory->AddVariable("deltaR_l2_j2", 'F');
  //factory->AddVariable("deltaR_ll_j1", 'F');
  //factory->AddVariable("deltaR_ll_j2", 'F');
  //factory->AddVariable("delta_phi_ll", 'F');
  factory->AddVariable("delta_phi_ll_MET", 'F');
  //factory->AddVariable("delta_phi_j1_MET", 'F');
  //factory->AddVariable("delta_phi_j1_j2", 'F');
  //factory->AddVariable("M_l1_j1", 'F');
  //factory->AddVariable("M_l2_j1", 'F');
  //factory->AddVariable("M_l1_j2", 'F');
  //factory->AddVariable("M_l2_j2", 'F');
  //factory->AddVariable("M_j1_j2", 'F');
  factory->AddVariable("M_ll", 'F');
  //factory->AddVariable("M_ll_sys", 'F');
  //factory->AddVariable("M_ll_j2", 'F');
  //factory->AddVariable("M_ll_j1j2", 'F');
  factory->AddVariable("MT_j1_MET", 'F');
  //factory->AddVariable("E_M_llj2", 'F');
  //factory->AddVariable("ET_sys", 'F');
  //factory->AddVariable("C_l1_j1", 'F');
  //factory->AddVariable("C_l2_j2", 'F');
  //factory->AddVariable("HT_sys", 'F');
  //factory->AddVariable("HT_ll", 'F');

  //Load the signal and background event samples from ROOT trees
  
  TString sigFileTrain = "_ALL/80_inc_ST_all.root";
  TString bkgFileTrain_ttbar = "_ALL/80_inc_TT_all.root";
  TString bkgFileTrain_DY = "_ALL/80_DYToLL_50_cut.root";
  TString bkgFileTrain_WW = "_ALL/80_WWTo2L2Nu_all.root";

  TFile *inputSTrain  = TFile::Open( sigFileTrain );
  TFile *inputBTrain_ttbar = TFile::Open( bkgFileTrain_ttbar );
  TFile *inputBTrain_DY = TFile::Open( bkgFileTrain_DY );
  TFile *inputBTrain_WW = TFile::Open( bkgFileTrain_WW );
 if (!inputSTrain) {
      std::cout << "ERROR: could not open data file" << std::endl;
      exit(1);
   }

 if (!inputBTrain_ttbar) {
      std::cout << "ERROR: could not open data file" << std::endl;
      exit(1);
   }


  std::cout << "--- TMVAnalysis    : Accessing Signal Train: " << sigFileTrain << std::endl;
  std::cout << "--- TMVAnalysis    : Accessing Background Train: " << bkgFileTrain_ttbar << std::endl;
  std::cout << "--- TMVAnalysis    : Accessing Background Train: " << bkgFileTrain_DY << std::endl;
  std::cout << "--- TMVAnalysis    : Accessing Background Train: " << bkgFileTrain_WW << std::endl;

  TTree *signalTrain     = (TTree*)inputSTrain->FindObjectAny("tap");
  TTree *backgroundTrain_ttbar = (TTree*)inputBTrain_ttbar->FindObjectAny("tap");
  TTree *backgroundTrain_DY = (TTree*)inputBTrain_DY->FindObjectAny("tap");
  TTree *backgroundTrain_WW = (TTree*)inputBTrain_WW->FindObjectAny("tap");

  factory->AddSignalTree( signalTrain, 1);

  factory->AddBackgroundTree( backgroundTrain_ttbar, 1.0);
  factory->AddBackgroundTree( backgroundTrain_DY, 2.0);
  //factory->AddBackgroundTree( backgroundTrain_WW, 0.2);

  // Set SF-weight
  factory->SetSignalWeightExpression    ("weight_SF*weight_lumi");
  factory->SetBackgroundWeightExpression("weight_SF*weight_lumi");
  
  // Apply additional cuts on the signal and background samples (can be different)
  TCut my_cut = "((isEE && pass_trigger_EE_step2) || (isMuMu && pass_trigger_MuMu_step2)) && (M_ll < 81 || M_ll > 101) && MET_Et >= 50 && n_jet == 1 && n_bjet == 1";
  //TCut my_cut = "isEMu && pass_trigger_EMu_step2";
  
  factory->PrepareTrainingAndTestTree( my_cut,my_cut, "nTrain_Signal=0:nTrain_Background=0:nTest_Signal=0:nTest_Background=0:SplitMode=Random:SplitSeed=88!V" );
  
  // ---- Book MVA methods
  //factory->BookMethod( TMVA::Types::kBDT, "BDT", "!H:!V:NTrees=800:nCuts=5:BoostType=AdaBoost" );
  factory->BookMethod( TMVA::Types::kMLP, "MLP", "H:!V:NeuronType=sigmoid:VarTransform=N:NCycles=500:HiddenLayers=8:TestRate=10:EstimatorType=sigmoid" ); 

  
// Train MVAs using the set of training events
  factory->TrainAllMethods();
  
   // ---- Evaluate all MVAs using the set of test events
  factory->TestAllMethods();
  
  // ----- Evaluate and compare performance of all configured MVAs
  factory->EvaluateAllMethods();
  
  // --------------------------------------------------------------
  
  // Save the output
  outputFile->Close();
  
  std::cout << "==> Wrote root file: " << outputFile->GetName() << std::endl;
  std::cout << "==> TMVAClassification is done!" << std::endl;
  
  delete factory;
  
  // Launch the GUI for the root macros
  //if (!gROOT->IsBatch()) TMVAGui( outfileName );
}

//SetSignalWeightExpression

