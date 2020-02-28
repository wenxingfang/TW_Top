cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/scan_script/output/
eval `scramv1 runtime -sh`
combine -M MultiDimFit /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tug_20180418_Ptll/mumu_FCNC_0.10.root      -m 125.7 -n Ptll_obs_mumu_Cug            --algo=grid --points=80    --setPhysicsModelParameterRanges r=-2,2
echo "AllCompleted"
echo "AllCompleted"
