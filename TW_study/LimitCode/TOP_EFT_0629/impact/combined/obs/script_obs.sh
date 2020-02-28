combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_Cg_1013_search/combined_Cg_1.00.root -m 125 --robustFit 1 --doInitialFit 
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_Cg_1013_search/combined_Cg_1.00.root -m 125 --robustFit 1 --doFits 
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_Cg_1013_search/combined_Cg_1.00.root -m 125  -o impacts_obs_Cg.json
plotImpacts.py -i impacts_obs_Cg.json -o impacts_combined_obs_Cg
echo "Cg obs done!"
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/combined_Cphiq_1.00.root -m 125 --robustFit 1 --doInitialFit 
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/combined_Cphiq_1.00.root -m 125 --robustFit 1 --doFits 
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/combined_Cphiq_1.00.root -m 125  -o impacts_obs_Cphiq.json
plotImpacts.py -i impacts_obs_Cphiq.json -o impacts_combined_obs_Cphiq
echo "Cphiq obs done!"
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/combined_Ctw_1.00.root -m 125 --robustFit 1 --doInitialFit 
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/combined_Ctw_1.00.root -m 125 --robustFit 1 --doFits 
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/combined_Ctw_1.00.root -m 125  -o impacts_obs_Ctw.json
plotImpacts.py -i impacts_obs_Ctw.json -o impacts_combined_obs_Ctw
echo "Ctw obs done!"
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/combined_Ctg_1.00.root -m 125 --robustFit 1 --doInitialFit 
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/combined_Ctg_1.00.root -m 125 --robustFit 1 --doFits 
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/combined_Ctg_1.00.root -m 125  -o impacts_obs_Ctg.json
plotImpacts.py -i impacts_obs_Ctg.json -o impacts_combined_obs_Ctg
echo "Ctg obs done!"
