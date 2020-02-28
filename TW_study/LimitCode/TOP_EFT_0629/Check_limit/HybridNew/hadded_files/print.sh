echo 'exp_combined_Cg:'
combine -M HybridNew --frequentist --testStat LHC /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901_Cg/combined_Cg_1.00.root   --grid exp_combined_Cg.root    --expectedFromGrid 0.5
echo 'obs_combined_Cg:'
combine -M HybridNew --frequentist --testStat LHC /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901_Cg/combined_Cg_1.00.root   --grid obs_combined_Cg.root    
echo 'exp_combined_Cphiq:'
combine -M HybridNew --frequentist --testStat LHC /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901/combined_Cphiq_1.00.root   --grid exp_combined_Cphiq.root --expectedFromGrid 0.5
echo 'obs_combined_Cphiq:'
combine -M HybridNew --frequentist --testStat LHC /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901/combined_Cphiq_1.00.root   --grid obs_combined_Cphiq.root 
echo 'exp_combined_Ctw:'
combine -M HybridNew --frequentist --testStat LHC /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901/combined_Ctw_1.00.root     --grid exp_combined_Ctw.root   --expectedFromGrid 0.5
echo 'obs_combined_Ctw:'
combine -M HybridNew --frequentist --testStat LHC /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901/combined_Ctw_1.00.root     --grid obs_combined_Ctw.root   
echo 'exp_combined_Ctg:'
combine -M HybridNew --frequentist --testStat LHC /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901/combined_Ctg_1.00.root     --grid exp_combined_Ctg.root   --expectedFromGrid 0.5
echo 'obs_combined_Ctg:'
combine -M HybridNew --frequentist --testStat LHC /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901/combined_Ctg_1.00.root     --grid obs_combined_Ctg.root   
echo 'exp_combined_Cug:'
combine -M HybridNew --frequentist --testStat LHC /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tug_20180625/combined_FCNC_0.10.root --grid exp_combined_Cug.root   --expectedFromGrid 0.5
echo 'obs_combined_Cug:'
combine -M HybridNew --frequentist --testStat LHC /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tug_20180625/combined_FCNC_0.10.root --grid obs_combined_Cug.root   
echo 'exp_combined_Ccg:'
combine -M HybridNew --frequentist --testStat LHC /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_20180625/combined_FCNC_0.10.root --grid exp_combined_Ccg.root   --expectedFromGrid 0.5
echo 'obs_combined_Ccg:'
combine -M HybridNew --frequentist --testStat LHC /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_20180625/combined_FCNC_0.10.root --grid obs_combined_Ccg.root   
