import math
import gc
import sys
import ROOT
import numpy as np
from array import array
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gROOT.ProcessLine("gErrorIgnoreLevel = 1;")
ROOT.TH1.AddDirectory(ROOT.kFALSE)

def draw_ratio_plot(hist,hist_dict, h_nominal, h_PDF_Up, h_PDF_Down, h_Qscale_Up, h_Qscale_Down, h_PS_Up, h_PS_Down, dir_out, date, Vtx, is_top):
        canvas = ROOT.TCanvas('canvas','',10,10,1100,628)
        canvas.cd()
        pad1=ROOT.TPad("pad1", "pad1", 0, 0.415, 1, 0.99 , 0)
        pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.4 , 0)
        pad1.Draw()
        pad2.Draw()
        pad2.SetGridy()
        pad1.SetTickx()
        pad1.SetTicky()
        pad2.SetTickx()
        pad2.SetTicky()
        pad1.SetBottomMargin(0.02)
        pad1.SetLeftMargin(0.14)
        pad1.SetRightMargin(0.05)
        pad2.SetTopMargin(0.0)
        pad2.SetBottomMargin(0.3)
        pad2.SetLeftMargin(0.14)
        pad2.SetRightMargin(0.05)
        pad1.SetLogx(ROOT.kFALSE)
        pad2.SetLogx(ROOT.kFALSE)
        pad1.SetLogy(ROOT.kFALSE)
        pad1.cd()

        x_min=h_nominal.GetXaxis().GetXmin()
        x_max=h_nominal.GetXaxis().GetXmax()
        y_min=0
        y_max=2*h_nominal.GetBinContent(h_nominal.GetMaximumBin())
        xaxis_name=hist_dict[hist]
        dummy = ROOT.TH2F("dummy","",1,x_min,x_max,1,y_min,y_max)
        dummy.SetStats(ROOT.kFALSE)
        dummy.GetXaxis().SetTitle(xaxis_name)
        str_GeV=""
        if "GeV" in xaxis_name:str_GeV=" GeV"
        str_y_bin=""if h_nominal.GetBinWidth(1)!=h_nominal.GetBinWidth(h_nominal.GetNbinsX()) else " / "+str(h_nominal.GetBinWidth(1))+str_GeV
        str_y="Event"
        dummy.GetYaxis().SetTitle(str_y+str_y_bin)
        dummy.GetXaxis().SetMoreLogLabels()
        dummy.GetXaxis().SetNoExponent() 
        dummy.GetYaxis().SetTitleOffset(0.65)
        dummy.GetXaxis().SetTitleOffset(1)
        dummy.GetYaxis().SetTitleSize(0.09)
        dummy.GetXaxis().SetTitleSize(0.0)
        dummy.GetXaxis().SetLabelSize(0.0)
        dummy.GetYaxis().SetLabelSize(0.06)
        dummy.Draw()
        color_nominal=2
        color_PDF=3
        color_Qscale=4
        color_PS=6
        h_nominal    .SetLineColor(color_nominal)
        h_PDF_Up     .SetLineColor(color_PDF)
        h_PDF_Down   .SetLineColor(color_PDF)
        h_Qscale_Up  .SetLineColor(color_Qscale)
        h_Qscale_Down.SetLineColor(color_Qscale)
        h_PS_Up      .SetLineColor(color_PS)
        h_PS_Down    .SetLineColor(color_PS)
        h_nominal    .SetMarkerColor(color_nominal)
        h_PDF_Up     .SetMarkerColor(color_PDF)
        h_PDF_Down   .SetMarkerColor(color_PDF)
        h_Qscale_Up  .SetMarkerColor(color_Qscale)
        h_Qscale_Down.SetMarkerColor(color_Qscale)
        h_PS_Up      .SetMarkerColor(color_PS)
        h_PS_Down    .SetMarkerColor(color_PS)
        h_nominal    .SetLineWidth(2)
        h_PDF_Up     .SetLineWidth(2)
        h_PDF_Down   .SetLineWidth(2)
        h_Qscale_Up  .SetLineWidth(2)
        h_Qscale_Down.SetLineWidth(2)
        h_PS_Up      .SetLineWidth(2)
        h_PS_Down    .SetLineWidth(2)
        h_nominal    .SetLineStyle(1)
        h_PDF_Up     .SetLineStyle(1)
        h_PDF_Down   .SetLineStyle(2)
        h_Qscale_Up  .SetLineStyle(1)
        h_Qscale_Down.SetLineStyle(2)
        h_PS_Up      .SetLineStyle(1)
        h_PS_Down    .SetLineStyle(2)
        h_nominal    .SetMarkerStyle(8)
        h_PDF_Up     .SetMarkerStyle(8)
        h_PDF_Down   .SetMarkerStyle(8)
        h_Qscale_Up  .SetMarkerStyle(8)
        h_Qscale_Down.SetMarkerStyle(8)
        h_PS_Up      .SetMarkerStyle(8)
        h_PS_Down    .SetMarkerStyle(8)
        h_nominal    .Draw("same:pe")
        h_PDF_Up     .Draw("same:hist")
        h_PDF_Down   .Draw("same:hist")
        h_Qscale_Up  .Draw("same:hist")
        h_Qscale_Down.Draw("same:hist")
        h_PS_Up      .Draw("same:hist")
        h_PS_Down    .Draw("same:hist")
        ROOT.gStyle.SetErrorX(0)
        dummy.Draw("AXISSAME")
        legend_x_min=0.5
        legend_x_max=0.88
        legend_y_min=0.6
        legend_y_max=0.88
        legend = ROOT.TLegend(legend_x_min,legend_y_min,legend_x_max,legend_y_max)
        legend.AddEntry(h_nominal,'%s(nominal)'%(Vtx),'l')
        legend.AddEntry(h_PDF_Up,'%s(PDF Up)'%(Vtx),'l')
        legend.AddEntry(h_PDF_Down,'%s(PDF Down)'%(Vtx),'l')
        legend.AddEntry(h_Qscale_Up  ,'%s(Qscale Up)'%(Vtx),'l')
        legend.AddEntry(h_Qscale_Down,'%s(Qscale Down)'%(Vtx),'l')
        legend.AddEntry(h_PS_Up      ,'%s(PS Up)'%(Vtx),'l')
        legend.AddEntry(h_PS_Down    ,'%s(PS Down)'%(Vtx),'l')
        legend.SetBorderSize(0)
        legend.SetTextFont(42)
        legend.SetTextSize(0.05)
        legend.Draw()
        label = ROOT.TLatex()
        label.SetTextAlign(12)
        label.SetTextFont(42)
        label.SetTextSize(0.05)
        label.SetNDC(ROOT.kTRUE)
        str_top=""
        str_level='particle-level'
        if is_7TeV:
            str_level='parton-level'
        if is_top:
            label.DrawLatex(0.22,0.80, '#it{tq} %s'%str_level)
            str_top="top"
        else:
            label.DrawLatex(0.22,0.80, "#it{#bar{t}q} %s"%str_level)
            str_top="atop"
        label.Draw()
        pad2.cd()
        r_y_min=0.95
        r_y_max=1.05
        #if Vtx=="Vtb":
        #    r_y_min=0.9
        #    r_y_max=1.1
        dummy_ratio = ROOT.TH2F("dummy_ratio","",1,x_min,x_max,1,r_y_min,r_y_max)
        dummy_ratio.SetStats(ROOT.kFALSE)
        dummy_ratio.GetXaxis().SetTitle(xaxis_name)
        dummy_ratio.GetYaxis().SetTitle("Scale/Nominal")
        dummy_ratio.GetYaxis().CenterTitle()
        dummy_ratio.GetXaxis().SetMoreLogLabels()
        dummy_ratio.GetXaxis().SetNoExponent() 
        dummy_ratio.GetYaxis().SetTitleOffset(0.6)
        dummy_ratio.GetXaxis().SetTitleOffset(1.1)
        dummy_ratio.GetYaxis().SetTitleSize(0.1)
        dummy_ratio.GetXaxis().SetTitleSize(0.1)
        dummy_ratio.GetXaxis().SetLabelSize(0.08)
        dummy_ratio.GetYaxis().SetLabelSize(0.08)
        dummy_ratio.Draw()
        ratio_PDF_Up=h_PDF_Up.Clone("ratio_PDF_Up")
        ratio_PDF_Up.Divide(h_nominal)
        ratio_PDF_Down=h_PDF_Down.Clone("ratio_PDF_Down")
        ratio_PDF_Down.Divide(h_nominal)
        ratio_Qscale_Up=h_Qscale_Up.Clone("ratio_Qscale_Up")
        ratio_Qscale_Up.Divide(h_nominal)
        ratio_Qscale_Down=h_Qscale_Down.Clone("ratio_Qscale_Down")
        ratio_Qscale_Down.Divide(h_nominal)
        ratio_PS_Up=h_PS_Up.Clone("ratio_PS_Up")
        ratio_PS_Up.Divide(h_nominal)
        ratio_PS_Down=h_PS_Down.Clone("ratio_PS_Down")
        ratio_PS_Down.Divide(h_nominal)
        ratio_PDF_Up.Draw("same:hist")
        ratio_PDF_Down.Draw("same:hist")
        ratio_Qscale_Up.Draw("same:hist")
        ratio_Qscale_Down.Draw("same:hist")
        ratio_PS_Up.Draw("same:hist")
        ratio_PS_Down.Draw("same:hist")
        dummy_ratio.Draw("AXISSAME")
        
        canvas.Print('%s/%s/%s_%s_%s.png'%(dir_out,date,Vtx,str_top,hist))    
        canvas.Print('%s/%s/%s_%s_%s.pdf'%(dir_out,date,Vtx,str_top,hist))    
        del canvas
        gc.collect()

