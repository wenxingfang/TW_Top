cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_tcg_NoTopPtReW/
combineCards.py  Name1=ee_xjet_1bjet_FCNC_0.10.txt > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tcg_NoTopPtReW/ee_FCNC_0.10.txt
combineCards.py  Name1=emu_xjet_1bjet_FCNC_0.10.txt > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tcg_NoTopPtReW/emu_FCNC_0.10.txt
combineCards.py  Name1=mumu_xjet_1bjet_FCNC_0.10.txt > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tcg_NoTopPtReW/mumu_FCNC_0.10.txt
combineCards.py  Name1=ee_xjet_1bjet_FCNC_0.10.txt Name2=emu_xjet_1bjet_FCNC_0.10.txt Name3=mumu_xjet_1bjet_FCNC_0.10.txt > /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tcg_NoTopPtReW/combined_FCNC_0.10.txt
echo 'done!'
