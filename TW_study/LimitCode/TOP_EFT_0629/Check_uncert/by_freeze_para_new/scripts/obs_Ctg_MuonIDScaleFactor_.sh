cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para_new/obs/Ctg
eval `scramv1 runtime -sh`
logsave  obs_Ctg_MuonIDScaleFactor_.log combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/obs/higgsCombineCtg.MultiDimFit.mH120.root -M MultiDimFit --setPhysicsModelParameterRanges r=-0.500000,0.500000   --algo grid --points 50   -n MuonIDScaleFactor_ --snapshotName MultiDimFit --freezeNuisances TT_TopMass_,tw_DS_,DY_QCD_,MuonIDScaleFactor_ 