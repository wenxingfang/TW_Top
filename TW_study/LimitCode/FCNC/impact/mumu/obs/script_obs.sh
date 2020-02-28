combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tug_1013/mumu_FCNC_0.10.root -m 125 --robustFit 1 --doInitialFit 
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tug_1013/mumu_FCNC_0.10.root -m 125 --robustFit 1 --doFits 
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tug_1013/mumu_FCNC_0.10.root -m 125  -o impacts_obs_Cug.json
plotImpacts.py -i impacts_obs_Cug.json -o impacts_mumu_obs_Cug
echo "Cug obs done!"
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_1013/mumu_FCNC_0.10.root -m 125 --robustFit 1 --doInitialFit 
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_1013/mumu_FCNC_0.10.root -m 125 --robustFit 1 --doFits 
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_1013/mumu_FCNC_0.10.root -m 125  -o impacts_obs_Ccg.json
plotImpacts.py -i impacts_obs_Ccg.json -o impacts_mumu_obs_Ccg
echo "Ccg obs done!"
