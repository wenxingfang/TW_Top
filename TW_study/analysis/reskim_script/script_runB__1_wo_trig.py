import os
import ROOT
ROOT.gSystem.Load('/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/reskim_script/so_data_mc/reskim_C.so')
ROOT.gSystem.Load('/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/reskim_script/so_data_mc/reskim_C_ACLiC_dict_rdict.pcm')
ch_runB= ROOT.TChain('IIHEAnalysis')
ch_runB.Add("/pnfs/iihe/cms/store/user/wenxing/DoubleEG//crab_DoubleEG_Run2016B-03Feb2017-v2_final/170408_110413/0000/outfile_109.root")
print 'add file done'
reskim_runB=ROOT.reskim(ch_runB, True, False, False, False,"wo_trig",0,9999999)
reskim_runB.Loop("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/reskim_script/reskim_out/normal_perone/reMiniAOD/DoubleEG/runB_109_noScale_check.root")
