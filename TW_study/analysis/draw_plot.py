import math
import gc
import sys
import ROOT
from array import array
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gROOT.ProcessLine("gErrorIgnoreLevel = 1;")
ROOT.TH1.AddDirectory(ROOT.kFALSE)

def Graph_Xerror0(graph_in):
    for i in range(0,graph_in.GetN()):
        graph_in.SetPointEXlow (i, 0)
        graph_in.SetPointEXhigh(i, 0)

def get_self_err(hist, style):
    if type(hist) == ROOT.TH1D:
        gr=ROOT.TGraphAsymmErrors(hist)
        for ibin in range(0,gr.GetN()):
            if gr.GetY()[ibin] !=0:
                gr.SetPointEYlow(ibin,gr.GetErrorYlow(ibin)/gr.GetY()[ibin])
                gr.SetPointEYhigh(ibin,gr.GetErrorYhigh(ibin)/gr.GetY()[ibin])
            else:
                gr.SetPointEYlow(ibin ,0)
                gr.SetPointEYhigh(ibin,0)
            if style ==1:
                gr.SetPoint(ibin,gr.GetX()[ibin],0)
            else:
                gr.SetPoint(ibin,gr.GetX()[ibin],1)
        return gr
    elif type(hist) == ROOT.TGraphAsymmErrors:
        gr=hist.Clone(hist.GetName()+"_ratio")
        for ibin in range(0,gr.GetN()):
            if gr.GetY()[ibin] !=0:
                gr.SetPointEYlow(ibin,gr.GetErrorYlow(ibin)/gr.GetY()[ibin])
                gr.SetPointEYhigh(ibin,gr.GetErrorYhigh(ibin)/gr.GetY()[ibin])
            else:
                gr.SetPointEYlow(ibin ,0)
                gr.SetPointEYhigh(ibin,0)
            if style ==1:
                gr.SetPoint(ibin,gr.GetX()[ibin],0)
            else:
                gr.SetPoint(ibin,gr.GetX()[ibin],1)
        return gr
    else:
        print "don't match"
def get_graph_ratio(g1, g2, style):
    g_ratio=g1.Clone("g_ratio")
    for ibin in range(0, g_ratio.GetN()):
         ratio=999
         err_down=0
         err_up=0
         if float(g2.GetY()[ibin]) !=0:
             if style==1:
                 ratio=float((g1.GetY()[ibin]-g2.GetY()[ibin])/g2.GetY()[ibin])
             else:
                 ratio=float(g1.GetY()[ibin]/g2.GetY()[ibin])
             err_down=float(g1.GetErrorYlow(ibin)/g2.GetY()[ibin])
             err_up  =float(g1.GetErrorYhigh(ibin)/g2.GetY()[ibin])
         g_ratio.SetPoint(ibin,g_ratio.GetX()[ibin],ratio)
         g_ratio.SetPointEYlow(ibin,err_down)
         g_ratio.SetPointEYhigh(ibin,err_up)
    return g_ratio

def histTograph(h_data):  
    h_data_bin_value={}
    h_data_bin_width={}
    for bin in range(1, h_data.GetNbinsX()+1):
        h_data_bin_value[bin]=h_data.GetBinContent(bin)*h_data.GetBinWidth(bin) 
        h_data_bin_width[bin]=h_data.GetBinWidth(bin) 
    g_data = ROOT.TGraphAsymmErrors(h_data)
    g_data.SetMarkerSize(0.5)
    g_data.SetMarkerStyle (20)
    alpha = float(1 - 0.6827)
    hist_weight=['h_mee_all','h_mee_all_BB','h_mee_all_BE','h_mee_all_EE']
    for i in range(0,g_data.GetN()): 
        N = g_data.GetY()[i]
        error_up=0
        error_low=0
        if h_data.GetName().split("data_")[-1] in hist_weight:
            N = h_data_bin_value[i+1]
        L = 0
        if N==0:
            L=0
        else: 
            L= float( ROOT.Math.gamma_quantile(alpha/2,N,1.) )
        U =float( ROOT.Math.gamma_quantile_c(alpha/2,N+1,1) )
        error_low=N-L
        error_up=U-N
        if h_data.GetName().split("data_")[-1] in hist_weight:
            error_low= (N-L)/h_data_bin_width[i+1]
            error_up=(U-N)/h_data_bin_width[i+1]
        if N==0:
            error_up=0
            error_low=0
        g_data.SetPointEYlow (i, error_low)
        g_data.SetPointEYhigh(i, error_up)
    return g_data

def draw_plots(chan, date, dir, stack,h_mc,h_data,out_name, xaxis_name, ratio_Style, log_hist):
    stat_style=3015
    stat_color=ROOT.kOrange-3
    stat_sys_style=1001
    stat_sys_color=ROOT.kGray
    canvas = ROOT.TCanvas('canvas','',50,50,865,780)
    canvas.SetLeftMargin(0.5)
    canvas.cd()
