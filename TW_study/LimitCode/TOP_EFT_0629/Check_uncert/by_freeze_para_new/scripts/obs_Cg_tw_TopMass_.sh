cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para_new/obs/Cg
eval `scramv1 runtime -sh`
logsave  obs_Cg_tw_TopMass_.log combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/obs/higgsCombineCg.MultiDimFit.mH120.root -M MultiDimFit --setPhysicsModelParameterRanges r=-1.000000,1.000000   --algo grid --points 50   -n tw_TopMass_ --snapshotName MultiDimFit --freezeNuisances TT_TopMass_,tw_DS_,DY_QCD_,MuonIDScaleFactor_,is1jet_1bjet_DY_normalisation,TT_PDF_,ee_1jet_1bjet_DY_stat_bin1_,ee_1jet_1bjet_TT_stat_bin1_,ee_1jet_1bjet_TW_stat_bin1_,ee_1jet_1bjet_other_stat_bin1_,ee_2jet_1bjet_DY_stat_bin1_,ee_2jet_1bjet_TT_stat_bin1_,ee_2jet_1bjet_TW_stat_bin1_,ee_2jet_1bjet_other_stat_bin1_,ee_2jet_2bjet_DY_stat_bin1_,ee_2jet_2bjet_TT_stat_bin1_,ee_2jet_2bjet_TW_stat_bin1_,ee_2jet_2bjet_other_stat_bin1_,emu_1jet_0bjet_DY_stat_bin1_,emu_1jet_0bjet_TT_stat_bin1_,emu_1jet_0bjet_TW_stat_bin1_,emu_1jet_0bjet_other_stat_bin1_,emu_1jet_1bjet_DY_stat_bin1_,emu_1jet_1bjet_TT_stat_bin1_,emu_1jet_1bjet_TW_stat_bin1_,emu_1jet_1bjet_other_stat_bin1_,emu_2jet_1bjet_DY_stat_bin1_,emu_2jet_1bjet_TT_stat_bin1_,emu_2jet_1bjet_TW_stat_bin1_,emu_2jet_1bjet_other_stat_bin1_,emu_2jet_2bjet_DY_stat_bin1_,emu_2jet_2bjet_TT_stat_bin1_,emu_2jet_2bjet_TW_stat_bin1_,emu_2jet_2bjet_other_stat_bin1_,mumu_1jet_1bjet_DY_stat_bin1_,mumu_1jet_1bjet_TT_stat_bin1_,mumu_1jet_1bjet_TW_stat_bin1_,mumu_1jet_1bjet_other_stat_bin1_,mumu_2jet_1bjet_DY_stat_bin1_,mumu_2jet_1bjet_TT_stat_bin1_,mumu_2jet_1bjet_TW_stat_bin1_,mumu_2jet_1bjet_other_stat_bin1_,mumu_2jet_2bjet_DY_stat_bin1_,mumu_2jet_2bjet_TT_stat_bin1_,mumu_2jet_2bjet_TW_stat_bin1_,mumu_2jet_2bjet_other_stat_bin1_,JetEnergyScale_,TW_normalisation,is1jet_0bjet_DY_normalisation,PileUp_,FSR_,is2jet_2bjet_DY_normalisation,MuonTrackEfficiencyScaleFactor_,tw_TopMass_ 