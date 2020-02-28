import ROOT
import os
import numpy
ROOT.TH1.AddDirectory(ROOT.kFALSE)


LHE_scale={}
f_scale=open("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/LHE_scale.txt","r")
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
cat["TTTo2L2Nu"]           =["TT_QCD"   ,"TT_QCD"  ]##[sample_name]=[out_put_name, input_name]
#cat["DYJetsToLL_M50_amc"]  =["DY_QCD"   ,"DY_QCD"  ]##[sample_name]=[out_put_name, input_name]
#cat["FCNC_ST_tug"]=["FCNC_QCD" ,"FCNC_QCD"]
#cat["FCNC_ST_tcg"]=["FCNC_QCD" ,"FCNC_QCD"]

Dir   ="./ntuples/saved_hist/Step2_20180623_top_pt_reweight/"
##Dir_SS="./ntuples/saved_hist/Step2_SameSign_20180609_newMVA/"##not used

f_nominal=ROOT.TFile(Dir+"emu_nominal_.root","read")

for icat in cat:
    hist_list=[]
    for ih in range(0,f_nominal.GetListOfKeys().GetSize()):
        hname=f_nominal.GetListOfKeys()[ih].GetName()
        if icat in hname and type(f_nominal.Get(hname)) == ROOT.TH1D and "FCNC_ST_tug_fs" not in hname and "FCNC_ST_tcg_fs" not in hname:
            hist_list.append(hname)
    print hist_list
    #for idir in [Dir,Dir_SS]:
    for idir in [Dir]:
        for chan in ["ee","emu","mumu"]:
        #for chan in ["emu"]:
            print idir+chan
            f_up  =ROOT.TFile("%s%s_%s_Up_.root"  %(idir,chan,cat[icat][0]),"UPDATE")
            f_down=ROOT.TFile("%s%s_%s_Down_.root"%(idir,chan,cat[icat][0]),"UPDATE")
            ############## save TTbar hist ########################
            for hname in hist_list:
                tmp_list=[]
                QCD_list=[]
                if "TT" in icat or "DY" in icat:
                    QCD_list=["1002","1003","1004","1005","1007","1009"]
                elif "FCNC" in icat:
                    QCD_list=["2","3","4","5","7","9"]
                else:
                    print "no match"
                for i in QCD_list:
                    if not os.path.isfile("%s%s_%s_%s_.root"%(idir,chan,cat[icat][1],i)):
                        print "no file %s%s_%s_%s_.root"%(idir,chan,cat[icat][1],i) 
                        continue
                    f_tmp=ROOT.TFile("%s%s_%s_%s_.root"%(idir,chan,cat[icat][1],i),"read")
                    tmp_name=hname.replace("nominal","%s_%s"%(cat[icat][1],str(i)))
                    scale_value=1
                    if LHE_scale[icat][str(i)]:
                        scale_value=float(LHE_scale[icat][str(i)])
                    else:
                        scale_value=1
                        print "don't find the scale for %s_%s"%(icat,str(i))
                    tmp_hist=f_tmp.Get(tmp_name)
                    tmp_hist.Scale(scale_value)##LHE scale to nominal cross section
                    #tmp_list.append(f_tmp.Get(tmp_name))
                    tmp_list.append(tmp_hist)
                    f_tmp.Close()
                hname_up  =hname.replace("nominal","%s_Up"  %(cat[icat][1]))
                hname_down=hname.replace("nominal","%s_Down"%(cat[icat][1]))
                hist_up  =tmp_list[0].Clone(hname_up)
                hist_down=tmp_list[0].Clone(hname_down)
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
