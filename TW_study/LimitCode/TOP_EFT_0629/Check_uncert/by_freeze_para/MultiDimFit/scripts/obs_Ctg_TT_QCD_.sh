cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para/MultiDimFit/obs/Ctg
eval `scramv1 runtime -sh`
logsave  obs_Ctg_TT_QCD_.log combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/obs/higgsCombineCtg.MultiDimFit.mH120.root -M MultiDimFit --setPhysicsModelParameterRanges r=-0.500000,0.500000  --robustFit=1   --minimizerTolerance=0.0001 --snapshotName MultiDimFit --freezeNuisances TT_QCD_ 