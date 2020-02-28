import os 
import ROOT 
ROOT.gSystem.Load("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/select_scripts/select_save_parton_C.so") 
ROOT.gROOT.ProcessLine('select_save_parton("1104")') 
print 'Done!'