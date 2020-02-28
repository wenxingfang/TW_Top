combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/emu_Cphiq_1.00.root -m 125 --robustFit 1 --doInitialFit -t -1 --expectSignal=0
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/emu_Cphiq_1.00.root -m 125 --robustFit 1 --doFits -t -1 --expectSignal=0
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/emu_Cphiq_1.00.root -m 125 -t -1 --expectSignal=0 -o impacts_exp_Cphiq.json
plotImpacts.py -i impacts_exp_Cphiq.json -o impacts_emu_exp_Cphiq
echo "Cphiq done!"
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/emu_Ctw_1.00.root -m 125 --robustFit 1 --doInitialFit -t -1 --expectSignal=0
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/emu_Ctw_1.00.root -m 125 --robustFit 1 --doFits -t -1 --expectSignal=0
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/emu_Ctw_1.00.root -m 125 -t -1 --expectSignal=0 -o impacts_exp_Ctw.json
plotImpacts.py -i impacts_exp_Ctw.json -o impacts_emu_exp_Ctw
echo "Ctw done!"
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/emu_Ctg_1.00.root -m 125 --robustFit 1 --doInitialFit -t -1 --expectSignal=0
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/emu_Ctg_1.00.root -m 125 --robustFit 1 --doFits -t -1 --expectSignal=0
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_1231_search/emu_Ctg_1.00.root -m 125 -t -1 --expectSignal=0 -o impacts_exp_Ctg.json
plotImpacts.py -i impacts_exp_Ctg.json -o impacts_emu_exp_Ctg
echo "Ctg done!"
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_Cg_1013_search/emu_Cg_1.00.root -m 125 --robustFit 1 --doInitialFit -t -1 --expectSignal=0
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_Cg_1013_search/emu_Cg_1.00.root -m 125 --robustFit 1 --doFits -t -1 --expectSignal=0
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_Cg_1013_search/emu_Cg_1.00.root -m 125 -t -1 --expectSignal=0 -o impacts_exp_Cg.json
plotImpacts.py -i impacts_exp_Cg.json -o impacts_emu_exp_Cg
echo "Cg done!"
