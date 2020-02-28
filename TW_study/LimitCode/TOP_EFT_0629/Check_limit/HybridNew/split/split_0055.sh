cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_limit/HybridNew/output/
eval `scramv1 runtime -sh`
combine -M HybridNew --frequentist --testStat LHC /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_20180625/combined_FCNC_0.10.root -H ProfileLikelihood --saveHybridResult --singlePoint 0.48 --saveToys -s -1 --clsAcc 0  -n obs_combined_Ccg_r_0.48 
echo "AllCompleted"