#    size = 0.25
#    pad1 = ROOT.TPad('pad1', '', 0.0, size, 1.0, 1.0, 0)
#    pad2 = ROOT.TPad('pad2', '', 0.0, 0.0, 1.0, size, 0)
#    pad1.Draw()
#    pad2.Draw() 
#    pad2.SetGridy()
#    pad2.SetTickx()
#    pad1.SetBottomMargin(0.035)
#    pad2.SetTopMargin(0)
#    pad2.SetBottomMargin(0.35)
#    pad1.SetRightMargin(0.07)
#    pad1.SetLeftMargin(0.13)
#    pad2.SetRightMargin(0.07)
#    pad2.SetLeftMargin(0.13)
    pad1=ROOT.TPad("pad1", "pad1", 0, 0.315, 1, 0.99 , 0)#used for the hist plot
    pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.3 , 0)#used for the ratio plot
    pad1.Draw()
    pad2.Draw() 
    pad2.SetGridy()
    pad2.SetTickx()
    pad1.SetBottomMargin(0.02)
    pad1.SetLeftMargin(0.14)
    pad1.SetRightMargin(0.05)
    pad2.SetTopMargin(0.0)
    pad2.SetBottomMargin(0.4)
    pad2.SetLeftMargin(0.14)
    pad2.SetRightMargin(0.05)
    pad1.cd()
    pad1.SetLogx(ROOT.kFALSE)
    pad2.SetLogx(ROOT.kFALSE)
    pad1.SetLogy(ROOT.kFALSE)
    ########### For XY Range #############
    nbin_x=h_data.GetNbinsX()
    x_min=h_data.GetBinLowEdge(1)
    x_max=h_data.GetBinLowEdge(h_data.GetNbinsX())+h_data.GetBinWidth(h_data.GetNbinsX())
    y_min=0
    y_max=2*h_data.GetBinContent(h_data.GetMaximumBin())
    if out_name == "H_jet_low_led_CSV" or out_name=="H_jet_Bmissed_CSV": 
        x_min=0 
        y_max=4E3
    if out_name in log_hist:
        pad1.SetLogy(ROOT.kTRUE)
        y_min=1E-1
        y_max=1E3*(round(y_max/10)*10)
    dummy = ROOT.TH2F("dummy","",nbin_x,x_min,x_max,1,y_min,y_max)
    dummy.SetStats(ROOT.kFALSE)
    if h_data.GetBinWidth(1)%1 != 0:  
        dummy.GetYaxis().SetTitle('Event / %.1f'%(h_data.GetBinWidth(1)))
        if "GeV" in xaxis_name:dummy.GetYaxis().SetTitle('Event / %.1f GeV'%(h_data.GetBinWidth(1)))
    else:
        dummy.GetYaxis().SetTitle('Event / %.0f'%(h_data.GetBinWidth(1)))
        if "GeV" in xaxis_name:dummy.GetYaxis().SetTitle('Event / %.0f GeV'%(h_data.GetBinWidth(1)))
#    dummy.GetYaxis().SetTitleSize(0.05)
#    dummy.GetYaxis().SetLabelSize(0.045)
#    dummy.GetYaxis().SetTitleOffset(1.35)
#    dummy.GetXaxis().SetLabelSize(0.045)
    dummy.GetXaxis().SetLabelSize(0)
    dummy.GetXaxis().SetMoreLogLabels()
    dummy.GetXaxis().SetNoExponent() 
    dummy.GetYaxis().SetTitleOffset(0.88)
    dummy.GetYaxis().SetTitleSize(0.08)
    dummy.GetYaxis().SetLabelSize(0.04/0.7)
    steps    =["Dilepton","Z veto","MET",">=2 jets",">=1 b jet"] 
    str_njet =["(0,0)","(1,0)","(1,1)","(2,0)","(2,1)","(2,2)","(3,0)","(3,1)","(3,2)","(3,3)","(4,0)","(4,1)","(4,2)","(4,3)","(4,4)"]
    if out_name == "H_steps":
        for stp in steps:
            dummy.GetXaxis().SetBinLabel(steps.index(stp)+1,stp)
    elif out_name == "H_njet_bjet": 
        for str_j in str_njet:
            dummy.GetXaxis().SetBinLabel(str_njet.index(str_j)+1,str_j)
    dummy.Draw()
    stack.Draw('sames:hist')
    dummy.Draw("AXISSAME")
    ########### For XY Range #############
    g_data=histTograph(h_data)
    g_data.SetLineColor(ROOT.kBlack)
    g_data.SetMarkerStyle(20)
    g_data.SetMarkerSize(0.8)
    Graph_Xerror0(g_data)
    h_mc.SetFillStyle(3015)
    h_mc.SetFillColorAlpha(ROOT.kOrange-3,1.0)
#    h_mc.SetFillColor(ROOT.kRed-6)
#    h_mc.SetFillStyle(3244)
    h_mc.Draw("sames:e2")
    g_data.Draw("pZ0")
    h_tmp_ST   =h_data.Clone("ST") 
    h_tmp_ttbar=h_data.Clone("ttbar") 
    h_tmp_DY   =h_data.Clone("DY") 
    h_tmp_other=h_data.Clone("other") 
    h_tmp_uncertainty =h_mc.Clone("Uncert") 
    h_tmp_ST    .SetLineColor(ROOT.kBlack) 
    h_tmp_ttbar .SetLineColor(ROOT.kBlack) 
    h_tmp_DY    .SetLineColor(ROOT.kBlack) 
    h_tmp_other .SetLineColor(ROOT.kBlack) 
    h_tmp_ST    .SetFillColor(Files["ST"].color) 
    h_tmp_ttbar .SetFillColor(Files["TTbar"].color) 
    h_tmp_DY    .SetFillColor(Files["DYToLL_M50"].color) 
    h_tmp_other .SetFillColor(Files["WJet"].color) 
#    legend = ROOT.TLegend(0.516741, 0.61, 0.870536, 0.88, "", "brNDC")
    legend = ROOT.TLegend(0.73,0.6,0.93,0.88)
    legend.AddEntry(g_data,'Data (2016)','ep')
    legend.AddEntry(h_tmp_ST,"ST_tw",'f')
    legend.AddEntry(h_tmp_ttbar,'t#bar{t}','f')
    legend.AddEntry(h_tmp_DY,'Z+jets','f')
    legend.AddEntry(h_tmp_other,'Others','f')
    legend.AddEntry(h_tmp_uncertainty,'Stat. uncertainty','f')
    legend.SetBorderSize(0)
#    legend.SetLineColor(1)
#    legend.SetLineStyle(1)
#    legend.SetLineWidth(1)
#    legend.SetFillColor(19)
#    legend.SetFillStyle(0)
    font = 42
    legend.SetTextFont(font)
    legend.Draw()
    label_cms = ROOT.TPaveLabel(0.712, 0.811, 0.969, 0.907, "CMS", "brNDC")
    label_cms.SetBorderSize(0)
    label_cms.SetFillColor(0)
    label_cms.SetFillStyle(0)
    label_cms.SetTextFont(61)
    label_cms.SetTextSize(0.44/0.75)
#    label_cms.Draw()
    label_prelim = ROOT.TPaveLabel(0.69, 0.745, 0.96, 0.841, "Preliminary", "brNDC")
    label_prelim.SetBorderSize(0)
    label_prelim.SetFillColor(0)
    label_prelim.SetFillStyle(0)
    label_prelim.SetTextFont(51)
    label_prelim.SetTextSize(0.44/0.75 * 0.8)
