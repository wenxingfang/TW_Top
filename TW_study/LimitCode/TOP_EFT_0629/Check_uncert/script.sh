combine  -M MultiDimFit --saveWorkspace  ../ws_20180901/combined_Ctg_1.00.root
combine higgsCombineTest.MultiDimFit.mH120.root -M MaxLikelihoodFit --snapshotName MultiDimFit --freezeNuisances tw_DS_ --robustFit=1  --minimizerTolerance=0.001 --setPhysicsModelParameterRanges r=-1,1
