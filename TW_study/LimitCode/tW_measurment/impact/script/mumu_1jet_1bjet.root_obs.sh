
cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/impact/output/mumu_1jet_1bjet.root//obs
eval `scramv1 runtime -sh`
logsave -a log.txt combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/mumu_1jet_1bjet.root -m 125 --rMax 3 --robustFit 1 --minimizerTolerance=0.001 --doInitialFit
logsave -a log.txt combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/mumu_1jet_1bjet.root -m 125 --rMax 3 --robustFit 1 --minimizerTolerance=0.01  --doFits     --parallel 8 
combineTool.py -M Impacts -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/mumu_1jet_1bjet.root -m 125  -o impacts.json
plotImpacts.py -i impacts.json -o impacts_mumu_1jet_1bjet_obs
