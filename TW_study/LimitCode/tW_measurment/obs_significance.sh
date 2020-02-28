echo "+++++for emu_1jet_1bjet +++++++++++++++++++++++++++++++++++++++++++"
combine -M ProfileLikelihood --signif data_card_ttbar_DY/emu_1jet_1bjet.txt
echo "+++++for emu_11_21 +++++++++++++++++++++++++++++++++++++++++++"
combine -M ProfileLikelihood --signif data_card_ttbar_DY/emu_11_21_card.txt
echo "+++++for emu_11_21_22 +++++++++++++++++++++++++++++++++++++++++++"
combine -M ProfileLikelihood --signif data_card_ttbar_DY/emu_11_21_22_card.txt
echo "+++++for emu+++++++++++++++++++++++++++++++++++++++++++"
combine -M ProfileLikelihood --signif data_card_ttbar_DY/emu_card.txt
echo "+++++for ee+++++++++++++++++++++++++++++++++++++++++++"
combine -M ProfileLikelihood --signif data_card_ttbar_DY/ee_card.txt
echo "+++++for mumu+++++++++++++++++++++++++++++++++++++++++++"
combine -M ProfileLikelihood --signif data_card_ttbar_DY/mumu_card.txt
echo "+++++for ee emu mumu+++++++++++++++++++++++++++++++++++++++++++"
combine -M ProfileLikelihood --signif data_card_ttbar_DY/ee_emu_mumu_card.txt
