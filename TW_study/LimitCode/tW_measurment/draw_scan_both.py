import ROOT
import os
from array import array
ROOT.gROOT.SetBatch(ROOT.kTRUE)

def sigma_band(gr):
    Sigma1_x_min=0
    Sigma1_x_max=0
    Sigma2_x_min=0
    Sigma2_x_max=0
    for iN in range(0,gr.GetN()):
        if iN!= gr.GetN()-1:
            if (gr.GetY()[iN]<1 and 1<gr.GetY()[iN+1]):
                Sigma1_x_max=(1-gr.GetY()[iN])*(gr.GetX()[iN+1]-gr.GetX()[iN])/(gr.GetY()[iN+1]-gr.GetY()[iN]) + gr.GetX()[iN]
            elif (gr.GetY()[iN+1]<1 and 1<gr.GetY()[iN]):
                Sigma1_x_min=(1-gr.GetY()[iN])*(gr.GetX()[iN+1]-gr.GetX()[iN])/(gr.GetY()[iN+1]-gr.GetY()[iN]) + gr.GetX()[iN]
            elif (gr.GetY()[iN]<3.84 and 3.84<gr.GetY()[iN+1]):
                Sigma2_x_max=(3.84-gr.GetY()[iN])*(gr.GetX()[iN+1]-gr.GetX()[iN])/(gr.GetY()[iN+1]-gr.GetY()[iN]) + gr.GetX()[iN]
            elif (gr.GetY()[iN+1]<3.84 and 3.84<gr.GetY()[iN]):
                Sigma2_x_min=(3.84-gr.GetY()[iN])*(gr.GetX()[iN+1]-gr.GetX()[iN])/(gr.GetY()[iN+1]-gr.GetY()[iN]) + gr.GetX()[iN]
            #elif (gr.GetY()[iN]<4 and 4<gr.GetY()[iN+1]):
            #    Sigma2_x_max=(4-gr.GetY()[iN])*(gr.GetX()[iN+1]-gr.GetX()[iN])/(gr.GetY()[iN+1]-gr.GetY()[iN]) + gr.GetX()[iN]
            #elif (gr.GetY()[iN+1]<4 and 4<gr.GetY()[iN]):
            #    Sigma2_x_min=(4-gr.GetY()[iN])*(gr.GetX()[iN+1]-gr.GetX()[iN])/(gr.GetY()[iN+1]-gr.GetY()[iN]) + gr.GetX()[iN]
    return [Sigma1_x_min,Sigma1_x_max,Sigma2_x_min,Sigma2_x_max]

