import os
import ROOT
ROOT.gSystem.Load('/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/reskim_script/so_data_mc/reskim_C.so')
ROOT.gSystem.Load('/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/reskim_script/so_data_mc/reskim_C_ACLiC_dict_rdict.pcm')
ch_LFV_ST_gc_Olq_fastsim= ROOT.TChain('IIHEAnalysis')
ch_LFV_ST_gc_Olq_fastsim.Add("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/FLV/signalFastSimSamples/ST_13TeV_LFV_gu_Olq_Madgraph.root")
print 'add file done'
reskim_LFV_ST_gc_Olq_fastsim=ROOT.reskim(ch_LFV_ST_gc_Olq_fastsim, False, False, False, False)
reskim_LFV_ST_gc_Olq_fastsim.Loop("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/reskim_script/reskim_out/normal/LFV_ST_gc_Olq_fastsim.root")
