cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/print_uncertinties/split_job
eval `scramv1 runtime -sh`
combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/print_uncertinties/workspace/higgsCombineTest.MultiDimFit.mH120.root -M MaxLikelihoodFit --rMax 2  --robustFit=1  --minimizerTolerance=0.001 --snapshotName MultiDimFit --freezeNuisances TT_PDF_ > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/print_uncertinties/output/TT_PDF.txt
echo "AllCompleted"
