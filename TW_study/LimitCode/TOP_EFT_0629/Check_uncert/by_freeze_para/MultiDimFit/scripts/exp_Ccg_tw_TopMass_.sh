cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para/MultiDimFit/exp/Ccg
eval `scramv1 runtime -sh`
logsave  exp_Ccg_tw_TopMass_.log combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/exp/higgsCombineCcg.MultiDimFit.mH120.root -M MultiDimFit --setPhysicsModelParameterRanges r=-2.000000,2.000000  --robustFit=1 -t -1 --expectSignal=0 --minimizerTolerance=0.0001 --snapshotName MultiDimFit --freezeNuisances tw_TopMass_ 