################# BEGIN ###############
is_7TeV=False

#dir_in="./ntuple/Reza_final_8TeV/"
dir_in="./ntuple/Reza_8TeV_notau_lastbin/"
if is_7TeV:
    dir_in="./ntuple/Reza_7TeV_lastbin/"
dir_out="./uncert_plots"
date="20171003"

F_Vtb_top_nominal     =ROOT.TFile()
F_Vtb_top_PDF_Up      =ROOT.TFile()
F_Vtb_top_PDF_Down    =ROOT.TFile()
F_Vtb_top_Qscale_Up   =ROOT.TFile()
F_Vtb_top_Qscale_Down =ROOT.TFile()
F_Vtb_top_PS_Up       =ROOT.TFile()
F_Vtb_top_PS_Down     =ROOT.TFile()
F_Vtb_atop_nominal    =ROOT.TFile()
F_Vtb_atop_PDF_Up     =ROOT.TFile()
F_Vtb_atop_PDF_Down   =ROOT.TFile()
F_Vtb_atop_Qscale_Up  =ROOT.TFile()
F_Vtb_atop_Qscale_Down=ROOT.TFile()
F_Vtb_atop_PS_Up      =ROOT.TFile()
F_Vtb_atop_PS_Down    =ROOT.TFile()
if is_7TeV==False:
    F_Vtb_top_nominal     =ROOT.TFile(dir_in+"hist_Vtb_top_nominal.root"       ,"read")
    F_Vtb_top_PDF_Up      =ROOT.TFile(dir_in+"hist_Vtb_top_PDFUp.root"         ,"read")
    F_Vtb_top_PDF_Down    =ROOT.TFile(dir_in+"hist_Vtb_top_PDFDown.root"       ,"read")
    F_Vtb_top_Qscale_Up   =ROOT.TFile(dir_in+"hist_Vtb_top_QScaleUp.root"      ,"read")
    F_Vtb_top_Qscale_Down =ROOT.TFile(dir_in+"hist_Vtb_top_QScaleDown.root"    ,"read")
    F_Vtb_top_PS_Up       =ROOT.TFile(dir_in+"hist_Vtb_top_PS_Up.root"         ,"read")
    F_Vtb_top_PS_Down     =ROOT.TFile(dir_in+"hist_Vtb_top_PS_Down.root"       ,"read")
    F_Vtb_atop_nominal    =ROOT.TFile(dir_in+"hist_Vtb_antitop_nominal.root"   ,"read")
    F_Vtb_atop_PDF_Up     =ROOT.TFile(dir_in+"hist_Vtb_antitop_PDFUp.root"     ,"read")
    F_Vtb_atop_PDF_Down   =ROOT.TFile(dir_in+"hist_Vtb_antitop_PDFDown.root"   ,"read")
    F_Vtb_atop_Qscale_Up  =ROOT.TFile(dir_in+"hist_Vtb_antitop_QScaleUp.root"  ,"read")
    F_Vtb_atop_Qscale_Down=ROOT.TFile(dir_in+"hist_Vtb_antitop_QScaleDown.root","read")
    F_Vtb_atop_PS_Up      =ROOT.TFile(dir_in+"hist_Vtb_antitop_PS_Up.root"     ,"read")
    F_Vtb_atop_PS_Down    =ROOT.TFile(dir_in+"hist_Vtb_antitop_PS_Down.root"   ,"read")



