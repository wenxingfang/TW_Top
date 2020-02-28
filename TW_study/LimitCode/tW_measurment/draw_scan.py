import ROOT
import os
from array import array
ROOT.gROOT.SetBatch(ROOT.kTRUE)

def draw(input_name,chan,region):
    if os.path.isfile(input_name) == False:return
    ch=ROOT.TChain("limit")
    ch.Add(input_name)
    mu  = array('f')
    NLL = array('f')
    for ientry in range(1,ch.GetEntries()):
        ch.GetEntry(ientry)
        mu .append(ch.r)
        NLL.append(2*ch.deltaNLL)
    Sigma1_x_min=0 
    Sigma1_x_max=0 
    Sigma2_x_min=0 
    Sigma2_x_max=0 
    gr=ROOT.TGraph(len(mu),mu,NLL)
    gr.Sort()
    gr.SetMarkerStyle(8)
    gr.SetLineWidth(2)
    gr.SetLineColor(4)
    ymin=1000
    index=0
    for iN in range(0,gr.GetN()):
        if gr.GetY()[iN]<ymin:
            ymin=gr.GetY()[iN]
            index=iN
        if iN!= gr.GetN()-1:
            if (gr.GetY()[iN]<1 and 1<gr.GetY()[iN+1]):
                Sigma1_x_max=(1-gr.GetY()[iN])*(gr.GetX()[iN+1]-gr.GetX()[iN])/(gr.GetY()[iN+1]-gr.GetY()[iN]) + gr.GetX()[iN]
            elif (gr.GetY()[iN+1]<1 and 1<gr.GetY()[iN]):
                Sigma1_x_min=(1-gr.GetY()[iN])*(gr.GetX()[iN+1]-gr.GetX()[iN])/(gr.GetY()[iN+1]-gr.GetY()[iN]) + gr.GetX()[iN]
            elif (gr.GetY()[iN]<3.84 and 3.84<gr.GetY()[iN+1]):
                Sigma2_x_max=(3.84-gr.GetY()[iN])*(gr.GetX()[iN+1]-gr.GetX()[iN])/(gr.GetY()[iN+1]-gr.GetY()[iN]) + gr.GetX()[iN]
            elif (gr.GetY()[iN+1]<3.84 and 3.84<gr.GetY()[iN]):
                Sigma2_x_min=(3.84-gr.GetY()[iN])*(gr.GetX()[iN+1]-gr.GetX()[iN])/(gr.GetY()[iN+1]-gr.GetY()[iN]) + gr.GetX()[iN]
            
    canvas = ROOT.TCanvas('canvas','',900, 600)
    canvas.cd()
    canvas.SetTickx()
    canvas.SetTicky()
    canvas.SetBottomMargin(0.13)
    y_min=int(ymin)-1
    y_min=0
    y_max=y_min+10
    x_min=int(gr.GetX()[index])-2
    x_max=int(gr.GetX()[index])+2
    x_min=0.4
    x_max=1.6
    #x_min=0
    #x_max=2
    y_min=0
    y_max=10
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
    gr.SetLineStyle(1)
    gr.SetMarkerSize(0)
    gr.Draw("pl")
    dummy.Draw("AXISSAME")
    line_0      =ROOT.TLine(x_min,0,x_max,0)
    #line_1sigma =ROOT.TLine(x_min,1,x_max,1)
    #line_2sigma =ROOT.TLine(x_min,3.84,x_max,3.84)
    line_1sigma =ROOT.TLine(Sigma1_x_min,1   ,Sigma1_x_max,1)
    line_1sigma_low =ROOT.TLine(Sigma1_x_min,0   ,Sigma1_x_min,1)
    line_1sigma_high=ROOT.TLine(Sigma1_x_max,0   ,Sigma1_x_max,1)
    line_2sigma =ROOT.TLine(Sigma2_x_min,3.84,Sigma2_x_max,3.84)
    line_2sigma_low =ROOT.TLine(Sigma2_x_min,0   ,Sigma2_x_min,3.84)
    line_2sigma_high=ROOT.TLine(Sigma2_x_max,0   ,Sigma2_x_max,3.84)
    print "%s_%s| 1sigma:%.2f to %.2f | 2sigma:%.2f to %.2f|"%(chan,region,float(Sigma1_x_min),float(Sigma1_x_max),float(Sigma2_x_min),float(Sigma2_x_max))
    line_0.SetLineColor(ROOT.kBlack)
    line_0.SetLineStyle(1)
    line_1sigma.SetLineColor(ROOT.kBlue)
    line_1sigma.SetLineStyle(2)
    line_1sigma.SetLineWidth(2)
    line_1sigma_low.SetLineColor(ROOT.kBlue)
    line_1sigma_low.SetLineStyle(2)
    line_1sigma_low.SetLineWidth(2)
    line_1sigma_high.SetLineColor(ROOT.kBlue)
    line_1sigma_high.SetLineStyle(2)
    line_1sigma_high.SetLineWidth(2)
    line_2sigma.SetLineColor(ROOT.kRed)
    line_2sigma.SetLineStyle(3)
    line_2sigma.SetLineWidth(2)
    line_2sigma_low.SetLineColor(ROOT.kRed)
    line_2sigma_low.SetLineStyle(3)
    line_2sigma_low.SetLineWidth(2)
    line_2sigma_high.SetLineColor(ROOT.kRed)
    line_2sigma_high.SetLineStyle(3)
    line_2sigma_high.SetLineWidth(2)
    line_0.Draw()
    line_1sigma.Draw()
    line_1sigma_low.Draw()
    line_1sigma_high.Draw()
    line_2sigma.Draw()
    line_2sigma_low.Draw()
    line_2sigma_high.Draw()
    legend = ROOT.TLegend(0.4,0.7,0.6,0.85)
    legend.AddEntry(line_1sigma,'1 #sigma CL','l')
    legend.AddEntry(line_2sigma,'2 #sigma CL','l')
    legend.SetBorderSize(0)
    legend.SetTextFont(42)
    legend.Draw()
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

#Dir="./scan_obs/"
Dir="./scan_exp/"

for chan in["ee","emu","mumu","combined"]:
    for region in ["_1j1t","_1j1t_2j1t","_1j1t_2j1t_2j2t",""]:
        #draw(Dir+"higgsCombine%s%s.MultiDimFit.mH120.root"%(str(chan),str(region)),str(chan),str(region))
        draw(Dir+"higgsCombineDY50_%s%s.MultiDimFit.mH120.root"%(str(chan),str(region)),str(chan),str(region))
#draw(Dir+"higgsCombineDY3.MultiDimFit.mH120.root","emu","r_DY3")
