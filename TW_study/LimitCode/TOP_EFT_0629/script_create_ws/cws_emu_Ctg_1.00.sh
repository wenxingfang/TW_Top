cd /user/wenxing/Limits/CMSSW_7_4_7/src
eval `scramv1 runtime -sh`
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/data_card_CtgTTOnly_combined/emu_Ctg_1.00.txt -o /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20190817_Ctg_TTOnly/emu_Ctg_1.00.root -P TOP_EFT_Models_search_NLO:Model_CtgTTOnly 
echo "done!"