F_Vts_top_nominal     =ROOT.TFile(dir_in+"hist_Vts_top_nominal.root"       ,"read")
F_Vts_top_PDF_Up      =ROOT.TFile(dir_in+"hist_Vts_top_PDFUp.root"         ,"read")
F_Vts_top_PDF_Down    =ROOT.TFile(dir_in+"hist_Vts_top_PDFDown.root"       ,"read")
F_Vts_top_Qscale_Up   =ROOT.TFile(dir_in+"hist_Vts_top_QScaleUp.root"      ,"read")
F_Vts_top_Qscale_Down =ROOT.TFile(dir_in+"hist_Vts_top_QScaleDown.root"    ,"read")
F_Vts_top_PS_Up       =ROOT.TFile(dir_in+"hist_Vts_top_PS_Up.root"         ,"read")
F_Vts_top_PS_Down     =ROOT.TFile(dir_in+"hist_Vts_top_PS_Down.root"       ,"read")
F_Vts_atop_nominal    =ROOT.TFile(dir_in+"hist_Vts_antitop_nominal.root"   ,"read")
F_Vts_atop_PDF_Up     =ROOT.TFile(dir_in+"hist_Vts_antitop_PDFUp.root"     ,"read")
F_Vts_atop_PDF_Down   =ROOT.TFile(dir_in+"hist_Vts_antitop_PDFDown.root"   ,"read")
F_Vts_atop_Qscale_Up  =ROOT.TFile(dir_in+"hist_Vts_antitop_QScaleUp.root"  ,"read")
F_Vts_atop_Qscale_Down=ROOT.TFile(dir_in+"hist_Vts_antitop_QScaleDown.root","read")
F_Vts_atop_PS_Up      =ROOT.TFile(dir_in+"hist_Vts_antitop_PS_Up.root"     ,"read")
F_Vts_atop_PS_Down    =ROOT.TFile(dir_in+"hist_Vts_antitop_PS_Down.root"   ,"read")

