import os 
import ROOT 
#ROOT.gROOT.ProcessLine(".L /user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/script_select/select_save_hist_sys.C+") 
ROOT.gSystem.Load("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/script_select/select_save_hist_sys_C.so") 
ROOT.gROOT.ProcessLine('select_save_hist_sys("emu","nominal","samesign")') 
print 'Done!'
