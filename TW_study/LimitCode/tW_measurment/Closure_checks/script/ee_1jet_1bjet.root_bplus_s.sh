
cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/output/ee_1jet_1bjet.root//bplus_s
eval `scramv1 runtime -sh`
combine -M MaxLikelihoodFit -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/ee_1jet_1bjet.root -t -1 --expectSignal 1
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n ee_1jet_1bjet_bplus_s_sorted > ee_1jet_1bjet_bplus_s

python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n TT_normalisation --poi TT_normalisation 
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n ISR_ --poi ISR_ 
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n JetEnergyScale_ --poi JetEnergyScale_ 
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n ElectronIDIsoScaleFactor_ --poi ElectronIDIsoScaleFactor_ 
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n Luminosity --poi Luminosity 