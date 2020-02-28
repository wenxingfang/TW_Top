import math
import gc
import sys
import ROOT
import numpy as np
from array import array
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gROOT.ProcessLine("gErrorIgnoreLevel = 1;")
ROOT.TH1.AddDirectory(ROOT.kFALSE)

def two_sigma_band(Dict):
    dict_band={}
    for ibin in range(1,len(Dict)+1):
        str_i=str(ibin)
        error_plus =math.sqrt(math.pow(data_top_Pt[str_i][1],2)+math.pow(data_top_Pt[str_i][2],2))
        error_minus=math.sqrt(math.pow(data_top_Pt[str_i][1],2)+math.pow(data_top_Pt[str_i][3],2))
        Up_2sigma  =data_top_Pt[str_i][0]+2*error_plus
        Down_2sigma=data_top_Pt[str_i][0]-2*error_minus
        dict_band[str_i]=[float(Up_2sigma),float(Down_2sigma)]
    return dict_band
    
def draw_plot(hist,data_dicit, hist_dict, h_data, h_Vtb, h_Vts, h_Vtd, dir_out, date, normalized):
        canvas = ROOT.TCanvas('canvas','',10,10,1100,628)
        canvas.SetLeftMargin(0.15)
        canvas.SetBottomMargin(0.15)
        canvas.cd()
        canvas.SetTickx()
        canvas.SetTicky()
        x_min=h_data.GetXaxis().GetXmin()
        x_max=h_data.GetXaxis().GetXmax()
        y_min=0
        y_max=2*h_data.GetBinContent(h_data.GetMaximumBin())
        if "pt_fine" in hist:
            canvas.SetLogy()
            y_min=1e-4
            y_max=2
            if is_7TeV and "atop" not in hist:
                y_min=1e-3
        xaxis_name=hist_dict[hist]
        dummy = ROOT.TH2F("dummy","",1,x_min,x_max,1,y_min,y_max)
        dummy.SetStats(ROOT.kFALSE)
        dummy.GetXaxis().SetTitle(xaxis_name)
        str_GeV=""
        if "GeV" in xaxis_name:str_GeV=" GeV"
        str_y_bin=""if h_data.GetBinWidth(1)!=h_data.GetBinWidth(h_data.GetNbinsX()) else " / "+str(h_data.GetBinWidth(1))+str_GeV
        str_y="Event"
        if Do_normalize_to_XS:
            str_y_bin=""
            tmp_str=xaxis_name.replace("(GeV)","")
            tmp_str1=""
            if "GeV" in xaxis_name:
                tmp_str1="[pb GeV^{-1}]"
            else:
                tmp_str1="[pb]"
            str_y="d#sigma/d%s %s"%(tmp_str,tmp_str1)
            if normalized:
                if "GeV" in xaxis_name:
                    tmp_str1="[GeV^{-1}]"
                else:
                    tmp_str1=""
                str_y="1/#sigma d#sigma/d%s %s"%(tmp_str,tmp_str1)
        dummy.GetYaxis().SetTitle(str_y+str_y_bin)
        dummy.GetXaxis().SetMoreLogLabels()
        dummy.GetXaxis().SetNoExponent() 
        dummy.GetYaxis().SetTitleOffset(1.0)
        dummy.GetXaxis().SetTitleOffset(0.95)
        dummy.GetYaxis().SetTitleSize(0.07)
        dummy.GetXaxis().SetTitleSize(0.07)
        dummy.GetXaxis().SetLabelSize(0.06)
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
    #    h_Vts.Draw("same:hist")
    #    h_Vtd.Draw("same:hist")
        ROOT.gStyle.SetErrorX(0)
        if hist in data_dicit:
            h_data.SetLineColor(ROOT.kBlack)
            h_data.SetLineWidth(2)
            h_data.SetMarkerStyle(8)
            h_data.SetMarkerColor(ROOT.kBlack)
            h_data.Draw("same:pe")
        #h_Vtb.Draw("same:pe")
        dummy.Draw("AXISSAME")
        legend_x_min=0.42
        legend_x_max=0.88
        legend_y_min=0.6
        legend_y_max=0.88
        legend = ROOT.TLegend(legend_x_min,legend_y_min,legend_x_max,legend_y_max)
        legend.AddEntry(h_Vtb,'MG5_aMC@NLO+Pythia8','l')
    #    legend.AddEntry(h_Vtb,'Vtb(MG5_aMC@NLO+Pythia8)','l')
    #    legend.AddEntry(h_Vts,'Vts(MG5_aMC@NLO+Pythia8)','l')
    #    legend.AddEntry(h_Vtd,'Vtd(MG5_aMC@NLO+Pythia8)','l')
        if hist in data_dicit:
            str_year="2012"
            if is_7TeV:str_year="2011"
            legend.AddEntry(h_data,'Data (ATLAS %s)'%(str_year),'ep')
        legend.SetBorderSize(0)
        legend.SetTextFont(42)
        legend.SetTextSize(0.05)
        legend.Draw()
        label = ROOT.TLatex()
        label.SetTextAlign(12)
        label.SetTextFont(42)
        label.SetTextSize(0.05)
        label.SetNDC(ROOT.kTRUE)
        str_level="particle-level"
        if is_7TeV:str_level="parton-level"
        if is_top:
            label.DrawLatex(0.22,0.80, '#it{tq} %s'%str_level)
        elif is_antitop:
            label.DrawLatex(0.22,0.80, "#it{#bar{t}q} %s"%str_level)
        label.Draw()
        label_lumi = ROOT.TLatex()
        label_lumi.SetTextAlign(12)
        label_lumi.SetTextFont(42)
        label_lumi.SetTextSize(0.05)
        label_lumi.SetNDC(ROOT.kTRUE)
        str_lumi="#sqrt{s} = 8 TeV, 20.2 fb^{-1}"
        if is_7TeV:str_lumi="#sqrt{s} = 7 TeV, 4.59 fb^{-1}"
        label_lumi.DrawLatex(0.67,0.93, str_lumi)
        canvas.Print('%s/%s/%s.png'%(dir_out,date,hist))    
        canvas.Print('%s/%s/%s.pdf'%(dir_out,date,hist))    
        del canvas
        gc.collect()

