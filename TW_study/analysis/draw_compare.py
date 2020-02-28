import ROOT
import gc
import math
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.TH1.AddDirectory(ROOT.kFALSE)

def draw_compare(h_1,h_2,h_3, ratio_style, label_legend1,label_legend2,label_legend3,chan,sample, Nvtx):
    canvas = ROOT.TCanvas('canvas','',100,100,1000,1000)
    canvas.cd()
    size = 0.25
    pad1 = ROOT.TPad('pad1', '', 0.0, size, 1.0, 1.0, 0)
    pad2 = ROOT.TPad('pad2', '', 0.0, 0.0, 1.0, size, 0)
    pad1.Draw()
    pad2.Draw() 
#    pad1.SetGridy()
    pad2.SetGridy()
    pad1.SetBottomMargin(0.07)
    pad2.SetTopMargin(0)
    pad2.SetBottomMargin(0.35)
    pad1.SetRightMargin(0.07)
    pad1.SetLeftMargin(0.13)
    pad2.SetRightMargin(0.07)
    pad2.SetLeftMargin(0.13)
    pad1.cd()
#    pad1.SetLogx()
#    pad1.SetLogy()
    pad1.SetTicky()
#    pad2.SetLogx()
    pad2.SetTicky()
    nbin=1
    x_min=0
    x_max=200
    y_min=0
    y_max=8E6
    y_max=1.5*h_1.GetBinContent(h_1.GetMaximumBin())
    dummy = ROOT.TH2D("dummy","",nbin,x_min,x_max,1,y_min,y_max)
    dummy.SetStats(ROOT.kFALSE)
    dummy_X_title='MET [GeV]'
    dummy_Y_title='Events / %.1f GeV'%(h_1.GetBinWidth(1))
    dummy.GetYaxis().SetTitle(dummy_Y_title)
    dummy.GetYaxis().SetTitleSize(0.05)
    dummy.GetYaxis().SetLabelSize(0.045)
    dummy.GetYaxis().SetTitleOffset(1.3)
    dummy.GetXaxis().SetTitle("")
    dummy.GetXaxis().SetLabelSize(0.045)
    dummy.GetXaxis().SetMoreLogLabels()
    dummy.GetXaxis().SetNoExponent()  
    dummy.Draw()
    h_1.SetMarkerColor(ROOT.kBlack)
    h_1.SetLineColor(ROOT.kBlack)
    h_1.SetMarkerStyle(20)
    h_1.SetMarkerSize(0.8)
    h_2.SetLineColor(ROOT.kRed)
    h_2.SetMarkerColor(ROOT.kRed)
    h_2.SetMarkerStyle(4)
    h_2.SetMarkerSize(0.8)
    h_3.SetLineColor(ROOT.kBlue)
    h_3.SetMarkerColor(ROOT.kBlue)
    h_3.SetMarkerStyle(4)
    h_3.SetMarkerSize(0.8)
    h_1.Draw("same:pe")
    h_2.Draw("same:hist")
    h_3.Draw("same:hist")
    dummy.Draw("AXISSAME")
    legend = ROOT.TLegend(0.6, 0.55, 0.90, 0.85, "", "brNDC")
    legend.AddEntry(h_1  ,label_legend1 ,'epl')
    legend.AddEntry(h_2  ,label_legend2 ,'l' )
    legend.AddEntry(h_3  ,label_legend3 ,'l' )
    legend.SetBorderSize(0)
    legend.SetLineColor(1)
    legend.SetLineStyle(1)
    legend.SetLineWidth(1)
    legend.SetFillColor(19)
    legend.SetFillStyle(0)
    font = 42
    legend.SetTextFont(font)
    legend.Draw()
    lable_y_min=0.88
    lable_y_max=0.95
    label_cms = ROOT.TPaveLabel(0.20, lable_y_min, 0.25, lable_y_max, "CMS", "brNDC")
    label_cms.SetBorderSize(0)
    label_cms.SetFillColor(0)
    label_cms.SetFillStyle(0)
    label_cms.SetTextFont(61)
    label_cms.SetTextSize(0.44/0.75)
    label_cms.Draw()
    label_prelim = ROOT.TPaveLabel(0.28, lable_y_min, 0.4, lable_y_max, "Preliminary", "brNDC")
    label_prelim.SetBorderSize(0)
    label_prelim.SetFillColor(0)
    label_prelim.SetFillStyle(0)
    label_prelim.SetTextFont(51)
    label_prelim.SetTextSize(0.44/0.75 * 0.8)
    label_prelim.Draw()
    label_lumi = ROOT.TPaveLabel(0.65, lable_y_min, 0.95, lable_y_max, "35.9 fb^{-1} (13 TeV)", "brNDC")
    label_lumi.SetBorderSize(0)
    label_lumi.SetFillColor(0)
    label_lumi.SetFillStyle(0)
    label_lumi.SetTextFont(font)
    label_lumi.SetTextSize(0.44)
    label_lumi.Draw()
    labels_region = ROOT.TPaveLabel(0.285268, 0.812937, 0.627902, 0.907343, "", "brNDC")
    labels_region.SetBorderSize(0)
    labels_region.SetFillColor(0)
    labels_region.SetFillStyle(0)
    labels_region.SetTextFont(font)
    labels_region.SetTextSize(0.425926 )  
    labels_region.SetLabel("DY(No Nvtx reweighting)")
    if chan=="ee":
       labels_region.SetLabel("ee : %s(%s reweighting)"%(sample,Nvtx))
    elif chan=="emu":
       labels_region.SetLabel("e#mu : %s(%s reweighting)"%(sample,Nvtx))
    elif chan=="mumu":
       labels_region.SetLabel("#mu#mu : %s(%s reweighting)"%(sample,Nvtx))
    labels_region.Draw()
    if "BB" in h_1.GetName():
        labels_region.SetLabel("Barrel-Barrel")
        labels_region.Draw()
    elif "BE" in h_1.GetName():
        labels_region.SetLabel("Barrel-Endcap")
        labels_region.Draw()
    elif "EE" in h_1.GetName():
        labels_region.SetLabel("Endcap-Endcap")
        labels_region.Draw()
    err_h1=ROOT.Double(0)
    err_h2=ROOT.Double(0)
    N_h1  = h_1.IntegralAndError(h_1.GetXaxis().FindBin(x_min+1E-4),h_1.GetXaxis().FindBin(x_max-1E-4),err_h1)
    N_h2  = h_2.IntegralAndError(h_2.GetXaxis().FindBin(x_min+1E-4),h_2.GetXaxis().FindBin(x_max-1E-4),err_h2)
    ratio = N_h1/N_h2 if N_h2!=0 else 0
    error_ratio=ratio*math.sqrt(math.pow(err_h1/N_h1,2)+math.pow(err_h2/N_h2,2)) if N_h1!=0 and N_h2!=0 else 0
    label_ratio_x_min=0.6
    label_ratio_x_max=0.85
    label_ratio_y_min=0.5
    label_ratio_y_max=0.6
    label_ratio = ROOT.TPaveLabel(label_ratio_x_min, label_ratio_y_min, label_ratio_x_max, label_ratio_y_max, "data/mc=%.3f #pm %.3f"%(ratio,error_ratio), "brNDC")
    label_ratio.SetBorderSize(0)
    label_ratio.SetFillColor(0)
    label_ratio.SetFillStyle(0)
    label_ratio.SetTextFont(font)
    label_ratio.SetTextSize(0.44)