F_Vtd_top_nominal     =ROOT.TFile(dir_in+"hist_Vtd_top_nominal.root"       ,"read")
F_Vtd_top_PDF_Up      =ROOT.TFile(dir_in+"hist_Vtd_top_PDFUp.root"         ,"read")
F_Vtd_top_PDF_Down    =ROOT.TFile(dir_in+"hist_Vtd_top_PDFDown.root"       ,"read")
F_Vtd_top_Qscale_Up   =ROOT.TFile(dir_in+"hist_Vtd_top_QScaleUp.root"      ,"read")
F_Vtd_top_Qscale_Down =ROOT.TFile(dir_in+"hist_Vtd_top_QScaleDown.root"    ,"read")
F_Vtd_top_PS_Up       =ROOT.TFile(dir_in+"hist_Vtd_top_PS_Up.root"         ,"read")
F_Vtd_top_PS_Down     =ROOT.TFile(dir_in+"hist_Vtd_top_PS_Down.root"       ,"read")
F_Vtd_atop_nominal    =ROOT.TFile(dir_in+"hist_Vtd_antitop_nominal.root"   ,"read")
F_Vtd_atop_PDF_Up     =ROOT.TFile(dir_in+"hist_Vtd_antitop_PDFUp.root"     ,"read")
F_Vtd_atop_PDF_Down   =ROOT.TFile(dir_in+"hist_Vtd_antitop_PDFDown.root"   ,"read")
F_Vtd_atop_Qscale_Up  =ROOT.TFile(dir_in+"hist_Vtd_antitop_QScaleUp.root"  ,"read")
F_Vtd_atop_Qscale_Down=ROOT.TFile(dir_in+"hist_Vtd_antitop_QScaleDown.root","read")
F_Vtd_atop_PS_Up      =ROOT.TFile(dir_in+"hist_Vtd_antitop_PS_Up.root"     ,"read")
F_Vtd_atop_PS_Down    =ROOT.TFile(dir_in+"hist_Vtd_antitop_PS_Down.root"   ,"read")