#    label_prelim.Draw()
    label_lumi = ROOT.TPaveLabel(0.69, 0.902, 0.994, 0.997, "35.9 fb^{-1} (13 TeV)", "brNDC")
    label_lumi.SetBorderSize(0)
    label_lumi.SetFillColor(0)
    label_lumi.SetFillStyle(0)
    label_lumi.SetTextFont(font)
    label_lumi.SetTextSize(0.44)
#    label_lumi.Draw()
    labels_region = ROOT.TPaveLabel(0.185268, 0.812937, 0.55, 0.907343, "", "brNDC")
    labels_region.SetBorderSize(0)
    labels_region.SetFillColor(0)
    labels_region.SetFillStyle(0)
    labels_region.SetTextFont(font)
    labels_region.SetTextSize(0.5 )  
    if "ee" in chan:
        labels_region.SetLabel("e^{+}e^{-}")
#        labels_region.Draw()
    elif "emu" in chan:
        labels_region.SetLabel("e^{#pm}#mu^{#mp}")
#        labels_region.Draw()
    elif "mumu" in chan:
        labels_region.SetLabel("#mu^{+}#mu^{-}")
#        labels_region.Draw()
########################################
    Label_cms_prelim = ROOT.TPaveText(0.15,0.83,0.4,0.83,"NDC")
    Label_cms_prelim.SetLineColor(10)
    Label_cms_prelim.SetFillColor(10)
    Label_cms_prelim.SetTextSize(0.052/0.7)
    Label_cms_prelim.SetTextAlign(12)
    Label_cms_prelim.AddText("CMS Preliminary")
    Label_cms_prelim.SetShadowColor(10)
    Label_cms_prelim.Draw()
    Label_lumi = ROOT.TPaveText(0.6,0.95,0.9,0.95,"NDC")
    Label_lumi.SetLineColor(10)
    Label_lumi.SetFillColor(10)
    Label_lumi.SetTextSize(0.06/0.7)
    Label_lumi.SetTextAlign(12)
    Label_lumi.SetTextFont(42)
    #Label_lumi.AddText("35.9 fb^{-1} (13 TeV)")
    Label_lumi.AddText("%.1f fb^{-1} (13 TeV)"%(float(Lumi)/1000))
    Label_lumi.SetShadowColor(10)
    Label_lumi.Draw()
    Label_chan=ROOT.TPaveText(0.18,0.72, 0.35,0.7,"blNDC")
    Label_chan.SetBorderSize(0)
    Label_chan.SetFillStyle(0)
    Label_chan.SetTextAlign(10)
    Label_chan.SetTextColor(1)
    Label_chan.SetTextFont(32)
    Label_chan.SetTextSize(0.12)
    if "ee" in chan:
        #Label_chan.AddText ('e^{#pm}e^{#mp}')
        Label_chan.AddText ('ee')
    elif "emu" in chan:
        #Label_chan.AddText ('e^{#pm}#mu^{#mp}')
        Label_chan.AddText ('e#mu')
    elif "mumu" in chan:
        #Label_chan.AddText ('#mu^{#pm}#mu^{#mp}')
        Label_chan.AddText ('#mu#mu')
    Label_chan.Draw()
##### for ratio label #######################
#    error_data=0
#    error_mc  =0
#    for ibin in range(1,h_data.GetNbinsX()+1):
#        error_data=math.sqrt(math.pow(error_data,2)+math.pow(h_data.GetBinError(ibin),2))
#        error_mc  =math.sqrt(math.pow(error_mc  ,2)+math.pow(  h_mc.GetBinError(ibin),2))
#    ratio=h_data.GetSumOfWeights()/h_mc.GetSumOfWeights() if h_mc.GetSumOfWeights()!=0 else 0
#    error_ratio=ratio*math.sqrt(math.pow(error_data/h_data.GetSumOfWeights(),2)+math.pow(error_mc/h_mc.GetSumOfWeights(),2)) if h_data.GetSumOfWeights()!=0 and h_mc.GetSumOfWeights()!=0 else 0
#    ratio=h_data.GetSumOfWeights()/h_mc.GetSumOfWeights() if h_mc.GetSumOfWeights()!=0 else 0
#    error_ratio=ratio*math.sqrt(math.pow(error_data/h_data.GetSumOfWeights(),2)+math.pow(error_mc/h_mc.GetSumOfWeights(),2)) if h_data.GetSumOfWeights()!=0 and h_mc.GetSumOfWeights()!=0 else 0
    err_data=ROOT.Double(0)
    err_mc  =ROOT.Double(0)
    N_data= h_data.IntegralAndError(h_data.GetXaxis().FindBin(x_min+1E-4),h_data.GetXaxis().FindBin(x_max-1E-4),err_data)
    N_mc  = h_mc  .IntegralAndError(h_mc.GetXaxis().FindBin(x_min+1E-4),h_mc.GetXaxis().FindBin(x_max-1E-4),err_mc)
    ratio = N_data/N_mc if N_mc!=0 else 0
    error_ratio=ratio*math.sqrt(math.pow(err_data/N_data,2)+math.pow(err_mc/N_mc,2)) if N_data!=0 and N_mc!=0 else 0

    label_ratio = ROOT.TPaveLabel(0.5, 0.53, 0.85, 0.63, "data/mc=%.2f #pm %.2f"%(ratio,error_ratio), "brNDC")
    label_ratio.SetBorderSize(0)
    label_ratio.SetFillColor(0)
    label_ratio.SetFillStyle(0)
    label_ratio.SetTextFont(font)
    label_ratio.SetTextSize(0.44)
    label_ratio.Draw()
    ######################################
    pad2.cd()
    ratio_y_min=-0.5
    ratio_y_max=0.5
    if ratio_Style!=1:
        ratio_y_min=0.8
        ratio_y_max=1.2
    dummy_ratio = ROOT.TH2F("dummy_ratio","",nbin_x,x_min,x_max,1,ratio_y_min,ratio_y_max)
    dummy_ratio.SetStats(ROOT.kFALSE)
    dummy_ratio.GetYaxis().SetTitle('Data/Pred.')
    if ratio_Style==1:
        dummy_ratio.GetYaxis().SetTitle('(data-mc)/mc')
    dummy_ratio.GetXaxis().SetTitle(xaxis_name)
