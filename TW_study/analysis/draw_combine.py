import ROOT
import gc
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.TH1.AddDirectory(ROOT.kFALSE)

def remove_zero_point(graph):
    for i in range(graph.GetN()-1,-1,-1):
        if graph.GetY()[i]==0:graph.RemovePoint(i)

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

def Graph_Xerror0(graph_in):
    for i in range(0,graph_in.GetN()):
        graph_in.SetPointEXlow (i, 0)
        graph_in.SetPointEXhigh(i, 0)

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

def draw_plots(chan, date, dir, stack,h_mc,h_data, g_stat_sys ,out_name, xaxis_name, ratio_Style, log_hist):
    stat_style=3015
    stat_color=ROOT.kOrange-3
    stat_sys_style=1001
    stat_sys_color=ROOT.kGray
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
    pad1.SetRightMargin(0.01)
    pad2.SetTopMargin(0.0)
    pad2.SetBottomMargin(0.4)
    pad2.SetLeftMargin(0.14)
    pad2.SetRightMargin(0.01)
    pad1.cd()
    pad1.SetLogx(ROOT.kFALSE)
    pad2.SetLogx(ROOT.kFALSE)
    pad1.SetLogy(ROOT.kFALSE)
    ########### For XY Range #############
    nbin_x=h_data.GetNbinsX()
    x_min=h_data.GetBinLowEdge(1)
    x_max=h_data.GetBinLowEdge(h_data.GetNbinsX())+h_data.GetBinWidth(h_data.GetNbinsX())
    y_min=0
    y_max=1.5*h_data.GetBinContent(h_data.GetMaximumBin())
    dummy = ROOT.TH2F("dummy","",nbin_x,x_min,x_max,1,y_min,y_max)
    dummy.SetStats(ROOT.kFALSE)
    dummy.GetYaxis().SetTitle('Events')
    dummy.GetXaxis().SetLabelSize(0)
    dummy.GetXaxis().SetMoreLogLabels()
    dummy.GetXaxis().SetNoExponent() 
    dummy.GetYaxis().SetTitleOffset(0.88)
    dummy.GetYaxis().SetTitleSize(0.08)
    dummy.GetYaxis().SetLabelSize(0.04/0.7)
    str_njet_limit_emu=["e#mu(0,0)","e#mu(1,0)","e#mu(1,1)","e#mu(#geq2,1)","e#mu(#geq2,2)"]
    str_njet_limit_ee=["ee(1,1)","ee(#geq2,1)","ee(#geq2,2)"]
    str_njet_limit_mumu=["#mu#mu(1,1)","#mu#mu(#geq2,1)","#mu#mu(#geq2,2)"]
    str_njet_limit_emu.extend(str_njet_limit_ee)
    str_njet_limit_emu.extend(str_njet_limit_mumu)
    if out_name == "H_Limit_N_jet_bjet_combined": 
        for ibin in range(1,nbin_x+1):
            dummy.GetXaxis().SetBinLabel(ibin,str_njet_limit_emu[ibin-1])
    dummy.Draw()
    stack.Draw('sames:hist')
    dummy.Draw("AXISSAME")
    ########### For XY Range #############
    g_data=histTograph(h_data)
    g_data.SetLineColor(ROOT.kBlack)
    g_data.SetMarkerStyle(20)
    g_data.SetMarkerSize(0.8)
    Graph_Xerror0(g_data)
    g_data_clone=g_data.Clone(g_data.GetName()+"_clone")
    remove_zero_point(g_data_clone)
    h_mc.SetFillStyle(3015)
    h_mc.SetFillColorAlpha(ROOT.kOrange-3,1.0)
    g_stat_sys.SetFillStyle(3015)
    g_stat_sys.SetFillColorAlpha(ROOT.kBlue-3,1.0)
    g_stat_sys.Draw("2p")
    h_mc.Draw("sames:e2")
    if remove_data==False:
        g_data_clone.Draw("pZ0")
    h_tmp_ST   =h_data.Clone("ST") 
    h_tmp_ttbar=h_data.Clone("ttbar") 
    h_tmp_DY   =h_data.Clone("DY") 
    h_tmp_other=h_data.Clone("other") 
    h_tmp_ss   =h_data.Clone("Jets") 
    h_tmp_uncertainty     =h_mc.Clone("stat_Uncert") 
    h_tmp_all_uncertainty =g_stat_sys.Clone("sys_Uncert") 
    h_tmp_ST    .SetLineColor(ROOT.kBlack) 
    h_tmp_ttbar .SetLineColor(ROOT.kBlack) 
    h_tmp_DY    .SetLineColor(ROOT.kBlack) 
    h_tmp_other .SetLineColor(ROOT.kBlack) 
    h_tmp_ss    .SetLineColor(ROOT.kBlack) 
    h_tmp_ST    .SetFillColor(MC_Sample["TW_top"]) 
    h_tmp_ttbar .SetFillColor(MC_Sample["TTTo2L2Nu"]) 
    h_tmp_DY    .SetFillColor(MC_Sample["DYJetsToLL_M50_amc"]) 
    h_tmp_other .SetFillColor(MC_Sample["WWTo2L2Nu"]) 
    h_tmp_ss    .SetFillColor(MC_Sample["WJet_mad"]) 
    legend = ROOT.TLegend(0.73,0.6,0.93,0.88)
    legend.AddEntry(g_data,'Data (2016)','ep')
    legend.AddEntry(h_tmp_ST,"ST_tw",'f')
    legend.AddEntry(h_tmp_ttbar,'t#bar{t}','f')
    legend.AddEntry(h_tmp_DY,'Z+jets','f')
    legend.AddEntry(h_tmp_other,'Others','f')
    if do_same_sign:
        legend.AddEntry(h_tmp_ss,   'Jets','f')
    legend.AddEntry(h_tmp_uncertainty,'Stat. uncertainty','f')
    legend.AddEntry(h_tmp_all_uncertainty,'Syst. uncertainty','f')
    legend.SetBorderSize(0)
    font = 42
    legend.SetTextFont(font)
    legend.Draw()
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
        Label_chan.AddText ('ee')
    elif "emu" in chan:
        Label_chan.AddText ('e#mu')
    elif "mumu" in chan:
        Label_chan.AddText ('#mu#mu')
    Label_chan.Draw()
    Label_region=ROOT.TPaveText(0.18,0.62, 0.35,0.6,"blNDC")
    Label_region.SetBorderSize(0)
    Label_region.SetFillStyle(0)
    Label_region.SetTextAlign(10)
    Label_region.SetTextColor(1)
    Label_region.SetTextFont(32)
    Label_region.SetTextSize(0.08)
    if "1j0b" in out_name: 
        Label_region.AddText('(1jet,0bjet)')
    elif "1j1b" in out_name: 
        Label_region.AddText('(1jet,1bjet)')
    elif "2j1b" in out_name: 
        Label_region.AddText('(2jet,1bjet)')
    elif "2j2b" in out_name: 
        Label_region.AddText('(2jet,2bjet)')
    Label_region.Draw()
