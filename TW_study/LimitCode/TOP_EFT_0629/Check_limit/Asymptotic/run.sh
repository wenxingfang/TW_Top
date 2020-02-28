echo 'combined_Cg:'
combine -M Asymptotic /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901_Cg/combined_Cg_1.00.root --setPhysicsModelParameterRanges r=-10,10 --qtilde 0
echo 'combined_Cphiq:'
combine -M Asymptotic /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901/combined_Cphiq_1.00.root --setPhysicsModelParameterRanges r=-10,10 --qtilde 0
echo 'combined_Ctw:'
combine -M Asymptotic /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901/combined_Ctw_1.00.root --setPhysicsModelParameterRanges r=-10,10 --qtilde 0
echo 'combined_Ctg:'
combine -M Asymptotic /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901/combined_Ctg_1.00.root --setPhysicsModelParameterRanges r=-1,1 --qtilde 0
echo 'combined_Cug:'
combine -M Asymptotic /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tug_20180625/combined_FCNC_0.10.root --setPhysicsModelParameterRanges r=-2,2 --qtilde 0
echo 'combined_Ccg:'
combine -M Asymptotic /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_20180625/combined_FCNC_0.10.root --setPhysicsModelParameterRanges r=-2,2 --qtilde 0
