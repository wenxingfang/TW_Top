#!/usr/bin/env python
import ROOT
import re
from array import array
ROOT.gROOT.SetBatch(ROOT.kTRUE)

def add_lumi():
    lowX=0.58
    lowY=0.835
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.30, lowY+0.16, "NDC")
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.SetTextSize(0.06)
    lumi.SetTextFont (   42 )
    lumi.AddText("2016, 35.9 fb^{-1} (13 TeV)")
    return lumi

def add_CMS():
    lowX=0.21
    lowY=0.70
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    lumi.SetTextFont(61)
    lumi.SetTextSize(0.06)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.AddText("CMS")
    return lumi

def add_Preliminary():
    lowX=0.21
    lowY=0.63
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    lumi.SetTextFont(52)
    lumi.SetTextSize(0.06)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.AddText("Preliminary")
    return lumi

def make_legend():
        output = ROOT.TLegend(0.40, 0.60, 0.92, 0.85, "", "brNDC")
        #output = ROOT.TLegend(0.2, 0.1, 0.47, 0.65, "", "brNDC")
        output.SetLineWidth(0)
        output.SetLineStyle(0)
        output.SetFillStyle(0)
        output.SetBorderSize(0)
        output.SetTextFont(62)
        return output

ROOT.gStyle.SetFrameLineWidth(3)
ROOT.gStyle.SetLineWidth(3)
ROOT.gStyle.SetOptStat(0)

c=ROOT.TCanvas("canvas","",0,0,600,600)
c.cd()

is_obs=True
str_obs="_obs"
if is_obs==False:
    str_obs="_exp"
file=None
if is_obs:
    file=ROOT.TFile("./output/ee_emu_mumu_card.root/bplus_s/obs/fit_shapes.root","r")
else:
    file=ROOT.TFile("./output/ee_emu_mumu_card.root/bplus_s/exp/fit_shapes.root","r")

#new_idx=ROOT.gROOT.GetListOfColors().GetSize() + 1
#adapt=ROOT.gROOT.GetColor(12)
#trans=ROOT.TColor(new_idx, adapt.GetRed(), adapt.GetGreen(),adapt.GetBlue(), "",0.5)

categories={}
categories["Name1_Name1_prefit"]  =[5,"ee_1j1t_prefit"] 
categories["Name1_Name2_prefit"]  =[6,"ee_2j1t_prefit"]
categories["Name1_Name3_prefit"]  =[1,"ee_2j2t_prefit"]
categories["Name2_Name1_prefit"]  =[5,"emu_1j0t_prefit"]
categories["Name2_Name2_prefit"]  =[5,"emu_1j1t_prefit"]
categories["Name2_Name3_prefit"]  =[6,"emu_2j1t_prefit"]
categories["Name2_Name4_prefit"]  =[1,"emu_2j2t_prefit"]
categories["Name3_Name1_prefit"]  =[5,"mumu_1j1t_prefit"]
categories["Name3_Name2_prefit"]  =[6,"mumu_2j1t_prefit"]
categories["Name3_Name3_prefit"]  =[1,"mumu_2j2t_prefit"]
categories["Name1_Name1_postfit"] =[5,"ee_1j1t_postfit"]
categories["Name1_Name2_postfit"] =[6,"ee_2j1t_postfit"]
categories["Name1_Name3_postfit"] =[1,"ee_2j2t_postfit"]
categories["Name2_Name1_postfit"] =[5,"emu_1j0t_postfit"]
categories["Name2_Name2_postfit"] =[5,"emu_1j1t_postfit"]
categories["Name2_Name3_postfit"] =[6,"emu_2j1t_postfit"]
categories["Name2_Name4_postfit"] =[1,"emu_2j2t_postfit"]
categories["Name3_Name1_postfit"] =[5,"mumu_1j1t_postfit"]
categories["Name3_Name2_postfit"] =[6,"mumu_2j1t_postfit"]
categories["Name3_Name3_postfit"] =[1,"mumu_2j2t_postfit"]






