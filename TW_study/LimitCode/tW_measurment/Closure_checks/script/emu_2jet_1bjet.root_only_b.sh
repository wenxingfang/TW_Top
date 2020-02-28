
cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/output/emu_2jet_1bjet.root//only_b
eval `scramv1 runtime -sh`
combine -M MaxLikelihoodFit -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_2jet_1bjet.root -t -1 --expectSignal 0
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n emu_2jet_1bjet_only_b_sorted > emu_2jet_1bjet_only_b

python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n ISR_ --poi ISR_ 
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n tw_DS_ --poi tw_DS_ 
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n JetEnergyResolution_ --poi JetEnergyResolution_ 
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n TT_Tune_ --poi TT_Tune_ 
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n JetEnergyScale_ --poi JetEnergyScale_ 