def draw_ratio_plot(hist,data_dicit, hist_dict, h_data, h_Vtb, h_Vts, h_Vtd, dir_out, date, normalized):
#        canvas = ROOT.TCanvas('canvas','',10,10,1000,1000)
        canvas = ROOT.TCanvas('canvas','',10,10,1100,628)
#        canvas.SetLeftMargin(0.18)
#        canvas.SetBottomMargin(0.10)
        canvas.cd()
#        canvas.SetTickx()
#        canvas.SetTicky()
        pad1=ROOT.TPad("pad1", "pad1", 0, 0.315, 1, 0.99 , 0)
        pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.3 , 0)
        pad1.Draw()
        pad2.Draw()
        pad2.SetGridy()
        pad1.SetTickx()
        pad1.SetTicky()
        pad2.SetTickx()
        pad2.SetTicky()
        pad1.SetBottomMargin(0.01)
        pad1.SetLeftMargin(0.15)
#        pad1.SetRightMargin(0.05)
        pad2.SetTopMargin(0.0)
        pad2.SetBottomMargin(0.4)
        pad2.SetLeftMargin(0.15)
#        pad2.SetRightMargin(0.05)
        pad1.SetLogx(ROOT.kFALSE)
        pad2.SetLogx(ROOT.kFALSE)
        pad2.SetFillStyle(4000)
        pad1.SetLogy(ROOT.kFALSE)
        pad1.cd()

        x_min=h_data.GetXaxis().GetXmin()
        x_max=h_data.GetXaxis().GetXmax()
        if hist is "H_bjet_Rap":
            x_min=0
            x_max=2.6
        y_min=0
        y_max=2*h_data.GetBinContent(h_data.GetMaximumBin())
        if "pt_fine" in hist:
            pad1.SetLogy()
            y_min=1e-4
            y_max=2
        xaxis_name=hist_dict[hist]
        dummy = ROOT.TH2F("dummy","",1,x_min,x_max,1,y_min,y_max)
        dummy.SetStats(ROOT.kFALSE)
        dummy.GetXaxis().SetTitle(xaxis_name)
        str_GeV=""
        if "GeV" in xaxis_name:str_GeV=" GeV"
        str_y_bin=""if h_data.GetBinWidth(1)!=h_data.GetBinWidth(h_data.GetNbinsX()) else " / "+str(h_data.GetBinWidth(1))+str_GeV
        str_y="Event"
        if Do_normalize_to_XS:
            str_y_bin=""
            tmp_str=xaxis_name.replace("(GeV)","")
            tmp_str1=""
            if "GeV" in xaxis_name:
                tmp_str1="[pb GeV^{-1}]"
            else:
                tmp_str1="[pb]"
            str_y="#frac{d#sigma}{d%s} %s"%(tmp_str,tmp_str1)
            if normalized:
                if "GeV" in xaxis_name:
                    tmp_str1="[GeV^{-1}]"
                else:
                    tmp_str1=""
                str_y="1/#sigma d#sigma/d%s %s"%(tmp_str,tmp_str1)
        dummy.GetYaxis().SetTitle(str_y+str_y_bin)
        dummy.GetXaxis().SetMoreLogLabels()
        dummy.GetXaxis().SetNoExponent() 
        dummy.GetYaxis().SetTitleOffset(0.7)
        dummy.GetXaxis().SetTitleOffset(1)
        dummy.GetYaxis().SetTitleSize(0.1)
        dummy.GetXaxis().SetTitleSize(0.0)
        dummy.GetXaxis().SetLabelSize(0.0)
        dummy.GetYaxis().SetLabelSize(0.09)
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
        if hist in data_dicit and is_13TeV==False:
            h_data.SetLineColor(ROOT.kBlack)
            h_data.SetLineWidth(2)
            h_data.SetMarkerStyle(8)
            h_data.SetMarkerColor(ROOT.kBlack)
            h_data.Draw("same:pe")
        dummy.Draw("AXISSAME")
        legend_x_min=0.45
        legend_x_max=0.8
        legend_y_min=0.52
        legend_y_max=0.88
        legend = ROOT.TLegend(legend_x_min,legend_y_min,legend_x_max,legend_y_max)
        legend.AddEntry(h_Vtb,'V_{tb} (MG5_aMC@NLO+Pythia8)','l')
        legend.AddEntry(h_Vts,'V_{ts} (MG5_aMC@NLO+Pythia8)','l')
        legend.AddEntry(h_Vtd,'V_{td} (MG5_aMC@NLO+Pythia8)','l')
        str_year="2012"
        if is_7TeV:
            str_year="2011"
        if hist in data_dicit and is_13TeV==False:
            legend.AddEntry(h_data,'Data (ATLAS %s)'%str_year,'ep')
        legend.SetBorderSize(0)
        legend.SetTextFont(42)
        legend.SetTextSize(0.07)
        legend.Draw()
        label = ROOT.TLatex()
        label.SetTextAlign(12)
        label.SetTextFont(42)
        label.SetTextSize(0.085)
        label.SetNDC(ROOT.kTRUE)
        str_level="particle-level"
        if is_7TeV:
            str_level="parton-level"
        if is_top:
            label.DrawLatex(0.22,0.75, '#it{tq} %s'%str_level)
        elif is_antitop:
            label.DrawLatex(0.22,0.75, "#it{#bar{t}q} %s"%str_level)
        label.Draw()
        label_lumi = ROOT.TLatex()
        label_lumi.SetTextAlign(12)
        label_lumi.SetTextFont(42)
        label_lumi.SetTextSize(0.08)
        label_lumi.SetNDC(ROOT.kTRUE)
        str_lumi=""
        if hist in data_dicit:
           str_lumi="#sqrt{s} = 8 TeV, 20.2 fb^{-1}"
           if is_7TeV:str_lumi="#sqrt{s} = 7 TeV, 4.59 fb^{-1}"
           elif is_13TeV:str_lumi="          #sqrt{s} = 13 TeV"
        else:
           str_lumi="            #sqrt{s} = 8 TeV"
           if is_7TeV:str_lumi="#sqrt{s} = 7 TeV, 4.59 fb^{-1}"
           elif is_13TeV:str_lumi="          #sqrt{s} = 13 TeV"
        label_lumi.DrawLatex(0.66,0.95, str_lumi)
        pad2.cd()
        ratio_y_min=0
        ratio_y_max=1.99
        if hist is "H_DR_top_jet":
            ratio_y_max=2.99
        elif hist is "H_bjet_Rap":
            ratio_y_min=0.5
            ratio_y_max=3.4
            if is_antitop:
                ratio_y_min=0.7
                ratio_y_max=1.49
        elif "pt_fine" in hist and "atop" not in hist:
            ratio_y_min=0.5
            ratio_y_max=2.9
            if "jet" in hist:
                ratio_y_max=2.4

        dummy_ratio = ROOT.TH2F("dummy_ratio","",1,x_min,x_max,1,ratio_y_min,ratio_y_max)
        dummy_ratio.SetStats(ROOT.kFALSE)
        dummy_ratio.GetXaxis().SetTitle(xaxis_name)
        dummy_ratio.GetYaxis().SetTitle("MC/Data")
        if is_13TeV or (hist not in data_dicit):
            dummy_ratio.GetYaxis().SetTitle("V_{tx}/V_{tb}")
        dummy_ratio.GetYaxis().CenterTitle()
        dummy_ratio.GetXaxis().SetMoreLogLabels()
        dummy_ratio.GetXaxis().SetNoExponent() 
        dummy_ratio.GetYaxis().SetTitleOffset(0.4)
        dummy_ratio.GetXaxis().SetTitleOffset(1)
        dummy_ratio.GetYaxis().SetTitleSize(0.18)
        dummy_ratio.GetXaxis().SetTitleSize(0.18)
        dummy_ratio.GetXaxis().SetLabelSize(0.18)
        dummy_ratio.GetYaxis().SetLabelSize(0.18)
        dummy_ratio.GetYaxis().SetNdivisions(405)
        dummy_ratio.Draw()
        ratio_Vtb=h_Vtb.Clone("ratio_Vtb")
        ratio_Vtb.Divide(h_data)
        ratio_Vts=h_Vts.Clone("ratio_Vts")
        ratio_Vts.Divide(h_data)
        ratio_Vtd=h_Vtd.Clone("ratio_Vtd")
        ratio_Vtd.Divide(h_data)
        ratio_Vtb.Draw("hist:same")
        ratio_Vts.Draw("hist:same")
        ratio_Vtd.Draw("hist:same")
        dummy_ratio.Draw("AXISSAME")
        canvas.Print('%s/%s/%s.png'%(dir_out,date,hist))    
        canvas.Print('%s/%s/%s.pdf'%(dir_out,date,hist))    
        del canvas
        gc.collect()
