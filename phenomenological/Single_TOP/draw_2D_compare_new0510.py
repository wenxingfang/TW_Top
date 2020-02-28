import ROOT
import math
from array import array
import gc
import numpy as np
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gSystem.Load("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/mod_limit_C.so")

#ROOT.RooAbsReal.defaultIntegratorConfig().Print("v")
ROOT.RooAbsReal.defaultIntegratorConfig().setEpsAbs(1e-10) 
ROOT.RooAbsReal.defaultIntegratorConfig().setEpsRel(1e-10) 

####    ############ Draw ############################################
def draw_compare(igr,gr_L, gr_S):
    canvas = ROOT.TCanvas('canvas','',900, 600)
    canvas.cd()
    canvas.SetTickx()
    canvas.SetTicky()
    canvas.SetBottomMargin(0.17)
    canvas.SetLeftMargin(0.15)
    y_min=0
    y_max=1
    x_min=0
    x_max=1;
    if only_draw_L:
        y_min=0 if gr_L[3].GetYaxis().GetXmin()==0 else gr_L[3].GetYaxis().GetXmin()-0.05
        y_max=gr_L[3].GetYaxis().GetXmax()+0.1 
        x_min=0 if gr_L[3].GetXaxis().GetXmin()==0 else gr_L[3].GetXaxis().GetXmin()-0.05
        x_max=gr_L[3].GetXaxis().GetXmax()+0.05 
    elif only_draw_S:
        y_min=0 if gr_S[3].GetYaxis().GetXmin()==0 else gr_S[3].GetYaxis().GetXmin()-0.05
        y_max=gr_S[3].GetYaxis().GetXmax()+0.1 
        x_min=0 if gr_S[3].GetXaxis().GetXmin()==0 else gr_S[3].GetXaxis().GetXmin()-0.05
        x_max=gr_S[3].GetXaxis().GetXmax()+0.05 
    else:
        y_min=0 if gr_L[3].GetYaxis().GetXmin()==0 else gr_L[3].GetYaxis().GetXmin()-0.05
        y_max=gr_L[3].GetYaxis().GetXmax()+0.1 
        x_min=0 if gr_L[3].GetXaxis().GetXmin()==0 else gr_L[3].GetXaxis().GetXmin()-0.05
        x_max=gr_L[3].GetXaxis().GetXmax()+0.05 
    
    x_title=""
    y_title=""
    if igr == "VtbVts":
        x_title="|V_{tb}|"
        y_title="|V_{ts}|"
        y_min=0#nominal
        y_max=0.5#nominal
        #x_min=0.8
        #x_min=0.89#nominal
        #x_max=1.05#nominal
        #x_max=1.1
        x_min=0.85#R0.9
        x_max=0.98#R0.9
    elif igr == "VtbVtd":
        x_title="|V_{tb}|"
        y_title="|V_{td}|"
        y_min=0#nominal
        y_max=0.25#nominal
        #y_max=0.4
        #x_min=0.8
        #x_min=0.89#nominal
        #x_max=1.05#nominal
        #x_max=1.1
        x_min=0.85#R0.9
        x_max=0.98#R0.9
    elif igr == "VtsVtd":
        x_title="|V_{ts}|"
        y_title="|V_{td}|"
        #y_min=0#nominal
        #y_max=0.25#nominal
        #y_max=0.35
        #x_min=0#nominal
        #x_max=0.4#nominal
        #x_min=0.12#R0.95
        #x_max=0.26#R0.95
        #y_min=0   #R0.99
        #y_max=0.15#R0.99
        #x_min=0.0 #R0.99
        #x_max=0.11#R0.99
        y_min=0   #R0.9
        y_max=0.2#R0.9
        x_min=0.24 #R0.9
        x_max=0.32#R0.9
    dummy = ROOT.TH2D("dummy","",1,x_min,x_max,1,y_min,y_max)
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
    dummy.GetXaxis().SetNdivisions(505)
    dummy.GetYaxis().SetNdivisions(505)
    dummy.Draw()
    width_line=3
    gr_S[0].SetMarkerColor(ROOT.TColor.GetColor("#ff00ff"))
    gr_S[0].SetFillColor  (ROOT.TColor.GetColor("#ff00ff"))
    gr_S[0].SetLineColor  (ROOT.TColor.GetColor("#ff00ff"))
    gr_S[0].SetMarkerStyle(22)
    gr_S[0].SetMarkerSize(1.5)
    gr_S[0].SetLineWidth  (width_line)
    gr_S[1].SetMarkerColor(ROOT.TColor.GetColor("#ffa500"))
    gr_S[1].SetFillColor  (ROOT.TColor.GetColor("#ffa500"))
    gr_S[1].SetLineColor  (ROOT.TColor.GetColor("#ffa500"))
    gr_S[1].SetMarkerStyle(8)
    gr_S[1].SetLineWidth  (width_line)
    gr_S[2].SetMarkerColor(ROOT.TColor.GetColor("#00ffff"))
    gr_S[2].SetFillColor  (ROOT.TColor.GetColor("#00ffff"))
    gr_S[2].SetLineColor  (ROOT.TColor.GetColor("#00ffff"))
    gr_S[2].SetMarkerStyle(8)
    gr_S[2].SetLineWidth  (width_line)
    gr_S[3].SetMarkerColor(ROOT.TColor.GetColor("#0000ff"))
    gr_S[3].SetFillColor  (ROOT.TColor.GetColor("#0000ff"))
    gr_S[3].SetLineColor  (ROOT.TColor.GetColor("#0000ff"))
    gr_S[3].SetMarkerStyle(8)
    gr_S[3].SetLineWidth  (width_line)
    gr_L[0].SetMarkerColor(ROOT.TColor.GetColor("#ff00ff"))
    gr_L[0].SetFillColor  (ROOT.TColor.GetColor("#ff00ff"))
    gr_L[0].SetLineColor  (ROOT.TColor.GetColor("#ff00ff"))
    gr_L[0].SetMarkerStyle(26)
    gr_L[0].SetMarkerSize(1.5)
    gr_L[0].SetLineWidth  (width_line)
    gr_L[1].SetMarkerColor(ROOT.TColor.GetColor("#ff5370"))
    gr_L[1].SetFillColor  (ROOT.TColor.GetColor("#ff5370"))
    gr_L[1].SetLineColor  (ROOT.TColor.GetColor("#ff5370"))
    gr_L[1].SetMarkerStyle(8)
    gr_L[1].SetLineWidth  (width_line)
    gr_L[2].SetMarkerColor(ROOT.TColor.GetColor("#76eec6"))
    gr_L[2].SetFillColor  (ROOT.TColor.GetColor("#76eec6"))
    gr_L[2].SetLineColor  (ROOT.TColor.GetColor("#76eec6"))
    gr_L[2].SetMarkerStyle(8)
    gr_L[2].SetLineWidth  (width_line)
    gr_L[3].SetMarkerColor(ROOT.TColor.GetColor("#6cbaf9"))
    gr_L[3].SetFillColor  (ROOT.TColor.GetColor("#6cbaf9"))
    gr_L[3].SetLineColor  (ROOT.TColor.GetColor("#6cbaf9"))
    gr_L[3].SetMarkerStyle(8)
    gr_L[3].SetLineWidth  (width_line)
    if only_draw_L:
        gr_L[0].SetMarkerStyle(22)
        gr_L[3].Draw("F")
        gr_L[2].Draw("F")
        gr_L[1].Draw("F")
        gr_L[0].Draw("p")
    elif only_draw_S:
        gr_S[3].Draw("F")
        gr_S[2].Draw("F")
        gr_S[1].Draw("F")
        gr_S[0].Draw("p")
    else:
        gr_S[3].Draw(draw_S)
        gr_S[2].Draw(draw_S)
        gr_S[1].Draw(draw_S)
        gr_L[3].Draw(draw_L)
        gr_L[2].Draw(draw_L)
        gr_L[1].Draw(draw_L)
        gr_S[0].Draw("p")
        gr_L[0].Draw("p")
    dummy.Draw("AXISSAME")
    legend = ROOT.TLegend(0.2,0.7,0.85,0.88)
    if only_draw_L:
        legend.AddEntry(gr_L[0],'best-fit %s'%str_L,'p')
        legend.AddEntry(gr_L[1],'68%% CL %s'%str_L     ,'F')
        legend.AddEntry(gr_L[2],'95%% CL %s'%str_L     ,'F')
        legend.AddEntry(gr_L[3],'99%% CL %s'%str_L     ,'F')
    elif only_draw_S:
        legend.AddEntry(gr_S[0],'best-fit %s'%str_S,'p')
        legend.AddEntry(gr_S[1],'68%% CL %s'%str_S     ,'f')
        legend.AddEntry(gr_S[2],'95%% CL %s'%str_S     ,'f')
        legend.AddEntry(gr_S[3],'99%% CL %s'%str_S     ,'f')
    else:
        legend.SetNColumns(2)
        legend.AddEntry(gr_S[0],'best-fit %s'%str_S,'p')
        legend.AddEntry(gr_L[0],'best-fit %s'%str_L,'p')
        legend.AddEntry(gr_S[1],'68%% CL %s'%str_S     ,'f')
        legend.AddEntry(gr_L[1],'68%% CL %s'%str_L     ,'l')
        legend.AddEntry(gr_S[2],'95%% CL %s'%str_S     ,'f')
        legend.AddEntry(gr_L[2],'95%% CL %s'%str_L     ,'l')
        legend.AddEntry(gr_S[3],'99%% CL %s'%str_S     ,'f')
        legend.AddEntry(gr_L[3],'99%% CL %s'%str_L     ,'l')
    legend.SetBorderSize(0)
    legend.SetTextFont(42)
    legend.SetTextSize(0.04)
    legend.Draw()
    label = ROOT.TLatex()
    label.SetTextAlign(12)
    label.SetTextFont(42)
    label.SetTextSize(0.05)
    label.SetNDC(ROOT.kTRUE)
    label.DrawLatex(0.15,0.93, chan)
    canvas.Print('./compare_2D_plot/%s.png'%(igr)) 
    canvas.Print('./compare_2D_plot/%s.pdf'%(igr)) 
    del canvas
    gc.collect()
