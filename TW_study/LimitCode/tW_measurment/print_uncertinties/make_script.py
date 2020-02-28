import os

Method="MaxLikelihoodFit"
#Method="MultiDimFit"

system={}
system["PileUp"] =["PileUp_"]                      
system["Trigger"]=["TriggerSF_"]                      
system["UnclusteredEn"]=["UnclusteredEn_"         ]                      
system["JER"]=["JetEnergyResolution_"   ]                      
system["JES"]=["JetEnergyScale_"        ]                      
system["Btag"]=["BtagScaleFactor_bc_"    ]                      
system["Missingtag"]=["BtagScaleFactor_udsg_"  ]                      
system["DY_PDF"]=["DY_PDF_"                ]                      
system["DY_QCD"]=["DY_QCD_"                ]                      
system["Luminosity"]=["Luminosity"              ]                        
system["TT_normalisation"]=["TT_normalisation"        ]                        
system["DY_normalisation"]=[]
system["DY_normalisation"].append("is1jet_0bjet_DY_normalisation_Norm")           
system["DY_normalisation"].append("is1jet_1bjet_DY_normalisation_Norm")           
system["DY_normalisation"].append("is2jet_1bjet_DY_normalisation_Norm")           
system["DY_normalisation"].append("is2jet_2bjet_DY_normalisation_Norm")           
system["Other_normalisation"]=["Othernormalisation_Norm"   ]                      
system["Jets_normalisation"] =["Jets_normalisation_Norm"   ]                      
system["ElectronIDIso"]      =["ElectronIDIsoScaleFactor_"  ]                  
system["ElectronReco"]       =["ElectronReconstructionScaleFactor_"  ]         
system["MuonID"]             =["MuonIDScaleFactor_"     ]                      
system["MuonIso"]            =["MuonIsoScaleFactor_"    ]                      
system["MuonTrack"]          =["MuonTrackEfficiencyScaleFactor_"  ]            
system["FSR"]                =["FSR_"                   ]                      
system["ISR"]                =["ISR_"                   ]                      
system["TT_CR"]              =["TT_CR_"                 ]                      
system["TT_PDF"]             =["TT_PDF_"                ]                      
system["TT_QCD"]             =["TT_QCD_"                ]                      
system["TT_mtop"]            =["TT_TopMass_"            ]                      
system["TT_Tune"]            =["TT_Tune_"               ]                      
system["TT_hdamp"]           =["TT_hdamp_"              ]                      
system["TW_DS"]              =["tw_DS_"                 ]                      
system["TW_ME"]              =["tw_MEscale_"            ]                      
system["TW_mtop"]            =["tw_TopMass_"            ]                      
system["MC_stat"] =[]                     
system["MC_stat"].append("ee_1jet_1bjet_DY_stat_bin1_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_DY_stat_bin2_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_DY_stat_bin3_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_DY_stat_bin4_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_DY_stat_bin5_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_DY_stat_bin6_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_DY_stat_bin7_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_TT_stat_bin1_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_TT_stat_bin2_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_TT_stat_bin3_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_TT_stat_bin4_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_TT_stat_bin5_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_TT_stat_bin6_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_TT_stat_bin7_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_TW_stat_bin1_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_TW_stat_bin2_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_TW_stat_bin3_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_TW_stat_bin4_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_TW_stat_bin5_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_TW_stat_bin6_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_TW_stat_bin7_"  )                     
system["MC_stat"].append("ee_1jet_1bjet_other_stat_bin1_"  )                  
system["MC_stat"].append("ee_1jet_1bjet_other_stat_bin2_"  )                  
system["MC_stat"].append("ee_1jet_1bjet_other_stat_bin3_"  )                  
system["MC_stat"].append("ee_1jet_1bjet_other_stat_bin4_"  )                  
system["MC_stat"].append("ee_1jet_1bjet_other_stat_bin5_"  )                  
system["MC_stat"].append("ee_1jet_1bjet_other_stat_bin6_"  )                  
system["MC_stat"].append("ee_1jet_1bjet_other_stat_bin7_"  )                  
system["MC_stat"].append("ee_2jet_1bjet_DY_stat_bin1_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_DY_stat_bin2_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_DY_stat_bin3_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_DY_stat_bin4_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_DY_stat_bin5_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_DY_stat_bin6_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_TT_stat_bin1_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_TT_stat_bin2_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_TT_stat_bin3_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_TT_stat_bin4_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_TT_stat_bin5_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_TT_stat_bin6_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_TW_stat_bin1_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_TW_stat_bin2_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_TW_stat_bin3_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_TW_stat_bin4_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_TW_stat_bin5_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_TW_stat_bin6_"  )                     
system["MC_stat"].append("ee_2jet_1bjet_other_stat_bin1_"  )                  
system["MC_stat"].append("ee_2jet_1bjet_other_stat_bin2_"  )                  
system["MC_stat"].append("ee_2jet_1bjet_other_stat_bin3_"  )                  
system["MC_stat"].append("ee_2jet_1bjet_other_stat_bin4_"  )                  
system["MC_stat"].append("ee_2jet_1bjet_other_stat_bin5_"  )                  
system["MC_stat"].append("ee_2jet_1bjet_other_stat_bin6_"  )                  
system["MC_stat"].append("ee_2jet_2bjet_DY_stat_bin1_"  )                     
system["MC_stat"].append("ee_2jet_2bjet_TT_stat_bin1_"  )                     
system["MC_stat"].append("ee_2jet_2bjet_TW_stat_bin1_"  )                     
system["MC_stat"].append("ee_2jet_2bjet_other_stat_bin1_"  )                  
system["MC_stat"].append("emu_1jet_0bjet_DY_stat_bin1_"  )               
system["MC_stat"].append("emu_1jet_0bjet_DY_stat_bin2_"  )               
system["MC_stat"].append("emu_1jet_0bjet_DY_stat_bin3_"  )               
system["MC_stat"].append("emu_1jet_0bjet_DY_stat_bin4_"  )               
system["MC_stat"].append("emu_1jet_0bjet_DY_stat_bin5_"  )               
system["MC_stat"].append("emu_1jet_0bjet_TT_stat_bin1_"  )               
system["MC_stat"].append("emu_1jet_0bjet_TT_stat_bin2_"  )               
system["MC_stat"].append("emu_1jet_0bjet_TT_stat_bin3_"  )               
system["MC_stat"].append("emu_1jet_0bjet_TT_stat_bin4_"  )               
system["MC_stat"].append("emu_1jet_0bjet_TT_stat_bin5_"  )               
system["MC_stat"].append("emu_1jet_0bjet_TW_stat_bin1_"  )               
system["MC_stat"].append("emu_1jet_0bjet_TW_stat_bin2_"  )               
system["MC_stat"].append("emu_1jet_0bjet_TW_stat_bin3_"  )               
system["MC_stat"].append("emu_1jet_0bjet_TW_stat_bin4_"  )               
system["MC_stat"].append("emu_1jet_0bjet_TW_stat_bin5_"  )               
system["MC_stat"].append("emu_1jet_0bjet_other_stat_bin1_"  )            
system["MC_stat"].append("emu_1jet_0bjet_other_stat_bin2_"  )            
system["MC_stat"].append("emu_1jet_0bjet_other_stat_bin3_"  )            
system["MC_stat"].append("emu_1jet_0bjet_other_stat_bin4_"  )            
system["MC_stat"].append("emu_1jet_0bjet_other_stat_bin5_"  )            
system["MC_stat"].append("emu_1jet_1bjet_DY_stat_bin1_"  )               
system["MC_stat"].append("emu_1jet_1bjet_DY_stat_bin2_"  )               
system["MC_stat"].append("emu_1jet_1bjet_DY_stat_bin3_"  )               
system["MC_stat"].append("emu_1jet_1bjet_DY_stat_bin4_"  )               
system["MC_stat"].append("emu_1jet_1bjet_DY_stat_bin5_"  )               
system["MC_stat"].append("emu_1jet_1bjet_DY_stat_bin6_"  )               
system["MC_stat"].append("emu_1jet_1bjet_DY_stat_bin7_"  )               
system["MC_stat"].append("emu_1jet_1bjet_TT_stat_bin1_"  )               
system["MC_stat"].append("emu_1jet_1bjet_TT_stat_bin2_"  )               
system["MC_stat"].append("emu_1jet_1bjet_TT_stat_bin3_"  )               
system["MC_stat"].append("emu_1jet_1bjet_TT_stat_bin4_"  )               
system["MC_stat"].append("emu_1jet_1bjet_TT_stat_bin5_"  )               
system["MC_stat"].append("emu_1jet_1bjet_TT_stat_bin6_"  )               
system["MC_stat"].append("emu_1jet_1bjet_TT_stat_bin7_"  )               
system["MC_stat"].append("emu_1jet_1bjet_TW_stat_bin1_"  )               
system["MC_stat"].append("emu_1jet_1bjet_TW_stat_bin2_"  )               
system["MC_stat"].append("emu_1jet_1bjet_TW_stat_bin3_"  )               
system["MC_stat"].append("emu_1jet_1bjet_TW_stat_bin4_"  )               
system["MC_stat"].append("emu_1jet_1bjet_TW_stat_bin5_"  )               
system["MC_stat"].append("emu_1jet_1bjet_TW_stat_bin6_"  )               
system["MC_stat"].append("emu_1jet_1bjet_TW_stat_bin7_"  )               
system["MC_stat"].append("emu_1jet_1bjet_other_stat_bin1_"  )            
system["MC_stat"].append("emu_1jet_1bjet_other_stat_bin2_"  )            
system["MC_stat"].append("emu_1jet_1bjet_other_stat_bin3_"  )            
system["MC_stat"].append("emu_1jet_1bjet_other_stat_bin4_"  )            
system["MC_stat"].append("emu_1jet_1bjet_other_stat_bin5_"  )            
system["MC_stat"].append("emu_1jet_1bjet_other_stat_bin6_"  )            
system["MC_stat"].append("emu_1jet_1bjet_other_stat_bin7_"  )            
system["MC_stat"].append("emu_2jet_1bjet_DY_stat_bin1_"  )               
system["MC_stat"].append("emu_2jet_1bjet_DY_stat_bin2_"  )               
system["MC_stat"].append("emu_2jet_1bjet_DY_stat_bin3_"  )               
system["MC_stat"].append("emu_2jet_1bjet_DY_stat_bin4_"  )               
system["MC_stat"].append("emu_2jet_1bjet_DY_stat_bin5_"  )               
system["MC_stat"].append("emu_2jet_1bjet_DY_stat_bin6_"  )               
system["MC_stat"].append("emu_2jet_1bjet_TT_stat_bin1_"  )               
system["MC_stat"].append("emu_2jet_1bjet_TT_stat_bin2_"  )               
system["MC_stat"].append("emu_2jet_1bjet_TT_stat_bin3_"  )               
system["MC_stat"].append("emu_2jet_1bjet_TT_stat_bin4_"  )               
system["MC_stat"].append("emu_2jet_1bjet_TT_stat_bin5_"  )               
system["MC_stat"].append("emu_2jet_1bjet_TT_stat_bin6_"  )               
system["MC_stat"].append("emu_2jet_1bjet_TW_stat_bin1_"  )               
system["MC_stat"].append("emu_2jet_1bjet_TW_stat_bin2_"  )               
system["MC_stat"].append("emu_2jet_1bjet_TW_stat_bin3_"  )               
system["MC_stat"].append("emu_2jet_1bjet_TW_stat_bin4_"  )               
system["MC_stat"].append("emu_2jet_1bjet_TW_stat_bin5_"  )               
system["MC_stat"].append("emu_2jet_1bjet_TW_stat_bin6_"  )               
system["MC_stat"].append("emu_2jet_1bjet_other_stat_bin1_"  )            
system["MC_stat"].append("emu_2jet_1bjet_other_stat_bin2_"  )            
system["MC_stat"].append("emu_2jet_1bjet_other_stat_bin3_"  )            
system["MC_stat"].append("emu_2jet_1bjet_other_stat_bin4_"  )            
system["MC_stat"].append("emu_2jet_1bjet_other_stat_bin5_"  )            
system["MC_stat"].append("emu_2jet_1bjet_other_stat_bin6_"  )            
system["MC_stat"].append("emu_2jet_2bjet_DY_stat_bin1_"  )               
system["MC_stat"].append("emu_2jet_2bjet_TT_stat_bin1_"  )               
system["MC_stat"].append("emu_2jet_2bjet_TW_stat_bin1_"  )               
system["MC_stat"].append("emu_2jet_2bjet_other_stat_bin1_"  )            
system["MC_stat"].append("mumu_1jet_1bjet_DY_stat_bin1_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_DY_stat_bin2_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_DY_stat_bin3_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_DY_stat_bin4_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_DY_stat_bin5_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_DY_stat_bin6_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_DY_stat_bin7_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_TT_stat_bin1_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_TT_stat_bin2_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_TT_stat_bin3_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_TT_stat_bin4_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_TT_stat_bin5_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_TT_stat_bin6_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_TT_stat_bin7_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_TW_stat_bin1_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_TW_stat_bin2_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_TW_stat_bin3_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_TW_stat_bin4_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_TW_stat_bin5_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_TW_stat_bin6_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_TW_stat_bin7_"  )                 
system["MC_stat"].append("mumu_1jet_1bjet_other_stat_bin1_"  )              
system["MC_stat"].append("mumu_1jet_1bjet_other_stat_bin2_"  )              
system["MC_stat"].append("mumu_1jet_1bjet_other_stat_bin3_"  )              
system["MC_stat"].append("mumu_1jet_1bjet_other_stat_bin4_"  )              
system["MC_stat"].append("mumu_1jet_1bjet_other_stat_bin5_"  )              
system["MC_stat"].append("mumu_1jet_1bjet_other_stat_bin6_"  )              
system["MC_stat"].append("mumu_1jet_1bjet_other_stat_bin7_"  )              
system["MC_stat"].append("mumu_2jet_1bjet_DY_stat_bin1_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_DY_stat_bin2_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_DY_stat_bin3_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_DY_stat_bin4_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_DY_stat_bin5_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_DY_stat_bin6_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_TT_stat_bin1_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_TT_stat_bin2_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_TT_stat_bin3_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_TT_stat_bin4_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_TT_stat_bin5_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_TT_stat_bin6_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_TW_stat_bin1_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_TW_stat_bin2_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_TW_stat_bin3_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_TW_stat_bin4_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_TW_stat_bin5_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_TW_stat_bin6_"  )                 
system["MC_stat"].append("mumu_2jet_1bjet_other_stat_bin1_"  )              
system["MC_stat"].append("mumu_2jet_1bjet_other_stat_bin2_"  )              
system["MC_stat"].append("mumu_2jet_1bjet_other_stat_bin3_"  )              
system["MC_stat"].append("mumu_2jet_1bjet_other_stat_bin4_"  )              
system["MC_stat"].append("mumu_2jet_1bjet_other_stat_bin5_"  )              
system["MC_stat"].append("mumu_2jet_1bjet_other_stat_bin6_"  )              
system["MC_stat"].append("mumu_2jet_2bjet_DY_stat_bin1_"  )                 
system["MC_stat"].append("mumu_2jet_2bjet_TT_stat_bin1_"  )                 
system["MC_stat"].append("mumu_2jet_2bjet_TW_stat_bin1_"  )                 
system["MC_stat"].append("mumu_2jet_2bjet_other_stat_bin1_"  )              
system["Remove_all"]=[]
system["Total"]=[]
f_out=open("all_script.txt","w")
savedworkspace="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/print_uncertinties/workspace/higgsCombineTest.MultiDimFit.mH120.root"
out_dir="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/print_uncertinties/output"
for isys in system:
    action=""
    if isys=="Remove_all":
        action="-S 0"
    elif isys=="Total":
        action=""
    else:
        first=True
        for i in system[isys]:
            if first:
                action="--freezeNuisances "+str(i)
                first=False
            else:
                action=action+","+str(i)
    f_out.write("combine %s -M %s --snapshotName MultiDimFit %s > %s/%s.txt\n"%(savedworkspace,Method,action,out_dir,isys))
f_out.close()