###########BEGIN###################

is_7TeV=True
is_13TeV=False
remove_MC_err=True
lumi_13TeV=3000 ##fb^-1
dir_in="./ntuple/Reza_8TeV_notau_lastbin/"# for final
#dir_in="./ntuple/Reza_8TeV_20180509_addDRjet/"##just for jet check
if is_7TeV:
    dir_in="./ntuple/Reza_7TeV_lastbin/"# for final
elif is_13TeV:
    dir_in="./ntuple/Reza_13TeV_notau_lastbin/" # for final
dir_out="./plots"
date="20170916"


is_top    =False
is_antitop=True

Do_normalize_to_XS  =True## always true
Do_normalize        =False

Increase_XS         =False##don't use 
Decrease_ATLAS      =True

Draw_plot           =True
Do_Save_hist        =False#for limit
f_Vtb=ROOT.TFile()
f_Vts=ROOT.TFile()
f_Vtd=ROOT.TFile()
if is_top:
    f_Vtb=ROOT.TFile(dir_in+"hist_Vtb_top_nominal.root","read")
    f_Vts=ROOT.TFile(dir_in+"hist_Vts_top_nominal.root","read")
    f_Vtd=ROOT.TFile(dir_in+"hist_Vtd_top_nominal.root","read")
elif is_antitop:
    f_Vtb=ROOT.TFile(dir_in+"hist_Vtb_antitop_nominal.root","read")
    f_Vts=ROOT.TFile(dir_in+"hist_Vts_antitop_nominal.root","read")
    f_Vtd=ROOT.TFile(dir_in+"hist_Vtd_antitop_nominal.root","read")
