cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para/MultiDimFit/exp/Ctg
eval `scramv1 runtime -sh`
logsave  exp_Ctg_MC_stat.log combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/exp/higgsCombineCtg.MultiDimFit.mH120.root -M MultiDimFit --setPhysicsModelParameterRanges r=-0.500000,0.500000  --robustFit=1 -t -1 --expectSignal=0 --minimizerTolerance=0.0001 --snapshotName MultiDimFit --freezeNuisances ee_1jet_1bjet_DY_stat_bin1_,ee_1jet_1bjet_DY_stat_bin2_,ee_1jet_1bjet_DY_stat_bin3_,ee_1jet_1bjet_DY_stat_bin4_,ee_1jet_1bjet_DY_stat_bin5_,ee_1jet_1bjet_TT_stat_bin1_,ee_1jet_1bjet_TT_stat_bin2_,ee_1jet_1bjet_TT_stat_bin3_,ee_1jet_1bjet_TT_stat_bin4_,ee_1jet_1bjet_TT_stat_bin5_,ee_1jet_1bjet_TW_stat_bin1_,ee_1jet_1bjet_TW_stat_bin2_,ee_1jet_1bjet_TW_stat_bin3_,ee_1jet_1bjet_TW_stat_bin4_,ee_1jet_1bjet_TW_stat_bin5_,ee_1jet_1bjet_other_stat_bin1_,ee_1jet_1bjet_other_stat_bin2_,ee_1jet_1bjet_other_stat_bin3_,ee_1jet_1bjet_other_stat_bin4_,ee_1jet_1bjet_other_stat_bin5_,ee_2jet_1bjet_DY_stat_bin1_,ee_2jet_1bjet_DY_stat_bin2_,ee_2jet_1bjet_DY_stat_bin3_,ee_2jet_1bjet_DY_stat_bin4_,ee_2jet_1bjet_DY_stat_bin5_,ee_2jet_1bjet_DY_stat_bin6_,ee_2jet_1bjet_TT_stat_bin1_,ee_2jet_1bjet_TT_stat_bin2_,ee_2jet_1bjet_TT_stat_bin3_,ee_2jet_1bjet_TT_stat_bin4_,ee_2jet_1bjet_TT_stat_bin5_,ee_2jet_1bjet_TT_stat_bin6_,ee_2jet_1bjet_TW_stat_bin1_,ee_2jet_1bjet_TW_stat_bin2_,ee_2jet_1bjet_TW_stat_bin3_,ee_2jet_1bjet_TW_stat_bin4_,ee_2jet_1bjet_TW_stat_bin5_,ee_2jet_1bjet_TW_stat_bin6_,ee_2jet_1bjet_other_stat_bin1_,ee_2jet_1bjet_other_stat_bin2_,ee_2jet_1bjet_other_stat_bin3_,ee_2jet_1bjet_other_stat_bin4_,ee_2jet_1bjet_other_stat_bin5_,ee_2jet_1bjet_other_stat_bin6_,ee_2jet_2bjet_DY_stat_bin1_,ee_2jet_2bjet_TT_stat_bin1_,ee_2jet_2bjet_TW_stat_bin1_,ee_2jet_2bjet_other_stat_bin1_,emu_1jet_0bjet_DY_stat_bin1_,emu_1jet_0bjet_DY_stat_bin2_,emu_1jet_0bjet_DY_stat_bin3_,emu_1jet_0bjet_DY_stat_bin4_,emu_1jet_0bjet_DY_stat_bin5_,emu_1jet_0bjet_TT_stat_bin1_,emu_1jet_0bjet_TT_stat_bin2_,emu_1jet_0bjet_TT_stat_bin3_,emu_1jet_0bjet_TT_stat_bin4_,emu_1jet_0bjet_TT_stat_bin5_,emu_1jet_0bjet_TW_stat_bin1_,emu_1jet_0bjet_TW_stat_bin2_,emu_1jet_0bjet_TW_stat_bin3_,emu_1jet_0bjet_TW_stat_bin4_,emu_1jet_0bjet_TW_stat_bin5_,emu_1jet_0bjet_other_stat_bin1_,emu_1jet_0bjet_other_stat_bin2_,emu_1jet_0bjet_other_stat_bin3_,emu_1jet_0bjet_other_stat_bin4_,emu_1jet_0bjet_other_stat_bin5_,emu_1jet_1bjet_DY_stat_bin1_,emu_1jet_1bjet_DY_stat_bin2_,emu_1jet_1bjet_DY_stat_bin3_,emu_1jet_1bjet_DY_stat_bin4_,emu_1jet_1bjet_DY_stat_bin5_,emu_1jet_1bjet_TT_stat_bin1_,emu_1jet_1bjet_TT_stat_bin2_,emu_1jet_1bjet_TT_stat_bin3_,emu_1jet_1bjet_TT_stat_bin4_,emu_1jet_1bjet_TT_stat_bin5_,emu_1jet_1bjet_TW_stat_bin1_,emu_1jet_1bjet_TW_stat_bin2_,emu_1jet_1bjet_TW_stat_bin3_,emu_1jet_1bjet_TW_stat_bin4_,emu_1jet_1bjet_TW_stat_bin5_,emu_1jet_1bjet_other_stat_bin1_,emu_1jet_1bjet_other_stat_bin2_,emu_1jet_1bjet_other_stat_bin3_,emu_1jet_1bjet_other_stat_bin4_,emu_1jet_1bjet_other_stat_bin5_,emu_2jet_1bjet_DY_stat_bin1_,emu_2jet_1bjet_DY_stat_bin2_,emu_2jet_1bjet_DY_stat_bin3_,emu_2jet_1bjet_DY_stat_bin4_,emu_2jet_1bjet_DY_stat_bin5_,emu_2jet_1bjet_DY_stat_bin6_,emu_2jet_1bjet_TT_stat_bin1_,emu_2jet_1bjet_TT_stat_bin2_,emu_2jet_1bjet_TT_stat_bin3_,emu_2jet_1bjet_TT_stat_bin4_,emu_2jet_1bjet_TT_stat_bin5_,emu_2jet_1bjet_TT_stat_bin6_,emu_2jet_1bjet_TW_stat_bin1_,emu_2jet_1bjet_TW_stat_bin2_,emu_2jet_1bjet_TW_stat_bin3_,emu_2jet_1bjet_TW_stat_bin4_,emu_2jet_1bjet_TW_stat_bin5_,emu_2jet_1bjet_TW_stat_bin6_,emu_2jet_1bjet_other_stat_bin1_,emu_2jet_1bjet_other_stat_bin2_,emu_2jet_1bjet_other_stat_bin3_,emu_2jet_1bjet_other_stat_bin4_,emu_2jet_1bjet_other_stat_bin5_,emu_2jet_1bjet_other_stat_bin6_,emu_2jet_2bjet_DY_stat_bin1_,emu_2jet_2bjet_TT_stat_bin1_,emu_2jet_2bjet_TW_stat_bin1_,emu_2jet_2bjet_other_stat_bin1_,mumu_1jet_1bjet_DY_stat_bin1_,mumu_1jet_1bjet_DY_stat_bin2_,mumu_1jet_1bjet_DY_stat_bin3_,mumu_1jet_1bjet_DY_stat_bin4_,mumu_1jet_1bjet_DY_stat_bin5_,mumu_1jet_1bjet_TT_stat_bin1_,mumu_1jet_1bjet_TT_stat_bin2_,mumu_1jet_1bjet_TT_stat_bin3_,mumu_1jet_1bjet_TT_stat_bin4_,mumu_1jet_1bjet_TT_stat_bin5_,mumu_1jet_1bjet_TW_stat_bin1_,mumu_1jet_1bjet_TW_stat_bin2_,mumu_1jet_1bjet_TW_stat_bin3_,mumu_1jet_1bjet_TW_stat_bin4_,mumu_1jet_1bjet_TW_stat_bin5_,mumu_1jet_1bjet_other_stat_bin1_,mumu_1jet_1bjet_other_stat_bin2_,mumu_1jet_1bjet_other_stat_bin3_,mumu_1jet_1bjet_other_stat_bin4_,mumu_1jet_1bjet_other_stat_bin5_,mumu_2jet_1bjet_DY_stat_bin1_,mumu_2jet_1bjet_DY_stat_bin2_,mumu_2jet_1bjet_DY_stat_bin3_,mumu_2jet_1bjet_DY_stat_bin4_,mumu_2jet_1bjet_DY_stat_bin5_,mumu_2jet_1bjet_DY_stat_bin6_,mumu_2jet_1bjet_TT_stat_bin1_,mumu_2jet_1bjet_TT_stat_bin2_,mumu_2jet_1bjet_TT_stat_bin3_,mumu_2jet_1bjet_TT_stat_bin4_,mumu_2jet_1bjet_TT_stat_bin5_,mumu_2jet_1bjet_TT_stat_bin6_,mumu_2jet_1bjet_TW_stat_bin1_,mumu_2jet_1bjet_TW_stat_bin2_,mumu_2jet_1bjet_TW_stat_bin3_,mumu_2jet_1bjet_TW_stat_bin4_,mumu_2jet_1bjet_TW_stat_bin5_,mumu_2jet_1bjet_TW_stat_bin6_,mumu_2jet_1bjet_other_stat_bin1_,mumu_2jet_1bjet_other_stat_bin2_,mumu_2jet_1bjet_other_stat_bin3_,mumu_2jet_1bjet_other_stat_bin4_,mumu_2jet_1bjet_other_stat_bin5_,mumu_2jet_1bjet_other_stat_bin6_,mumu_2jet_2bjet_DY_stat_bin1_,mumu_2jet_2bjet_TT_stat_bin1_,mumu_2jet_2bjet_TW_stat_bin1_,mumu_2jet_2bjet_other_stat_bin1_ 