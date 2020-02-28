import ROOT
import math
#Dir="./ntuples/saved_hist/Step2_0816_Rinout/"
Dir="./ntuples/saved_hist/Step2_1013_xjet_1bjet/"
f_ee  =ROOT.TFile(Dir+"ee_nominal_.root","read")
f_mumu=ROOT.TFile(Dir+"mumu_nominal_.root","read")
hist="nominal__data__H_Rinout_Mll_Region"
#hist="nominal__data__H_Rinout_Mll_NoMET_Region"
for region in ["all","0j0b","1j0b","1j1b","2j1b","2j2b"]:
    hist_name=hist.replace("Region",str(region))
    h_ee  =f_ee  .Get(hist_name)
    h_mumu=f_mumu.Get(hist_name)
    N_ee  =h_ee  .GetBinContent(2)
    N_mumu=h_mumu.GetBinContent(2)
    k_ee_error=math.sqrt(1/(4*N_ee*math.pow(N_mumu,3))*(N_mumu*N_mumu*N_ee+N_ee*N_ee*N_mumu))
    k_mumu_error=math.sqrt(1/(4*N_mumu*math.pow(N_ee,3))*(N_ee*N_ee*N_mumu+N_mumu*N_mumu*N_ee))
    print region+"|",
    print "ee:%d|mumu:%d|kee:%.2f +/- %.5f|kmumu:%.2f +/- %.5f|\n"%(N_ee,N_mumu,math.sqrt(N_ee/N_mumu),k_ee_error,math.sqrt(N_mumu/N_ee),k_mumu_error)
   
