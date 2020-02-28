import os
import ROOT

sample_path={}


vtb_antitop_8TeV="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/final_8TeV/outfile_vtb_antitop_8TeV.root"
vts_antitop_8TeV="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/final_8TeV/outfile_vts_antitop_8TeV.root"
vtd_antitop_8TeV="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/final_8TeV/outfile_vtd_antitop_8TeV.root"
vtb_top_8TeV    ="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/final_8TeV/outfile_vtb_top_8TeV.root"
vts_top_8TeV    ="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/final_8TeV/outfile_vts_top_8TeV.root"
vtd_top_8TeV    ="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/final_8TeV/outfile_vtd_top_8TeV.root"
vts_antitop_7TeV="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/final_7TeV/vts_antitop_7TeV.root"
vtd_antitop_7TeV="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/final_7TeV/vtd_antitop_7TeV.root"
vts_top_7TeV    ="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/final_7TeV/vts_top_7TeV.root"
vtd_top_7TeV    ="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/final_7TeV/vtd_top_7TeV.root"

sample_path["Vtb_antitop_8TeV"]=vtb_antitop_8TeV
sample_path["Vts_antitop_8TeV"]=vts_antitop_8TeV
sample_path["Vtd_antitop_8TeV"]=vtd_antitop_8TeV
sample_path["Vtb_top_8TeV"]    =vtb_top_8TeV    
sample_path["Vts_top_8TeV"]    =vts_top_8TeV    
sample_path["Vtd_top_8TeV"]    =vtd_top_8TeV    
sample_path["Vts_antitop_7TeV"]=vts_antitop_7TeV
sample_path["Vtd_antitop_7TeV"]=vtd_antitop_7TeV
sample_path["Vts_top_7TeV"]    =vts_top_7TeV    
sample_path["Vtd_top_7TeV"]    =vtd_top_7TeV    

LHE_sum_weight={}
for sample_name in sample_path:
    LHE_sum_weight[sample_name]={}
    f = ROOT.TFile.Open(sample_path[sample_name])
    if not f:
        print 'not exist'+sample_path[sample_name]
    tree_meta = f.Get('meta')
    tree_meta.GetEntry(0)
    for ID in range(0,len(tree_meta.mc_weightsId)):
        #print tree_meta.mc_weightsId[ID]+":"+str(tree_meta.mc_sumofWeights[ID])
        if str(tree_meta.mc_weightsId[ID]) not in LHE_sum_weight[sample_name]:
            LHE_sum_weight[sample_name][str(tree_meta.mc_weightsId[ID])]=tree_meta.mc_sumofWeights[ID]
        else:
            LHE_sum_weight[sample_name][str(tree_meta.mc_weightsId[ID])]+=tree_meta.mc_sumofWeights[ID]

    
#print LHE_sum_weight

f_out=open("LHE_scale.txt","w")
nominal_sum_w={}
nominal_sum_w["Vtb_antitop_8TeV"]=1
nominal_sum_w["Vts_antitop_8TeV"]=1
nominal_sum_w["Vtd_antitop_8TeV"]=1
nominal_sum_w["Vtb_top_8TeV"]    =1
nominal_sum_w["Vts_top_8TeV"]    =1
nominal_sum_w["Vtd_top_8TeV"]    =1
nominal_sum_w["Vts_antitop_7TeV"]=1
nominal_sum_w["Vtd_antitop_7TeV"]=1
nominal_sum_w["Vts_top_7TeV"]    =1
nominal_sum_w["Vtd_top_7TeV"]    =1

if LHE_sum_weight["Vtb_antitop_8TeV"]["1001"]:
    nominal_sum_w["Vtb_antitop_8TeV"]=LHE_sum_weight["Vtb_antitop_8TeV"]["1001"]
if LHE_sum_weight["Vts_antitop_8TeV"]["1001"]:
    nominal_sum_w["Vts_antitop_8TeV"]=LHE_sum_weight["Vts_antitop_8TeV"]["1001"]
if LHE_sum_weight["Vtd_antitop_8TeV"]["1001"]:
    nominal_sum_w["Vtd_antitop_8TeV"]=LHE_sum_weight["Vtd_antitop_8TeV"]["1001"]
if LHE_sum_weight["Vtb_top_8TeV"]["1001"]:
    nominal_sum_w["Vtb_top_8TeV"]=LHE_sum_weight["Vtb_top_8TeV"]["1001"]
if LHE_sum_weight["Vts_top_8TeV"]["1001"]:
    nominal_sum_w["Vts_top_8TeV"]=LHE_sum_weight["Vts_top_8TeV"]["1001"]
if LHE_sum_weight["Vtd_top_8TeV"]["1001"]:
    nominal_sum_w["Vtd_top_8TeV"]=LHE_sum_weight["Vtd_top_8TeV"]["1001"]

if LHE_sum_weight["Vts_antitop_7TeV"]["1001"]:
    nominal_sum_w["Vts_antitop_7TeV"]=LHE_sum_weight["Vts_antitop_7TeV"]["1001"]
if LHE_sum_weight["Vtd_antitop_7TeV"]["1001"]:
    nominal_sum_w["Vtd_antitop_7TeV"]=LHE_sum_weight["Vtd_antitop_7TeV"]["1001"]
if LHE_sum_weight["Vts_top_7TeV"]["1001"]:
    nominal_sum_w["Vts_top_7TeV"]=LHE_sum_weight["Vts_top_7TeV"]["1001"]
if LHE_sum_weight["Vtd_top_7TeV"]["1001"]:
    nominal_sum_w["Vtd_top_7TeV"]=LHE_sum_weight["Vtd_top_7TeV"]["1001"]
for sname in LHE_sum_weight:
    for ID in LHE_sum_weight[sname]:
        scale=nominal_sum_w[sname]/LHE_sum_weight[sname][ID]
        f_out.write(str(sname)+":"+str(ID)+":"+str(scale)+"\n")
f_out.close()
print "done!"
