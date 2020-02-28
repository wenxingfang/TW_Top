cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/GOD/output/
eval `scramv1 runtime -sh`
combine -M GoodnessOfFit /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tug_1013/ee_FCNC_0.10.root --algo=saturated -t 100 > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/GOD/output/exp_ee_Cug.txt
echo "Completed"
echo "AllCompleted"