hist_dict={
"H_lep_pt"          :"P_{T}(Lepton) (GeV)",
"H_lep_eta"         :"#eta(Lepton)",
"H_lep_phi"         :"#phi(Lepton)",
"H_lep_Rap"         :"|y|(Lepton)",
"H_bjet_pt"         :"P_{T}(b-jet) (GeV)",
"H_bjet_eta"        :"#eta(b-jet)",
"H_bjet_phi"        :"#phi(b-jet)",
"H_bjet_Rap"        :"|y|(b-jet)",
"H_Nu_pt"           :"P_{T}(Nu) (GeV)",
"H_Nu_eta"          :"#eta(Nu)",
"H_Nu_phi"          :"#phi(Nu)",
"H_Nu_Rap"          :"|y|(Nu)",
"H_W_pt"            :"P_{T}(W) (GeV)",
"H_W_eta"           :"#eta(W)",
"H_W_phi"           :"#phi(W)",
"H_W_Rap"           :"|y|(W)",
"H_W_mass"          :"M(W) (GeV)",
"H_top_pt"          :"P_{T}(t) (GeV)",
"H_top_pt_fine"     :"P_{T}(t) (GeV)",
"H_top_eta"         :"#eta(t)",
"H_top_phi"         :"#phi(t)",
"H_top_Rap"         :"|y|(t)",
"H_top_Rap_fine"    :"|y|(t)",
"H_top_mass"        :"M(t) (GeV)",
"H_atop_pt"         :"P_{T}(t) (GeV)",
"H_atop_pt_fine"    :"P_{T}(t) (GeV)",
"H_atop_eta"        :"#eta(t)",
"H_atop_phi"        :"#phi(t)",
"H_atop_Rap"        :"|y|(t)",
"H_atop_Rap_fine"   :"|y|(t)",
"H_atop_mass"       :"M(t) (GeV)",
"H_top_jet_pt"          :"P_{T}(j) (GeV)",
"H_top_jet_pt_fine"     :"P_{T}(j) (GeV)",
"H_top_jet_eta"         :"#eta(j)",
"H_top_jet_phi"         :"#phi(j)",
"H_top_jet_Rap"         :"|y|(j)",
"H_top_jet_Rap_fine"    :"|y|(j)",
"H_atop_jet_pt"      :"P_{T}(j) (GeV)",
"H_atop_jet_pt_fine" :"P_{T}(j) (GeV)",
"H_atop_jet_eta"     :"#eta(j)",
"H_atop_jet_phi"     :"#phi(j)",
"H_atop_jet_Rap"     :"|y|(j)",
"H_atop_jet_Rap_fine":"|y|(j)",
"H_MET_pt"          :"P_{T}(MET) (GeV)",
"H_MET_phi"         :"#phi(MET)",
"H_DR_lep_Nu"       :"#DeltaR(lepton,Nu)",
"H_DR_W_bjet"       :"#DeltaR(W,b-jet)"
}
if is_7TeV:
    hist_dict={
    "H_top_pt"          :"P_{T}(t) (GeV)",
    "H_top_pt_fine"     :"P_{T}(t) (GeV)",
    "H_top_eta"         :"#eta(t)",
    "H_top_phi"         :"#phi(t)",
    "H_top_Rap"         :"|y|(t)",
    "H_top_Rap_fine"    :"|y|(t)",
    "H_top_mass"        :"M(t) (GeV)",
    "H_atop_pt"         :"P_{T}(t) (GeV)",
    "H_atop_pt_fine"    :"P_{T}(t) (GeV)",
    "H_atop_eta"        :"#eta(t)",
    "H_atop_phi"        :"#phi(t)",
    "H_atop_Rap"        :"|y|(t)",
    "H_atop_Rap_fine"   :"|y|(t)",
    "H_atop_mass"       :"M(t) (GeV)",
    }