#    label_ratio.Draw()
    pad2.cd()
    ratio_y_min=0.5
    ratio_y_max=1.5
    dummy_ratio = ROOT.TH2D("dummy_ratio","",nbin,x_min,x_max,1,ratio_y_min,ratio_y_max)
    dummy_ratio.SetStats(ROOT.kFALSE)
    dummy_ratio.GetYaxis().SetTitle('Ratio')
    dummy_ratio.GetYaxis().CenterTitle()
    dummy_ratio.GetXaxis().SetTitle(dummy_X_title)
    dummy_ratio.SetMarkerSize(0.7)
    dummy_ratio.GetXaxis().SetTitleSize(0.14)
    dummy_ratio.GetXaxis().SetTitleOffset(1.1)
    dummy_ratio.GetXaxis().SetLabelSize(0.13)
    dummy_ratio.GetXaxis().SetMoreLogLabels()
    dummy_ratio.GetXaxis().SetNoExponent()  
    dummy_ratio.GetYaxis().SetNdivisions(405)
    dummy_ratio.GetYaxis().SetTitleSize(0.14)
    dummy_ratio.GetYaxis().SetLabelSize(0.13)
    dummy_ratio.GetYaxis().SetTitleOffset(0.38)
    dummy_ratio.Draw()
    if ratio_style==1:
        graph_eff = ROOT.TGraphAsymmErrors()
        graph_eff.Divide(h_2,h_1,"cl=0.683 b(1,1) mode")
        graph_eff.SetMarkerStyle(7)
        graph_eff.Draw('pZ0')
    else:
        h_ratio2=h_2.Clone("ratio_%s"%(h_2.GetName()))
        h_ratio3=h_3.Clone("ratio_%s"%(h_3.GetName()))
        h_ratio2.Divide(h_1)
        h_ratio3.Divide(h_1)
        h_ratio2.SetMarkerStyle(7)
        h_ratio3.SetMarkerStyle(7)
        h_ratio2.Draw('same:pe')
        h_ratio3.Draw('same:pe')
    dummy_ratio.Draw("AXISSAME")
    canvas.Print('./compare_plots/%s.png'%(h_1.GetName()))    
    del canvas
    gc.collect()

