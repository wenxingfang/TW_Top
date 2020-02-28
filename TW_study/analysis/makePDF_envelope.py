import ROOT
import os
import numpy
ROOT.TH1.AddDirectory(ROOT.kFALSE)

cat={}
#cat["TTTo2L2Nu"]  =["TT_PDF"       ,"TT_PDF"  ]##[sample_name]=[out_put_name, input_name]
cat["FCNC_ST_tug"]=["FCNC_tug_PDF" ,"FCNC_PDF"]
cat["FCNC_ST_tcg"]=["FCNC_tcg_PDF" ,"FCNC_PDF"]

Dir   ="./ntuples/saved_hist/Step2_0806/"
Dir_SS="./ntuples/saved_hist/Step2_SameSign_0806/"

f_nominal=ROOT.TFile(Dir+"emu_nominal_.root","read")

for icat in cat:
    hist_list=[]
    for ih in range(0,f_nominal.GetListOfKeys().GetSize()):
        hname=f_nominal.GetListOfKeys()[ih].GetName()
        #if "TTTo2L2Nu" in hname and type(f_nominal.Get(hname)) == ROOT.TH1D:
        if icat in hname and type(f_nominal.Get(hname)) == ROOT.TH1D and "FCNC_ST_tug_fs" not in hname and "FCNC_ST_tcg_fs" not in hname:
            hist_list.append(hname)
    print hist_list
    for idir in [Dir,Dir_SS]:
        for chan in ["ee","emu","mumu"]:
        #for chan in ["ee","mumu"]:
            print idir+chan
            #f_up  =ROOT.TFile("%s%s_TT_PDF_Up_.root"  %(idir,chan),"RECREATE")
            #f_down=ROOT.TFile("%s%s_TT_PDF_Down_.root"%(idir,chan),"RECREATE")
            f_up  =ROOT.TFile("%s%s_%s_Up_.root"  %(idir,chan,cat[icat][0]),"RECREATE")
            f_down=ROOT.TFile("%s%s_%s_Down_.root"%(idir,chan,cat[icat][0]),"RECREATE")
            ############## save TTbar hist ########################
            for hname in hist_list:
                tmp_list=[]
                pdf_min=1
                pdf_max=2
                if icat=="TTTo2L2Nu":
                    pdf_min=2001
                    pdf_max=2103
                elif (icat=="FCNC_ST_tug" or icat=="FCNC_ST_tcg"):
                    pdf_min=10
                    pdf_max=111
                else:
                    print "wrong name!!"
                for i in range(pdf_min,pdf_max):
                    if not os.path.isfile("%s%s_%s_%s_.root"%(idir,chan,cat[icat][1],i)):
                        print "no file %s%s_%s_%s_.root"%(idir,chan,cat[icat][1],i) 
                        continue
                    #f_tmp=ROOT.TFile("%s%s_TT_PDF_%s_.root"%(idir,chan,i),"read")
                    f_tmp=ROOT.TFile("%s%s_%s_%s_.root"%(idir,chan,cat[icat][1],i),"read")
                    #tmp_name=hname.replace("nominal","TT_PDF_%s"%str(i))
                    tmp_name=hname.replace("nominal","%s_%s"%(cat[icat][1],str(i)))
                    tmp_list.append(f_tmp.Get(tmp_name))
                    f_tmp.Close()
                #hname_up  =hname.replace("nominal","TT_PDF_Up")
                #hname_down=hname.replace("nominal","TT_PDF_Down")
                hname_up  =hname.replace("nominal","%s_Up"  %(cat[icat][1]))
                hname_down=hname.replace("nominal","%s_Down"%(cat[icat][1]))
                hist_up  =tmp_list[0].Clone(hname_up)
                hist_down=tmp_list[0].Clone(hname_down)
                for ibin in range(1,hist_up.GetNbinsX()+1):
                    list_value=[]
                    for ihist in tmp_list:
                        list_value.append(ihist.GetBinContent(ibin))
                    down_up=numpy.percentile(list_value,[15.865,84.135])
                    hist_down.SetBinContent(ibin,down_up[0]) 
                    hist_up  .SetBinContent(ibin,down_up[1]) 
                f_up.cd()
                hist_up.Write()
                f_down.cd()
                hist_down.Write()
             #### save other hist #####################3#########
            f_nom=ROOT.TFile("%s%s_nominal_.root"%(idir,chan),"read")
            for ih in range(0,f_nom.GetListOfKeys().GetSize()):
                hname=f_nom.GetListOfKeys()[ih].GetName()
                #if "TTTo2L2Nu" in hname:continue
                if icat in hname:continue
                hist_name=str(hname)
                #up_name  =hist_name.replace("nominal","TT_PDF_Up"  )
                #down_name=hist_name.replace("nominal","TT_PDF_Down")
                up_name  =hist_name.replace("nominal","%s_Up"  %(cat[icat][1]))
                down_name=hist_name.replace("nominal","%s_Down"%(cat[icat][1]))
                f_up.cd()
                f_nom.Get(hname).Write(up_name)
                f_down.cd()
                f_nom.Get(hname).Write(down_name)
            f_up.Close()
            f_down.Close()
    
    print "created %s up and down file"%(cat[icat][0])
f_nominal.Close()
