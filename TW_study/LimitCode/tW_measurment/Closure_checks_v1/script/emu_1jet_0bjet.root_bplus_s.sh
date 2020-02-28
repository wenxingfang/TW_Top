
cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks_v1/output/emu_1jet_0bjet.root//bplus_s
eval `scramv1 runtime -sh`
combine -M MaxLikelihoodFit -d /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_1jet_0bjet.root -t -1 --expectSignal 1

PostFitShapesFromWorkspace -o fit_shapes.root -f mlfit.root:fit_s --postfit --sampling --print -w /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/emu_1jet_0bjet.root > postfit.print