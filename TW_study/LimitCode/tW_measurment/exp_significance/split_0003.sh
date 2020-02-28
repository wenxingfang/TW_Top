cd /user/wenxing/Limits/CMSSW_7_4_7/src
eval `scramv1 runtime -sh`
combine -M ProfileLikelihood --significance /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_1jet_1bjet.txt       -t 100 --expectSignal=1 > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/exp_sig_output/ttbar_DY_emu_1j1t.txt
echo "AllCompleted"
