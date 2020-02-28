cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/Impact/obs/Ctg
eval `scramv1 runtime -sh`
logsave -a log.txt combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/higgsCombineCtg.MultiDimFit.mH120.root -m 125 --setPhysicsModelParameterRanges r=-0.5,0.5 --robustFit 1 --minimizerTolerance=0.001 --doInitialFit  
logsave -a log.txt combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/higgsCombineCtg.MultiDimFit.mH120.root -m 125 --setPhysicsModelParameterRanges r=-0.5,0.5 --robustFit 1 --minimizerTolerance=0.01  --doFits   
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/higgsCombineCtg.MultiDimFit.mH120.root -m 125 -o impacts.json  
plotImpacts.py -i impacts.json -o impacts_obs_Ctg
