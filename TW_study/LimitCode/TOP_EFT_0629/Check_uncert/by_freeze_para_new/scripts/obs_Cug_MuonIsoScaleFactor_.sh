cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para_new/obs/Cug
eval `scramv1 runtime -sh`
logsave  obs_Cug_MuonIsoScaleFactor_.log combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/obs/higgsCombineCug.MultiDimFit.mH120.root -M MultiDimFit --setPhysicsModelParameterRanges r=-2.000000,2.000000   --algo grid --points 50   -n MuonIsoScaleFactor_ --snapshotName MultiDimFit --freezeNuisances TT_TopMass_,isxjet_1bjet_DY_normalisation_Norm,tw_DS_,MuonIDScaleFactor_,UnclusteredEn_,Jets_normalisation_Norm,TT_normalisation_Norm,TT_PDF_,ee_xjet_1bjet_DY_stat_bin10_,ee_xjet_1bjet_DY_stat_bin1_,ee_xjet_1bjet_DY_stat_bin2_,ee_xjet_1bjet_DY_stat_bin3_,ee_xjet_1bjet_DY_stat_bin4_,ee_xjet_1bjet_DY_stat_bin5_,ee_xjet_1bjet_DY_stat_bin6_,ee_xjet_1bjet_DY_stat_bin7_,ee_xjet_1bjet_DY_stat_bin8_,ee_xjet_1bjet_DY_stat_bin9_,ee_xjet_1bjet_FCNCSignal_stat_bin10_,ee_xjet_1bjet_FCNCSignal_stat_bin1_,ee_xjet_1bjet_FCNCSignal_stat_bin2_,ee_xjet_1bjet_FCNCSignal_stat_bin3_,ee_xjet_1bjet_FCNCSignal_stat_bin4_,ee_xjet_1bjet_FCNCSignal_stat_bin5_,ee_xjet_1bjet_FCNCSignal_stat_bin6_,ee_xjet_1bjet_FCNCSignal_stat_bin7_,ee_xjet_1bjet_FCNCSignal_stat_bin8_,ee_xjet_1bjet_FCNCSignal_stat_bin9_,ee_xjet_1bjet_TT_stat_bin10_,ee_xjet_1bjet_TT_stat_bin1_,ee_xjet_1bjet_TT_stat_bin2_,ee_xjet_1bjet_TT_stat_bin3_,ee_xjet_1bjet_TT_stat_bin4_,ee_xjet_1bjet_TT_stat_bin5_,ee_xjet_1bjet_TT_stat_bin6_,ee_xjet_1bjet_TT_stat_bin7_,ee_xjet_1bjet_TT_stat_bin8_,ee_xjet_1bjet_TT_stat_bin9_,ee_xjet_1bjet_TW_stat_bin10_,ee_xjet_1bjet_TW_stat_bin1_,ee_xjet_1bjet_TW_stat_bin2_,ee_xjet_1bjet_TW_stat_bin3_,ee_xjet_1bjet_TW_stat_bin4_,ee_xjet_1bjet_TW_stat_bin5_,ee_xjet_1bjet_TW_stat_bin6_,ee_xjet_1bjet_TW_stat_bin7_,ee_xjet_1bjet_TW_stat_bin8_,ee_xjet_1bjet_TW_stat_bin9_,ee_xjet_1bjet_other_stat_bin10_,ee_xjet_1bjet_other_stat_bin1_,ee_xjet_1bjet_other_stat_bin2_,ee_xjet_1bjet_other_stat_bin3_,ee_xjet_1bjet_other_stat_bin4_,ee_xjet_1bjet_other_stat_bin5_,ee_xjet_1bjet_other_stat_bin6_,ee_xjet_1bjet_other_stat_bin7_,ee_xjet_1bjet_other_stat_bin8_,ee_xjet_1bjet_other_stat_bin9_,emu_xjet_1bjet_DY_stat_bin10_,emu_xjet_1bjet_DY_stat_bin1_,emu_xjet_1bjet_DY_stat_bin2_,emu_xjet_1bjet_DY_stat_bin3_,emu_xjet_1bjet_DY_stat_bin4_,emu_xjet_1bjet_DY_stat_bin5_,emu_xjet_1bjet_DY_stat_bin6_,emu_xjet_1bjet_DY_stat_bin7_,emu_xjet_1bjet_DY_stat_bin8_,emu_xjet_1bjet_DY_stat_bin9_,emu_xjet_1bjet_FCNCSignal_stat_bin10_,emu_xjet_1bjet_FCNCSignal_stat_bin1_,emu_xjet_1bjet_FCNCSignal_stat_bin2_,emu_xjet_1bjet_FCNCSignal_stat_bin3_,emu_xjet_1bjet_FCNCSignal_stat_bin4_,emu_xjet_1bjet_FCNCSignal_stat_bin5_,emu_xjet_1bjet_FCNCSignal_stat_bin6_,emu_xjet_1bjet_FCNCSignal_stat_bin7_,emu_xjet_1bjet_FCNCSignal_stat_bin8_,emu_xjet_1bjet_FCNCSignal_stat_bin9_,emu_xjet_1bjet_TT_stat_bin10_,emu_xjet_1bjet_TT_stat_bin1_,emu_xjet_1bjet_TT_stat_bin2_,emu_xjet_1bjet_TT_stat_bin3_,emu_xjet_1bjet_TT_stat_bin4_,emu_xjet_1bjet_TT_stat_bin5_,emu_xjet_1bjet_TT_stat_bin6_,emu_xjet_1bjet_TT_stat_bin7_,emu_xjet_1bjet_TT_stat_bin8_,emu_xjet_1bjet_TT_stat_bin9_,emu_xjet_1bjet_TW_stat_bin10_,emu_xjet_1bjet_TW_stat_bin1_,emu_xjet_1bjet_TW_stat_bin2_,emu_xjet_1bjet_TW_stat_bin3_,emu_xjet_1bjet_TW_stat_bin4_,emu_xjet_1bjet_TW_stat_bin5_,emu_xjet_1bjet_TW_stat_bin6_,emu_xjet_1bjet_TW_stat_bin7_,emu_xjet_1bjet_TW_stat_bin8_,emu_xjet_1bjet_TW_stat_bin9_,emu_xjet_1bjet_other_stat_bin10_,emu_xjet_1bjet_other_stat_bin1_,emu_xjet_1bjet_other_stat_bin2_,emu_xjet_1bjet_other_stat_bin3_,emu_xjet_1bjet_other_stat_bin4_,emu_xjet_1bjet_other_stat_bin5_,emu_xjet_1bjet_other_stat_bin6_,emu_xjet_1bjet_other_stat_bin7_,emu_xjet_1bjet_other_stat_bin8_,emu_xjet_1bjet_other_stat_bin9_,mumu_xjet_1bjet_DY_stat_bin10_,mumu_xjet_1bjet_DY_stat_bin1_,mumu_xjet_1bjet_DY_stat_bin2_,mumu_xjet_1bjet_DY_stat_bin3_,mumu_xjet_1bjet_DY_stat_bin4_,mumu_xjet_1bjet_DY_stat_bin5_,mumu_xjet_1bjet_DY_stat_bin6_,mumu_xjet_1bjet_DY_stat_bin7_,mumu_xjet_1bjet_DY_stat_bin8_,mumu_xjet_1bjet_DY_stat_bin9_,mumu_xjet_1bjet_FCNCSignal_stat_bin10_,mumu_xjet_1bjet_FCNCSignal_stat_bin1_,mumu_xjet_1bjet_FCNCSignal_stat_bin2_,mumu_xjet_1bjet_FCNCSignal_stat_bin3_,mumu_xjet_1bjet_FCNCSignal_stat_bin4_,mumu_xjet_1bjet_FCNCSignal_stat_bin5_,mumu_xjet_1bjet_FCNCSignal_stat_bin6_,mumu_xjet_1bjet_FCNCSignal_stat_bin7_,mumu_xjet_1bjet_FCNCSignal_stat_bin8_,mumu_xjet_1bjet_FCNCSignal_stat_bin9_,mumu_xjet_1bjet_TT_stat_bin10_,mumu_xjet_1bjet_TT_stat_bin1_,mumu_xjet_1bjet_TT_stat_bin2_,mumu_xjet_1bjet_TT_stat_bin3_,mumu_xjet_1bjet_TT_stat_bin4_,mumu_xjet_1bjet_TT_stat_bin5_,mumu_xjet_1bjet_TT_stat_bin6_,mumu_xjet_1bjet_TT_stat_bin7_,mumu_xjet_1bjet_TT_stat_bin8_,mumu_xjet_1bjet_TT_stat_bin9_,mumu_xjet_1bjet_TW_stat_bin10_,mumu_xjet_1bjet_TW_stat_bin1_,mumu_xjet_1bjet_TW_stat_bin2_,mumu_xjet_1bjet_TW_stat_bin3_,mumu_xjet_1bjet_TW_stat_bin4_,mumu_xjet_1bjet_TW_stat_bin5_,mumu_xjet_1bjet_TW_stat_bin6_,mumu_xjet_1bjet_TW_stat_bin7_,mumu_xjet_1bjet_TW_stat_bin8_,mumu_xjet_1bjet_TW_stat_bin9_,mumu_xjet_1bjet_other_stat_bin10_,mumu_xjet_1bjet_other_stat_bin1_,mumu_xjet_1bjet_other_stat_bin2_,mumu_xjet_1bjet_other_stat_bin3_,mumu_xjet_1bjet_other_stat_bin4_,mumu_xjet_1bjet_other_stat_bin5_,mumu_xjet_1bjet_other_stat_bin6_,mumu_xjet_1bjet_other_stat_bin7_,mumu_xjet_1bjet_other_stat_bin8_,mumu_xjet_1bjet_other_stat_bin9_,TW_normalisation_Norm,JetEnergyScale_,FCNC_PDF_,PileUp_,FSR_,MuonTrackEfficiencyScaleFactor_,tw_TopMass_,TT_Tune_,Luminosity,BtagScaleFactor_udsg_,FCNC_PS_,ElectronReconstructionScaleFactor_,TT_QCD_,ISR_,Othernormalisation_Norm,TT_CR_,BtagScaleFactor_bc_,MuonIsoScaleFactor_ 