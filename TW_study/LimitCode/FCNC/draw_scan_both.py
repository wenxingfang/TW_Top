import ROOT
import math
import os
from array import array
ROOT.gROOT.SetBatch(ROOT.kTRUE)

def sigma_band(gr):
    Sigma1_x_min=0
    Sigma1_x_max=0
    Sigma2_x_min=0
    Sigma2_x_max=0
    Min=999
    best_fit=999
    for iN in range(0,gr.GetN()):
        if iN!= gr.GetN()-1:
            if gr.GetY()[iN]<Min:
                Min=gr.GetY()[iN]
                best_fit=gr.GetX()[iN]
            if (gr.GetY()[iN]<1 and 1<gr.GetY()[iN+1]):
                Sigma1_x_max=(1-gr.GetY()[iN])*(gr.GetX()[iN+1]-gr.GetX()[iN])/(gr.GetY()[iN+1]-gr.GetY()[iN]) + gr.GetX()[iN]
            elif (gr.GetY()[iN+1]<1 and 1<gr.GetY()[iN]):
                Sigma1_x_min=(1-gr.GetY()[iN])*(gr.GetX()[iN+1]-gr.GetX()[iN])/(gr.GetY()[iN+1]-gr.GetY()[iN]) + gr.GetX()[iN]
            elif (gr.GetY()[iN]<3.84 and 3.84<gr.GetY()[iN+1]):
                Sigma2_x_max=(3.84-gr.GetY()[iN])*(gr.GetX()[iN+1]-gr.GetX()[iN])/(gr.GetY()[iN+1]-gr.GetY()[iN]) + gr.GetX()[iN]
            elif (gr.GetY()[iN+1]<3.84 and 3.84<gr.GetY()[iN]):
                Sigma2_x_min=(3.84-gr.GetY()[iN])*(gr.GetX()[iN+1]-gr.GetX()[iN])/(gr.GetY()[iN+1]-gr.GetY()[iN]) + gr.GetX()[iN]
    return [Sigma1_x_min,Sigma1_x_max,Sigma2_x_min,Sigma2_x_max,best_fit]