#    dummy_ratio.SetMarkerSize(0.7)
#    dummy_ratio.GetXaxis().SetTitleSize(0.14)
#    dummy_ratio.GetXaxis().SetTitleOffset(1.0)
#    dummy_ratio.GetXaxis().SetLabelSize(0.13)
#    dummy_ratio.GetYaxis().SetNdivisions(405)
#    dummy_ratio.GetYaxis().SetTitleSize(0.14)
#    dummy_ratio.GetYaxis().SetLabelSize(0.13)
#    dummy_ratio.GetYaxis().SetTitleOffset(0.35)
    dummy_ratio.GetXaxis().SetMoreLogLabels()
    dummy_ratio.GetXaxis().SetNoExponent()  
    dummy_ratio.GetXaxis().SetTitleSize(0.058/0.3)
    dummy_ratio.GetYaxis().SetTitleSize(0.045/0.3)
    dummy_ratio.GetXaxis().SetTitleFont(42)
    dummy_ratio.GetYaxis().SetTitleFont(42)
    dummy_ratio.GetXaxis().SetTickLength(0.05)
    dummy_ratio.GetYaxis().SetTickLength(0.05)
    dummy_ratio.GetXaxis().SetLabelSize(0.045/0.3)
    dummy_ratio.GetYaxis().SetLabelSize(0.04/0.3)
    dummy_ratio.GetXaxis().SetLabelOffset(0.02)
    dummy_ratio.GetYaxis().SetLabelOffset(0.01)
    dummy_ratio.GetYaxis().SetTitleOffset(0.41)
    dummy_ratio.GetXaxis().SetTitleOffset(0.23/0.25)
    dummy_ratio.GetYaxis().SetNdivisions(504)
    if out_name == "H_steps":
        for stp in steps:
            dummy_ratio.GetXaxis().SetBinLabel(steps.index(stp)+1,stp)
    elif out_name == "H_njet_bjet": 
        for str_j in str_njet:
            dummy_ratio.GetXaxis().SetBinLabel(str_njet.index(str_j)+1,str_j)
    dummy_ratio.Draw()
    g_mc    = ROOT.TGraphAsymmErrors(h_mc)
    g_ratio = get_graph_ratio(g_data, g_mc, ratio_Style)
    Graph_Xerror0(g_ratio) 
    g_mc_stat    =get_self_err(h_mc, ratio_Style)
#    g_mc_stat.SetFillColor(stat_color)
    g_mc_stat.SetFillStyle(stat_style)
    g_mc_stat.SetFillColorAlpha(ROOT.kOrange-3,1.0)
    g_mc_stat.Draw("2p")
    dummy_ratio.Draw("AXISSAME")
    g_ratio.Draw("pZ0")

    #####################################
    canvas.Print('%s/%s/%s.png'%(dir,date,out_name))    
    del canvas
    gc.collect()
     
def H2D_2H1D(h2):
    h_x=h2.ProjectionX("h_x")
    h_y=h2.ProjectionY("h_y")
    for ix in range(1, h2.GetXaxis().GetNbins()+1):
        x_value=0
        x_err  =0
        for iy in range(1, h2.GetYaxis().GetNbins()+1):
            x_value=x_value+h2.GetBinContent(ix,iy)
            x_err  =math.sqrt(math.pow(x_err,2)+math.pow(h2.GetBinError(ix,iy),2))
        h_x.SetBinContent(ix,x_value)
        h_x.SetBinError  (ix,x_err  )
    for iy in range(1, h2.GetYaxis().GetNbins()+1):
        y_value=0
        y_err  =0
        for ix in range(1, h2.GetXaxis().GetNbins()+1):
            y_value=y_value+h2.GetBinContent(ix,iy)
            y_err  =math.sqrt(math.pow(y_err,2)+math.pow(h2.GetBinError(ix,iy),2))
        h_y.SetBinContent(iy,y_value)
        h_y.SetBinError  (iy,y_err  )
    return [h_x,h_y]

def draw_graph_compare(g1,g2,out_name,chan):
    canvas = ROOT.TCanvas('canvas','',50,50,865,780)
    canvas.SetLeftMargin(0.5)
    canvas.cd()
    pad1=ROOT.TPad("pad1", "pad1", 0, 0.315, 1, 0.99 , 0)#used for the hist plot
    pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.3 , 0)#used for the ratio plot
    pad1.Draw()
    pad2.Draw() 
    pad2.SetGridy()
    pad2.SetTickx()
    pad1.SetBottomMargin(0.02)
    pad1.SetLeftMargin(0.14)
    pad1.SetRightMargin(0.05)
    pad2.SetTopMargin(0.0)
    pad2.SetBottomMargin(0.42)
    pad2.SetLeftMargin(0.14)
    pad2.SetRightMargin(0.05)
    pad1.cd()
    x_min=g1.GetX()[0]-g1.GetErrorXlow(0)
    x_max=g1.GetX()[g1.GetN()-1]+g1.GetErrorXhigh(g1.GetN()-1)
    y_min=0.97
    y_max=1.005
    if "eta" in out_name:
        y_min=0.97
        y_max=1.005
    if "pt" in out_name:
        y_min=0.92
        y_max=1.02
    dummy = ROOT.TH2D("dummy","",1,x_min,x_max,1,y_min,y_max)
    dummy.SetStats(ROOT.kFALSE)
    dummy.GetYaxis().SetTitle('Efficiency')
    dummy.GetXaxis().SetLabelSize(0)
    dummy.GetXaxis().SetMoreLogLabels()
    dummy.GetXaxis().SetNoExponent() 
    dummy.GetYaxis().SetTitleOffset(0.88)
    dummy.GetYaxis().SetTitleSize(0.08)
    dummy.GetYaxis().SetLabelSize(0.04/0.7)
    dummy.Draw()
    g1.SetMarkerColor(ROOT.kBlue)
    g1.SetMarkerStyle(8)
    g1.SetLineColor(ROOT.kBlue)
    g2.SetFillColor(ROOT.kRed-10)
    g2.SetMarkerStyle(8)
    g2.SetMarkerColor(ROOT.kRed)
    g2.SetLineColor(ROOT.kRed)
    g2.Draw("e20")
    g2.Draw("pe0")
    g1.Draw("pe0")

    legend = ROOT.TLegend(0.2,0.73,0.5,0.88)
    legend.AddEntry(g1,'Data (2016)','lep')
    legend.AddEntry(g2,"MC",'flpe')
    legend.SetBorderSize(0)
    font = 42
    legend.SetTextFont(font)
    legend.Draw()

