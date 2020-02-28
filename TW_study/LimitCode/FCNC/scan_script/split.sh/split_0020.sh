cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/scan_script/output/
eval `scramv1 runtime -sh`
combine -M MultiDimFit /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_20180418/combined_FCNC_0.10.root       -m 125.7 -n obs_combined_Ccg        --algo=grid --points=80    --setPhysicsModelParameterRanges r=-2,2
echo "AllCompleted"
echo "AllCompleted"
