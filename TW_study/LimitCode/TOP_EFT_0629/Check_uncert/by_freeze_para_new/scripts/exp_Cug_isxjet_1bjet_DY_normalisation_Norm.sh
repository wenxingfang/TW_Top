cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para_new/exp/Cug
eval `scramv1 runtime -sh`
logsave  exp_Cug_isxjet_1bjet_DY_normalisation_Norm.log combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/exp/higgsCombineCug.MultiDimFit.mH120.root -M MultiDimFit --setPhysicsModelParameterRanges r=-2.000000,2.000000   --algo grid --points 50 -t -1 --expectSignal=0 -n isxjet_1bjet_DY_normalisation_Norm --snapshotName MultiDimFit --freezeNuisances TT_TopMass_,isxjet_1bjet_DY_normalisation_Norm 