################## ratio ########################
    pad2.cd()
    ratio_y_min=0.95
    ratio_y_max=1.05
    dummy_ratio = ROOT.TH2F("dummy_ratio","",1,x_min,x_max,1,ratio_y_min,ratio_y_max)
    dummy_ratio.SetStats(ROOT.kFALSE)
    dummy_ratio.GetYaxis().SetTitle('Scale factor')
    dummy_ratio.GetXaxis().SetMoreLogLabels()
    dummy_ratio.GetXaxis().SetNoExponent()  
    dummy_ratio.GetXaxis().SetTitleSize(0.058/0.3)
    dummy_ratio.GetYaxis().SetTitleSize(0.045/0.3)
    dummy_ratio.GetXaxis().SetTitleFont(42)
    dummy_ratio.GetYaxis().SetTitleFont(42)
    dummy_ratio.GetXaxis().SetTickLength(0.05)
    dummy_ratio.GetYaxis().SetTickLength(0.05)
    dummy_ratio.GetXaxis().SetLabelSize(0.045/0.3)
    dummy_ratio.GetYaxis().SetLabelSize(0.04/0.3)
    dummy_ratio.GetXaxis().SetLabelOffset(0.02)
    dummy_ratio.GetYaxis().SetLabelOffset(0.01)
    dummy_ratio.GetYaxis().SetTitleOffset(0.41)
    dummy_ratio.GetXaxis().SetTitleOffset(0.23/0.25)
    dummy_ratio.GetYaxis().SetNdivisions(405)
    dummy_ratio.GetXaxis().SetTitle("")
    if "pt" in out_name:
        dummy_ratio.GetXaxis().SetTitle("P_{T}^{Leading lepton} (GeV)")
        if "sub" in out_name:
            dummy_ratio.GetXaxis().SetTitle("P_{T}^{Sub-leading lepton} (GeV)")
    elif "eta" in out_name:
        str_eta=" "
        if chan=="ee":str_eta="sc" 
        print "channel:%s,%s"%(chan,str_eta)
        dummy_ratio.GetXaxis().SetTitle("#eta_{"+str_eta+"}^{Leading lepton}")
        if "sub" in out_name:
            dummy_ratio.GetXaxis().SetTitle("#eta_{"+str_eta+"}^{Sub-leading lepton}")
    elif "MET" in out_name:
        dummy_ratio.GetXaxis().SetTitle("MET(T1Txy)(GeV)")
    elif "Nvtx" in out_name:
        dummy_ratio.GetXaxis().SetTitle("Nvtx")
    elif "Njet" in out_name:
        dummy_ratio.GetXaxis().SetTitle("Number of jet")
    elif "Nbjet" in out_name:
        dummy_ratio.GetXaxis().SetTitle("Number of b jet")
    dummy_ratio.Draw()
    g_ratio=g1.Clone("ratio")
    g_ratio.SetLineColor(ROOT.kBlack)
    g_ratio.SetMarkerColor(ROOT.kBlack)
    g_ratio.SetMarkerStyle(8)
    for ir in range(0,g1.GetN()):
        ratio_value=g1.GetY()[ir]/g2.GetY()[ir] if g2.GetY()[ir] !=0 else 0
        g1_err_up  =g1.GetEYhigh()[ir]
        g1_err_down=g1.GetEYlow()[ir]
        g2_err_up  =g2.GetEYhigh()[ir]
        g2_err_down=g2.GetEYlow()[ir]
        ratio_err_up  =ratio_value*math.sqrt(math.pow(g1_err_up  /g1.GetY()[ir],2)+math.pow(g2_err_up  /g2.GetY()[ir],2)) if g1.GetY()[ir]!=0 and g2.GetY()[ir] !=0 else 0
        ratio_err_down=ratio_value*math.sqrt(math.pow(g1_err_down/g1.GetY()[ir],2)+math.pow(g2_err_down/g2.GetY()[ir],2)) if g1.GetY()[ir]!=0 and g2.GetY()[ir] !=0 else 0
        g_ratio.SetPoint(ir,g_ratio.GetX()[ir],ratio_value)
        g_ratio.SetPointEYhigh(ir,ratio_err_up  )
        g_ratio.SetPointEYlow (ir,ratio_err_down)
    g_ratio.Draw("pe0")
    fline = ROOT.TF1('fline', '[0]')
    fline.SetParameters(0,1)
    fline.SetLineColor(ROOT.kBlue)
    fline.SetLineWidth(2)
    g_ratio.Fit(fline,"","",x_min,x_max)
    fit_ratio_label = ROOT.TLatex()
    fit_ratio_label.SetTextAlign(12)
    fit_ratio_label.SetTextSize(0.09)
    fit_ratio_label.SetNDC(ROOT.kTRUE)
    fit_ratio_label.DrawLatex(0.65,0.95, '#chi^{2}/ndof    %.2f / %d'%(fline.GetChisquare(),fline.GetNDF()))
#    fit_ratio_label.DrawLatex(0.15,0.5 ,'Prob            %.3f '%(fline.GetProb()))
    fit_ratio_label.DrawLatex(0.65,0.85 ,'p0              %.3f #pm %.3f'%(fline.GetParameter(0),fline.GetParError(0)))
    canvas.Print('%s/%s/%s.png'%(dir,date,out_name))    
    del canvas
    gc.collect()


class file_object:
    def __init__(self, file_name, name, event, crosssection, color):
        self.name = name
        self.file_name = file_name
        self.event = event
        self.crosssection = crosssection
        self.lumi = self.event/self.crosssection
        self.color = color
        #self.tfilename = 'ntuples/saved_hist/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/Step1_trigger_new/%s.root'%(self.file_name)
        self.tfilename = 'ntuples/saved_hist/Step1_jetpt30/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/Step1_GH/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/Step1_noPUreweight/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/step1_new_reNvtx/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/step1_trigger/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/Step2_jetpt30_74X/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/Step2_jetpt30_74X_reNvtx/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/Step2_jetpt20_reNvtx/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/Step2_reNvtx_1j1b_new/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/Step2_reNvtx_2j1b_new/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/Step2_reNvtx_0j_1j0b_new/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/Step2_jetpt50/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/Step2_jetpt40/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/Step2_Btag_M_1j1b/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/Step2_Btag_M_2j1b/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/Step2_nvtx_reweight/%s.root'%(self.file_name)
        #self.tfilename = 'ntuples/saved_hist/step1_nvtx_30_35/%s.root'%(self.file_name)
        self.tfile = ROOT.TFile(self.tfilename,'READ')