##### for ratio #######################
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
    dummy_ratio.GetXaxis().SetMoreLogLabels()
    dummy_ratio.GetXaxis().SetNoExponent()  
    dummy_ratio.GetXaxis().SetTitleSize(0.058/0.3)
    dummy_ratio.GetYaxis().SetTitleSize(0.045/0.3)
    dummy_ratio.GetXaxis().SetTitleFont(42)
    dummy_ratio.GetYaxis().SetTitleFont(42)
    dummy_ratio.GetXaxis().SetTickLength(0.05)
    dummy_ratio.GetYaxis().SetTickLength(0.05)
    dummy_ratio.GetXaxis().SetLabelSize(0.035/0.3)
    dummy_ratio.GetYaxis().SetLabelSize(0.04/0.3)
    dummy_ratio.GetXaxis().SetLabelOffset(0.02)
    dummy_ratio.GetYaxis().SetLabelOffset(0.01)
    dummy_ratio.GetYaxis().SetTitleOffset(0.41)
    dummy_ratio.GetXaxis().SetTitleOffset(0.23/0.25)
    dummy_ratio.GetXaxis().CenterLabels()
    dummy_ratio.GetYaxis().SetNdivisions(504)
    if out_name == "H_Limit_N_jet_bjet_combined": 
        for ibin in range(1,nbin_x+1):
            dummy_ratio.GetXaxis().SetBinLabel(ibin,str_njet_limit_emu[ibin-1])
    dummy_ratio.Draw()
    g_mc    = ROOT.TGraphAsymmErrors(h_mc)
    g_ratio = get_graph_ratio(g_data, g_mc, ratio_Style)
    Graph_Xerror0(g_ratio) 
    g_mc_stat    =get_self_err(h_mc      , ratio_Style)
    g_mc_stat_sys=get_self_err(g_stat_sys, ratio_Style)
    g_mc_stat.SetFillStyle(stat_style)
    g_mc_stat.SetFillColorAlpha(ROOT.kOrange-3,1.0)
    g_mc_stat_sys.SetFillStyle(stat_style)
    g_mc_stat_sys.SetFillColorAlpha(ROOT.kBlue-3,1.0)
    g_mc_stat_sys.Draw("2p")
    g_mc_stat.Draw("2p")
    dummy_ratio.Draw("AXISSAME")
    if remove_data==False:
        g_ratio.Draw("pZ0")
    #####################################
    canvas.Print('%s/%s/%s.png'%(dir,date,out_name))    
    del canvas
    gc.collect()


do_same_sign=True
remove_data =False
 
dir_out="./combine_out"
date="20170614"
MC_Sample={}
MC_Sample["TW_top"                ]=ROOT.kOrange-3
MC_Sample["TW_antitop"            ]=ROOT.kOrange-3
MC_Sample["TTTo2L2Nu"             ]=ROOT.kRed-4
MC_Sample["DYJetsToLL_M10to50_amc"]=ROOT.kBlue-3
MC_Sample["DYJetsToLL_M50_amc"    ]=ROOT.kBlue-3
MC_Sample["TTWJetsToQQ"           ]=ROOT.kGreen
MC_Sample["TTWJetsToLNu"          ]=ROOT.kGreen
MC_Sample["TTZToLLNuNu"           ]=ROOT.kGreen
MC_Sample["TTZToQQ"               ]=ROOT.kGreen
MC_Sample["TTGJets"               ]=ROOT.kGreen
MC_Sample["WJet_mad"              ]=ROOT.kGreen
if do_same_sign:
    MC_Sample["WJet_mad"              ]=ROOT.kYellow