else:
    print "choose top or anti-top"   
f_Vtb_top =ROOT.TFile(dir_in+"hist_Vtb_top_nominal.root","read")
f_Vtb_atop=ROOT.TFile(dir_in+"hist_Vtb_antitop_nominal.root","read")
f_Vts_top =ROOT.TFile(dir_in+"hist_Vts_top_nominal.root","read")
f_Vts_atop=ROOT.TFile(dir_in+"hist_Vts_antitop_nominal.root","read")
f_Vtd_top =ROOT.TFile(dir_in+"hist_Vtd_top_nominal.root","read")
f_Vtd_atop=ROOT.TFile(dir_in+"hist_Vtd_antitop_nominal.root","read")
Lumi=20200
Vtb_event=1
Vts_event=1
Vtd_event=1
Vtb_top_event =130990
Vtb_atop_event=134976
Vts_top_event =209564
Vts_atop_event=206884
Vtd_top_event =198232
Vtd_atop_event=206196
if is_7TeV:
    Vtb_top_event =134885
    Vtb_atop_event=137070
    Vts_top_event =207560
    Vts_atop_event=209506
    Vtd_top_event =198714
    Vtd_atop_event=208683
elif is_13TeV:
    Vtb_top_event =25328
    Vtb_atop_event=25026
    Vts_top_event =40014
    Vts_atop_event=39592
    Vtd_top_event =38414
    Vtd_atop_event=38944

if is_top:
    Vtb_event=Vtb_top_event
    Vts_event=Vts_top_event
    Vtd_event=Vtd_top_event
elif is_antitop:
    Vtb_event=Vtb_atop_event
    Vts_event=Vts_atop_event
    Vtd_event=Vtd_atop_event

data_top_fid =9.78*0.324
data_atop_fid=5.77*0.324
if is_7TeV:
    data_top_fid =47.9*0.324
    data_atop_fid=20.19*0.324
elif is_13TeV:
    data_top_fid =136.5*0.324#be same with Vtb==1,Vts=Vtd=0
    data_atop_fid=82.1 *0.324#
data_fid=1
if is_top:
    data_fid=data_top_fid
elif is_antitop:
    data_fid=data_atop_fid


Vtb_XS=1
Vts_XS=1
Vtd_XS=1
Vtb_top_XS =56.3 *0.324
Vtb_atop_XS=30.7 *0.324
Vts_top_XS =132.5*0.324
Vts_atop_XS=69.6 *0.324
Vtd_top_XS =406.4*0.324
Vtd_atop_XS=109.0*0.324
if is_7TeV:
      Vtb_top_XS =43.7 *0.324
      Vtb_atop_XS=22.8 *0.324
      Vts_top_XS =104.2*0.324
      Vts_atop_XS=52.2 *0.324
      Vtd_top_XS =329.2*0.324
      Vtd_atop_XS=84.4 *0.324
elif is_13TeV:
      Vtb_top_XS =136.5 *0.324
      Vtb_atop_XS=82.1  *0.324
      Vts_top_XS =300.72*0.324
      Vts_atop_XS=177.1 *0.324
      Vtd_top_XS =772.8 *0.324
      Vtd_atop_XS=260.4 *0.324
if is_top:
    Vtb_XS=Vtb_top_XS
    Vts_XS=Vts_top_XS
    Vtd_XS=Vtd_top_XS
    if Increase_XS:
        Vtb_XS=Vtb_top_XS/0.324
        Vts_XS=Vts_top_XS/0.324
        Vtd_XS=Vtd_top_XS/0.324
   
elif is_antitop:
    Vtb_XS=Vtb_atop_XS
    Vts_XS=Vts_atop_XS
    Vtd_XS=Vtd_atop_XS
    if Increase_XS:
        Vtb_XS=Vtb_atop_XS/0.324
        Vts_XS=Vts_atop_XS/0.324
        Vtd_XS=Vtd_atop_XS/0.324



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
add_hist_8TeV={
"H_DR_lep_jet" :"#DeltaR(lepton,j)",
"H_DR_bjet_jet":"#DeltaR(bjet,j)",
"H_DR_top_jet" :"#DeltaR(t,j)",
"H_DR_atop_jet" :"#DeltaR(#bar{t},j)"
}
#hist_dict.update(add_hist_8TeV)
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

data_top_Pt={}
data_top_Pt["1"]=[1e-3*38.0 ,1e-3*3.1 ,1e-3*3.3 ,1e-3*3.4 ]
data_top_Pt["2"]=[1e-3*120.9,1e-3*8.4 ,1e-3*8.0 ,1e-3*8.2 ]
data_top_Pt["3"]=[1e-3*125.2,1e-3*5.3 ,1e-3*7.7 ,1e-3*7.9 ]
data_top_Pt["4"]=[1e-3*68.1 ,1e-3*3.9 ,1e-3*5.1 ,1e-3*5.0 ]
data_top_Pt["5"]=[1e-3*27.5 ,1e-3*1.5 ,1e-3*2.1 ,1e-3*2.1 ]
data_top_Pt["6"]=[1e-3*7.55 ,1e-3*0.76,1e-3*0.67,1e-3*0.56]
data_top_Pt["7"]=[1e-3*1.50 ,1e-3*0.24,1e-3*0.23,1e-3*0.23]

