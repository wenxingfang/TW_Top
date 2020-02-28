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
void test1(){
vector<float> *v1  =    new std::vector<float>();;
vector<float> *v2  =    new std::vector<float>();;
for(unsigned int i=0; i<10;i++){ v1->push_back(i+0.1);}
for(unsigned int j=0;j<v1->size();j++){v2->push_back(v1->at(j));}
for(unsigned int k=0;k<v2->size();k++){std::cout<<"k="<<k<<",v1="<<v1->at(k)<<",v2="<<v2->at(k)<<std::endl;}
}
