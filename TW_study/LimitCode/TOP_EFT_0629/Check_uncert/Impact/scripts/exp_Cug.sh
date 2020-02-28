cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/Impact/exp/Cug
eval `scramv1 runtime -sh`
logsave -a log.txt combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/higgsCombineCug.MultiDimFit.mH120.root -m 125 --setPhysicsModelParameterRanges r=-2.0,2.0 --robustFit 1 --minimizerTolerance=0.001 --doInitialFit -t -1 --expectSignal=0
logsave -a log.txt combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/higgsCombineCug.MultiDimFit.mH120.root -m 125 --setPhysicsModelParameterRanges r=-2.0,2.0 --robustFit 1 --minimizerTolerance=0.01  --doFits  -t -1 --expectSignal=0
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/higgsCombineCug.MultiDimFit.mH120.root -m 125 -o impacts.json -t -1 --expectSignal=0
plotImpacts.py -i impacts.json -o impacts_exp_Cug