draw_L="L"
draw_S="F"
Dir="./limit_out/"
#Dir="./limit_out_fixRcms/"
chan="#sigma_{diff}^{t-ch} (LHC)                                   #sqrt{s} = 8 TeV, 20.2 fb^{-1}"
#chan="#sigma_{fid}^{t-ch} (LHC)                                   #sqrt{s} = 8 TeV, 20.2 fb^{-1}"
#chan="LHC + Tevatron"
#chan="#sigma_{diff}^{t-ch} (LHC 13TeV)"
#F_S=ROOT.TFile(Dir+"limit_2D_dchi2_8TeV_Ratio_st_fid_obs.root","read")
#str_S='Observed'
#F_L=ROOT.TFile(Dir+"limit_2D_dchi2_8TeV_Ratio_st_fid_exp.root","read")
#str_L='Expected'
#F_S=ROOT.TFile(Dir+"limit_2D_dchi2_Diff_8TeV_Ratio_obs_R0.9.root","read")
#str_S='Observed'
#F_L=ROOT.TFile(Dir+"limit_2D_dchi2_Diff_8TeV_Ratio_exp_R0.9.root","read")
#str_L='Expected'
F_S=ROOT.TFile(Dir+"FixR2_limit_2D_dchi2_Diff_8TeV_Ratio_obs_R0.9.root","read")
str_S='Observed'
F_L=ROOT.TFile(Dir+"FixR2_limit_2D_dchi2_Diff_8TeV_Ratio_exp_R0.9.root","read")
str_L='Expected'
#F_S=ROOT.TFile(Dir+"limit_2D_dchi2_Diff_8TeV_7TeV_Inclusive_obs_R0.9.root","read")
#str_S='Observed'
#F_L=ROOT.TFile(Dir+"limit_2D_dchi2_Diff_8TeV_7TeV_Inclusive_exp_R0.9.root","read")
#str_L='Expected'
#F_S=ROOT.TFile(Dir+"FixR1_limit_2D_dchi2_Diff_8TeV_7TeV_Inclusive_obs_R0.9.root","read")
#str_S='Observed'
#F_L=ROOT.TFile(Dir+"FixR1_limit_2D_dchi2_Diff_8TeV_7TeV_Inclusive_exp_R0.9.root","read")
#str_L='Expected'


