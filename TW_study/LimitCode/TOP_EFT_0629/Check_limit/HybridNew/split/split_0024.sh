cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_limit/HybridNew/output/
eval `scramv1 runtime -sh`
combine -M HybridNew --frequentist --testStat LHC /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901/combined_Ctw_1.00.root -H ProfileLikelihood --saveHybridResult --singlePoint 6.65 --saveToys -s -1 --clsAcc 0  -n obs_combined_Ctw_r_6.65 
echo "AllCompleted"
