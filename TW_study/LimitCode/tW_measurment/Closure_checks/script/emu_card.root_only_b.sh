
cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/output/emu_card.root//only_b
eval `scramv1 runtime -sh`
combine -M MaxLikelihoodFit -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_card.root -t -1 --expectSignal 0
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n emu_card_only_b_sorted > emu_card_only_b

python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n FSR_ --poi FSR_ 
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n BtagScaleFactor_bc_ --poi BtagScaleFactor_bc_ 
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n JetEnergyResolution_ --poi JetEnergyResolution_ 
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n is1jet_1bjet_DY_normalisation_Norm --poi is1jet_1bjet_DY_normalisation_Norm 
python ~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py -a mlfit.root -g plots.root -n tw_MEscale_ --poi tw_MEscale_ 