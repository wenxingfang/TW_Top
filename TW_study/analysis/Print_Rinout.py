import ROOT
import math
import os
ROOT.TH1.AddDirectory(ROOT.kFALSE)


Dir="./ntuples/saved_hist/Step2_1013_xjet_1bjet/"
#Dir="./ntuples/saved_hist/Step2_0818_QCD/"

F_ee  =ROOT.TFile(Dir+"ee_nominal_.root"  ,"read")
F_emu =ROOT.TFile(Dir+"emu_nominal_.root" ,"read")
F_mumu=ROOT.TFile(Dir+"mumu_nominal_.root","read")
Lumi=35867
MC_Sample={}
MC_Sample["DYJetsToLL_M10to50_amc"]=[29332494 ,18610  ]
MC_Sample["DYJetsToLL_M50_amc"    ]=[68009629 ,5765.4 ]
region_list=[]
region_list.append("H_Rinout_Mll_all" ) 
region_list.append("H_Rinout_Mll_0j0b") 
region_list.append("H_Rinout_Mll_1j0b") 
region_list.append("H_Rinout_Mll_1j1b") 
region_list.append("H_Rinout_Mll_2j1b") 
region_list.append("H_Rinout_Mll_2j2b")

Kll={}
Kll["all" ]={"ee":[0.66,0.00085],"mumu":[1.51,0.00193]}
Kll["0j0b"]={"ee":[0.66,0.00103],"mumu":[1.53,0.00241]}
Kll["1j0b"]={"ee":[0.67,0.00192],"mumu":[1.50,0.00432]}
Kll["1j1b"]={"ee":[0.68,0.00663],"mumu":[1.48,0.01445]}
Kll["2j1b"]={"ee":[0.70,0.00704],"mumu":[1.42,0.01422]}
Kll["2j2b"]={"ee":[0.69,0.00846],"mumu":[1.44,0.01757]}




for chan in ["ee","mumu"]:
    print chan
    for ihist in region_list:
        print ihist,
        h_data_emu=F_emu.Get("nominal__data__%s"%(ihist))
        h_data    =h_data_emu.Clone("%s_%s"%(chan,ihist))
        h_DY      =h_data_emu.Clone("%s_%s"%(chan,ihist))
        h_DY.Scale(0)
        #h_DY.Sumw2()
        if chan=="ee":
            h_data=F_ee.Get("nominal__data__%s"%(ihist))    
            h_DY.Add(F_ee.Get("nominal__DYJetsToLL_M10to50_amc__%s"%(ihist)),float(Lumi*MC_Sample["DYJetsToLL_M10to50_amc"][1])/MC_Sample["DYJetsToLL_M10to50_amc"][0])    
            h_DY.Add(F_ee.Get("nominal__DYJetsToLL_M50_amc__%s"%(ihist))    ,float(Lumi*MC_Sample["DYJetsToLL_M50_amc"][1])/MC_Sample["DYJetsToLL_M50_amc"][0])    
        elif chan=="mumu":
            h_data=F_mumu.Get("nominal__data__%s"%(ihist))    
            h_DY.Add(F_mumu.Get("nominal__DYJetsToLL_M10to50_amc__%s"%(ihist)),float(Lumi*MC_Sample["DYJetsToLL_M10to50_amc"][1])/MC_Sample["DYJetsToLL_M10to50_amc"][0])    
            h_DY.Add(F_mumu.Get("nominal__DYJetsToLL_M50_amc__%s"%(ihist))    ,float(Lumi*MC_Sample["DYJetsToLL_M50_amc"][1])/MC_Sample["DYJetsToLL_M50_amc"][0])    
        else: print "wrong channel!"
        data_in =h_data.GetBinContent(2)
        data_out=h_data.GetBinContent(1)+h_data.GetBinContent(3)
        DY_in   =h_DY.GetBinContent(2)
        DY_in_err =h_DY.GetBinError(2)
        DY_out  =h_DY.GetBinContent(1)+h_DY.GetBinContent(3)
        DY_ratio_out_in=float(DY_out/DY_in)
        data_emu_in=h_data_emu.GetBinContent(2)
        kll=1
        kll_err=0
        region=ihist.split("H_Rinout_Mll_")[-1]
        kll    =Kll[region][chan][0]
        kll_err=Kll[region][chan][1]
        #if   chan=="mumu":
        #    kll=1.49#1.44
        #    kll_err=0.00029
        #elif chan=="ee"  :
        #    kll=0.67#0.70
        #    kll_err=0.00013

        N_out=DY_ratio_out_in*(data_in-0.5*data_emu_in*kll) 
        C_DY=N_out/DY_out
        C_DY_err=math.sqrt(data_in*math.pow(1/DY_in,2)+DY_in_err*DY_in_err*math.pow((data_in-0.5*data_emu_in*kll)/(DY_in*DY_in),2)+data_emu_in*math.pow(0.5*kll/DY_in,2)+kll_err*kll_err*math.pow(0.5*data_emu_in/DY_in,2))
        print "data_in:%d|data_out:%d|DY_in:%.3f|DY_out:%.3f|DY_ratio_out_in:%.3f|data_emu_in:%d|Final_Data_Out:%.3f|C:%.3f +/- %.3f|"%(data_in,data_out,DY_in,DY_out,DY_ratio_out_in,data_emu_in,N_out,C_DY,C_DY_err)
F_ee.Close()
F_emu.Close()
F_mumu.Close()
