cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para_new/obs/Cphiq
eval `scramv1 runtime -sh`
logsave  obs_Cphiq_MuonIDScaleFactor_.log combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/obs/higgsCombineCphiq.MultiDimFit.mH120.root -M MultiDimFit --setPhysicsModelParameterRanges r=-4.000000,2.000000   --algo grid --points 50   -n MuonIDScaleFactor_ --snapshotName MultiDimFit --freezeNuisances TT_TopMass_,tw_DS_,DY_QCD_,MuonIDScaleFactor_ 