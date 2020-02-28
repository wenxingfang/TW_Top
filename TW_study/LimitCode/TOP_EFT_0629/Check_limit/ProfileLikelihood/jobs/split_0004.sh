cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_limit/ProfileLikelihood/out_info/
eval `scramv1 runtime -sh`
combine -M ProfileLikelihood /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tug_20180625/combined_FCNC_0.10.root -t 100 --setPhysicsModelParameterRanges r=-2,2 >  /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_limit/ProfileLikelihood/out_info/exp_combined_Cug_0.10.log
echo "AllCompleted"