data_atop_Pt={}
data_atop_Pt["1"]=[1e-3*22.5 ,1e-3*2.7 ,1e-3*2.5 ,1e-3*2.4 ]
data_atop_Pt["2"]=[1e-3*85.6 ,1e-3*7.8 ,1e-3*7.2 ,1e-3*6.3 ]
data_atop_Pt["3"]=[1e-3*84.7 ,1e-3*4.7 ,1e-3*5.4 ,1e-3*6.9 ]
data_atop_Pt["4"]=[1e-3*30.9 ,1e-3*3.3 ,1e-3*4.6 ,1e-3*4.4 ]
data_atop_Pt["5"]=[1e-3*14.4 ,1e-3*1.3 ,1e-3*1.2 ,1e-3*1.2 ]
data_atop_Pt["6"]=[1e-3*1.35 ,1e-3*0.23,1e-3*0.35,1e-3*0.30]

data_top_y={}
data_top_y["1"]=[9.00 ,0.45 ,0.43 ,0.43 ]
data_top_y["2"]=[8.99 ,0.47 ,0.47 ,0.49 ]
data_top_y["3"]=[8.15 ,0.48 ,0.59 ,0.60 ]
data_top_y["4"]=[6.88 ,0.32 ,0.38 ,0.37 ]
data_top_y["5"]=[5.70 ,0.26 ,0.49 ,0.48 ]
data_top_y["6"]=[3.47 ,0.22 ,0.26 ,0.25 ]
data_top_y["7"]=[1.61 ,0.08 ,0.11 ,0.11 ]

data_atop_y={}
data_atop_y["1"]=[6.65 ,0.44 ,0.50 ,0.49 ]
data_atop_y["2"]=[4.68 ,0.43 ,0.41 ,0.43 ]
data_atop_y["3"]=[4.97 ,0.42 ,0.40 ,0.39 ]
data_atop_y["4"]=[4.08 ,0.29 ,0.34 ,0.33 ]
data_atop_y["5"]=[3.21 ,0.23 ,0.27 ,0.27 ]
data_atop_y["6"]=[2.30 ,0.20 ,0.20 ,0.21 ]
data_atop_y["7"]=[0.76 ,0.07 ,0.08 ,0.07 ]

data_top_jet_Pt={}
data_top_jet_Pt["1"]=[1e-3*199  ,1e-3*10   ,1e-3*18   ,1e-3*19   ]
data_top_jet_Pt["2"]=[1e-3*151  ,1e-3*9    ,1e-3*13   ,1e-3*14   ]
data_top_jet_Pt["3"]=[1e-3*102.3,1e-3*7.0  ,1e-3*6.8  ,1e-3*5.8  ]
data_top_jet_Pt["4"]=[1e-3*58.5 ,1e-3*3.5  ,1e-3*3.5  ,1e-3*3.9  ]
data_top_jet_Pt["5"]=[1e-3*22.8 ,1e-3*1.3  ,1e-3*1.4  ,1e-3*1.4  ]
data_top_jet_Pt["6"]=[1e-3*3.29 ,1e-3*0.26 ,1e-3*0.24 ,1e-3*0.22 ]

data_atop_jet_Pt={}
data_atop_jet_Pt["1"]=[1e-3*147  ,1e-3*9    ,1e-3*12   ,1e-3*12   ]
data_atop_jet_Pt["2"]=[1e-3*86.4 ,1e-3*7.8  ,1e-3*8.3  ,1e-3*8.5  ]
data_atop_jet_Pt["3"]=[1e-3*54.2 ,1e-3*6.2  ,1e-3*5.1  ,1e-3*6.0  ]
data_atop_jet_Pt["4"]=[1e-3*33.0 ,1e-3*3.1  ,1e-3*3.7  ,1e-3*3.9  ]
data_atop_jet_Pt["5"]=[1e-3*10.7 ,1e-3*1.1  ,1e-3*1.3  ,1e-3*1.2  ]
data_atop_jet_Pt["6"]=[1e-3*1.36 ,1e-3*0.22 ,1e-3*0.26 ,1e-3*0.22 ]

data_top_jet_y={}
data_top_jet_y["1"]=[1.62 ,0.14 ,0.28 ,0.28 ]
data_top_jet_y["2"]=[2.40 ,0.18 ,0.22 ,0.20 ]
data_top_jet_y["3"]=[2.21 ,0.15 ,0.19 ,0.20 ]
data_top_jet_y["4"]=[3.72 ,0.16 ,0.19 ,0.19 ]
data_top_jet_y["5"]=[3.23 ,0.13 ,0.16 ,0.17 ]
data_top_jet_y["6"]=[1.50 ,0.06 ,0.10 ,0.10 ]

data_atop_jet_y={}
data_atop_jet_y["1"]=[1.17 ,0.14 ,0.27 ,0.27 ]
data_atop_jet_y["2"]=[1.39 ,0.17 ,0.18 ,0.18 ]
data_atop_jet_y["3"]=[1.85 ,0.14 ,0.16 ,0.16 ]
data_atop_jet_y["4"]=[1.73 ,0.13 ,0.12 ,0.12 ]
data_atop_jet_y["5"]=[1.70 ,0.10 ,0.12 ,0.12 ]
data_atop_jet_y["6"]=[0.655,0.040,0.053,0.051]


