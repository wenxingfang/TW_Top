cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para/MultiDimFit/obs/Ccg
eval `scramv1 runtime -sh`
logsave  obs_Ccg_TT_CR_.log combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/obs/higgsCombineCcg.MultiDimFit.mH120.root -M MultiDimFit --setPhysicsModelParameterRanges r=-2.000000,2.000000  --robustFit=1   --minimizerTolerance=0.0001 --snapshotName MultiDimFit --freezeNuisances TT_CR_ 