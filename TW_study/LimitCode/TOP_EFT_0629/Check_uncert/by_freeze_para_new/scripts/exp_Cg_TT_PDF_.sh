cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para_new/exp/Cg
eval `scramv1 runtime -sh`
logsave  exp_Cg_TT_PDF_.log combine /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/exp/higgsCombineCg.MultiDimFit.mH120.root -M MultiDimFit --setPhysicsModelParameterRanges r=-1.000000,1.000000   --algo grid --points 50 -t -1 --expectSignal=0 -n TT_PDF_ --snapshotName MultiDimFit --freezeNuisances TT_TopMass_,tw_DS_,DY_QCD_,MuonIDScaleFactor_,is1jet_1bjet_DY_normalisation,TT_PDF_ 