#Channel="ee"
Channel="emu"
#Channel="mumu"
do_plot_main    =True
do_trigger_study=False

Lumi=35867
#Lumi=12610.131
#Lumi=7110.75
#Lumi=16146.177

Files={}
Files["data"]          =file_object(Channel+"_"+"hist_RunBCDEFGH"            ,"data"          , Lumi    ,1      ,ROOT.kBlack)
#Files["data"]          =file_object(Channel+"_"+"hist_RunBCD"           ,"data"          , Lumi    ,1      ,ROOT.kBlack)
#Files["data"]          =file_object(Channel+"_"+"hist_RunEF"            ,"data"           , Lumi    ,1      ,ROOT.kBlack)
#Files["data"]          =file_object(Channel+"_"+"hist_RunGH"            ,"data"          , Lumi    ,1      ,ROOT.kBlack)
Files["ST"]            =file_object(Channel+"_"+"hist_TW_top"                ,"ST"            ,3256548  ,19.47  ,ROOT.kOrange-3)
Files["ST_anti"]       =file_object(Channel+"_"+"hist_TW_antitop"            ,"ST_anti"       ,3256309  ,19.47  ,ROOT.kOrange-3)
#Files["TTbar"]         =file_object(Channel+"_"+"hist_TTTo2L2Nu"             ,"TTTo2L2Nu"     ,78353860 ,87.31  ,ROOT.TColor.GetColor("#bf1c00"))
Files["TTbar"]         =file_object(Channel+"_"+"hist_TTTo2L2Nu"             ,"TTTo2L2Nu"     ,78353860 ,87.31  ,ROOT.kRed-4)
Files["DYToLL_M10to50"]=file_object(Channel+"_"+"hist_DYJetsToLL_M10to50_amc","DYToLL_M10to50",29168419 ,18610  ,ROOT.kBlue-3)
Files["DYToLL_M50"]    =file_object(Channel+"_"+"hist_DYJetsToLL_M50_amc"    ,"DYToLL_M50"    ,81589928 ,5765.4 ,ROOT.kBlue-3)
Files["TTWJetsToQQ"]   =file_object(Channel+"_"+"hist_TTWJetsToQQ"           ,"TTWJetsToQQ"   ,303544   ,0.4062 ,ROOT.kGreen)
Files["TTWJetsToLNu"]  =file_object(Channel+"_"+"hist_TTWJetsToLNu"          ,"TTWJetsToLNu"  ,999098   ,0.2043 ,ROOT.kGreen)
Files["TTZToLLNuNu"]   =file_object(Channel+"_"+"hist_TTZToLLNuNu"           ,"TTZToLLNuNu"   ,2548448  ,0.2529 ,ROOT.kGreen)
Files["TTZToQQ"]       =file_object(Channel+"_"+"hist_TTZToQQ"               ,"TTZToQQ"       ,313867   ,0.5297 ,ROOT.kGreen)
Files["TTGJets"]       =file_object(Channel+"_"+"hist_TTGJets"               ,"TTGJets"       ,3125711  ,3.697  ,ROOT.kGreen)
Files["WJet"]          =file_object(Channel+"_"+"hist_WJet_mad"              ,"WJet"          ,57025279 ,61526.7,ROOT.kBlue)
Files["WWTo2L2Nu"]     =file_object(Channel+"_"+"hist_WWTo2L2Nu"             ,"WWTo2L2Nu"     ,1998956  ,12.178 ,ROOT.kYellow)
Files["WZ_3LNu"]       =file_object(Channel+"_"+"hist_WZ_3LNu"               ,"WZ_3LNu"       ,1993154  ,4.42965,ROOT.kGreen)
Files["WZ_2L2Q"]       =file_object(Channel+"_"+"hist_WZ_2L2Q"               ,"WZ_2L2Q"       ,15879128 ,5.595  ,ROOT.kGreen)
Files["ZZ_2L2Nu"]      =file_object(Channel+"_"+"hist_ZZ_2L2Nu"              ,"ZZ_2L2Nu"      ,8842251  ,0.564  ,ROOT.kGreen)
Files["ZZ_4L"]         =file_object(Channel+"_"+"hist_ZZTo4L"                ,"ZZ_4L"         ,6617088  ,1.212  ,ROOT.kGreen)
Files["WG_LNuG"]       =file_object(Channel+"_"+"hist_WG_LNuG"               ,"WG_LNuG"       ,6489447  ,489    ,ROOT.kRed)

Files["DYToLL_M10to50_mad"]=file_object(Channel+"_"+"hist_DYJetsToLL_M10to50_mad","DYToLL_M10to50",35192445 ,18610  ,ROOT.kBlue-3)
Files["DYToLL_M50_mad"]    =file_object(Channel+"_"+"hist_DYJetsToLL_M50_mad"    ,"DYToLL_M50"    ,49009985 ,5765.4 ,ROOT.kBlue-3)
Files["DYToEE"]            =file_object(Channel+"_"+"hist_DYToEE"                ,"DYToEE"        ,49897656 ,1921.8 ,ROOT.kBlue-3)

List_files=["WG_LNuG","ZZ_4L","ZZ_2L2Nu","WZ_2L2Q","WZ_3LNu","WWTo2L2Nu","WJet","TTGJets","TTZToQQ","TTZToLLNuNu","TTWJetsToLNu","TTWJetsToQQ","DYToLL_M50","DYToLL_M10to50","TTbar","ST_anti","ST","data"]


