cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/GOD/make_script/
eval `scramv1 runtime -sh`
combine -M GoodnessOfFit /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/ee_Ctw_1.00.root --algo=saturated        > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/GOD/output/obs_ee_Ctw.txt
echo "Completed"
echo "AllCompleted"
