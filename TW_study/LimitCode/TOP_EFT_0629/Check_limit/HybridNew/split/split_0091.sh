cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_limit/HybridNew/output/
eval `scramv1 runtime -sh`
combine -M HybridNew --frequentist --testStat LHC /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901/combined_Ctg_1.00.root -H ProfileLikelihood --saveHybridResult --singlePoint 0.19 --saveToys -s -1 --clsAcc 0  -n exp_combined_Ctg_r_0.19 --expectedFromGrid 0.5
echo "AllCompleted"
