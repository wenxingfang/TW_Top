cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/GOD/output/
eval `scramv1 runtime -sh`
combine -M GoodnessOfFit /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_1013/emu_FCNC_0.10.root --algo=saturated        > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/GOD/output/obs_emu_Ccg.txt
echo "Completed"
echo "AllCompleted"
