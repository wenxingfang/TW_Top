combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tug_1013/emu_FCNC_0.10.root -m 125 --robustFit 1 --doInitialFit -t -1 --expectSignal=0
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tug_1013/emu_FCNC_0.10.root -m 125 --robustFit 1 --doFits -t -1 --expectSignal=0
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tug_1013/emu_FCNC_0.10.root -m 125 -t -1 --expectSignal=0 -o impacts_exp_Cug.json
plotImpacts.py -i impacts_exp_Cug.json -o impacts_emu_exp_Cug
echo "Cug done!"
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_1013/emu_FCNC_0.10.root -m 125 --robustFit 1 --doInitialFit -t -1 --expectSignal=0
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_1013/emu_FCNC_0.10.root -m 125 --robustFit 1 --doFits -t -1 --expectSignal=0
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_1013/emu_FCNC_0.10.root -m 125 -t -1 --expectSignal=0 -o impacts_exp_Ccg.json
plotImpacts.py -i impacts_exp_Ccg.json -o impacts_emu_exp_Ccg
echo "Ccg done!"