def draw(input_exp,input_obs,chan,region):
    if os.path.isfile(input_exp) == False or os.path.isfile(input_obs) == False:return
    ch_exp=ROOT.TChain("limit")
    ch_exp.Add(input_exp)
    ch_obs=ROOT.TChain("limit")
    ch_obs.Add(input_obs)
    mu_exp  = array('f')
    NLL_exp = array('f')
    mu_obs  = array('f')
    NLL_obs = array('f')
    for ientry in range(1,ch_exp.GetEntries()):
        ch_exp.GetEntry(ientry)
        mu_exp.append(ch_exp.r)
        NLL_exp.append(2*ch_exp.deltaNLL)
    for ientry in range(1,ch_obs.GetEntries()):
        ch_obs.GetEntry(ientry)
        if 2*ch_obs.deltaNLL > 13:continue
        mu_obs.append(ch_obs.r)
        NLL_obs.append(2*ch_obs.deltaNLL)
    Sigma1_x_min_exp=0 
    Sigma1_x_max_exp=0 
    Sigma2_x_min_exp=0 
    Sigma2_x_max_exp=0 
    Sigma1_x_min_obs=0 
    Sigma1_x_max_obs=0 
    Sigma2_x_min_obs=0 
    Sigma2_x_max_obs=0 
    gr_exp=ROOT.TGraph(len(mu_exp),mu_exp,NLL_exp)
    gr_exp.Sort()
    gr_exp.SetMarkerStyle(8)
    gr_exp.SetLineWidth(2)
    gr_exp.SetLineColor(4)
    gr_obs=ROOT.TGraph(len(mu_obs),mu_obs,NLL_obs)
    gr_obs.Sort()
    gr_obs.SetMarkerStyle(8)
    gr_obs.SetLineWidth(2)
    gr_obs.SetLineColor(2)
    Sigma1_x_min_exp=sigma_band(gr_exp)[0]
    Sigma1_x_max_exp=sigma_band(gr_exp)[1]
    Sigma2_x_min_exp=sigma_band(gr_exp)[2]
    Sigma2_x_max_exp=sigma_band(gr_exp)[3]
    Sigma1_x_min_obs=sigma_band(gr_obs)[0]
    Sigma1_x_max_obs=sigma_band(gr_obs)[1]
    Sigma2_x_min_obs=sigma_band(gr_obs)[2]
    Sigma2_x_max_obs=sigma_band(gr_obs)[3]
            
    canvas = ROOT.TCanvas('canvas','',900, 600)
    canvas.cd()
    canvas.SetTickx()
    canvas.SetTicky()
    canvas.SetBottomMargin(0.13)
    y_min=0
    #y_max=y_min+10
    y_max=y_min+6
    x_min=0.4
    x_max=1.4
    if chan=="ee":
        x_min=0.3
        x_max=1.65
    elif chan=="emu":
        x_min=0.4
        x_max=1.6
        if region=="":
            x_min=0.55
            x_max=1.4
        elif region=="_1j1t":
            x_min=0.25
            x_max=1.6
    elif chan=="mumu":
        x_min=0.4
        x_max=1.7
    dummy = ROOT.TH2D("dummy","",1,x_min,x_max,1,y_min,y_max)
    dummy.SetStats(ROOT.kFALSE)
    dummy.GetYaxis().SetTitle("-2 #Delta ln L")
    x_title="r"
    dummy.GetXaxis().SetTitle("%s"%x_title)
    dummy.GetXaxis().SetTitleSize(0.07)
    dummy.GetYaxis().SetTitleSize(0.07)
    dummy.GetYaxis().SetLabelSize(0.06)
    dummy.GetXaxis().SetLabelSize(0.06)
    dummy.GetYaxis().SetLabelOffset(0.01)
    dummy.GetXaxis().SetLabelOffset(0.015)
    dummy.GetYaxis().SetTitleOffset(0.7)
    dummy.GetXaxis().SetTitleOffset(0.9)
    dummy.GetXaxis().SetMoreLogLabels()
    dummy.GetXaxis().SetNoExponent()
    dummy.GetXaxis().CenterTitle()
    dummy.GetYaxis().CenterTitle()
    dummy.Draw()
    #gr.Draw("PC")
    gr_exp.SetLineStyle(1)
    gr_exp.SetLineWidth(2)
    gr_exp.SetMarkerSize(0)
    gr_exp.Draw("pl")
    gr_obs.SetLineStyle(1)
    gr_obs.SetLineWidth(2)
    gr_obs.SetMarkerSize(0)
    if Unblind:
        gr_obs.Draw("pl")
    dummy.Draw("AXISSAME")
    #sigma_color=ROOT.TColor.GetColor("#ffd700")
    sigma_color=ROOT.TColor.GetColor("#c0c0c0")
#    sigma_color=ROOT.kGray
    line_1sigma =ROOT.TLine(x_min,1,x_max,1)
    line_2sigma =ROOT.TLine(x_min,3.84,x_max,3.84)
#    line_2sigma =ROOT.TLine(x_min,4,x_max,4)
    line_1sigma.SetLineColor(sigma_color)
    line_1sigma.SetLineStyle(2)
    line_1sigma.SetLineWidth(3)
    line_2sigma.SetLineColor(sigma_color)
    line_2sigma.SetLineStyle(2)
    line_2sigma.SetLineWidth(3)
    line_1sigma.Draw()
    line_2sigma.Draw()
    print "%s_%s|exp 1sigma:%.2f to %.2f |exp 2sigma:%.2f to %.2f|"%(chan,region,float(Sigma1_x_min_exp),float(Sigma1_x_max_exp),float(Sigma2_x_min_exp),float(Sigma2_x_max_exp))
    if Unblind:
        print "%s_%s|obs 1sigma:%.2f to %.2f |obs 2sigma:%.2f to %.2f|"%(chan,region,float(Sigma1_x_min_obs),float(Sigma1_x_max_obs),float(Sigma2_x_min_obs),float(Sigma2_x_max_obs))