MC_Sample["WWTo2L2Nu"             ]=ROOT.kGreen
MC_Sample["WZ_3LNu"               ]=ROOT.kGreen
MC_Sample["WZ_2L2Q"               ]=ROOT.kGreen
MC_Sample["ZZ_2L2Nu"              ]=ROOT.kGreen
MC_Sample["ZZ_4L"                 ]=ROOT.kGreen
MC_Sample["WG_LNuG"               ]=ROOT.kGreen
sample_list=["WJet_mad","WG_LNuG","ZZ_4L","ZZ_2L2Nu","WZ_2L2Q","WZ_3LNu","WWTo2L2Nu","TTGJets","TTZToQQ","TTZToLLNuNu","TTWJetsToLNu","TTWJetsToQQ","DYJetsToLL_M50_amc","DYJetsToLL_M10to50_amc","TTTo2L2Nu","TW_antitop","TW_top"]

Lumi=35867

dict_hist={}
str_extra="_Limit_plot"
Channels=["ee","emu","mumu"]
F_in = ROOT.TFile("./ee" +str_extra+".root","READ")
for ih in range(0,F_in.GetListOfKeys().GetSize()):
    hname=F_in.GetListOfKeys()[ih].GetName()
    if hname == "sys_stat_err":continue
    h_combine=ROOT.TH1D("combine_%s"%(hname),"",11,0,11) 
    h_combine.SetStats(ROOT.kFALSE)
    for chan in Channels:
        File = ROOT.TFile("./"+chan+str_extra+".root","READ")
        h_tmp=File.Get(hname)
        if chan == "emu":
            for ibin in range(1,6):
                h_combine.SetBinContent(ibin,h_tmp.GetBinContent(ibin)) 
                h_combine.SetBinError  (ibin,h_tmp.GetBinError  (ibin)) 
        elif chan == "ee":
            for ibin in range(6,9):
                h_combine.SetBinContent(ibin,h_tmp.GetBinContent(ibin-3)) 
                h_combine.SetBinError  (ibin,h_tmp.GetBinError  (ibin-3)) 
        elif chan == "mumu":
            for ibin in range(9,12):
                h_combine.SetBinContent(ibin,h_tmp.GetBinContent(ibin-6)) 
                h_combine.SetBinError  (ibin,h_tmp.GetBinError  (ibin-6)) 
        File.Close()
    dict_hist[hname]=h_combine
F_in.Close()
gr_sys_stat=ROOT.TGraphAsymmErrors(dict_hist["data"]).Clone("combine_sys_stat")
for chan in Channels:
    File = ROOT.TFile("./"+chan+str_extra+".root","READ")
    gr_tmp=File.Get("sys_stat_err")
    if chan == "emu":
        for iN in range(0,5):
            gr_sys_stat.SetPoint(iN,gr_sys_stat.GetX()[iN],gr_tmp.GetY()[iN])
            gr_sys_stat.SetPointEYhigh(iN,gr_tmp.GetEYhigh()[iN])
            gr_sys_stat.SetPointEYlow (iN,gr_tmp.GetEYlow()[iN])
    elif chan == "ee":
        for iN in range(5,8):
            gr_sys_stat.SetPoint(iN,gr_sys_stat.GetX()[iN],gr_tmp.GetY()[iN-3])
            gr_sys_stat.SetPointEYhigh(iN,gr_tmp.GetEYhigh()[iN-3])
            gr_sys_stat.SetPointEYlow (iN,gr_tmp.GetEYlow()[iN-3])
    elif chan == "mumu":
        for iN in range(8,11):
            gr_sys_stat.SetPoint(iN,gr_sys_stat.GetX()[iN],gr_tmp.GetY()[iN-6])
            gr_sys_stat.SetPointEYhigh(iN,gr_tmp.GetEYhigh()[iN-6])
            gr_sys_stat.SetPointEYlow (iN,gr_tmp.GetEYlow()[iN-6])
    File.Close()
h_sum_mc=dict_hist["data"].Clone("sum_mc")
h_sum_mc.Scale(0)
stack=ROOT.THStack()
for hname in sample_list:
   dict_hist[hname].SetStats(0)
   dict_hist[hname].SetLineColor(MC_Sample[hname])
   dict_hist[hname].SetFillColor(MC_Sample[hname])
   h_sum_mc.Add(dict_hist[hname])
   stack.Add(dict_hist[hname])

print "begin draw plot.."
draw_plots("combined", date, dir_out, stack,h_sum_mc,dict_hist["data"], gr_sys_stat ,"H_Limit_N_jet_bjet_combined", "(nJets,nBtags)", 0, [])
print "done draw plot!"