def draw(input_exp,input_obs,chan,region, coulp):
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
        if 2*ch_exp.deltaNLL > 10: continue ##remove very large points
        if transfer_to_coulping:
            if coulp=="Cug":
                #mu_exp .append(float(ch_exp.r/math.sqrt(68*1.27)))
                mu_exp .append(float(ch_exp.r/math.sqrt(16.7*1.27)))
            elif coulp=="Ccg":
                #mu_exp .append(float(ch_exp.r/math.sqrt(18*1.27)))
                mu_exp .append(float(ch_exp.r/math.sqrt(4.57*1.27)))
            else:
                mu_exp .append(ch_exp.r)
        else:
            mu_exp.append(ch_exp.r)
        NLL_exp.append(2*ch_exp.deltaNLL)
    for ientry in range(1,ch_obs.GetEntries()):
        ch_obs.GetEntry(ientry)
        if 2*ch_obs.deltaNLL > 10: continue ##remove very large points
        if transfer_to_coulping:
            if coulp=="Cug":
                #mu_obs .append(float(ch_obs.r/math.sqrt(68*1.27)))
                mu_obs .append(float(ch_obs.r/math.sqrt(16.7*1.27)))
            elif coulp=="Ccg":
                #mu_obs .append(float(ch_obs.r/math.sqrt(18*1.27)))
                mu_obs .append(float(ch_obs.r/math.sqrt(4.57*1.27)))
            else:
                mu_obs .append(ch_obs.r)
        else:
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
    best_exp        =sigma_band(gr_exp)[4]
    Sigma1_x_min_obs=sigma_band(gr_obs)[0]
    Sigma1_x_max_obs=sigma_band(gr_obs)[1]
    Sigma2_x_min_obs=sigma_band(gr_obs)[2]
    Sigma2_x_max_obs=sigma_band(gr_obs)[3]
    best_obs        =sigma_band(gr_obs)[4]
            
    canvas = ROOT.TCanvas('canvas','',900, 600)
    canvas.cd()
    canvas.SetTickx()
    canvas.SetTicky()
    canvas.SetBottomMargin(0.18)
    y_min=0
    y_max=y_min+6
    x_min=0.4
    x_max=1.6
    if coulp=="Cphiq":
        x_title="C_{#phiq}"
        x_min=-6
        x_max=6
        if "ee" in chan or "mumu" in chan:
            x_min=-8
            x_max=6
        elif "combined" in chan:
            x_min=-4
            x_max=4
    elif coulp=="Ctw":
        x_title="C_{tW}"
        x_min=-4
        x_max=8
        if "combined" not in chan :
            x_min=-6
            x_max=10
    elif coulp=="Ctg":
        x_title="C_{tG}"
        x_min=-0.4
        x_max=0.4
        if "combined" in chan:
            x_min=-0.3
            x_max=0.3
    elif coulp=="Cg":
        x_title="C_{G}"
        x_min=-1.5
        x_max=1.5
    elif coulp=="Cug":
        x_title="C_{uG}"
        x_min=-0.2
        x_max=0.2
        if "combined" in chan:
            x_min=-0.08
            x_max=0.08
    elif coulp=="Ccg":
        x_title="C_{cG}"
        x_min=-0.3
        x_max=0.3
        if "combined" in chan:
            x_min=-0.2
            x_max=0.2
    dummy = ROOT.TH2D("dummy","",1,x_min,x_max,1,y_min,y_max)
    dummy.SetStats(ROOT.kFALSE)
    dummy.GetYaxis().SetTitle("-2 #Deltaln L")
    dummy.GetXaxis().SetTitle("%s"%x_title)
    dummy.GetXaxis().SetTitleSize(0.07)
    dummy.GetYaxis().SetTitleSize(0.07)
    dummy.GetYaxis().SetLabelSize(0.06)
    dummy.GetXaxis().SetLabelSize(0.06)
    dummy.GetYaxis().SetLabelOffset(0.01)
    dummy.GetXaxis().SetLabelOffset(0.015)
    dummy.GetYaxis().SetTitleOffset(0.65)
    dummy.GetXaxis().SetTitleOffset(1)
    dummy.GetXaxis().SetMoreLogLabels()
    dummy.GetXaxis().SetNoExponent()
#    dummy.GetXaxis().CenterTitle()
#    dummy.GetYaxis().CenterTitle()
    dummy.Draw()
    #gr.Draw("PC")
    #gr_exp.SetLineStyle(1)
    gr_exp.SetLineStyle(10)
    gr_exp.SetLineWidth(2)
    gr_exp.SetMarkerSize(0)
    gr_exp.Draw("pc")
