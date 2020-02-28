cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para/MultiDimFit/obs/Ccg
eval `scramv1 runtime -sh`
logsave  obs_Ccg_MC_stat.log combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/obs/higgsCombineCcg.MultiDimFit.mH120.root -M MultiDimFit --setPhysicsModelParameterRanges r=-2.000000,2.000000  --robustFit=1   --minimizerTolerance=0.0001 --snapshotName MultiDimFit --freezeNuisances ee_xjet_1bjet_DY_stat_bin10_,ee_xjet_1bjet_DY_stat_bin1_,ee_xjet_1bjet_DY_stat_bin2_,ee_xjet_1bjet_DY_stat_bin3_,ee_xjet_1bjet_DY_stat_bin4_,ee_xjet_1bjet_DY_stat_bin5_,ee_xjet_1bjet_DY_stat_bin6_,ee_xjet_1bjet_DY_stat_bin7_,ee_xjet_1bjet_DY_stat_bin8_,ee_xjet_1bjet_DY_stat_bin9_,ee_xjet_1bjet_FCNCSignal_stat_bin10_,ee_xjet_1bjet_FCNCSignal_stat_bin1_,ee_xjet_1bjet_FCNCSignal_stat_bin2_,ee_xjet_1bjet_FCNCSignal_stat_bin3_,ee_xjet_1bjet_FCNCSignal_stat_bin4_,ee_xjet_1bjet_FCNCSignal_stat_bin5_,ee_xjet_1bjet_FCNCSignal_stat_bin6_,ee_xjet_1bjet_FCNCSignal_stat_bin7_,ee_xjet_1bjet_FCNCSignal_stat_bin8_,ee_xjet_1bjet_FCNCSignal_stat_bin9_,ee_xjet_1bjet_TT_stat_bin10_,ee_xjet_1bjet_TT_stat_bin1_,ee_xjet_1bjet_TT_stat_bin2_,ee_xjet_1bjet_TT_stat_bin3_,ee_xjet_1bjet_TT_stat_bin4_,ee_xjet_1bjet_TT_stat_bin5_,ee_xjet_1bjet_TT_stat_bin6_,ee_xjet_1bjet_TT_stat_bin7_,ee_xjet_1bjet_TT_stat_bin8_,ee_xjet_1bjet_TT_stat_bin9_,ee_xjet_1bjet_TW_stat_bin10_,ee_xjet_1bjet_TW_stat_bin1_,ee_xjet_1bjet_TW_stat_bin2_,ee_xjet_1bjet_TW_stat_bin3_,ee_xjet_1bjet_TW_stat_bin4_,ee_xjet_1bjet_TW_stat_bin5_,ee_xjet_1bjet_TW_stat_bin6_,ee_xjet_1bjet_TW_stat_bin7_,ee_xjet_1bjet_TW_stat_bin8_,ee_xjet_1bjet_TW_stat_bin9_,ee_xjet_1bjet_other_stat_bin10_,ee_xjet_1bjet_other_stat_bin1_,ee_xjet_1bjet_other_stat_bin2_,ee_xjet_1bjet_other_stat_bin3_,ee_xjet_1bjet_other_stat_bin4_,ee_xjet_1bjet_other_stat_bin5_,ee_xjet_1bjet_other_stat_bin6_,ee_xjet_1bjet_other_stat_bin7_,ee_xjet_1bjet_other_stat_bin8_,ee_xjet_1bjet_other_stat_bin9_,emu_xjet_1bjet_DY_stat_bin10_,emu_xjet_1bjet_DY_stat_bin1_,emu_xjet_1bjet_DY_stat_bin2_,emu_xjet_1bjet_DY_stat_bin3_,emu_xjet_1bjet_DY_stat_bin4_,emu_xjet_1bjet_DY_stat_bin5_,emu_xjet_1bjet_DY_stat_bin6_,emu_xjet_1bjet_DY_stat_bin7_,emu_xjet_1bjet_DY_stat_bin8_,emu_xjet_1bjet_DY_stat_bin9_,emu_xjet_1bjet_FCNCSignal_stat_bin10_,emu_xjet_1bjet_FCNCSignal_stat_bin1_,emu_xjet_1bjet_FCNCSignal_stat_bin2_,emu_xjet_1bjet_FCNCSignal_stat_bin3_,emu_xjet_1bjet_FCNCSignal_stat_bin4_,emu_xjet_1bjet_FCNCSignal_stat_bin5_,emu_xjet_1bjet_FCNCSignal_stat_bin6_,emu_xjet_1bjet_FCNCSignal_stat_bin7_,emu_xjet_1bjet_FCNCSignal_stat_bin8_,emu_xjet_1bjet_FCNCSignal_stat_bin9_,emu_xjet_1bjet_TT_stat_bin10_,emu_xjet_1bjet_TT_stat_bin1_,emu_xjet_1bjet_TT_stat_bin2_,emu_xjet_1bjet_TT_stat_bin3_,emu_xjet_1bjet_TT_stat_bin4_,emu_xjet_1bjet_TT_stat_bin5_,emu_xjet_1bjet_TT_stat_bin6_,emu_xjet_1bjet_TT_stat_bin7_,emu_xjet_1bjet_TT_stat_bin8_,emu_xjet_1bjet_TT_stat_bin9_,emu_xjet_1bjet_TW_stat_bin10_,emu_xjet_1bjet_TW_stat_bin1_,emu_xjet_1bjet_TW_stat_bin2_,emu_xjet_1bjet_TW_stat_bin3_,emu_xjet_1bjet_TW_stat_bin4_,emu_xjet_1bjet_TW_stat_bin5_,emu_xjet_1bjet_TW_stat_bin6_,emu_xjet_1bjet_TW_stat_bin7_,emu_xjet_1bjet_TW_stat_bin8_,emu_xjet_1bjet_TW_stat_bin9_,emu_xjet_1bjet_other_stat_bin10_,emu_xjet_1bjet_other_stat_bin1_,emu_xjet_1bjet_other_stat_bin2_,emu_xjet_1bjet_other_stat_bin3_,emu_xjet_1bjet_other_stat_bin4_,emu_xjet_1bjet_other_stat_bin5_,emu_xjet_1bjet_other_stat_bin6_,emu_xjet_1bjet_other_stat_bin7_,emu_xjet_1bjet_other_stat_bin8_,emu_xjet_1bjet_other_stat_bin9_,mumu_xjet_1bjet_DY_stat_bin10_,mumu_xjet_1bjet_DY_stat_bin1_,mumu_xjet_1bjet_DY_stat_bin2_,mumu_xjet_1bjet_DY_stat_bin3_,mumu_xjet_1bjet_DY_stat_bin4_,mumu_xjet_1bjet_DY_stat_bin5_,mumu_xjet_1bjet_DY_stat_bin6_,mumu_xjet_1bjet_DY_stat_bin7_,mumu_xjet_1bjet_DY_stat_bin8_,mumu_xjet_1bjet_DY_stat_bin9_,mumu_xjet_1bjet_FCNCSignal_stat_bin10_,mumu_xjet_1bjet_FCNCSignal_stat_bin1_,mumu_xjet_1bjet_FCNCSignal_stat_bin2_,mumu_xjet_1bjet_FCNCSignal_stat_bin3_,mumu_xjet_1bjet_FCNCSignal_stat_bin4_,mumu_xjet_1bjet_FCNCSignal_stat_bin5_,mumu_xjet_1bjet_FCNCSignal_stat_bin6_,mumu_xjet_1bjet_FCNCSignal_stat_bin7_,mumu_xjet_1bjet_FCNCSignal_stat_bin8_,mumu_xjet_1bjet_FCNCSignal_stat_bin9_,mumu_xjet_1bjet_TT_stat_bin10_,mumu_xjet_1bjet_TT_stat_bin1_,mumu_xjet_1bjet_TT_stat_bin2_,mumu_xjet_1bjet_TT_stat_bin3_,mumu_xjet_1bjet_TT_stat_bin4_,mumu_xjet_1bjet_TT_stat_bin5_,mumu_xjet_1bjet_TT_stat_bin6_,mumu_xjet_1bjet_TT_stat_bin7_,mumu_xjet_1bjet_TT_stat_bin8_,mumu_xjet_1bjet_TT_stat_bin9_,mumu_xjet_1bjet_TW_stat_bin10_,mumu_xjet_1bjet_TW_stat_bin1_,mumu_xjet_1bjet_TW_stat_bin2_,mumu_xjet_1bjet_TW_stat_bin3_,mumu_xjet_1bjet_TW_stat_bin4_,mumu_xjet_1bjet_TW_stat_bin5_,mumu_xjet_1bjet_TW_stat_bin6_,mumu_xjet_1bjet_TW_stat_bin7_,mumu_xjet_1bjet_TW_stat_bin8_,mumu_xjet_1bjet_TW_stat_bin9_,mumu_xjet_1bjet_other_stat_bin10_,mumu_xjet_1bjet_other_stat_bin1_,mumu_xjet_1bjet_other_stat_bin2_,mumu_xjet_1bjet_other_stat_bin3_,mumu_xjet_1bjet_other_stat_bin4_,mumu_xjet_1bjet_other_stat_bin5_,mumu_xjet_1bjet_other_stat_bin6_,mumu_xjet_1bjet_other_stat_bin7_,mumu_xjet_1bjet_other_stat_bin8_,mumu_xjet_1bjet_other_stat_bin9_ 