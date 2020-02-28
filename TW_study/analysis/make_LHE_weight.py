import os
import ROOT

sample_path={}

TTTo2L2Nu_path  =["/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC_0511_bjetsf/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8_sumLHEweight/crab_TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-MiniAOD/170827_144420/0000/","/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC_0511_bjetsf/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8_sumLHEweight/crab_TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-MiniAOD/170827_144420/0001/","/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC_0511_bjetsf/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8_sumLHEweight/crab_TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-MiniAOD/170827_144420/0002/","/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC_0511_bjetsf/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8_sumLHEweight/crab_TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-MiniAOD/170827_144420/0003/"]                

ST_tW_tug_path=["/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC_0511_bjetsf/ST_tW_tugFCNC_leptonDecays_Madgraph/crab_ST_tW_tugFCNC_leptonDecays_Madgraph/170827_144241/0000/"]
ST_tW_tcg_path=["/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC_0511_bjetsf/ST_tW_tcgFCNC_leptonDecays_Madgraph/crab_ST_tW_tcgFCNC_leptonDecays_Madgraph/170827_144108/0000/"]

DYJetsToLL_M50_amc_path=['/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC_0511_bjetsf/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_LHEweight/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-MiniAOD/171006_170939/0000/','/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC_0511_bjetsf/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_LHEweight/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-MiniAOD/171006_170939/0001/','/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC_0511_bjetsf/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_LHEweight/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-MiniAOD/171006_170939/0002/','/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC_0511_bjetsf/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_LHEweight/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-MiniAOD/171006_170939/0003/','/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC_0511_bjetsf/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_LHEweight/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-MiniAOD/171006_170939/0004/','/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC_0511_bjetsf/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_LHEweight/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-MiniAOD/171006_170939/0005/','/pnfs/iihe/cms/store/user/wenxing/FINAL_sample/MC_0511_bjetsf/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_LHEweight/crab_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-MiniAOD/171006_170939/0006/']

sample_path['TTTo2L2Nu']=TTTo2L2Nu_path        
sample_path['FCNC_ST_tug']=ST_tW_tug_path        
sample_path['FCNC_ST_tcg']=ST_tW_tcg_path        
sample_path['DYJetsToLL_M50_amc'] =DYJetsToLL_M50_amc_path        

LHE_sum_weight={}
for sample_name in sample_path:
    LHE_sum_weight[sample_name]={}
    for path in sample_path[sample_name]:
        filenames = os.listdir(path)
        for fname in filenames:
            filename = path +  fname
            if 'fail' in fname:
                continue
            f = ROOT.TFile.Open(filename)
            if not f:
                print 'not exist'+fname
            tree_meta = f.Get('meta')
            tree_meta.GetEntry(0)
            for ID in range(0,len(tree_meta.mc_weightsId)):
                #print tree_meta.mc_weightsId[ID]+":"+str(tree_meta.mc_sumofWeights[ID])
                if str(tree_meta.mc_weightsId[ID]) not in LHE_sum_weight[sample_name]:
                    LHE_sum_weight[sample_name][str(tree_meta.mc_weightsId[ID])]=tree_meta.mc_sumofWeights[ID]
                else:
                    LHE_sum_weight[sample_name][str(tree_meta.mc_weightsId[ID])]+=tree_meta.mc_sumofWeights[ID]

    
#print LHE_sum_weight

f_out=open("LHE_scale_DY.txt","w")
nominal_sum_w={}
nominal_sum_w["TTTo2L2Nu"]=1
nominal_sum_w["FCNC_ST_tug"]=1
nominal_sum_w["FCNC_ST_tcg"]=1
nominal_sum_w["DYJetsToLL_M50_amc"]=1
if LHE_sum_weight["TTTo2L2Nu"]["1001"]:
    nominal_sum_w["TTTo2L2Nu"]=LHE_sum_weight["TTTo2L2Nu"]["1001"]
if LHE_sum_weight["DYJetsToLL_M50_amc"]["1001"]:
    nominal_sum_w["DYJetsToLL_M50_amc"]=LHE_sum_weight["DYJetsToLL_M50_amc"]["1001"]
if LHE_sum_weight["FCNC_ST_tug"]["1"]:
    nominal_sum_w["FCNC_ST_tug"]=LHE_sum_weight["FCNC_ST_tug"]["1"]
if LHE_sum_weight["FCNC_ST_tcg"]["1"]:
    nominal_sum_w["FCNC_ST_tcg"]=LHE_sum_weight["FCNC_ST_tcg"]["1"]
print "nominal ttbar sum LHE weight: %f"%(nominal_sum_w["TTTo2L2Nu"])
print "nominal DY sum LHE weight:  %f"%(nominal_sum_w["DYJetsToLL_M50_amc"])
print "nominal tug sum LHE weight: %f"  %(nominal_sum_w["FCNC_ST_tug"])
print "nominal tcg sum LHE weight: %f"  %(nominal_sum_w["FCNC_ST_tcg"])
for sname in LHE_sum_weight:
    for ID in LHE_sum_weight[sname]:
        scale=nominal_sum_w[sname]/LHE_sum_weight[sname][ID]
        f_out.write(str(sname)+":"+str(ID)+":"+str(scale)+"\n")
f_out.close()
print "done!"
