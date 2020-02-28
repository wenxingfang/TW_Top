#
#echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
#echo "### emu_1jet_1bjet ############# observed ##################################"
#combine -M MaxLikelihoodFit data_card_ttbar_DY/emu_1jet_1bjet.txt
#echo "### emu_1jet_1bjet ############ expected ##################################"
#combine -M MaxLikelihoodFit data_card_ttbar_DY/emu_1jet_1bjet.txt  -t -1 --expectSignal=1
#
#echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
#echo "### emu_11_21 ############# observed ##################################"
#combine -M MaxLikelihoodFit data_card_ttbar_DY/emu_11_21_card.txt
#echo "### emu_11_21 ############# expected ##################################"
#combine -M MaxLikelihoodFit data_card_ttbar_DY/emu_11_21_card.txt  -t -1 --expectSignal=1
#
#echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
#echo "### emu_11_21_22 ############# observed ##################################"
#combine -M MaxLikelihoodFit data_card_ttbar_DY/emu_11_21_22_card.txt
#echo "### emu_11_21_22 ############# expected ##################################"
#combine -M MaxLikelihoodFit data_card_ttbar_DY/emu_11_21_22_card.txt  -t -1 --expectSignal=1
#
#echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
#echo "### emu ############# observed ##################################"
#combine -M MaxLikelihoodFit data_card_ttbar_DY/emu_card.txt
#echo "### emu ############# expected ##################################"
#combine -M MaxLikelihoodFit data_card_ttbar_DY/emu_card.txt  -t -1 --expectSignal=1
#
#echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
#echo "### ee ############# observed ##################################"
#combine -M MaxLikelihoodFit data_card_ttbar_DY/ee_card.txt
#echo "### ee ############# expected ##################################"
#combine -M MaxLikelihoodFit data_card_ttbar_DY/ee_card.txt  -t -1 --expectSignal=1
#
#echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
#echo "### mumu ############# observed ##################################"
#combine -M MaxLikelihoodFit data_card_ttbar_DY/mumu_card.txt
#echo "### mumu ############# expected ##################################"
#combine -M MaxLikelihoodFit data_card_ttbar_DY/mumu_card.txt  -t -1 --expectSignal=1


echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "### combined ############# observed ##################################"
#combine -M MaxLikelihoodFit data_card_ttbar_DY/ee_emu_mumu_card.txt 
##combine -M MaxLikelihoodFit data_card_ttbar_DY/ee_emu_mumu_card.txt --saveWorkspace ## don't use
combine data_card_ttbar_DY/ee_emu_mumu_card.txt -M MultiDimFit --saveWorkspace
echo "### combined ############# expected ##################################"
#combine -M MaxLikelihoodFit data_card_ttbar_DY/ee_emu_mumu_card.txt  -t -1 --expectSignal=1
