cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para_new/obs/Cphiq
eval `scramv1 runtime -sh`
logsave  obs_Cphiq_BtagScaleFactor_udsg_.log combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/obs/higgsCombineCphiq.MultiDimFit.mH120.root -M MultiDimFit --setPhysicsModelParameterRanges r=-4.000000,2.000000   --algo grid --points 50   -n BtagScaleFactor_udsg_ --snapshotName MultiDimFit --freezeNuisances TT_TopMass_,tw_DS_,DY_QCD_,MuonIDScaleFactor_,UnclusteredEn_,is1jet_1bjet_DY_normalisation,TT_PDF_,ee_1jet_1bjet_DY_stat_bin1_,ee_1jet_1bjet_DY_stat_bin2_,ee_1jet_1bjet_DY_stat_bin3_,ee_1jet_1bjet_DY_stat_bin4_,ee_1jet_1bjet_DY_stat_bin5_,ee_1jet_1bjet_TT_stat_bin1_,ee_1jet_1bjet_TT_stat_bin2_,ee_1jet_1bjet_TT_stat_bin3_,ee_1jet_1bjet_TT_stat_bin4_,ee_1jet_1bjet_TT_stat_bin5_,ee_1jet_1bjet_TW_stat_bin1_,ee_1jet_1bjet_TW_stat_bin2_,ee_1jet_1bjet_TW_stat_bin3_,ee_1jet_1bjet_TW_stat_bin4_,ee_1jet_1bjet_TW_stat_bin5_,ee_1jet_1bjet_other_stat_bin1_,ee_1jet_1bjet_other_stat_bin2_,ee_1jet_1bjet_other_stat_bin3_,ee_1jet_1bjet_other_stat_bin4_,ee_1jet_1bjet_other_stat_bin5_,ee_2jet_1bjet_DY_stat_bin1_,ee_2jet_1bjet_DY_stat_bin2_,ee_2jet_1bjet_DY_stat_bin3_,ee_2jet_1bjet_DY_stat_bin4_,ee_2jet_1bjet_DY_stat_bin5_,ee_2jet_1bjet_DY_stat_bin6_,ee_2jet_1bjet_TT_stat_bin1_,ee_2jet_1bjet_TT_stat_bin2_,ee_2jet_1bjet_TT_stat_bin3_,ee_2jet_1bjet_TT_stat_bin4_,ee_2jet_1bjet_TT_stat_bin5_,ee_2jet_1bjet_TT_stat_bin6_,ee_2jet_1bjet_TW_stat_bin1_,ee_2jet_1bjet_TW_stat_bin2_,ee_2jet_1bjet_TW_stat_bin3_,ee_2jet_1bjet_TW_stat_bin4_,ee_2jet_1bjet_TW_stat_bin5_,ee_2jet_1bjet_TW_stat_bin6_,ee_2jet_1bjet_other_stat_bin1_,ee_2jet_1bjet_other_stat_bin2_,ee_2jet_1bjet_other_stat_bin3_,ee_2jet_1bjet_other_stat_bin4_,ee_2jet_1bjet_other_stat_bin5_,ee_2jet_1bjet_other_stat_bin6_,ee_2jet_2bjet_DY_stat_bin1_,ee_2jet_2bjet_TT_stat_bin1_,ee_2jet_2bjet_TW_stat_bin1_,ee_2jet_2bjet_other_stat_bin1_,emu_1jet_0bjet_DY_stat_bin1_,emu_1jet_0bjet_DY_stat_bin2_,emu_1jet_0bjet_DY_stat_bin3_,emu_1jet_0bjet_DY_stat_bin4_,emu_1jet_0bjet_DY_stat_bin5_,emu_1jet_0bjet_TT_stat_bin1_,emu_1jet_0bjet_TT_stat_bin2_,emu_1jet_0bjet_TT_stat_bin3_,emu_1jet_0bjet_TT_stat_bin4_,emu_1jet_0bjet_TT_stat_bin5_,emu_1jet_0bjet_TW_stat_bin1_,emu_1jet_0bjet_TW_stat_bin2_,emu_1jet_0bjet_TW_stat_bin3_,emu_1jet_0bjet_TW_stat_bin4_,emu_1jet_0bjet_TW_stat_bin5_,emu_1jet_0bjet_other_stat_bin1_,emu_1jet_0bjet_other_stat_bin2_,emu_1jet_0bjet_other_stat_bin3_,emu_1jet_0bjet_other_stat_bin4_,emu_1jet_0bjet_other_stat_bin5_,emu_1jet_1bjet_DY_stat_bin1_,emu_1jet_1bjet_DY_stat_bin2_,emu_1jet_1bjet_DY_stat_bin3_,emu_1jet_1bjet_DY_stat_bin4_,emu_1jet_1bjet_DY_stat_bin5_,emu_1jet_1bjet_TT_stat_bin1_,emu_1jet_1bjet_TT_stat_bin2_,emu_1jet_1bjet_TT_stat_bin3_,emu_1jet_1bjet_TT_stat_bin4_,emu_1jet_1bjet_TT_stat_bin5_,emu_1jet_1bjet_TW_stat_bin1_,emu_1jet_1bjet_TW_stat_bin2_,emu_1jet_1bjet_TW_stat_bin3_,emu_1jet_1bjet_TW_stat_bin4_,emu_1jet_1bjet_TW_stat_bin5_,emu_1jet_1bjet_other_stat_bin1_,emu_1jet_1bjet_other_stat_bin2_,emu_1jet_1bjet_other_stat_bin3_,emu_1jet_1bjet_other_stat_bin4_,emu_1jet_1bjet_other_stat_bin5_,emu_2jet_1bjet_DY_stat_bin1_,emu_2jet_1bjet_DY_stat_bin2_,emu_2jet_1bjet_DY_stat_bin3_,emu_2jet_1bjet_DY_stat_bin4_,emu_2jet_1bjet_DY_stat_bin5_,emu_2jet_1bjet_DY_stat_bin6_,emu_2jet_1bjet_TT_stat_bin1_,emu_2jet_1bjet_TT_stat_bin2_,emu_2jet_1bjet_TT_stat_bin3_,emu_2jet_1bjet_TT_stat_bin4_,emu_2jet_1bjet_TT_stat_bin5_,emu_2jet_1bjet_TT_stat_bin6_,emu_2jet_1bjet_TW_stat_bin1_,emu_2jet_1bjet_TW_stat_bin2_,emu_2jet_1bjet_TW_stat_bin3_,emu_2jet_1bjet_TW_stat_bin4_,emu_2jet_1bjet_TW_stat_bin5_,emu_2jet_1bjet_TW_stat_bin6_,emu_2jet_1bjet_other_stat_bin1_,emu_2jet_1bjet_other_stat_bin2_,emu_2jet_1bjet_other_stat_bin3_,emu_2jet_1bjet_other_stat_bin4_,emu_2jet_1bjet_other_stat_bin5_,emu_2jet_1bjet_other_stat_bin6_,emu_2jet_2bjet_DY_stat_bin1_,emu_2jet_2bjet_TT_stat_bin1_,emu_2jet_2bjet_TW_stat_bin1_,emu_2jet_2bjet_other_stat_bin1_,mumu_1jet_1bjet_DY_stat_bin1_,mumu_1jet_1bjet_DY_stat_bin2_,mumu_1jet_1bjet_DY_stat_bin3_,mumu_1jet_1bjet_DY_stat_bin4_,mumu_1jet_1bjet_DY_stat_bin5_,mumu_1jet_1bjet_TT_stat_bin1_,mumu_1jet_1bjet_TT_stat_bin2_,mumu_1jet_1bjet_TT_stat_bin3_,mumu_1jet_1bjet_TT_stat_bin4_,mumu_1jet_1bjet_TT_stat_bin5_,mumu_1jet_1bjet_TW_stat_bin1_,mumu_1jet_1bjet_TW_stat_bin2_,mumu_1jet_1bjet_TW_stat_bin3_,mumu_1jet_1bjet_TW_stat_bin4_,mumu_1jet_1bjet_TW_stat_bin5_,mumu_1jet_1bjet_other_stat_bin1_,mumu_1jet_1bjet_other_stat_bin2_,mumu_1jet_1bjet_other_stat_bin3_,mumu_1jet_1bjet_other_stat_bin4_,mumu_1jet_1bjet_other_stat_bin5_,mumu_2jet_1bjet_DY_stat_bin1_,mumu_2jet_1bjet_DY_stat_bin2_,mumu_2jet_1bjet_DY_stat_bin3_,mumu_2jet_1bjet_DY_stat_bin4_,mumu_2jet_1bjet_DY_stat_bin5_,mumu_2jet_1bjet_DY_stat_bin6_,mumu_2jet_1bjet_TT_stat_bin1_,mumu_2jet_1bjet_TT_stat_bin2_,mumu_2jet_1bjet_TT_stat_bin3_,mumu_2jet_1bjet_TT_stat_bin4_,mumu_2jet_1bjet_TT_stat_bin5_,mumu_2jet_1bjet_TT_stat_bin6_,mumu_2jet_1bjet_TW_stat_bin1_,mumu_2jet_1bjet_TW_stat_bin2_,mumu_2jet_1bjet_TW_stat_bin3_,mumu_2jet_1bjet_TW_stat_bin4_,mumu_2jet_1bjet_TW_stat_bin5_,mumu_2jet_1bjet_TW_stat_bin6_,mumu_2jet_1bjet_other_stat_bin1_,mumu_2jet_1bjet_other_stat_bin2_,mumu_2jet_1bjet_other_stat_bin3_,mumu_2jet_1bjet_other_stat_bin4_,mumu_2jet_1bjet_other_stat_bin5_,mumu_2jet_1bjet_other_stat_bin6_,mumu_2jet_2bjet_DY_stat_bin1_,mumu_2jet_2bjet_TT_stat_bin1_,mumu_2jet_2bjet_TW_stat_bin1_,mumu_2jet_2bjet_other_stat_bin1_,JetEnergyScale_,is1jet_0bjet_DY_normalisation,ISR_,FSR_,MuonTrackEfficiencyScaleFactor_,tw_TopMass_,TT_Tune_,Luminosity,BtagScaleFactor_udsg_ 