for i in categories:
   Data =file.Get(i).Get("data_obs")
   other=file.Get(i).Get("other")
   TW   =file.Get(i).Get("TW")
   DY   =file.Get(i).Get("DY")
   TT   =file.Get(i).Get("TT")
   jets =file.Get(i).Get("jets")

#   Data.GetXaxis().SetTitle("")
#   Data.GetXaxis().SetTitleSize(0)
#   Data.GetXaxis().SetNdivisions(505)
#   Data.GetYaxis().SetLabelFont(42)
#   Data.GetYaxis().SetLabelOffset(0.01)
#   Data.GetYaxis().SetLabelSize(0.06)
#   Data.GetYaxis().SetTitleSize(0.075)
#   Data.GetYaxis().SetTitleOffset(1.04)
#   Data.SetTitle("")
#   Data.GetYaxis().SetTitle("Events/bin")


   TW.SetFillColor(ROOT.TColor.GetColor("#efe7ae"))
   other.SetFillColor(ROOT.TColor.GetColor("#11e7ae"))
   jets.SetFillColor(ROOT.TColor.GetColor("#a278aa"))
   DY.SetFillColor(ROOT.TColor.GetColor("#4567f1"))
   TT.SetFillColor(ROOT.TColor.GetColor("#cc0000"))

   Data.SetMarkerStyle(20)
   Data.SetLineColor(1)
   Data.SetMarkerSize(1)
   jets.SetLineColor(1)
   TT.SetLineColor(1)
   TW.SetLineColor(1)
   DY.SetLineColor(1)
   other.SetLineColor(1)

   errorBand=file.Get(i).Get("jets").Clone()
   errorBand.Add(other)
   errorBand.Add(DY)
   errorBand.Add(TT)
   errorBand.Add(TW)

   stack=ROOT.THStack("stack","stack")
   stack.Add(jets)
   stack.Add(other)
   stack.Add(DY)
   stack.Add(TT)
   stack.Add(TW)

   errorBand.SetMarkerSize(0)
   errorBand.SetFillColor(ROOT.TColor.GetColor("#87919b"))
   errorBand.SetFillStyle(3001)
   errorBand.SetLineWidth(1)




   pad1 = ROOT.TPad("pad1","pad1",0,0.35,1,1)
   pad1.Draw()
   pad1.cd()
   pad1.SetFillColor(0)
   pad1.SetBorderMode(0)
   pad1.SetBorderSize(10)
   pad1.SetTickx(1)
   pad1.SetTicky(1)
   pad1.SetLeftMargin(0.18)
   pad1.SetRightMargin(0.05)
   pad1.SetTopMargin(0.122)
   pad1.SetBottomMargin(0.026)
   pad1.SetFrameFillStyle(0)
   pad1.SetFrameLineStyle(0)
   pad1.SetFrameLineWidth(3)
   pad1.SetFrameBorderMode(0)
   pad1.SetFrameBorderSize(10)

   x_min=0
   x_max=categories[i][0]
   y_min=0
   y_max=1.8*Data.GetMaximum()
   dummy=ROOT.TH2F("dummy_%s"%(i),"",1,x_min,x_max,1,y_min,y_max)   
   dummy.GetXaxis().SetTitle("")
   dummy.GetXaxis().SetTitleSize(0)
   dummy.GetXaxis().SetNdivisions(505)
   dummy.GetYaxis().SetLabelFont(42)
   dummy.GetYaxis().SetLabelOffset(0.01)
   dummy.GetYaxis().SetLabelSize(0.06)
   dummy.GetYaxis().SetTitleSize(0.075)
   dummy.GetYaxis().SetTitleOffset(1.04)
   dummy.SetTitle("")
   dummy.GetYaxis().SetTitle("Events/bin")
   dummy.GetXaxis().SetLabelSize(0)
   dummy.Draw()
   stack.Draw("histsame")
   errorBand.Draw("e2same")
   if is_obs:
       Data.Draw("pesame")
   dummy.Draw("AXISsame")

   legende=make_legend()
   legende.SetNColumns(3)
   if is_obs:
       legende.AddEntry(Data,"Observed","elp")
   legende.AddEntry(TT,"TT","f")
   legende.AddEntry(TW,"TW","f")
   legende.AddEntry(DY,"DY","f")
   legende.AddEntry(jets,"jets","f")
   legende.AddEntry(other,"other","f")
   legende.AddEntry(errorBand,"Uncertainty","f")
   legende.Draw()

   l1=add_lumi()
   l1.Draw("same")
   l2=add_CMS()
   l2.Draw("same")
   l3=add_Preliminary()
   l3.Draw("same")
 
   pad1.RedrawAxis()

   categ  = ROOT.TPaveText(0.21, 0.5+0.013, 0.43, 0.70+0.155, "NDC")
   categ.SetBorderSize(   0 )
   categ.SetFillStyle(    0 )
   categ.SetTextAlign(   12 )
   categ.SetTextSize ( 0.06 )
   categ.SetTextColor(    1 )
   categ.SetTextFont (   42 )
   if "prefit" in i:
     categ.AddText("Prefit")
   elif "postfit" in i:
     categ.AddText("Postfit")
   
   categ.Draw()

   c.cd()
   pad2 = ROOT.TPad("pad2","pad2",0,0,1,0.35);
   pad2.SetTopMargin(0.05);
   pad2.SetBottomMargin(0.35);
   pad2.SetLeftMargin(0.18);
   pad2.SetRightMargin(0.05);
   pad2.SetTickx(1)
   pad2.SetTicky(1)
   pad2.SetFrameLineWidth(3)
   pad2.SetGridx()
   pad2.SetGridy()
   pad2.Draw()
   pad2.cd()
   y_ratio_min=0.8
   y_ratio_max=1.2
   dummy_ratio=ROOT.TH2F("ratio_%s"%(i),"",1,x_min,x_max,1,y_ratio_min,y_ratio_max)   

   h1=Data.Clone()
   h1.SetMarkerStyle(20)
   h3=errorBand.Clone()
   hwoE=errorBand.Clone()
   for iii in range (1,hwoE.GetNbinsX()+1):
     hwoE.SetBinError(iii,0)
   h3.Sumw2()
   h1.Sumw2()
   h1.SetStats(0)
   h1.Divide(hwoE)
   h3.Divide(hwoE)
   dummy_ratio.SetTitle("")
   dummy_ratio.GetXaxis().SetTitle("NN output")
   dummy_ratio.GetXaxis().SetLabelSize(0.08)
   dummy_ratio.GetYaxis().SetLabelSize(0.08)
   dummy_ratio.GetYaxis().SetTitle("Data/Pred.")
   dummy_ratio.GetXaxis().SetNdivisions(505)
   dummy_ratio.GetYaxis().SetNdivisions(5)
   dummy_ratio.GetXaxis().SetTitleSize(0.15)
   dummy_ratio.GetYaxis().SetTitleSize(0.15)
   dummy_ratio.GetYaxis().SetTitleOffset(0.56)
   dummy_ratio.GetXaxis().SetTitleOffset(1.04)
   dummy_ratio.GetXaxis().SetLabelSize(0.11)
   dummy_ratio.GetYaxis().SetLabelSize(0.11)
   dummy_ratio.GetXaxis().SetTitleFont(42)
   dummy_ratio.GetYaxis().SetTitleFont(42)
   dummy_ratio.Draw()
   h3.Draw("e2same")
   if is_obs:
       h1.Draw("e0psame")
   dummy_ratio.Draw("AXISsame")
   c.cd()
   pad1.Draw()

   ROOT.gPad.RedrawAxis()

   c.Modified()
   c.SaveAs("./plot_pre_post_fit/"+categories[i][1]+str_obs+".png")


