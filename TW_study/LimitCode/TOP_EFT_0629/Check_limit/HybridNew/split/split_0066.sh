cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_limit/HybridNew/output/
eval `scramv1 runtime -sh`
combine -M HybridNew --frequentist --testStat LHC /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901_Cg/combined_Cg_1.00.root -H ProfileLikelihood --saveHybridResult --singlePoint 1.14 --saveToys -s -1 --clsAcc 0  -n exp_combined_Cg_r_1.14 --expectedFromGrid 0.5
echo "AllCompleted"