#F_S=ROOT.TFile(Dir+"limit_2D_dchi2_Diff_8TeV_Ratio_obs.root","read")
#str_S='Observed'
#F_L=ROOT.TFile(Dir+"limit_2D_dchi2_Diff_8TeV_Ratio_exp.root","read")
#str_L='Expected'
#F_S=ROOT.TFile(Dir+"limit_2D_dchi2_Diff_8TeV_7TeV_Inclusive_obs.root","read")
#str_S='Observed'
#F_L=ROOT.TFile(Dir+"limit_2D_dchi2_Diff_8TeV_7TeV_Inclusive_exp.root","read")
#str_L='Expected'
#F_S=ROOT.TFile(Dir+"limit_2D_dchi2_Diff_13TeV_Ratio3000fb_exp.root","read")
#str_S='Expected 3000 fb^{-1}'
#F_L=ROOT.TFile(Dir+"limit_2D_dchi2_Diff_13TeV_Ratio300fb_exp.root","read")
#str_L='Expected 300 fb^{-1}'

only_draw_L=False
only_draw_S=False

gr_dicti={}
gr_dicti["VtbVts"]={}
gr_dicti["VtbVtd"]={}
gr_dicti["VtsVtd"]={}

gr_dicti["VtbVts"]["L"]=[F_L.Get("VtbVts_best"),F_L.Get("VtbVts_1s"),F_L.Get("VtbVts_2s"),F_L.Get("VtbVts_3s")]
gr_dicti["VtbVtd"]["L"]=[F_L.Get("VtbVtd_best"),F_L.Get("VtbVtd_1s"),F_L.Get("VtbVtd_2s"),F_L.Get("VtbVtd_3s")]
gr_dicti["VtsVtd"]["L"]=[F_L.Get("VtsVtd_best"),F_L.Get("VtsVtd_1s"),F_L.Get("VtsVtd_2s"),F_L.Get("VtsVtd_3s")]
gr_dicti["VtbVts"]["S"]=[F_S.Get("VtbVts_best"),F_S.Get("VtbVts_1s"),F_S.Get("VtbVts_2s"),F_S.Get("VtbVts_3s")]
gr_dicti["VtbVtd"]["S"]=[F_S.Get("VtbVtd_best"),F_S.Get("VtbVtd_1s"),F_S.Get("VtbVtd_2s"),F_S.Get("VtbVtd_3s")]
gr_dicti["VtsVtd"]["S"]=[F_S.Get("VtsVtd_best"),F_S.Get("VtsVtd_1s"),F_S.Get("VtsVtd_2s"),F_S.Get("VtsVtd_3s")]
for igr in gr_dicti:
    gr_L=gr_dicti[igr]["L"]
    gr_S=gr_dicti[igr]["S"]
    draw_compare(igr,gr_L, gr_S)
print "done!"
