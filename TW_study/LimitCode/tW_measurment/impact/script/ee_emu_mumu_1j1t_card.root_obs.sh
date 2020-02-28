
cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/impact/output/ee_emu_mumu_1j1t_card.root//obs
eval `scramv1 runtime -sh`
logsave -a log.txt combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/ee_emu_mumu_1j1t_card.root -m 125 --rMax 3 --robustFit 1 --minimizerTolerance=0.001 --doInitialFit
logsave -a log.txt combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/ee_emu_mumu_1j1t_card.root -m 125 --rMax 3 --robustFit 1 --minimizerTolerance=0.01  --doFits     --parallel 8 
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/ee_emu_mumu_1j1t_card.root -m 125  -o impacts.json
plotImpacts.py -i impacts.json -o impacts_ee_emu_mumu_1j1t_card_obs
