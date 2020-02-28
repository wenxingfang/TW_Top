cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/print_uncertinties/split_job
eval `scramv1 runtime -sh`
combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/print_uncertinties/workspace/higgsCombineTest.MultiDimFit.mH120.root -M MaxLikelihoodFit --rMax 2  --robustFit=1  --minimizerTolerance=0.001 --snapshotName MultiDimFit --freezeNuisances is1jet_0bjet_DY_normalisation_Norm,is1jet_1bjet_DY_normalisation_Norm,is2jet_1bjet_DY_normalisation_Norm,is2jet_2bjet_DY_normalisation_Norm > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/print_uncertinties/output/DY_normalisation.txt
echo "AllCompleted"
