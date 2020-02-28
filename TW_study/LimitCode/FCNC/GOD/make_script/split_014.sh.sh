cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/GOD/output/
eval `scramv1 runtime -sh`
combine -M GoodnessOfFit /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_1013/combined_FCNC_0.10.root --algo=saturated        > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/GOD/output/obs_combined_Ccg.txt
echo "Completed"
echo "AllCompleted"
