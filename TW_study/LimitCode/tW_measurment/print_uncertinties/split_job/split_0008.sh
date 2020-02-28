cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/print_uncertinties/split_job
eval `scramv1 runtime -sh`
combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/print_uncertinties/workspace/higgsCombineTest.MultiDimFit.mH120.root -M MaxLikelihoodFit --rMax 2  --robustFit=1  --minimizerTolerance=0.001 --snapshotName MultiDimFit --freezeNuisances tw_TopMass_ > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/print_uncertinties/output/TW_mtop.txt
echo "AllCompleted"