dir_hist={"H_Mll":"M_{ll} (GeV/c^{2})","H_Mll_Zpeak":"M_{ll} (GeV/c^{2})","H_Ptll":"Pt_{ll} (GeV/c)","H_lepton_led_pt":"P_{T}^{leading lepton} (GeV/c)","H_lepton_led_eta":"#eta^{leading lepton}","H_lepton_led_phi":"#phi^{leading lepton}","H_lepton_sub_pt":"P_{T}^{Sub-leading lepton} (GeV/c)","H_lepton_sub_eta":"#eta^{Sub-leading lepton}","H_lepton_sub_phi":"#phi^{Sub-leading lepton}","H_jet_led_pt":"P_{T}^{leading jet} (GeV/c)","H_jet_led_eta":"#eta^{leading jet}","H_jet_led_phi":"#phi^{leading jet}","H_jet_sub_pt":"P_{T}^{Sub-leading jet} (GeV/c)","H_jet_sub_eta":"#eta^{Sub-leading jet}","H_jet_sub_phi":"#phi^{Sub-leading jet}","H_jet_forward_led_pt":"P_{T}^{leading jet}(2.4<|#eta|<5.2) (GeV/c)","H_N_loose_jets":"Number of jet","H_N_loose_jets_low":"Number of jet(20<Pt<30)","H_N_b_jets":"Number of bjet","H_N_b_jets_low":"Number of bjet(20<Pt<30)","H_N_eta2p4_30_jets":"N jets(2.4<|#eta|<5.2,Pt>30)","H_N_eta2p4_40_jets":"N jets(2.4<|#eta|<5.2,Pt>40)","H_MET_Et":"MET","H_MET_phi":"MET_{#phi}","H_MET_Z_phi":"#Delta#phi(MET,ll)","H_MET_T1Txy_et":"MET(T1Txy)","H_MET_T1Txy_phi":"MET(T1Txy)_{#phi}","H_MET_Z_T1Txy_phi":"#Delta#phi(MET(T1Txy),ll)","H_MET_T1Txy_sf":"MET(T1Txy)_{significance}","H_HT_sys":"HT^{sys}","H_Pt_sys":"Pt^{sys}","H_MT_sys":"MT^{sys}","H_pv_n":"Nvtx","H_rho":"#rho","H_steps":"","H_njet_bjet":"(nJets, nBtags)","H_Ptll_phi":"#phi_{ll}","H_ll_Dphi":"#Delta#phi(ll)","H_ll_DR":"#DeltaR(ll)","H_Rll":"Rapidity(ll)","H_N_b_jets_low":"Number of bjet(20-30 GeV)","H_jet_low_led_CSV":"CSV^{Leading jet} (20<Pt<30)","H_jet_Bmissed_CSV":"CSV(jet in 2j1t)","H_HT":"HT"}


date="20170427"
dir="./plots"
ratio_style=2# 1:(data-mc)/mc,other data/mc
#print_hist_name="H_Mll"
#log_hist_name=["H_jet_low_led_CSV","H_jet_forward_led_pt","H_Mll","H_Mll_Zpeak"]
log_hist_name=["H_jet_forward_led_pt"]
print_hist_name=["H_njet_bjet"]

Save_hist=["H_pv_n"]

if do_plot_main:
    f_out=ROOT.TFile("Saved.root","RECREATE")
    for hist in dir_hist:
        if Files["data"].tfile.Get(hist):
            h_data=Files["data"].tfile.Get(hist)
            h_data.Sumw2()
            h_data.SetStats(0)
            h_mc =h_data.Clone("h_sum_mc")
            h_mc.Sumw2()
            h_mc.Scale(0)
            stack=ROOT.THStack()
            for File in List_files:
                if File=="data":continue
                scale=float(Lumi/Files[File].lumi)
                h_tmp=Files[File].tfile.Get(hist)
                h_tmp.Sumw2()
                h_tmp.SetStats(0)
                h_tmp.SetLineColor(Files[File].color)
                h_tmp.SetFillColor(Files[File].color)
                h_tmp.Scale(scale)
                h_mc.Add(h_tmp)
                stack.Add(h_tmp)
                err=ROOT.Double(0)
                if hist in print_hist_name:print "%s:%s: %.1f #pm %.1f"%(hist,File,h_tmp.IntegralAndError(1,h_tmp.GetNbinsX(),err),err)
                if hist in print_hist_name:print "%s:%s: %.1f , %.1f"  %(hist,File,h_tmp.GetBinContent(3),h_tmp.GetBinContent(5))
            if hist in print_hist_name:
                print "%s: total exp: %.1f #pm %.1f"%(hist,h_mc.IntegralAndError(1,h_mc.GetNbinsX(),err),err)
                print "%s: data     : %.1f #pm %.1f"%(hist,h_data.IntegralAndError(1,h_data.GetNbinsX(),err),err)
            draw_plots(Channel, date, dir, stack, h_mc, h_data, hist, dir_hist[hist], ratio_style,log_hist_name)
            if hist in Save_hist:
                f_out.cd()
                h_data.Scale(1/h_data.GetSumOfWeights())
                h_mc  .Scale(1/h_mc  .GetSumOfWeights())
                h_data.Divide(h_mc)
                h_data.Write()
    f_out.Close()   
    print "Plotting Done!!"
        

