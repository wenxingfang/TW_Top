#include "TMVA/Tools.h"
#include "TMVA/Reader.h"
#include "TString.h"
using namespace TMVA;

struct MVA_Reader_0j0t{
float v1=0;
float v2=0;
float v3=0;
float v4=0;
float v5=0;
TMVA::Reader *reader;
MVA_Reader_0j0t(TString method){
reader = new TMVA::Reader( "!Color:Silent" );
reader->AddVariable("leading_pt" ,&v1);
reader->AddVariable("PT_ll"      ,&v2);
reader->AddVariable("delta_PT_ll",&v3);
reader->AddVariable("M_ll"       ,&v4);
reader->AddVariable("C_ll"       ,&v5);
reader->BookMVA("region", "/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/MVA/TMVA_new_20180608/0j0b/weights/TMVA_"+method+".weights.xml");
}
double Eval(){
return reader->EvaluateMVA("region");
}
};

struct MVA_Reader_1j0t{
float v1=0;
float v2=0;
float v3=0;
float v4=0;
float v5=0;
float v6=0;
float v7=0;
TMVA::Reader *reader;
MVA_Reader_1j0t(TString method){
reader = new TMVA::Reader( "!Color:Silent" );
reader->AddVariable("leading_pt"       ,&v1);
reader->AddVariable("PT_ll"            ,&v2);
reader->AddVariable("delta_PT_ll"      ,&v3);
reader->AddVariable("M_ll"             ,&v4);
reader->AddVariable("C_ll"             ,&v5);
reader->AddVariable("C_l1_j1"          ,&v6);
reader->AddVariable("delta_phi_ll_j1"  ,&v7);
reader->BookMVA("region", "/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/MVA/TMVA_new_20180608/1j0b/weights/TMVA_"+method+".weights.xml");
}
double Eval(){
return reader->EvaluateMVA("region");
}
};

////0801/////////////
struct MVA_Reader_1j1t{
float v1=0;
float v2=0;
float v3=0;
float v4=0;
float v5=0;
float v6=0;
TMVA::Reader *reader;
MVA_Reader_1j1t(TString method){
reader = new TMVA::Reader( "!Color:Silent" );
reader->AddVariable("PT_ll_j1"       ,&v1); 
reader->AddVariable("deltaR_l1_j1"   ,&v2); 
reader->AddVariable("deltaR_ll"      ,&v3); 
reader->AddVariable("delta_phi_ll_j1",&v4); 
reader->AddVariable("C_ll_j1"        ,&v5); 
reader->AddVariable("PT_l1j1"        ,&v6); 
reader->BookMVA("region", "/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/MVA/TMVA_new_20180608/1j1b/weights/TMVA_"+method+".weights.xml");
}
double Eval(){
return reader->EvaluateMVA("region");
}
};

/////////////////
struct MVA_Reader_2j1t{
float v1=0;
float v2=0;
float v3=0;
float v4=0;
float v5=0;
float v6=0;
float v7=0;
float v8=0;
TMVA::Reader *reader;
MVA_Reader_2j1t(TString method){
reader = new TMVA::Reader( "!Color:Silent" );
reader->AddVariable("leading_pt"        ,&v1); 
reader->AddVariable("PT_ll"             ,&v2); 
reader->AddVariable("delta_PT_l2_j2"    ,&v3); 
reader->AddVariable("deltaR_l1_j2"      ,&v4); 
reader->AddVariable("deltaR_ll_j1"      ,&v5); 
reader->AddVariable("delta_phi_ll_j1"   ,&v6); 
reader->AddVariable("M_l1_j2"           ,&v7); 
reader->AddVariable("M_j1_j2"           ,&v8); 
reader->BookMVA("region", "/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/MVA/TMVA_new_20180608/2j1b/weights/TMVA_"+method+".weights.xml");
}
double Eval(){
return reader->EvaluateMVA("region");
}
};




struct MVA_Reader_BSM{
float v1=0;
float v2=0;
float v3=0;
float v4=0;
float v5=0;
float v6=0;
float v7=0;
float v8=0;
float v9=0;
TMVA::Reader *reader;
MVA_Reader_BSM(TString method){
reader = new TMVA::Reader( "!Color:Silent" );
reader->AddVariable("leading_pt"    ,&v1); 
reader->AddVariable("PT_ll"         ,&v2); 
reader->AddVariable("delta_PT_ll"   ,&v3); 
reader->AddVariable("M_ll"          ,&v4); 
reader->AddVariable("C_ll"          ,&v5); 
reader->AddVariable("PT_ll_j1"      ,&v6); 
reader->AddVariable("deltaR_ll_j1"  ,&v7); 
reader->AddVariable("M_l2_j1"       ,&v8); 
reader->AddVariable("C_l1_j1"       ,&v9); 
reader->BookMVA("region", "/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/MVA/TMVA_FastSim/Wtb_emu/weights/TMVA_"+method+".weights.xml");
}
double Eval(){
return reader->EvaluateMVA("region");
}
};

struct MVA_Reader_FCNC_tug{
float v1=0;
float v2=0;
float v3=0;
float v4=0;
float v5=0;
float v6=0;
float v7=0;
float v8=0;
float v9=0;
TMVA::Reader *reader;
MVA_Reader_FCNC_tug(TString method){
reader = new TMVA::Reader( "!Color:Silent" );
reader->AddVariable("leading_pt"    ,&v1); 
reader->AddVariable("PT_ll"         ,&v2); 
reader->AddVariable("delta_PT_ll"   ,&v3); 
reader->AddVariable("M_ll"          ,&v4); 
reader->AddVariable("C_ll"          ,&v5); 
reader->AddVariable("PT_ll_j1"      ,&v6); 
reader->AddVariable("deltaR_ll_j1"  ,&v7); 
reader->AddVariable("M_l2_j1"       ,&v8); 
reader->AddVariable("C_l1_j1"       ,&v9); 
//reader->BookMVA("region", "/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/MVA/TMVA_FastSim/FCNC_tug/weights/TMVA_"+method+".weights.xml");
reader->BookMVA("region", "/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/MVA/TMVA_FullSim/FCNC_tug/weights/TMVA_"+method+".weights.xml");
}
double Eval(){
return reader->EvaluateMVA("region");
}
};
 
struct MVA_Reader_FCNC_tcg{
float v1=0;
float v2=0;
float v3=0;
float v4=0;
float v5=0;
float v6=0;
float v7=0;
float v8=0;
float v9=0;
TMVA::Reader *reader;
MVA_Reader_FCNC_tcg(TString method){
reader = new TMVA::Reader( "!Color:Silent" );
reader->AddVariable("leading_pt"    ,&v1); 
reader->AddVariable("PT_ll"         ,&v2); 
reader->AddVariable("delta_PT_ll"   ,&v3); 
reader->AddVariable("M_ll"          ,&v4); 
reader->AddVariable("C_ll"          ,&v5); 
reader->AddVariable("PT_ll_j1"      ,&v6); 
reader->AddVariable("deltaR_ll_j1"  ,&v7); 
reader->AddVariable("M_l2_j1"       ,&v8); 
reader->AddVariable("C_l1_j1"       ,&v9); 
reader->BookMVA("region", "/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/MVA/TMVA_FastSim/FCNC_tcg/weights/TMVA_"+method+".weights.xml");
}
double Eval(){
return reader->EvaluateMVA("region");
}
};
 
 
 
 
 
 
 
 




