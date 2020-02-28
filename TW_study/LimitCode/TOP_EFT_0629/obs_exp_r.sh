#
#echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
#echo "### Ctg ee ############# observed ##################################"
#combine -M MaxLikelihoodFit ws_20180418/ee_Ctg_1.00.root --rMin -0.01 --rMax 0.01
#echo "### Ctg emu ############# observed ##################################"
#combine -M MaxLikelihoodFit ws_20180418/emu_Ctg_1.00.root --rMin -0.01 --rMax 0.01 
#echo "### Ctg mumu ############# observed ##################################"
#combine -M MaxLikelihoodFit ws_20180418/mumu_Ctg_1.00.root --rMin -0.1 --rMax 0 
#echo "### Ctg combined ############# observed ##################################"
#combine -M MaxLikelihoodFit ws_20180418/combined_Ctg_1.00.root --rMin 0 --rMax 0.04 
#
#echo "### Ctw ee ############# observed ##################################"
#combine -M MaxLikelihoodFit ws_20180418/ee_Ctw_1.00.root 
#echo "### Ctw emu ############# observed ##################################"
#combine -M MaxLikelihoodFit ws_20180418/emu_Ctw_1.00.root 
#echo "### Ctw mumu ############# observed ##################################"
#combine -M MaxLikelihoodFit ws_20180418/mumu_Ctw_1.00.root 
#echo "### Ctw combined ############# observed ##################################"
#combine -M MaxLikelihoodFit ws_20180418/combined_Ctw_1.00.root 
#
#echo "### Cphiq ee ############# observed ##################################"
#combine -M MaxLikelihoodFit ws_20180418/ee_Cphiq_1.00.root 
#echo "### Cphiq emu ############# observed ##################################"
#combine -M MaxLikelihoodFit ws_20180418/emu_Cphiq_1.00.root 
#echo "### Cphiq mumu ############# observed ##################################"
#combine -M MaxLikelihoodFit ws_20180418/mumu_Cphiq_1.00.root 
#echo "### Cphiq combined ############# observed ##################################"
#combine -M MaxLikelihoodFit ws_20180418/combined_Cphiq_1.00.root 

echo "### Cg ee ############# observed ##################################"
combine -M MaxLikelihoodFit ws_20180418_Cg/ee_Cg_1.00.root 
echo "### Cg emu ############# observed ##################################"
combine -M MaxLikelihoodFit ws_20180418_Cg/emu_Cg_1.00.root 
echo "### Cg mumu ############# observed ##################################"
combine -M MaxLikelihoodFit ws_20180418_Cg/mumu_Cg_1.00.root 
echo "### Cg combined ############# observed ##################################"
combine -M MaxLikelihoodFit ws_20180418_Cg/combined_Cg_1.00.root 
