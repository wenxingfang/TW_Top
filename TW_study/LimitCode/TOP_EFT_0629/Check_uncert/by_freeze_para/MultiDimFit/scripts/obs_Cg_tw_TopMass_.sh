cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para/MultiDimFit/obs/Cg
eval `scramv1 runtime -sh`
logsave  obs_Cg_tw_TopMass_.log combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/obs/higgsCombineCg.MultiDimFit.mH120.root -M MultiDimFit --setPhysicsModelParameterRanges r=-1.000000,1.000000  --robustFit=1   --minimizerTolerance=0.0001 --snapshotName MultiDimFit --freezeNuisances tw_TopMass_ 