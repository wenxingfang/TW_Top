
cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/impact/output/emu_11_21_22_card.root//exp
eval `scramv1 runtime -sh`
logsave -a log.txt combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_11_21_22_card.root -m 125 --rMax 3 --robustFit 1 --minimizerTolerance=0.001 --doInitialFit             -t -1 --expectSignal=1 
logsave -a log.txt combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_11_21_22_card.root -m 125 --rMax 3 --robustFit 1 --minimizerTolerance=0.01  --doFits     --parallel 8  -t -1 --expectSignal=1 
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_11_21_22_card.root -m 125  -o impacts.json             -t -1 --expectSignal=1
plotImpacts.py -i impacts.json -o impacts_emu_11_21_22_card_exp
