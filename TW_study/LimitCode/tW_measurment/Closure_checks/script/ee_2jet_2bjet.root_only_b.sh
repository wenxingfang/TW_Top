
cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/output/ee_2jet_2bjet.root//only_b
eval `scramv1 runtime -sh`
combine -M MaxLikelihoodFit -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/ee_2jet_2bjet.root -t -1 --expectSignal 0
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n ee_2jet_2bjet_only_b_sorted > ee_2jet_2bjet_only_b

python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n FSR_ --poi FSR_ 
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n TT_normalisation --poi TT_normalisation 
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n JetEnergyScale_ --poi JetEnergyScale_ 
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n ElectronIDIsoScaleFactor_ --poi ElectronIDIsoScaleFactor_ 
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n BtagScaleFactor_bc_ --poi BtagScaleFactor_bc_ 