if do_trigger_study:
    Files_trig={}
    Files_trig["data" ]         =file_object(Channel+"_"+"trig_hist_RunBCDEFGH"            ,"data"          , Lumi    ,1      ,ROOT.kBlack)
    Files_trig["mc"]         =file_object(Channel+"_"+"trig_hist_TTTo2L2Nu"             ,"TTTo2L2Nu"     ,78353860 ,87.31  ,ROOT.kRed-4)
    #Files_trig["data" ]         =file_object(Channel+"_"+"trig_old_hist_RunBCDEFGH"            ,"data"          , Lumi    ,1      ,ROOT.kBlack)
    #Files_trig["data" ]         =file_object(Channel+"_"+"trig_old_hist_RunBCDE"            ,"data"          , Lumi    ,1      ,ROOT.kBlack)
    #Files_trig["data" ]         =file_object(Channel+"_"+"trig_old_hist_RunFGH"            ,"data"          , Lumi    ,1      ,ROOT.kBlack)
    #Files_trig["mc"]         =file_object(Channel+"_"+"trig_old_hist_TTTo2L2Nu"             ,"TTTo2L2Nu"     ,78353860 ,87.31  ,ROOT.kRed-4)
    hist_list=['H2_pt1_pt2','H2_MET_Nvtx','H2_Njet_Nbjet']
    if   Channel=="ee"  :
        hist_list.append('H2_ee_eta1_eta2')
        hist_list.append('H_ee_region')
    elif Channel=="emu" :
        hist_list.append('H2_emu_eta1_eta2')
        hist_list.append('H_emu_region')
    elif Channel=="mumu":
        hist_list.append('H2_mumu_eta1_eta2')
        hist_list.append('H_mumu_region')

    for hname in hist_list:
        if "region" not in hname:
            h_2D_data     =Files_trig["data" ].tfile.Get(hname)
            h_2D_mc       =Files_trig["mc" ].tfile.Get(hname)
            h_2D_data_pass=Files_trig["data" ].tfile.Get(hname+"_pass")
            h_2D_mc_pass  =Files_trig["mc" ].tfile.Get(hname+"_pass")
            h_data_x      =H2D_2H1D(h_2D_data)[0] 
            h_data_y      =H2D_2H1D(h_2D_data)[1] 
            h_mc_x        =H2D_2H1D(h_2D_mc)[0] 
            h_mc_y        =H2D_2H1D(h_2D_mc)[1] 
            h_data_pass_x =H2D_2H1D(h_2D_data_pass)[0] 
            h_data_pass_y =H2D_2H1D(h_2D_data_pass)[1] 
            h_mc_pass_x   =H2D_2H1D(h_2D_mc_pass)[0] 
            h_mc_pass_y   =H2D_2H1D(h_2D_mc_pass)[1] 
            eff_data_x = ROOT.TGraphAsymmErrors()
            eff_data_y = ROOT.TGraphAsymmErrors()
            eff_mc_x   = ROOT.TGraphAsymmErrors()
            eff_mc_y   = ROOT.TGraphAsymmErrors()
            eff_data_x.Divide(h_data_pass_x,h_data_x,"cl=0.683 b(1,1) mode")
            eff_data_y.Divide(h_data_pass_y,h_data_y,"cl=0.683 b(1,1) mode")
            eff_mc_x  .Divide(h_mc_pass_x  ,h_mc_x  ,"cl=0.683 b(1,1) mode")
            eff_mc_y  .Divide(h_mc_pass_y  ,h_mc_y  ,"cl=0.683 b(1,1) mode")
            out_name1="_unname1"
            out_name2="_unname2"
            if "eta" in hname:
                out_name1="lead_eta"
                out_name2="sub_eta"
            elif "pt" in hname:
                out_name1="lead_pt"
                out_name2="sub_pt"
            elif "MET" in hname:
                out_name1="MET"
                out_name2="Nvtx"
            elif "Njet" in hname:
                out_name1="Njet"
                out_name2="Nbjet"
            draw_graph_compare(eff_data_x,eff_mc_x,out_name1,Channel)
            draw_graph_compare(eff_data_y,eff_mc_y,out_name2,Channel)

            can = ROOT.TCanvas('can','',50,50,865,780)
            can.cd()
            h_data_x.Draw("hist")
            h_data_pass_x.Draw("same:pe")
            can.Print('%s/%s/%s.png'%(dir,date,hname+"_data_x"))    
            can.Clear()
            h_data_y.Draw("hist")
            h_data_pass_y.Draw("same:pe")
            can.Print('%s/%s/%s.png'%(dir,date,hname+"_data_y"))    
            can.Clear()
            h_mc_x.Draw("hist")
            h_mc_pass_x.Draw("same:pe")
            can.Print('%s/%s/%s.png'%(dir,date,hname+"_mc_x"))    
            can.Clear()
            h_mc_y.Draw("hist")
            h_mc_pass_y.Draw("same:pe")
            can.Print('%s/%s/%s.png'%(dir,date,hname+"_mc_y"))    
            del can
            gc.collect()
        else:
            h_data     =Files_trig["data" ].tfile.Get(hname)
            h_data_pass=Files_trig["data" ].tfile.Get(hname+"_pass")
            h_mc       =Files_trig["mc" ].tfile.Get(hname)
            h_mc_pass  =Files_trig["mc" ].tfile.Get(hname+"_pass")
            eff_data   = ROOT.TGraphAsymmErrors()
            eff_mc     = ROOT.TGraphAsymmErrors()
            eff_data  .Divide(h_data_pass,h_data  ,"cl=0.683 b(1,1) mode")
            eff_mc    .Divide(h_mc_pass  ,h_mc  ,"cl=0.683 b(1,1) mode")
            print "|%s    | BB                 | BE                 | EE                 |   BB+BE+EE   |"%(Channel)
            print "| data |",
            for ix in range(0,eff_data.GetN()):
                print " %.3f +%.3f/-%.3f |"%(eff_data.GetY()[ix],eff_data.GetErrorYhigh(ix),eff_data.GetErrorYlow(ix)),
            print "\n"
            print "| MC   |",
            for ix in range(0,eff_mc.GetN()):
                print " %.3f +%.3f/-%.3f |"%(eff_mc.GetY()[ix],eff_mc.GetErrorYhigh(ix),eff_mc.GetErrorYlow(ix)),
            print "\n"
            print "| sf   |",
            for ir in range(0,eff_mc.GetN()):
                ratio_value  =eff_data.GetY()[ir]/eff_mc.GetY()[ir] if eff_mc.GetY()[ir] !=0 else 0
                data_err_up  =eff_data.GetEYhigh()[ir]
                data_err_down=eff_data.GetEYlow()[ir]
                mc_err_up    =eff_mc.GetEYhigh()[ir]
                mc_err_down  =eff_mc.GetEYlow()[ir]
                ratio_err_up  =ratio_value*math.sqrt(math.pow(data_err_up  /eff_data.GetY()[ir],2)+math.pow(mc_err_up  /eff_mc.GetY()[ir],2)) if eff_data.GetY()[ir]!=0 and eff_mc.GetY()[ir] !=0 else 0
                ratio_err_down=ratio_value*math.sqrt(math.pow(data_err_down/eff_data.GetY()[ir],2)+math.pow(mc_err_down/eff_mc.GetY()[ir],2)) if eff_data.GetY()[ir]!=0 and eff_mc.GetY()[ir] !=0 else 0
                print " %.3f +%.3f/-%.3f |"%(ratio_value,ratio_err_up,ratio_err_down),
            print "\n"
            print "trigger sf table done!" 