data_7TeV_top_Pt={}
data_7TeV_top_Pt["1"]=[1e-3*440 ,1e-3*70]
data_7TeV_top_Pt["2"]=[1e-3*370 ,1e-3*60]
data_7TeV_top_Pt["3"]=[1e-3*250 ,1e-3*40]
data_7TeV_top_Pt["4"]=[1e-3*133 ,1e-3*27]
data_7TeV_top_Pt["5"]=[1e-3*7.8 ,1e-3*1.9]
data_7TeV_atop_Pt={}
data_7TeV_atop_Pt["1"]=[1e-3*190 ,1e-3*50]
data_7TeV_atop_Pt["2"]=[1e-3*230 ,1e-3*40]
data_7TeV_atop_Pt["3"]=[1e-3*97  ,1e-3*27]
data_7TeV_atop_Pt["4"]=[1e-3*13.0,1e-3*9.7]
data_7TeV_atop_Pt["5"]=[1e-3*1.4 ,1e-3*0.9]
data_7TeV_top_y={}
data_7TeV_top_y["1"]=[28   ,4  ]
data_7TeV_top_y["2"]=[27.3 ,3.3]
data_7TeV_top_y["3"]=[22.1 ,3.0]
data_7TeV_top_y["4"]=[10.7 ,1.6]
data_7TeV_atop_y={}
data_7TeV_atop_y["1"]=[15.0 ,3.4]
data_7TeV_atop_y["2"]=[13.3 ,3.3]
data_7TeV_atop_y["3"]=[11.2 ,2.6]
data_7TeV_atop_y["4"]=[3.3  ,0.9]
if is_7TeV:
    data_top_Pt=data_7TeV_top_Pt
    data_atop_Pt=data_7TeV_atop_Pt
    data_top_y=data_7TeV_top_y
    data_atop_y=data_7TeV_atop_y




data_dicit={}
data_dicit["H_top_pt_fine"      ]=data_top_Pt
data_dicit["H_top_Rap_fine"     ]=data_top_y
data_dicit["H_top_jet_pt_fine"  ]=data_top_jet_Pt
data_dicit["H_top_jet_Rap_fine" ]=data_top_jet_y
data_dicit["H_atop_pt_fine"     ]=data_atop_Pt
data_dicit["H_atop_Rap_fine"    ]=data_atop_y
data_dicit["H_atop_jet_pt_fine" ]=data_atop_jet_Pt
data_dicit["H_atop_jet_Rap_fine"]=data_atop_jet_y

BR=0.324
if Decrease_ATLAS:
    for cat in data_dicit:
        for ibin in data_dicit[cat]:
            for iv in range(0,len(data_dicit[cat][ibin])):
                data_dicit[cat][ibin][iv]=BR*data_dicit[cat][ibin][iv]
    print "decrease ATLAS by %f"%(BR)

#Dict_bands={}
#Dict_bands["H_top_pt_fine"      ]=two_sigma_band(data_dicit["H_top_pt_fine"      ])
#Dict_bands["H_top_Rap_fine"     ]=two_sigma_band(data_dicit["H_top_Rap_fine"     ])
#Dict_bands["H_top_jet_pt_fine"  ]=two_sigma_band(data_dicit["H_top_jet_pt_fine"  ])
#Dict_bands["H_top_jet_Rap_fine" ]=two_sigma_band(data_dicit["H_top_jet_Rap_fine" ])
#Dict_bands["H_atop_pt_fine"     ]=two_sigma_band(data_dicit["H_atop_pt_fine"     ])
#Dict_bands["H_atop_Rap_fine"    ]=two_sigma_band(data_dicit["H_atop_Rap_fine"    ])
#Dict_bands["H_atop_jet_pt_fine" ]=two_sigma_band(data_dicit["H_atop_jet_pt_fine" ])
#Dict_bands["H_atop_jet_Rap_fine"]=two_sigma_band(data_dicit["H_atop_jet_Rap_fine"])

Dict_Limit={}

