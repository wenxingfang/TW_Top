cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para_new/exp/Ctw
eval `scramv1 runtime -sh`
logsave  exp_Ctw_Total.log combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/exp/higgsCombineCtw.MultiDimFit.mH120.root -M MultiDimFit --setPhysicsModelParameterRanges r=-2.000000,7.000000   --algo grid --points 50 -t -1 --expectSignal=0 -n Total --snapshotName MultiDimFit  