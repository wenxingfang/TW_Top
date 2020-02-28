import math
import gc
import sys
import ROOT
import numpy as np
from array import array
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gROOT.ProcessLine("gErrorIgnoreLevel = 1;")
ROOT.TH1.AddDirectory(ROOT.kFALSE)

def draw_ratio_plot(hist,hist_dict, h_Vtb, h_Vts, h_Vtd, dir_out, date):
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

        x_min=h_Vtb.GetXaxis().GetXmin()
        x_max=h_Vtb.GetXaxis().GetXmax()
        y_min=0
        y_max=2*h_Vtb.GetBinContent(h_Vtb.GetMaximumBin())
        xaxis_name=hist_dict[hist]
        dummy = ROOT.TH2F("dummy","",1,x_min,x_max,1,y_min,y_max)
        dummy.SetStats(ROOT.kFALSE)
        dummy.GetXaxis().SetTitle(xaxis_name)
        dummy.GetYaxis().SetTitle("Fraction")
        dummy.GetXaxis().SetMoreLogLabels()
        dummy.GetXaxis().SetNoExponent() 
        dummy.GetYaxis().SetTitleOffset(0.65)
        dummy.GetXaxis().SetTitleOffset(1)
        dummy.GetYaxis().SetTitleSize(0.09)
        dummy.GetXaxis().SetTitleSize(0.0)
        dummy.GetXaxis().SetLabelSize(0.0)
        dummy.GetYaxis().SetLabelSize(0.06)
        dummy.Draw()
        color_Vtb=4
        color_Vts=2
        color_Vtd=3
        h_Vtb.SetLineColor(color_Vtb)
        h_Vts.SetLineColor(color_Vts)
        h_Vtd.SetLineColor(color_Vtd)
        h_Vtb.SetLineWidth(2)
        h_Vts.SetLineWidth(2)
        h_Vtd.SetLineWidth(2)
        h_Vtb.SetMarkerStyle(8)
        h_Vts.SetMarkerStyle(8)
        h_Vtd.SetMarkerStyle(8)
        h_Vtb.SetMarkerColor(color_Vtb)
        h_Vts.SetMarkerColor(color_Vts)
        h_Vtd.SetMarkerColor(color_Vtd)
        h_Vtb.Draw("same:hist")
        h_Vts.Draw("same:hist")
        h_Vtd.Draw("same:hist")
        ROOT.gStyle.SetErrorX(0)
        dummy.Draw("AXISSAME")
        legend_x_min=0.5
        legend_x_max=0.88
        legend_y_min=0.6
        legend_y_max=0.88
        legend = ROOT.TLegend(legend_x_min,legend_y_min,legend_x_max,legend_y_max)
        legend.AddEntry(h_Vtb,'Vtb(MG5@LO)','l')
        legend.AddEntry(h_Vts,'Vts(MG5@LO)','l')
        legend.AddEntry(h_Vtd,'Vtd(MG5@LO)','l')
        legend.SetBorderSize(0)
        legend.SetTextFont(42)
        legend.SetTextSize(0.05)
        legend.Draw()
        label = ROOT.TLatex()
        label.SetTextAlign(12)
        label.SetTextFont(42)
        label.SetTextSize(0.05)
        label.SetNDC(ROOT.kTRUE)
        str_level="LHE-level"
        label.DrawLatex(0.22,0.80, "%s"%str_level)
        label.Draw()
        pad2.cd()
        dummy_ratio = ROOT.TH2F("dummy_ratio","",1,x_min,x_max,1,0,2)
        dummy_ratio.SetStats(ROOT.kFALSE)
        dummy_ratio.GetXaxis().SetTitle(xaxis_name)
        dummy_ratio.GetYaxis().SetTitle("ratio")
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
        ratio_Vts=h_Vts.Clone("ratio_Vts")
        ratio_Vts.Divide(h_Vtb)
        ratio_Vtd=h_Vtd.Clone("ratio_Vtd")
        ratio_Vtd.Divide(h_Vtb)
        ratio_Vts.Draw("hist:same")
        ratio_Vtd.Draw("hist:same")
        dummy_ratio.Draw("AXISSAME")
        canvas.Print('%s/%s/%s.png'%(dir_out,date,hist))    
        canvas.Print('%s/%s/%s.pdf'%(dir_out,date,hist))    
        del canvas
        gc.collect()

hist_dict={
"H_lp_pt":"P_{T}(l^{+}) (GeV)",	
"H_lp_pt_fine":"P_{T}(l^{+}) (GeV)",	
"H_lp_eta":"#eta(l^{+})",	
"H_lp_phi":"#phi(l^{+})",	
"H_lp_Rap":"|y|(l^{+})",	
"H_lp_Rap_fine":"|y|(l^{+})",	
"H_lm_pt":"P_{T}(l^{-}) (GeV)",	
"H_lm_pt_fine":"P_{T}(l^{-}) (GeV)",	
"H_lm_eta":"#eta(l^{-})",	
"H_lm_phi":"#phi(l^{-})",	
"H_lm_Rap":"|y|(l^{-})",	
"H_lm_Rap_fine":"|y|(l^{-})",	
"H_bjet_pt":"P_{T}(b) (GeV)",	
"H_bjet_pt_fine":"P_{T}(b) (GeV)",	
"H_bjet_eta":"#eta(b)",	
"H_bjet_phi":"#phi(b)",	
"H_bjet_Rap":"|y|(b)",	
"H_bjet_Rap_fine":"|y|(b)",	
"H_MET_pt":"P_{T}(MET) (GeV)",	
"H_MET_phi":"#phi(MET)",	
"H_DR_ll":"#DeltaR(l^{+},l^{-})"
}
dir_in="./ntuple/Reza_final_tW_13TeV/"
dir_out="./tW_13TeV_plot/"
date="20171018"
f_Vtb=ROOT.TFile(dir_in+"hist_Vtb.root","read")
f_Vts=ROOT.TFile(dir_in+"hist_Vts.root","read")
f_Vtd=ROOT.TFile(dir_in+"hist_Vtd.root","read")

for hist in hist_dict:
    h_Vtb=f_Vtb.Get(hist)
    h_Vts=f_Vts.Get(hist)
    h_Vtd=f_Vtd.Get(hist)
#    h_Vtb.Sumw2(ROOT.kTRUE)
#    h_Vts.Sumw2(ROOT.kTRUE)
#    h_Vtd.Sumw2(ROOT.kTRUE)
    
    if True:
        h_Vtb.Scale(1/h_Vtb.GetSumOfWeights())
        h_Vts.Scale(1/h_Vts.GetSumOfWeights())
        h_Vtd.Scale(1/h_Vtd.GetSumOfWeights())
        
    draw_ratio_plot(hist,hist_dict, h_Vtb, h_Vts, h_Vtd, dir_out, date)
print "done!"
