cd /user/wenxing/Limits/CMSSW_7_4_7/src/
eval `scramv1 runtime -sh`
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tcg_NoTopPtReW/ee_FCNC_0.10.txt -o /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_20190608_NoTopPtReW/ee_FCNC_0.10.root -P TOP_EFT_Models_search:Model_FCNC 
echo "done!"