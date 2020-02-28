cd /user/wenxing/Limits/CMSSW_7_4_7/src
eval `scramv1 runtime -sh`
combine -M ProfileLikelihood --significance /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/ee_emu_mumu_card.txt     -t 100 --expectSignal=1 > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/exp_sig_output/ttbar_DY_combined.txt
echo "AllCompleted"
