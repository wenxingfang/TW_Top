cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/split_job
eval `scramv1 runtime -sh`
combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/higgsCombineCtg.MultiDimFit.mH120.root -M MaxLikelihoodFit --setPhysicsModelParameterRanges r=-0.400000,0.100000  --robustFit=1  --minimizerTolerance=0.0001 --snapshotName MultiDimFit --freezeNuisances is1jet_0bjet_DY_normalisation_Norm,is1jet_1bjet_DY_normalisation_Norm,is2jet_1bjet_DY_normalisation_Norm,is2jet_2bjet_DY_normalisation_Norm > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/output/Ctg_DY_normalisation.txt
echo "AllCompleted"
