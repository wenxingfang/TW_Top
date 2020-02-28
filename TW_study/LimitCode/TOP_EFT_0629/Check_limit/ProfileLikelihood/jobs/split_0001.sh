cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_limit/ProfileLikelihood/out_info/
eval `scramv1 runtime -sh`
combine -M ProfileLikelihood /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901/combined_Ctg_1.00.root -t 100 --setPhysicsModelParameterRanges r=-1,1 >  /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_limit/ProfileLikelihood/out_info/exp_combined_Ctg_1.00.log
echo "AllCompleted"