if Draw_plot:
    for hist in hist_dict:
        if is_top:
            if "atop" in hist:continue
        elif is_antitop:
            if "_top_" in hist:continue
        h_Vtb=f_Vtb.Get(hist)
        h_Vts=f_Vts.Get(hist)
        h_Vtd=f_Vtd.Get(hist)
        if h_Vtb is None:
            print "don't find hist %s , continue"%(hist)
            continue
        Vtb_eff=h_Vtb.GetSumOfWeights()/Vtb_event
        Vts_eff=h_Vts.GetSumOfWeights()/Vts_event
        Vtd_eff=h_Vtd.GetSumOfWeights()/Vtd_event
        print "eff Vtb=%f,inc eff=%f, XS=%f"%(Vtb_eff,0.324*Vtb_eff,Vtb_eff*Vtb_XS)
        print "eff Vts=%f,inc eff=%f, XS=%f"%(Vts_eff,0.324*Vts_eff,Vts_eff*Vts_XS)
        print "eff Vtd=%f,inc eff=%f, XS=%f"%(Vtd_eff,0.324*Vtd_eff,Vtd_eff*Vtd_XS)
        Vtb_fid=Vtb_eff*Vtb_XS
        Vts_fid=Vts_eff*Vts_XS
        Vtd_fid=Vtd_eff*Vtd_XS
        if Do_normalize_to_XS and h_Vtb.GetSumOfWeights()!=0 and h_Vts.GetSumOfWeights()!=0 and h_Vtd.GetSumOfWeights()!=0:
            h_Vtb.Scale(Vtb_XS*Vtb_eff/h_Vtb.GetSumOfWeights())
            h_Vts.Scale(Vts_XS*Vts_eff/h_Vts.GetSumOfWeights())
            h_Vtd.Scale(Vtd_XS*Vtd_eff/h_Vtd.GetSumOfWeights())
            if True:
                for ibin in range(1,h_Vtb.GetNbinsX()+1):
                    h_Vtb.SetBinContent(ibin,h_Vtb.GetBinContent(ibin)/h_Vtb.GetBinWidth(ibin))
                    h_Vts.SetBinContent(ibin,h_Vts.GetBinContent(ibin)/h_Vts.GetBinWidth(ibin))
                    h_Vtd.SetBinContent(ibin,h_Vtd.GetBinContent(ibin)/h_Vtd.GetBinWidth(ibin))
                    h_Vtb.SetBinError(ibin,h_Vtb.GetBinError(ibin)/h_Vtb.GetBinWidth(ibin))
                    h_Vts.SetBinError(ibin,h_Vts.GetBinError(ibin)/h_Vts.GetBinWidth(ibin))
                    h_Vtd.SetBinError(ibin,h_Vtd.GetBinError(ibin)/h_Vtd.GetBinWidth(ibin))
        h_data=h_Vtb.Clone("data_%s_"%h_Vtb.GetName())
        if hist in data_dicit:
            for ibin in range(1,h_data.GetNbinsX()+1):
                value=data_dicit[hist][str(ibin)][0]
                error=0
                if is_7TeV:error=data_dicit[hist][str(ibin)][1]
                else:
                    error=math.sqrt(math.pow(data_dicit[hist][str(ibin)][1],2)+math.pow(data_dicit[hist][str(ibin)][2],2)) if math.pow(data_dicit[hist][str(ibin)][2],2) > math.pow(data_dicit[hist][str(ibin)][3],2) else math.sqrt(math.pow(data_dicit[hist][str(ibin)][1],2)+math.pow(data_dicit[hist][str(ibin)][3],2))
                h_data.SetBinContent(ibin,value)
                h_data.SetBinError (ibin,error)
        if Do_normalize:##normalized
            h_Vtb.Scale(1/Vtb_fid)  
            h_Vts.Scale(1/Vts_fid)  
            h_Vtd.Scale(1/Vtd_fid)  
            h_data.Scale(1/data_fid)  
        if is_13TeV or (hist not in data_dicit):
            h_data=h_Vtb.Clone("data13TeV_%s_"%h_Vtb.GetName())
        if Do_normalize==False:
            draw_plot(hist,data_dicit, hist_dict, h_data, h_Vtb, h_Vts, h_Vtd, dir_out, date, Do_normalize)
        if Do_normalize:
            draw_ratio_plot(hist,data_dicit, hist_dict, h_data, h_Vtb, h_Vts, h_Vtd, dir_out, date, Do_normalize)