hist_list=["H_top_pt_fine","H_top_Rap_fine","H_top_jet_pt_fine","H_top_jet_Rap_fine","H_atop_pt_fine","H_atop_Rap_fine","H_atop_jet_pt_fine","H_atop_jet_Rap_fine"]
if is_7TeV:
    hist_list=["H_top_pt_fine","H_top_Rap_fine","H_atop_pt_fine","H_atop_Rap_fine"]
sys_uncert={}
vtx_list=["Vts","Vtd","Vtb"]
if is_7TeV:
    vtx_list=["Vts","Vtd"]
for Vtx in vtx_list:
    sys_uncert[Vtx]={}
    for is_top in [True,False]:
        for hist in hist_dict: 
            if is_top and "atop" in hist:continue
            elif is_top==False and "_top" in hist:continue
            h_nominal    =ROOT.TH1D() 
            h_PDF_Up     =ROOT.TH1D() 
            h_PDF_Down   =ROOT.TH1D() 
            h_Qscale_Up  =ROOT.TH1D() 
            h_Qscale_Down=ROOT.TH1D() 
            h_PS_Up      =ROOT.TH1D() 
            h_PS_Down    =ROOT.TH1D() 
            if Vtx== "Vts" and is_top==True :
                h_nominal    =F_Vts_top_nominal    .Get(hist) 
                h_PDF_Up     =F_Vts_top_PDF_Up     .Get(hist) 
                h_PDF_Down   =F_Vts_top_PDF_Down   .Get(hist) 
                h_Qscale_Up  =F_Vts_top_Qscale_Up  .Get(hist) 
                h_Qscale_Down=F_Vts_top_Qscale_Down.Get(hist) 
                h_PS_Up      =F_Vts_top_PS_Up      .Get(hist) 
                h_PS_Down    =F_Vts_top_PS_Down    .Get(hist) 
            elif Vtx== "Vts" and is_top==False :
                h_nominal    =F_Vts_atop_nominal    .Get(hist) 
                h_PDF_Up     =F_Vts_atop_PDF_Up     .Get(hist) 
                h_PDF_Down   =F_Vts_atop_PDF_Down   .Get(hist) 
                h_Qscale_Up  =F_Vts_atop_Qscale_Up  .Get(hist) 
                h_Qscale_Down=F_Vts_atop_Qscale_Down.Get(hist) 
                h_PS_Up      =F_Vts_atop_PS_Up      .Get(hist) 
                h_PS_Down    =F_Vts_atop_PS_Down    .Get(hist) 
            elif Vtx== "Vtd" and is_top==True :
                h_nominal    =F_Vtd_top_nominal    .Get(hist) 
                h_PDF_Up     =F_Vtd_top_PDF_Up     .Get(hist) 
                h_PDF_Down   =F_Vtd_top_PDF_Down   .Get(hist) 
                h_Qscale_Up  =F_Vtd_top_Qscale_Up  .Get(hist) 
                h_Qscale_Down=F_Vtd_top_Qscale_Down.Get(hist) 
                h_PS_Up      =F_Vtd_top_PS_Up      .Get(hist) 
                h_PS_Down    =F_Vtd_top_PS_Down    .Get(hist) 
            elif Vtx== "Vtd" and is_top==False :
                h_nominal    =F_Vtd_atop_nominal    .Get(hist) 
                h_PDF_Up     =F_Vtd_atop_PDF_Up     .Get(hist) 
                h_PDF_Down   =F_Vtd_atop_PDF_Down   .Get(hist) 
                h_Qscale_Up  =F_Vtd_atop_Qscale_Up  .Get(hist) 
                h_Qscale_Down=F_Vtd_atop_Qscale_Down.Get(hist) 
                h_PS_Up      =F_Vtd_atop_PS_Up      .Get(hist) 
                h_PS_Down    =F_Vtd_atop_PS_Down    .Get(hist) 
            elif Vtx== "Vtb" and is_top==True :
                h_nominal    =F_Vtb_top_nominal    .Get(hist) 
                h_PDF_Up     =F_Vtb_top_PDF_Up     .Get(hist) 
                h_PDF_Down   =F_Vtb_top_PDF_Down   .Get(hist) 
                h_Qscale_Up  =F_Vtb_top_Qscale_Up  .Get(hist) 
                h_Qscale_Down=F_Vtb_top_Qscale_Down.Get(hist) 
                h_PS_Up      =F_Vtb_top_PS_Up      .Get(hist) 
                h_PS_Down    =F_Vtb_top_PS_Down    .Get(hist) 
            elif Vtx== "Vtb" and is_top==False :
                h_nominal    =F_Vtb_atop_nominal    .Get(hist) 
                h_PDF_Up     =F_Vtb_atop_PDF_Up     .Get(hist) 
                h_PDF_Down   =F_Vtb_atop_PDF_Down   .Get(hist) 
                h_Qscale_Up  =F_Vtb_atop_Qscale_Up  .Get(hist) 
                h_Qscale_Down=F_Vtb_atop_Qscale_Down.Get(hist) 
                h_PS_Up      =F_Vtb_atop_PS_Up      .Get(hist) 
                h_PS_Down    =F_Vtb_atop_PS_Down    .Get(hist) 
            draw_ratio_plot(hist,hist_dict, h_nominal, h_PDF_Up, h_PDF_Down, h_Qscale_Up, h_Qscale_Down, h_PS_Up, h_PS_Down, dir_out, date, Vtx, is_top)
            if hist in hist_list:
                sys_uncert[Vtx][hist]=[]
                for ibin in range(1,h_nominal.GetNbinsX()+1):
                    diff_PDF=math.fabs(h_nominal.GetBinContent(ibin)-h_PDF_Up.GetBinContent(ibin)) if math.fabs(h_nominal.GetBinContent(ibin)-h_PDF_Up.GetBinContent(ibin))>math.fabs(h_nominal.GetBinContent(ibin)-h_PDF_Down.GetBinContent(ibin)) else math.fabs(h_nominal.GetBinContent(ibin)-h_PDF_Down.GetBinContent(ibin)) ##Here the effective number of event for sys sample is the same with nominal one, so no scale is needed
                    diff_Qscale=math.fabs(h_nominal.GetBinContent(ibin)-h_Qscale_Up.GetBinContent(ibin)) if math.fabs(h_nominal.GetBinContent(ibin)-h_Qscale_Up.GetBinContent(ibin))>math.fabs(h_nominal.GetBinContent(ibin)-h_Qscale_Down.GetBinContent(ibin)) else math.fabs(h_nominal.GetBinContent(ibin)-h_Qscale_Down.GetBinContent(ibin))
                    diff_PS=math.fabs(h_nominal.GetBinContent(ibin)-h_PS_Up.GetBinContent(ibin)) if math.fabs(h_nominal.GetBinContent(ibin)-h_PS_Up.GetBinContent(ibin))>math.fabs(h_nominal.GetBinContent(ibin)-h_PS_Down.GetBinContent(ibin)) else math.fabs(h_nominal.GetBinContent(ibin)-h_PS_Down.GetBinContent(ibin))
                    value=math.sqrt(math.pow(diff_PDF,2)+math.pow(diff_Qscale,2)+math.pow(diff_PS,2))/h_nominal.GetBinContent(ibin)
                    sys_uncert[Vtx][hist].append(value)
print sys_uncert
sys_uncert_final={}
for Vtx in vtx_list:
    sys_uncert_final[Vtx]=[]
    for hist in hist_list:
        if hist in sys_uncert[Vtx]:
            for iv in sys_uncert[Vtx][hist]:
                sys_uncert_final[Vtx].append(iv)
        else:print "wrong name %s"%hist

print sys_uncert_final
