cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/split_job
eval `scramv1 runtime -sh`
combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/higgsCombineCphiq.MultiDimFit.mH120.root -M MaxLikelihoodFit --setPhysicsModelParameterRanges r=-3.000000,0.000000  --robustFit=1  --minimizerTolerance=0.0001 --snapshotName MultiDimFit --freezeNuisances ee_1jet_1bjet_DY_stat_bin1_,ee_1jet_1bjet_DY_stat_bin2_,ee_1jet_1bjet_DY_stat_bin3_,ee_1jet_1bjet_DY_stat_bin4_,ee_1jet_1bjet_DY_stat_bin5_,ee_1jet_1bjet_DY_stat_bin6_,ee_1jet_1bjet_DY_stat_bin7_,ee_1jet_1bjet_TT_stat_bin1_,ee_1jet_1bjet_TT_stat_bin2_,ee_1jet_1bjet_TT_stat_bin3_,ee_1jet_1bjet_TT_stat_bin4_,ee_1jet_1bjet_TT_stat_bin5_,ee_1jet_1bjet_TT_stat_bin6_,ee_1jet_1bjet_TT_stat_bin7_,ee_1jet_1bjet_TW_stat_bin1_,ee_1jet_1bjet_TW_stat_bin2_,ee_1jet_1bjet_TW_stat_bin3_,ee_1jet_1bjet_TW_stat_bin4_,ee_1jet_1bjet_TW_stat_bin5_,ee_1jet_1bjet_TW_stat_bin6_,ee_1jet_1bjet_TW_stat_bin7_,ee_1jet_1bjet_other_stat_bin1_,ee_1jet_1bjet_other_stat_bin2_,ee_1jet_1bjet_other_stat_bin3_,ee_1jet_1bjet_other_stat_bin4_,ee_1jet_1bjet_other_stat_bin5_,ee_1jet_1bjet_other_stat_bin6_,ee_1jet_1bjet_other_stat_bin7_,ee_2jet_1bjet_DY_stat_bin1_,ee_2jet_1bjet_DY_stat_bin2_,ee_2jet_1bjet_DY_stat_bin3_,ee_2jet_1bjet_DY_stat_bin4_,ee_2jet_1bjet_DY_stat_bin5_,ee_2jet_1bjet_DY_stat_bin6_,ee_2jet_1bjet_TT_stat_bin1_,ee_2jet_1bjet_TT_stat_bin2_,ee_2jet_1bjet_TT_stat_bin3_,ee_2jet_1bjet_TT_stat_bin4_,ee_2jet_1bjet_TT_stat_bin5_,ee_2jet_1bjet_TT_stat_bin6_,ee_2jet_1bjet_TW_stat_bin1_,ee_2jet_1bjet_TW_stat_bin2_,ee_2jet_1bjet_TW_stat_bin3_,ee_2jet_1bjet_TW_stat_bin4_,ee_2jet_1bjet_TW_stat_bin5_,ee_2jet_1bjet_TW_stat_bin6_,ee_2jet_1bjet_other_stat_bin1_,ee_2jet_1bjet_other_stat_bin2_,ee_2jet_1bjet_other_stat_bin3_,ee_2jet_1bjet_other_stat_bin4_,ee_2jet_1bjet_other_stat_bin5_,ee_2jet_1bjet_other_stat_bin6_,ee_2jet_2bjet_DY_stat_bin1_,ee_2jet_2bjet_TT_stat_bin1_,ee_2jet_2bjet_TW_stat_bin1_,ee_2jet_2bjet_other_stat_bin1_,emu_1jet_0bjet_DY_stat_bin1_,emu_1jet_0bjet_DY_stat_bin2_,emu_1jet_0bjet_DY_stat_bin3_,emu_1jet_0bjet_DY_stat_bin4_,emu_1jet_0bjet_DY_stat_bin5_,emu_1jet_0bjet_TT_stat_bin1_,emu_1jet_0bjet_TT_stat_bin2_,emu_1jet_0bjet_TT_stat_bin3_,emu_1jet_0bjet_TT_stat_bin4_,emu_1jet_0bjet_TT_stat_bin5_,emu_1jet_0bjet_TW_stat_bin1_,emu_1jet_0bjet_TW_stat_bin2_,emu_1jet_0bjet_TW_stat_bin3_,emu_1jet_0bjet_TW_stat_bin4_,emu_1jet_0bjet_TW_stat_bin5_,emu_1jet_0bjet_other_stat_bin1_,emu_1jet_0bjet_other_stat_bin2_,emu_1jet_0bjet_other_stat_bin3_,emu_1jet_0bjet_other_stat_bin4_,emu_1jet_0bjet_other_stat_bin5_,emu_1jet_1bjet_DY_stat_bin1_,emu_1jet_1bjet_DY_stat_bin2_,emu_1jet_1bjet_DY_stat_bin3_,emu_1jet_1bjet_DY_stat_bin4_,emu_1jet_1bjet_DY_stat_bin5_,emu_1jet_1bjet_DY_stat_bin6_,emu_1jet_1bjet_DY_stat_bin7_,emu_1jet_1bjet_TT_stat_bin1_,emu_1jet_1bjet_TT_stat_bin2_,emu_1jet_1bjet_TT_stat_bin3_,emu_1jet_1bjet_TT_stat_bin4_,emu_1jet_1bjet_TT_stat_bin5_,emu_1jet_1bjet_TT_stat_bin6_,emu_1jet_1bjet_TT_stat_bin7_,emu_1jet_1bjet_TW_stat_bin1_,emu_1jet_1bjet_TW_stat_bin2_,emu_1jet_1bjet_TW_stat_bin3_,emu_1jet_1bjet_TW_stat_bin4_,emu_1jet_1bjet_TW_stat_bin5_,emu_1jet_1bjet_TW_stat_bin6_,emu_1jet_1bjet_TW_stat_bin7_,emu_1jet_1bjet_other_stat_bin1_,emu_1jet_1bjet_other_stat_bin2_,emu_1jet_1bjet_other_stat_bin3_,emu_1jet_1bjet_other_stat_bin4_,emu_1jet_1bjet_other_stat_bin5_,emu_1jet_1bjet_other_stat_bin6_,emu_1jet_1bjet_other_stat_bin7_,emu_2jet_1bjet_DY_stat_bin1_,emu_2jet_1bjet_DY_stat_bin2_,emu_2jet_1bjet_DY_stat_bin3_,emu_2jet_1bjet_DY_stat_bin4_,emu_2jet_1bjet_DY_stat_bin5_,emu_2jet_1bjet_DY_stat_bin6_,emu_2jet_1bjet_TT_stat_bin1_,emu_2jet_1bjet_TT_stat_bin2_,emu_2jet_1bjet_TT_stat_bin3_,emu_2jet_1bjet_TT_stat_bin4_,emu_2jet_1bjet_TT_stat_bin5_,emu_2jet_1bjet_TT_stat_bin6_,emu_2jet_1bjet_TW_stat_bin1_,emu_2jet_1bjet_TW_stat_bin2_,emu_2jet_1bjet_TW_stat_bin3_,emu_2jet_1bjet_TW_stat_bin4_,emu_2jet_1bjet_TW_stat_bin5_,emu_2jet_1bjet_TW_stat_bin6_,emu_2jet_1bjet_other_stat_bin1_,emu_2jet_1bjet_other_stat_bin2_,emu_2jet_1bjet_other_stat_bin3_,emu_2jet_1bjet_other_stat_bin4_,emu_2jet_1bjet_other_stat_bin5_,emu_2jet_1bjet_other_stat_bin6_,emu_2jet_2bjet_DY_stat_bin1_,emu_2jet_2bjet_TT_stat_bin1_,emu_2jet_2bjet_TW_stat_bin1_,emu_2jet_2bjet_other_stat_bin1_,mumu_1jet_1bjet_DY_stat_bin1_,mumu_1jet_1bjet_DY_stat_bin2_,mumu_1jet_1bjet_DY_stat_bin3_,mumu_1jet_1bjet_DY_stat_bin4_,mumu_1jet_1bjet_DY_stat_bin5_,mumu_1jet_1bjet_DY_stat_bin6_,mumu_1jet_1bjet_DY_stat_bin7_,mumu_1jet_1bjet_TT_stat_bin1_,mumu_1jet_1bjet_TT_stat_bin2_,mumu_1jet_1bjet_TT_stat_bin3_,mumu_1jet_1bjet_TT_stat_bin4_,mumu_1jet_1bjet_TT_stat_bin5_,mumu_1jet_1bjet_TT_stat_bin6_,mumu_1jet_1bjet_TT_stat_bin7_,mumu_1jet_1bjet_TW_stat_bin1_,mumu_1jet_1bjet_TW_stat_bin2_,mumu_1jet_1bjet_TW_stat_bin3_,mumu_1jet_1bjet_TW_stat_bin4_,mumu_1jet_1bjet_TW_stat_bin5_,mumu_1jet_1bjet_TW_stat_bin6_,mumu_1jet_1bjet_TW_stat_bin7_,mumu_1jet_1bjet_other_stat_bin1_,mumu_1jet_1bjet_other_stat_bin2_,mumu_1jet_1bjet_other_stat_bin3_,mumu_1jet_1bjet_other_stat_bin4_,mumu_1jet_1bjet_other_stat_bin5_,mumu_1jet_1bjet_other_stat_bin6_,mumu_1jet_1bjet_other_stat_bin7_,mumu_2jet_1bjet_DY_stat_bin1_,mumu_2jet_1bjet_DY_stat_bin2_,mumu_2jet_1bjet_DY_stat_bin3_,mumu_2jet_1bjet_DY_stat_bin4_,mumu_2jet_1bjet_DY_stat_bin5_,mumu_2jet_1bjet_DY_stat_bin6_,mumu_2jet_1bjet_TT_stat_bin1_,mumu_2jet_1bjet_TT_stat_bin2_,mumu_2jet_1bjet_TT_stat_bin3_,mumu_2jet_1bjet_TT_stat_bin4_,mumu_2jet_1bjet_TT_stat_bin5_,mumu_2jet_1bjet_TT_stat_bin6_,mumu_2jet_1bjet_TW_stat_bin1_,mumu_2jet_1bjet_TW_stat_bin2_,mumu_2jet_1bjet_TW_stat_bin3_,mumu_2jet_1bjet_TW_stat_bin4_,mumu_2jet_1bjet_TW_stat_bin5_,mumu_2jet_1bjet_TW_stat_bin6_,mumu_2jet_1bjet_other_stat_bin1_,mumu_2jet_1bjet_other_stat_bin2_,mumu_2jet_1bjet_other_stat_bin3_,mumu_2jet_1bjet_other_stat_bin4_,mumu_2jet_1bjet_other_stat_bin5_,mumu_2jet_1bjet_other_stat_bin6_,mumu_2jet_2bjet_DY_stat_bin1_,mumu_2jet_2bjet_TT_stat_bin1_,mumu_2jet_2bjet_TW_stat_bin1_,mumu_2jet_2bjet_other_stat_bin1_ > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/output/Cphiq_MC_stat.txt
echo "AllCompleted"
