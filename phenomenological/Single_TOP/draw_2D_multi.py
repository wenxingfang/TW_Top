import ROOT
import math
from array import array
import gc
import numpy as np
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.TH1.AddDirectory(ROOT.kFALSE)

#ROOT.RooAbsReal.defaultIntegratorConfig().Print("v")
ROOT.RooAbsReal.defaultIntegratorConfig().setEpsAbs(1e-10) 
ROOT.RooAbsReal.defaultIntegratorConfig().setEpsRel(1e-10) 

####    ############ Draw ############################################
def draw_compare(igr,grs,squeue):
    canvas = ROOT.TCanvas('canvas','',900, 600)
    canvas.cd()
    canvas.SetTickx()
    canvas.SetTicky()
    canvas.SetBottomMargin(0.17)
    canvas.SetLeftMargin(0.15)
    y_min=0
    y_max=2
    x_min=0
    x_max=2;
    x_title=""
    y_title=""
    if igr == "VtbVts":
        x_title="|V_{tb}|"
        y_title="|V_{ts}|"
    elif igr == "VtbVtd":
        x_title="|V_{tb}|"
        y_title="|V_{td}|"
    elif igr == "VtsVtd":
        x_title="|V_{ts}|"
        y_title="|V_{td}|"
    dummy = ROOT.TH2D("dummy","",1,x_min,x_max,1,y_min,y_max)
    dummy.SetStats(ROOT.kFALSE)
    dummy.GetYaxis().SetTitle("%s"%y_title)
    dummy.GetXaxis().SetTitle("%s"%x_title)
    dummy.GetXaxis().SetTitleSize(0.07)
    dummy.GetYaxis().SetTitleSize(0.07)
    dummy.GetYaxis().SetLabelSize(0.06)
    dummy.GetXaxis().SetLabelSize(0.06)
    dummy.GetYaxis().SetLabelOffset(0.01)
    dummy.GetXaxis().SetLabelOffset(0.01)
    dummy.GetYaxis().SetTitleOffset(1)
    dummy.GetXaxis().SetTitleOffset(1)
    dummy.GetXaxis().SetMoreLogLabels()
    dummy.GetXaxis().SetNoExponent()
    dummy.GetXaxis().CenterTitle()
    dummy.GetYaxis().CenterTitle()
    dummy.Draw()
    legend = ROOT.TLegend(0.65,0.55,0.88,0.88)
    for igg in squeue:
        for ig in grs:
            if ig.GetName() == igg:
                #ig.SetFillColor  (ROOT.TColor.GetColor(name_dict[ig.GetName()]))
                ig.SetFillColorAlpha(ROOT.TColor.GetColor(name_dict[ig.GetName()]),0.5)
                ig.SetLineColor  (ROOT.TColor.GetColor(name_dict[ig.GetName()]))
                #ig.SetMarkerColor(ROOT.TColor.GetColor(name_dict[ig.GetName()]))
                #ig.SetMarkerStyle(8)
                #ig.SetFillStyle(3004)
                #ig.SetLineWidth(2)
                ig.Draw("F")
                #ig.Draw("C")
                if igg in legend_name_dict:
                    legend.AddEntry(ig,'%s'%legend_name_dict[igg],'F')
                else:
                    legend.AddEntry(ig,'%s'%ig.GetName(),'F')
    for ig in grs:
        ig.SetLineColor  (ROOT.TColor.GetColor(name_dict[ig.GetName()]))
        ig.SetLineWidth(2)
        #ig.Draw("C")
        ig.Draw("l")
    dummy.Draw("AXISSAME")
    legend.SetBorderSize(0)
    legend.SetTextFont(42)
    legend.SetTextSize(0.04)
    legend.Draw()
    label = ROOT.TLatex()
    label.SetTextAlign(12)
    label.SetTextFont(42)
    label.SetTextSize(0.05)
    label.SetNDC(ROOT.kTRUE)
    label.DrawLatex(0.22,0.80, str_CL[Sigma])
    label_chan = ROOT.TLatex()
    label_chan.SetTextAlign(12)
    label_chan.SetTextFont(42)
    label_chan.SetTextSize(0.05)
    label_chan.SetNDC(ROOT.kTRUE)
    label_chan.DrawLatex(0.15,0.93, chan)
    canvas.Print('./compare_2D_plot/multi_%s.png'%(igr)) 
    canvas.Print('./compare_2D_plot/multi_%s.pdf'%(igr)) 
    del canvas
    gc.collect()

class file_object:
    def __init__(self,name,file_name,color):
        self.name=name
        self.file_name=file_name
        self.File=ROOT.TFile(file_name,"read")
        self.color=color
str_method="dchi2"
Sigma="1s"#"2s","3s"
chan="LHC 8TeV"
str_CL={"1s":"68% CL Expected","2s":"95% CL Expected","3s":"99% CL Expected"}
file_path="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/limit_out/"
#name_dict={"Diff_8TeV_Ratio":"#027202","Ratio_8TeV":"#3399ff","ST_Ratio_8TeV":"#ffa500","Width_8TeV":"#b0b09e","Rt_8TeV":"#00ffff","tW_Ratio_8TeV":"#ff6666"}
#legend_name_dict={"Diff_8TeV_Ratio":"#sigma_{diff}^{t-ch}","Ratio_8TeV":"R","ST_Ratio_8TeV":"#sigma_{t-ch}+R","Width_8TeV":"#Gamma_{t}","Rt_8TeV":"R_{t}","tW_Ratio_8TeV":"#sigma_{tW-ch}+R"}
#squeue=["Rt_8TeV","Width_8TeV","tW_Ratio_8TeV","ST_Ratio_8TeV","Ratio_8TeV","Diff_8TeV_Ratio"]
name_dict={"Diff_8TeV_Ratio":"#027202","ST_Ratio_8TeV":"#ffa500","Width_8TeV":"#b0b09e","Rt_8TeV":"#00ffff","tW_Ratio_8TeV":"#ff6666"}
legend_name_dict={"Diff_8TeV_Ratio":"#sigma_{diff}^{t-ch}+R","Ratio_8TeV":"R","ST_Ratio_8TeV":"#sigma_{t-ch}+R","Width_8TeV":"#Gamma_{t}","Rt_8TeV":"R_{t}","tW_Ratio_8TeV":"#sigma_{tW-ch}+R"}
squeue=["Rt_8TeV","Width_8TeV","tW_Ratio_8TeV","ST_Ratio_8TeV","Diff_8TeV_Ratio"]
file_list=[]
for iname in name_dict:
    file_list.append(file_object(iname,file_path+"limit_2D_%s_%s_exp.root"%(str_method,iname),ROOT.TColor.GetColor(name_dict[iname])))

gr_dict={}
for ic in ["VtbVts","VtbVtd","VtsVtd"]:
    gr_dict[ic]=[]
    for ifile in file_list:
        h_tmp=ifile.File.Get("%s_%s"%(ic,Sigma))
        h_tmp.SetName(ifile.name)
        gr_dict[ic].append(h_tmp)
print gr_dict
for igr in gr_dict:
    draw_compare(igr,gr_dict[igr],squeue)
print "done!"
