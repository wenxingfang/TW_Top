cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/split_job
eval `scramv1 runtime -sh`
combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/higgsCombineCtw.MultiDimFit.mH120.root -M MaxLikelihoodFit --setPhysicsModelParameterRanges r=0.000000,6.000000  --robustFit=1  --minimizerTolerance=0.0001 --snapshotName MultiDimFit --freezeNuisances FSR_ > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/output/Ctw_FSR.txt
echo "AllCompleted"