#    gr_exp.Draw("pl")
    gr_obs.SetLineStyle(1)
    gr_obs.SetLineWidth(2)
    gr_obs.SetMarkerSize(0)
    if Unblind:
        gr_obs.Draw("pl")
    dummy.Draw("AXISSAME")
    sigma_color=ROOT.TColor.GetColor("#c0c0c0")
    line_1sigma =ROOT.TLine(x_min,1,x_max,1)
    line_2sigma =ROOT.TLine(x_min,3.84,x_max,3.84)
    line_1sigma.SetLineColor(sigma_color)
    line_1sigma.SetLineStyle(2)
    line_1sigma.SetLineWidth(3)
    line_2sigma.SetLineColor(sigma_color)
    line_2sigma.SetLineStyle(2)
    line_2sigma.SetLineWidth(3)
    line_1sigma.Draw()
    line_2sigma.Draw()
    print "exp:%-5s_%-8s%-15s| best: %.3f | 1sigma:%.3f to %.3f | 2sigma:%.3f to %.3f|"%(coulp,chan,region,float(0),float(Sigma1_x_min_exp),float(Sigma1_x_max_exp),float(Sigma2_x_min_exp),float(Sigma2_x_max_exp))
    if Unblind:
        print "obs:%-5s_%-8s%-15s| best: %.3f | 1sigma:%.3f to %.3f | 2sigma:%.3f to %.3f|"%(coulp,chan,region,float(best_obs),float(Sigma1_x_min_obs),float(Sigma1_x_max_obs),float(Sigma2_x_min_obs),float(Sigma2_x_max_obs))
    legend = ROOT.TLegend(0.4,0.7,0.6,0.85)
    legend.AddEntry(gr_exp,'Expected','l')
    if Unblind:
        legend.AddEntry(gr_obs,'Observed','l')
    legend.SetBorderSize(0)
    legend.SetTextFont(42)
    legend.Draw()
    label_lamda = ROOT.TLatex(0.4,0.65,"#Lambda = 1 TeV")
    label_lamda.SetNDC(ROOT.kTRUE)
    label_lamda.Draw()
    #label_1sigma = ROOT.TLatex(0.92,0.26,"1 #sigma")
    label_1sigma = ROOT.TLatex(0.92,0.28,"68%")
    label_1sigma.SetNDC(ROOT.kTRUE)
    label_1sigma.SetTextColor(sigma_color)
    label_1sigma.Draw()
    #label_2sigma = ROOT.TLatex(0.92,0.61,"2 #sigma")
    label_2sigma = ROOT.TLatex(0.92,0.62,"95%")
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
    if "1j0t_1j1t" in region:
        str_region="(1j0t+1j1t)"
    if "1j1t_2j1t" in region:
        str_region="(1j1t+2j1t)"
    if "1j1t_2j1t_2j2t" in region:
        str_region="(1j1t+2j1t+#geq2j2t)"
    if chan=="ee":
        label.DrawLatex(0.34,0.55, "ee%s"%str_region)
    elif chan=="emu":
        label.DrawLatex(0.34,0.55, "e#mu%s"%str_region)
    elif chan=="mumu":
        label.DrawLatex(0.34,0.55, "#mu#mu%s"%str_region)
    elif chan=="combined":
        label.DrawLatex(0.34,0.55, "%s"%str_region)
    Label_cms_prelim = ROOT.TPaveText(0.085,0.92,0.4,0.96,"NDC")
    Label_cms_prelim.SetLineColor(10)
    Label_cms_prelim.SetFillColor(10)
    Label_cms_prelim.SetTextSize(0.075)
    Label_cms_prelim.SetTextAlign(12)
    Label_cms_prelim.SetTextFont(61)
    if for_paper_style:
        Label_cms_prelim.AddText("CMS")
    else:
        Label_cms_prelim.AddText("CMS Preliminary")
    Label_cms_prelim.SetShadowColor(10)
    Label_cms_prelim.Draw()
    Label_lumi = ROOT.TPaveText(0.615,0.92,0.815,0.96,"NDC")
    Label_lumi.SetLineColor(10)
    Label_lumi.SetFillColor(10)
    Label_lumi.SetTextSize(0.06)
    Label_lumi.SetTextAlign(12)
    Label_lumi.SetTextFont(42)
    Label_lumi.AddText("35.9 fb^{-1} (13 TeV)")
    Label_lumi.SetShadowColor(10)
    Label_lumi.Draw()
    canvas.Print('./scan_plot/%s_%s%s_scan.png'%(coulp,chan,region))

Dir="./scan_both/"
#Dir="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/scan_script/for_plot/"
for_paper_style=True
Unblind=True
transfer_to_coulping=False

for coup in ["Ctg","Ctw","Cphiq","Cg","Cug","Ccg"]:
    for chan in["ee","emu","mumu","combined"]:
        for region in ["_1j1t","_1j0t_1j1t","_1j1t_2j1t","_1j1t_2j1t_2j2t",""]:
            draw(Dir+"higgsCombineexp_%s_%s%s.MultiDimFit.mH125.7.root"%(str(chan),str(coup),str(region)),Dir+"higgsCombineobs_%s_%s%s.MultiDimFit.mH125.7.root"%(str(chan),str(coup),str(region)),str(chan),str(region),str(coup))
#            draw(Dir+"higgsCombinePtll_obs_%s_%s%s.MultiDimFit.mH125.7.root"%(str(chan),str(coup),str(region)),Dir+"higgsCombinePtll_obs_%s_%s%s.MultiDimFit.mH125.7.root"%(str(chan),str(coup),str(region)),str(chan),str(region),str(coup))
