cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para_new/obs/Cphiq
eval `scramv1 runtime -sh`
logsave  obs_Cphiq_Total.log combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/obs/higgsCombineCphiq.MultiDimFit.mH120.root -M MultiDimFit --setPhysicsModelParameterRanges r=-4.000000,2.000000   --algo grid --points 50   -n Total --snapshotName MultiDimFit  