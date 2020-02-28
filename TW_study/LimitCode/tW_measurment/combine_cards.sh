cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/ 
combineCards.py Name1=emu_1jet_0bjet.txt  Name2=emu_1jet_1bjet.txt  Name3=emu_2jet_1bjet.txt  Name4=emu_2jet_2bjet.txt                         > emu_card.txt
combineCards.py                           Name1=emu_1jet_1bjet.txt  Name2=emu_2jet_1bjet.txt                                                   > emu_11_21_card.txt
combineCards.py                           Name1=emu_1jet_1bjet.txt  Name2=emu_2jet_1bjet.txt  Name3=emu_2jet_2bjet.txt                         > emu_11_21_22_card.txt
combineCards.py                           Name1=ee_1jet_1bjet.txt   Name2=ee_2jet_1bjet.txt   Name3=ee_2jet_2bjet.txt                          > ee_card.txt
combineCards.py                           Name1=mumu_1jet_1bjet.txt Name2=mumu_2jet_1bjet.txt Name3=mumu_2jet_2bjet.txt                        > mumu_card.txt
combineCards.py Name1=ee_card.txt         Name2=emu_card.txt        Name3=mumu_card.txt                                                        > ee_emu_mumu_card.txt
combineCards.py Name1=ee_1jet_1bjet.txt   Name2=emu_1jet_1bjet.txt  Name3=mumu_1jet_1bjet.txt                                                  > ee_emu_mumu_1j1t_card.txt
combineCards.py Name1=ee_card.txt         Name2=emu_card.txt                                                                                   > ee_emu_card.txt
combineCards.py Name1=ee_card.txt         Name2=mumu_card.txt                                                                                  > ee_mumu_card.txt
combineCards.py Name1=emu_card.txt        Name2=mumu_card.txt                                                                                  > emu_mumu_card.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_1jet_1bjet.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_11_21_card.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_11_21_22_card.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_card.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/ee_card.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/mumu_card.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/ee_emu_mumu_card.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/ee_emu_mumu_1j1t_card.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_1jet_0bjet.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_1jet_1bjet.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_2jet_1bjet.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_2jet_2bjet.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/ee_1jet_1bjet.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/ee_2jet_1bjet.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/ee_2jet_2bjet.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/mumu_1jet_1bjet.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/mumu_2jet_1bjet.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/mumu_2jet_2bjet.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/ee_emu_card.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/ee_mumu_card.txt
text2workspace.py /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_mumu_card.txt
echo "done!"
