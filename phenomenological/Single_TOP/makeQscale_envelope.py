import ROOT
import os
import numpy
ROOT.TH1.AddDirectory(ROOT.kFALSE)

is_7TeV=True

Use_scale=True


LHE_scale={}
f_scale=open("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/LHE_scale.txt","r")
lines=f_scale.readlines()
for line in lines:
    li=line.replace("\n","")
    sname=li.split(":")[0]
    LHE_ID=li.split(":")[1]
    scale =li.split(":")[-1]
    if sname not in LHE_scale:
        LHE_scale[sname]={}
        LHE_scale[sname][LHE_ID]=scale
    else:
        LHE_scale[sname][LHE_ID]=scale
print "imported LHE scale file"



cat={}
cat["Vts_top"]     =["hist_Vts_top"    ,"hist_Vts_top"    ]##[sample_name]=[out_put_name, input_name]
cat["Vts_antitop"] =["hist_Vts_antitop","hist_Vts_antitop"]##[sample_name]=[out_put_name, input_name]
cat["Vtd_top"]     =["hist_Vtd_top"    ,"hist_Vtd_top"    ]##[sample_name]=[out_put_name, input_name]
cat["Vtd_antitop"] =["hist_Vtd_antitop","hist_Vtd_antitop"]##[sample_name]=[out_put_name, input_name]
if is_7TeV==False:
    cat["Vtb_top"]     =["hist_Vtb_top"    ,"hist_Vtb_top"    ]##[sample_name]=[out_put_name, input_name]
    cat["Vtb_antitop"] =["hist_Vtb_antitop","hist_Vtb_antitop"]##[sample_name]=[out_put_name, input_name]

#Dir   ="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/ntuple/Reza_final_8TeV/"
Dir   ="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/ntuple/Reza_8TeV_notau_lastbin/"
if is_7TeV:
    Dir   ="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/ntuple/Reza_7TeV_lastbin/"

f_nominal=ROOT.TFile(Dir+"hist_Vts_top_nominal.root","read")

for icat in cat:
    hist_list=[]
    for ih in range(0,f_nominal.GetListOfKeys().GetSize()):
        hname=f_nominal.GetListOfKeys()[ih].GetName()
        if type(f_nominal.Get(hname)) == ROOT.TH1D :
            hist_list.append(hname)
    print hist_list
    for idir in [Dir]:
        f_up  =ROOT.TFile("%s%s_QScaleUp.root"  %(idir,cat[icat][0]),"RECREATE")
        f_down=ROOT.TFile("%s%s_QScaleDown.root"%(idir,cat[icat][0]),"RECREATE")
        ############## save TTbar hist ########################
        for hname in hist_list:
            tmp_list=[]
            QCD_list=["1002","1003","1004","1005","1007","1009"]
            for i in QCD_list:
                if not os.path.isfile("%s%s_%s.root"%(idir,cat[icat][1],i)):
                    print "no file %s%s_%s.root"%(idir,cat[icat][1],i) 
                    continue
                f_tmp=ROOT.TFile("%s%s_%s.root"%(idir,cat[icat][1],i),"read")
                scale_value=1
                if Use_scale:
                    str_E="_8TeV"
                    if is_7TeV:
                        str_E="_7TeV"
                    if LHE_scale[icat+str_E][str(i)]:
                        scale_value=float(LHE_scale[icat+str_E][str(i)])
                    else:
                        scale_value=1
                        print "don't find the scale for %s_%s"%(icat,str(i))
                tmp_hist=f_tmp.Get(hname)
                tmp_hist.Scale(scale_value)##LHE scale to nominal cross section
                tmp_list.append(tmp_hist)
                f_tmp.Close()
            hist_up  =tmp_list[0].Clone(hname)
            hist_down=tmp_list[0].Clone(hname)
            for ibin in range(1,hist_up.GetNbinsX()+1):
                list_value=[]
                for ihist in tmp_list:
                    list_value.append(ihist.GetBinContent(ibin))
                down=numpy.min(list_value)
                up  =numpy.max(list_value)
                hist_down.SetBinContent(ibin,down) 
                hist_up  .SetBinContent(ibin,up) 
            f_up.cd()
            hist_up.Write("",ROOT.TObject.kOverwrite)
            f_down.cd()
            hist_down.Write("",ROOT.TObject.kOverwrite)
        f_up.Close()
        f_down.Close()
    
    print "created %s up and down file"%(icat)
f_nominal.Close()
