
echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "### tug ee ############# observed ##################################"
combine -M MaxLikelihoodFit ws_search_tug_20180418/ee_FCNC_0.10.root 
echo "### tug emu ############# observed ##################################"
combine -M MaxLikelihoodFit ws_search_tug_20180418/emu_FCNC_0.10.root 
echo "### tug mumu ############# observed ##################################"
combine -M MaxLikelihoodFit ws_search_tug_20180418/mumu_FCNC_0.10.root 
echo "### tug combined ############# observed ##################################"
combine -M MaxLikelihoodFit ws_search_tug_20180418/combined_FCNC_0.10.root 

echo "### tcg ee ############# observed ##################################"
combine -M MaxLikelihoodFit ws_search_tcg_20180418/ee_FCNC_0.10.root 
echo "### tcg emu ############# observed ##################################"
combine -M MaxLikelihoodFit ws_search_tcg_20180418/emu_FCNC_0.10.root 
echo "### tcg mumu ############# observed ##################################"
combine -M MaxLikelihoodFit ws_search_tcg_20180418/mumu_FCNC_0.10.root 
echo "### tcg combined ############# observed ##################################"
combine -M MaxLikelihoodFit ws_search_tcg_20180418/combined_FCNC_0.10.root 
