cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para_new/obs/Cug
eval `scramv1 runtime -sh`
logsave  obs_Cug_Jets_normalisation_Norm.log combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/obs/higgsCombineCug.MultiDimFit.mH120.root -M MultiDimFit --setPhysicsModelParameterRanges r=-2.000000,2.000000   --algo grid --points 50   -n Jets_normalisation_Norm --snapshotName MultiDimFit --freezeNuisances TT_TopMass_,isxjet_1bjet_DY_normalisation_Norm,tw_DS_,MuonIDScaleFactor_,UnclusteredEn_,Jets_normalisation_Norm 