if Do_Save_hist:
    str_TeV="_8TeV"
    if is_13TeV:
        str_TeV=str("_13TeV_%dfb"%(lumi_13TeV))
    nbin=51
    hist_list=["H_top_pt_fine","H_top_Rap_fine","H_top_jet_pt_fine","H_top_jet_Rap_fine","H_atop_pt_fine","H_atop_Rap_fine","H_atop_jet_pt_fine","H_atop_jet_Rap_fine"]
    if is_7TeV:
        str_TeV="_7TeV"
        nbin=18
        hist_list=["H_top_pt_fine","H_top_Rap_fine","H_atop_pt_fine","H_atop_Rap_fine"]
    F_out=ROOT.TFile("Limit_hist%s.root"%(str_TeV),"RECREATE")
    hist_out_data=ROOT.TH1D("data","",nbin,0,nbin)
    hist_out_Vtb=hist_out_data.Clone("Vtb")
    hist_out_Vts=hist_out_data.Clone("Vts")
    hist_out_Vtd=hist_out_data.Clone("Vtd")
    N_bin=0
    for hist in hist_list:
        if hist not in data_dicit:continue
        h_Vtb=f_Vtb_top.Get(hist)
        h_Vts=f_Vts_top.Get(hist)
        h_Vtd=f_Vtd_top.Get(hist)
        Vtb_eff=h_Vtb.GetSumOfWeights()/Vtb_top_event
        Vts_eff=h_Vts.GetSumOfWeights()/Vts_top_event
        Vtd_eff=h_Vtd.GetSumOfWeights()/Vtd_top_event
        h_Vtb.Scale(Vtb_top_XS*Vtb_eff/h_Vtb.GetSumOfWeights())
        h_Vts.Scale(Vts_top_XS*Vts_eff/h_Vts.GetSumOfWeights())
        h_Vtd.Scale(Vtd_top_XS*Vtd_eff/h_Vtd.GetSumOfWeights())
        if "atop" in hist:
            h_Vtb=f_Vtb_atop.Get(hist)
            h_Vts=f_Vts_atop.Get(hist)
            h_Vtd=f_Vtd_atop.Get(hist)
            Vtb_eff=h_Vtb.GetSumOfWeights()/Vtb_atop_event
            Vts_eff=h_Vts.GetSumOfWeights()/Vts_atop_event
            Vtd_eff=h_Vtd.GetSumOfWeights()/Vtd_atop_event
            h_Vtb.Scale(Vtb_atop_XS*Vtb_eff/h_Vtb.GetSumOfWeights())
            h_Vts.Scale(Vts_atop_XS*Vts_eff/h_Vts.GetSumOfWeights())
            h_Vtd.Scale(Vtd_atop_XS*Vtd_eff/h_Vtd.GetSumOfWeights())
        if True:
            for ibin in range(1,h_Vtb.GetNbinsX()+1):
                h_Vtb.SetBinContent(ibin,h_Vtb.GetBinContent(ibin)/h_Vtb.GetBinWidth(ibin))
                h_Vts.SetBinContent(ibin,h_Vts.GetBinContent(ibin)/h_Vts.GetBinWidth(ibin))
                h_Vtd.SetBinContent(ibin,h_Vtd.GetBinContent(ibin)/h_Vtd.GetBinWidth(ibin))
                h_Vtb.SetBinError(ibin,h_Vtb.GetBinError(ibin)/h_Vtb.GetBinWidth(ibin))
                h_Vts.SetBinError(ibin,h_Vts.GetBinError(ibin)/h_Vts.GetBinWidth(ibin))
                h_Vtd.SetBinError(ibin,h_Vtd.GetBinError(ibin)/h_Vtd.GetBinWidth(ibin))
        h_data=h_Vtb.Clone("data_%s_"%hist)
        for ibin in range(1,h_data.GetNbinsX()+1):
            value=data_dicit[hist][str(ibin)][0]
            error=0
            if is_7TeV:
                error=data_dicit[hist][str(ibin)][1]
            elif is_13TeV:
                #error=math.sqrt(math.pow(data_dicit[hist][str(ibin)][1]/math.sqrt(lumi_13TeV/20.2),2)+math.pow(data_dicit[hist][str(ibin)][2]*(0.5+0.5*math.sqrt(20.2/lumi_13TeV)),2)) if math.pow(data_dicit[hist][str(ibin)][2],2) < math.pow(data_dicit[hist][str(ibin)][3],2) else math.sqrt(math.pow(data_dicit[hist][str(ibin)][1]/math.sqrt(lumi_13TeV/20.2),2)+math.pow(data_dicit[hist][str(ibin)][3]*(0.5+0.5*math.sqrt(20.2/lumi_13TeV)),2))##for 13TeV prediction, sys uncert scaled by 0.5
                #factor=(136.5/56.3)*0.51*20.2/lumi_13TeV
                factor=math.sqrt(20.2/lumi_13TeV)
                error=math.sqrt(math.pow(data_dicit[hist][str(ibin)][1]*factor,2)+math.pow(data_dicit[hist][str(ibin)][2]*factor,2)) if math.pow(data_dicit[hist][str(ibin)][2],2) < math.pow(data_dicit[hist][str(ibin)][3],2) else math.sqrt(math.pow(data_dicit[hist][str(ibin)][1]*factor,2)+math.pow(data_dicit[hist][str(ibin)][3]*factor,2))##for 13TeV prediction, sys uncert scaled by 0.5
            else:
                error=math.sqrt(math.pow(data_dicit[hist][str(ibin)][1],2)+math.pow(data_dicit[hist][str(ibin)][2],2)) if math.pow(data_dicit[hist][str(ibin)][2],2) < math.pow(data_dicit[hist][str(ibin)][3],2) else math.sqrt(math.pow(data_dicit[hist][str(ibin)][1],2)+math.pow(data_dicit[hist][str(ibin)][3],2))
            if is_13TeV==False:
                h_data.SetBinContent(ibin,value)
            h_data.SetBinError (ibin,error)
        for ibin in range(1,h_data.GetNbinsX()+1):
            if (ibin+N_bin) > hist_out_data.GetNbinsX():print "error on number of bins"
            hist_out_data.SetBinContent(ibin+N_bin,h_data.GetBinContent(ibin))
            hist_out_Vtb .SetBinContent(ibin+N_bin,h_Vtb .GetBinContent(ibin))
            hist_out_Vts .SetBinContent(ibin+N_bin,h_Vts .GetBinContent(ibin))
            hist_out_Vtd .SetBinContent(ibin+N_bin,h_Vtd .GetBinContent(ibin))
            hist_out_data.SetBinError  (ibin+N_bin,h_data.GetBinError  (ibin))
            if is_13TeV and remove_MC_err:
                hist_out_Vtb .SetBinError  (ibin+N_bin,1e-6*h_Vtb .GetBinError  (ibin))
                hist_out_Vts .SetBinError  (ibin+N_bin,1e-6*h_Vts .GetBinError  (ibin))
                hist_out_Vtd .SetBinError  (ibin+N_bin,1e-6*h_Vtd .GetBinError  (ibin))
            else:
                hist_out_Vtb .SetBinError  (ibin+N_bin,h_Vtb .GetBinError  (ibin))
                hist_out_Vts .SetBinError  (ibin+N_bin,h_Vts .GetBinError  (ibin))
                hist_out_Vtd .SetBinError  (ibin+N_bin,h_Vtd .GetBinError  (ibin))
        N_bin=N_bin+h_data.GetNbinsX()
    if N_bin!= hist_out_data.GetNbinsX():print "different on number of bins"
    F_out.cd()
    hist_out_data.Write()
    hist_out_Vtb .Write()
    hist_out_Vts .Write()
    hist_out_Vtd .Write()
    F_out.Close()
    print "save hist done!"
    

