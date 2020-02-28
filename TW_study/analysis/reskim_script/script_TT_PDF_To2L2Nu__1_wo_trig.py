import os
import ROOT
ROOT.gSystem.Load('/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/reskim_script/so_data_mc/reskim_C.so')
ROOT.gSystem.Load('/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/reskim_script/so_data_mc/reskim_C_ACLiC_dict_rdict.pcm')
ch_TT_PDF_To2L2Nu= ROOT.TChain('IIHEAnalysis')
#ch_TT_PDF_To2L2Nu.Add("/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC_0511_bjetsf/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8_LHE/crab_TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-MiniAOD/170718_145618/0000/outfile_1.root")
ch_TT_PDF_To2L2Nu.Add("/pnfs/iihe/cms/store/user/wenxing/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/crab_TT_TuneCUETP8M2T4_13TeV-powheg-MiniAOD/170819_175317/0000/outfile_101.root")
print 'add file done'
reskim_TT_PDF_To2L2Nu=ROOT.reskim(ch_TT_PDF_To2L2Nu, False, False, False, False,"wo_trig",0,9999999)
reskim_TT_PDF_To2L2Nu.Loop("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/reskim_script/reskim_out/normal_perone/reMiniAOD/MC/mc_all/TT_PDF_To2L2Nu__1_wo_trig.root")