#    line_1sigma_exp     =ROOT.TLine(Sigma1_x_min_exp,1   ,Sigma1_x_max_exp,1)
#    line_1sigma_low_exp =ROOT.TLine(Sigma1_x_min_exp,0   ,Sigma1_x_min_exp,1)
#    line_1sigma_high_exp=ROOT.TLine(Sigma1_x_max_exp,0   ,Sigma1_x_max_exp,1)
#    line_2sigma_exp     =ROOT.TLine(Sigma2_x_min_exp,3.84,Sigma2_x_max_exp,3.84)
#    line_2sigma_low_exp =ROOT.TLine(Sigma2_x_min_exp,0   ,Sigma2_x_min_exp,3.84)
#    line_2sigma_high_exp=ROOT.TLine(Sigma2_x_max_exp,0   ,Sigma2_x_max_exp,3.84)
#    line_1sigma_exp.SetLineColor(ROOT.kBlue)
#    line_1sigma_exp.SetLineStyle(2)
#    line_1sigma_exp.SetLineWidth(2)
#    line_1sigma_low_exp.SetLineColor(ROOT.kBlue)
#    line_1sigma_low_exp.SetLineStyle(2)
#    line_1sigma_low_exp.SetLineWidth(2)
#    line_1sigma_high_exp.SetLineColor(ROOT.kBlue)
#    line_1sigma_high_exp.SetLineStyle(2)
#    line_1sigma_high_exp.SetLineWidth(2)
#    line_2sigma_exp.SetLineColor(ROOT.kRed)
#    line_2sigma_exp.SetLineStyle(3)
#    line_2sigma_exp.SetLineWidth(2)
#    line_2sigma_low_exp.SetLineColor(ROOT.kRed)
#    line_2sigma_low_exp.SetLineStyle(3)
#    line_2sigma_low_exp.SetLineWidth(2)
#    line_2sigma_high_exp.SetLineColor(ROOT.kRed)
#    line_2sigma_high_exp.SetLineStyle(3)
#    line_2sigma_high_exp.SetLineWidth(2)
#    line_1sigma_exp.Draw()
#    line_1sigma_low_exp.Draw()
#    line_1sigma_high_exp.Draw()
#    line_2sigma_exp.Draw()
#    line_2sigma_low_exp.Draw()
#    line_2sigma_high_exp.Draw()
    legend = ROOT.TLegend(0.4,0.7,0.6,0.85)
    legend.AddEntry(gr_exp,'Expected','l')
    if Unblind:
        legend.AddEntry(gr_obs,'Observed','l')
    legend.SetBorderSize(0)
    legend.SetTextFont(42)
    legend.Draw()
    #label_1sigma = ROOT.TLatex(0.92,0.194,"1 #sigma")
    label_1sigma = ROOT.TLatex(0.92,0.24,"68%")
    label_1sigma.SetNDC(ROOT.kTRUE)
    label_1sigma.SetTextColor(sigma_color)
    label_1sigma.Draw()
    #label_2sigma = ROOT.TLatex(0.92,0.415,"2 #sigma")
    label_2sigma = ROOT.TLatex(0.92,0.61,"95%")
    label_2sigma.SetNDC(ROOT.kTRUE)
    label_2sigma.SetTextColor(sigma_color)
    label_2sigma.Draw()
    label = ROOT.TLatex()
    label.SetTextAlign(12)
    label.SetTextSize(0.08)
    label.SetNDC(ROOT.kTRUE)
    str_region=""
    if "1j1t" in region:
        str_region="(1j1t)"
    if "1j1t_2j1t" in region:
        str_region="(1j1t+2j1t)"
    if "1j1t_2j1t_2j2t" in region:
        str_region="(1j1t+2j1t+#geq2j2t)"
    if chan=="ee":
        label.DrawLatex(0.34,0.65, "ee%s"%str_region)
    elif chan=="emu":
        label.DrawLatex(0.34,0.65, "e#mu%s"%str_region)
    elif chan=="mumu":
        label.DrawLatex(0.34,0.65, "#mu#mu%s"%str_region)
    elif chan=="combined":
        label.DrawLatex(0.34,0.65, "combined%s"%str_region)
    Label_cms_prelim = ROOT.TPaveText(0.09,0.91,0.4,0.95,"NDC")
    Label_cms_prelim.SetLineColor(10)
    Label_cms_prelim.SetFillColor(10)
    Label_cms_prelim.SetTextSize(0.05)
    Label_cms_prelim.SetTextAlign(12)
    Label_cms_prelim.AddText("CMS Preliminary")
    Label_cms_prelim.SetShadowColor(10)
    Label_cms_prelim.Draw()
    Label_lumi = ROOT.TPaveText(0.665,0.91,0.85,0.95,"NDC")
    Label_lumi.SetLineColor(10)
    Label_lumi.SetFillColor(10)
    Label_lumi.SetTextSize(0.05)
    Label_lumi.SetTextAlign(12)
    Label_lumi.SetTextFont(42)
    Label_lumi.AddText("35.9 fb^{-1} (13 TeV)")
    Label_lumi.SetShadowColor(10)
    Label_lumi.Draw()
    canvas.Print('./scan_plot/%s_%s_scan.png'%(chan,region))

Dir="./scan_both/"
Unblind=True

for chan in["ee","emu","mumu","combined"]:
    for region in ["_1j1t","_1j1t_2j1t","_1j1t_2j1t_2j2t",""]:
        draw(Dir+"higgsCombineexp_%s%s.MultiDimFit.mH120.root"%(str(chan),str(region)),Dir+"higgsCombineobs_%s%s.MultiDimFit.mH120.root"%(str(chan),str(region)),str(chan),str(region))
#draw(Dir+"higgsCombineDY3.MultiDimFit.mH120.root","emu","r_DY3")
