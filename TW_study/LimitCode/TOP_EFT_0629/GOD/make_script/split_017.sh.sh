cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/GOD/make_script/
eval `scramv1 runtime -sh`
combine -M GoodnessOfFit /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/mumu_Cphiq_1.00.root --algo=saturated -t 100 > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/GOD/output/exp_mumu_Cphiq.txt
echo "Completed"
echo "AllCompleted"