Lumi=35867
MC_Sample={}
MC_Sample["DYJetsToLL_M10to50_amc"]=[29332494 ,18610  ]
MC_Sample["DYJetsToLL_M50_amc"    ]=[68009629 ,5765.4 ]
MC_Sample["TW_top"                ]=[8609398  ,19.47  ]
MC_Sample["TW_antitop"            ]=[8681265  ,19.47  ]
MC_Sample["TTTo2L2Nu"             ]=[64910035 ,87.31  ]

#Dir="./ntuples/saved_hist/Step1_0725_PDF_uncluster_NoNvtex/"
Dir="./ntuples/saved_hist/Step1_0726_PDF_uncluster_Nvtex/"
for sample in ["DY","TT","TW"]:
    for chan in ["ee","emu","mumu"]:
        F1=ROOT.TFile(Dir+chan+"_nominal_.root","read")
        F2=ROOT.TFile(Dir+chan+"_UnclusteredEnUp_.root","read")
        F3=ROOT.TFile(Dir+chan+"_UnclusteredEnDown_.root","read")
        h1=F1.Get("nominal__DYJetsToLL_M10to50_amc__H_MET_Et").Clone("%s_nominal_%s_H_MET_Et"%(chan,sample))
        h2=F2.Get("UnclusteredEnUp__DYJetsToLL_M10to50_amc__H_MET_Et")  .Clone("%s_UnclusteredEnUp_%s_H_MET_Et"  %(chan,sample))
        h3=F3.Get("UnclusteredEnDown__DYJetsToLL_M10to50_amc__H_MET_Et").Clone("%s_UnclusteredEnDown_%s_H_MET_Et"%(chan,sample))
        h1.Scale(0)
        h2.Scale(0)
        h3.Scale(0)
        for im in MC_Sample:
            if sample not in im:continue
            h1.Add(F1.Get("nominal__%s__H_MET_Et"%(im)),float(Lumi)/float(MC_Sample[im][0]/MC_Sample[im][1]))
            h2.Add(F2.Get("UnclusteredEnUp__%s__H_MET_Et"%(im)),float(Lumi)/float(MC_Sample[im][0]/MC_Sample[im][1]))
            h3.Add(F3.Get("UnclusteredEnDown__%s__H_MET_Et"%(im)),float(Lumi)/float(MC_Sample[im][0]/MC_Sample[im][1]))
        draw_compare(h1,h2,h3,0,"nominal","UnclusteredEnUp","UnclusteredEnDown",chan,sample, "Nvtx")#style 1 for ratio error like efficiency
