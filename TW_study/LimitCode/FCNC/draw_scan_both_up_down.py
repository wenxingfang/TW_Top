import ROOT
import math
import os
from array import array
import numpy as np
ROOT.gROOT.SetBatch(ROOT.kTRUE)

def make_array(ch,max_DNLL, coulp, transfer, scale):
    tmp_mu  = array('f')
    tmp_NLL  = array('f')
    Br = 0.324
    for ientry in range(1,ch.GetEntries()):
        ch.GetEntry(ientry)
        if 2*ch.deltaNLL > max_DNLL: continue ##remove very large points
        elif 2*ch.deltaNLL < 0: continue ##remove negative
        if transfer:
            if coulp=="Cug":
                if scale=="up":
                    tmp_mu .append(float(ch.r/math.sqrt(1.07*16.7*Br*Br*1.27)))
                elif scale=="down":
                    tmp_mu .append(float(ch.r/math.sqrt(0.94*16.7*Br*Br*1.27)))
                else:
                    tmp_mu .append(float(ch.r/math.sqrt(16.7*Br*Br*1.27)))
            elif coulp=="Ccg":
                if scale=="up":
                    tmp_mu .append(float(ch.r/math.sqrt(1.044*4.57*Br*Br*1.27)))
                elif scale=="down":
                    tmp_mu .append(float(ch.r/math.sqrt(0.957*4.57*Br*Br*1.27)))
                else:
                    tmp_mu .append(float(ch.r/math.sqrt(4.57*Br*Br*1.27)))
            else:
                tmp_mu .append(ch.r)
        else:
            tmp_mu.append(ch.r)
        tmp_NLL.append(2*ch.deltaNLL)
    return [tmp_mu,tmp_NLL]

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

def sigma_band_Fun(fun, low, up, points):
    Sigma1_x_min=0
    Sigma1_x_max=0
    Sigma2_x_min=0
    Sigma2_x_max=0
    Min=999
    best_fit=999
    interval = (up-low)/points
    List = [ low + i*interval for i in range(0,points+1) ]
    for iN in List:
        if List.index(iN)==0 or List.index(iN)==(len(List)-1):continue
        if fun.Eval(iN)<Min:
            Min=fun.Eval(iN)
            best_fit=iN
        if fun.Eval(iN)<1 and 1<fun.Eval(List[List.index(iN)+1]):
            Sigma1_x_max=(1-fun.Eval(iN))*(List[List.index(iN)+1]-iN)/(fun.Eval(List[List.index(iN)+1])-fun.Eval(iN)) + iN
        elif fun.Eval(List[List.index(iN)+1])<1 and 1<fun.Eval(iN):
            Sigma1_x_min=(1-fun.Eval(iN))*(List[List.index(iN)+1]-iN)/(fun.Eval(List[List.index(iN)+1])-fun.Eval(iN)) + iN
        elif fun.Eval(iN)<3.84 and 3.84<fun.Eval(List[List.index(iN)+1]):
            Sigma2_x_max=(3.84-fun.Eval(iN))*(List[List.index(iN)+1]-iN)/(fun.Eval(List[List.index(iN)+1])-fun.Eval(iN)) + iN
        elif fun.Eval(List[List.index(iN)+1])<3.84 and 3.84<fun.Eval(iN):
            Sigma2_x_min=(3.84-fun.Eval(iN))*(List[List.index(iN)+1]-iN)/(fun.Eval(List[List.index(iN)+1])-fun.Eval(iN)) + iN
        #elif (gr.GetY()[iN]<3.84 and 3.84<gr.GetY()[iN+1]):
        #    Sigma2_x_max=(3.84-gr.GetY()[iN])*(gr.GetX()[iN+1]-gr.GetX()[iN])/(gr.GetY()[iN+1]-gr.GetY()[iN]) + gr.GetX()[iN]
        #elif (gr.GetY()[iN+1]<3.84 and 3.84<gr.GetY()[iN]):
        #    Sigma2_x_min=(3.84-gr.GetY()[iN])*(gr.GetX()[iN+1]-gr.GetX()[iN])/(gr.GetY()[iN+1]-gr.GetY()[iN]) + gr.GetX()[iN]
    return [Sigma1_x_min,Sigma1_x_max,Sigma2_x_min,Sigma2_x_max,best_fit]


def draw(input_exp,input_exp_up,input_exp_down,input_obs,input_obs_up,input_obs_down,chan,region, coulp):
    if os.path.isfile(input_exp) == False or os.path.isfile(input_obs) == False or os.path.isfile(input_exp_up) == False or os.path.isfile(input_exp_down) == False or os.path.isfile(input_obs_up) == False or os.path.isfile(input_obs_down) == False :return
    print "for %s %s %s"%(coulp,chan,region)
    ch_exp=ROOT.TChain("limit")
    ch_exp.Add(input_exp)
    ch_exp_up=ROOT.TChain("limit")
    ch_exp_up.Add(input_exp_up)
    ch_exp_down=ROOT.TChain("limit")
    ch_exp_down.Add(input_exp_down)
    ch_obs=ROOT.TChain("limit")
    ch_obs.Add(input_obs)
    ch_obs_up=ROOT.TChain("limit")
    ch_obs_up.Add(input_obs_up)
    ch_obs_down=ROOT.TChain("limit")
    ch_obs_down.Add(input_obs_down)
    max_DNLL=6
    mu_exp       = make_array(ch_exp      ,max_DNLL, coulp, transfer_to_coulping,"")[0]
    NLL_exp      = make_array(ch_exp      ,max_DNLL, coulp, transfer_to_coulping,"")[1]
    mu_exp_up    = make_array(ch_exp_up   ,max_DNLL, coulp, transfer_to_coulping,"up")[0]
    NLL_exp_up   = make_array(ch_exp_up   ,max_DNLL, coulp, transfer_to_coulping,"up")[1]
    mu_exp_down  = make_array(ch_exp_down ,max_DNLL, coulp, transfer_to_coulping,"down")[0]
    NLL_exp_down = make_array(ch_exp_down ,max_DNLL, coulp, transfer_to_coulping,"down")[1]
    mu_obs       = make_array(ch_obs      ,max_DNLL, coulp, transfer_to_coulping,"")[0]
    NLL_obs      = make_array(ch_obs      ,max_DNLL, coulp, transfer_to_coulping,"")[1]
    mu_obs_up    = make_array(ch_obs_up   ,max_DNLL, coulp, transfer_to_coulping,"up")[0]
    NLL_obs_up   = make_array(ch_obs_up   ,max_DNLL, coulp, transfer_to_coulping,"up")[1]
    mu_obs_down  = make_array(ch_obs_down ,max_DNLL, coulp, transfer_to_coulping,"down")[0]
    NLL_obs_down = make_array(ch_obs_down ,max_DNLL, coulp, transfer_to_coulping,"down")[1]
    Sigma1_x_min_exp=0 
    Sigma1_x_max_exp=0 
    Sigma2_x_min_exp=0 
    Sigma2_x_max_exp=0 
    Sigma1_x_min_obs=0 
    Sigma1_x_max_obs=0 
    Sigma2_x_min_obs=0 
    Sigma2_x_max_obs=0 
    #sigma_color=ROOT.TColor.GetColor("#c0c0c0")
    #sigma_color=ROOT.TColor.GetColor("#a5a29c")
    sigma_color=ROOT.TColor.GetColor("#7c7975")
    gr_exp=ROOT.TGraph(len(mu_exp),mu_exp,NLL_exp)
    gr_exp.Sort()
    gr_exp.SetMarkerStyle(8)
    gr_exp.SetLineWidth(4)
    gr_exp.SetLineColor(2)
#    gr_exp.SetLineColor(sigma_color)
#    gr_exp.SetLineStyle(10)
    #gr_exp.SetLineStyle(7)
    gr_exp.SetLineStyle(2)
    gr_exp.SetMarkerSize(0)
    gr_exp_up=ROOT.TGraph(len(mu_exp_up),mu_exp_up,NLL_exp_up)
    gr_exp_up.Sort()
    gr_exp_up.SetMarkerStyle(8)
    gr_exp_up.SetLineWidth(2)
    gr_exp_up.SetLineColor(2)
    gr_exp_up.SetLineStyle(10)
    gr_exp_up.SetMarkerSize(0)
    gr_exp_down=ROOT.TGraph(len(mu_exp_down),mu_exp_down,NLL_exp_down)
    gr_exp_down.Sort()
    gr_exp_down.SetMarkerStyle(8)
    gr_exp_down.SetLineWidth(2)
    gr_exp_down.SetLineColor(4)
    gr_exp_down.SetLineStyle(10)
    gr_exp_down.SetMarkerSize(0)
    gr_obs=ROOT.TGraph(len(mu_obs),mu_obs,NLL_obs)
    gr_obs.Sort()
    gr_obs.SetMarkerStyle(8)
    gr_obs.SetLineWidth(4)
    gr_obs.SetLineColor(1)
    gr_obs.SetLineStyle(1)
    gr_obs.SetMarkerSize(0)
#    print len(mu_obs)
#    print len(mu_obs_up)
#    print len(mu_obs_down)
    ROOT.gStyle.SetLineStyleString(11,"50 50")
    gr_obs_up=ROOT.TGraph(len(mu_obs_up),mu_obs_up,NLL_obs_up)
    gr_obs_up.Sort()
    gr_obs_up.SetMarkerStyle(8)
    gr_obs_up.SetLineWidth(2)
    #gr_obs_up.SetLineColor(ROOT.TColor.GetColor("#00800"))
    gr_obs_up.SetLineColor(4)
    gr_obs_up.SetLineStyle(11)
    #gr_obs_up.SetLineStyle(8)
    #gr_obs_up.SetLineStyle(7)
    gr_obs_up.SetMarkerSize(0)
    gr_obs_down=ROOT.TGraph(len(mu_obs_down),mu_obs_down,NLL_obs_down)
    gr_obs_down.Sort()
    gr_obs_down.SetMarkerStyle(8)
    gr_obs_down.SetLineWidth(2)
    gr_obs_down.SetLineColor(4)
    gr_obs_down.SetLineStyle(9)
    gr_obs_down.SetMarkerSize(0)
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

    Sigma1_x_min_exp_up   =0
    Sigma1_x_max_exp_up   =0
    Sigma2_x_min_exp_up   =0
    Sigma2_x_max_exp_up   =0
    best_exp_up           =0
    Sigma1_x_min_obs_up   =0
    Sigma1_x_max_obs_up   =0
    Sigma2_x_min_obs_up   =0
    Sigma2_x_max_obs_up   =0
    best_obs_up           =0
    Sigma1_x_min_exp_down =0
    Sigma1_x_max_exp_down =0
    Sigma2_x_min_exp_down =0
    Sigma2_x_max_exp_down =0
    best_exp_down         =0
    Sigma1_x_min_obs_down =0
    Sigma1_x_max_obs_down =0
    Sigma2_x_min_obs_down =0
    Sigma2_x_max_obs_down =0
    best_obs_down         =0
    Sigma1_x_min_exp_up   =sigma_band(gr_exp_up)[0]
    Sigma1_x_max_exp_up   =sigma_band(gr_exp_up)[1]
    Sigma2_x_min_exp_up   =sigma_band(gr_exp_up)[2]
    Sigma2_x_max_exp_up   =sigma_band(gr_exp_up)[3]
    best_exp_up           =sigma_band(gr_exp_up)[4]
    Sigma1_x_min_obs_up   =sigma_band(gr_obs_up)[0]
    Sigma1_x_max_obs_up   =sigma_band(gr_obs_up)[1]
    Sigma2_x_min_obs_up   =sigma_band(gr_obs_up)[2]
    Sigma2_x_max_obs_up   =sigma_band(gr_obs_up)[3]
    best_obs_up           =sigma_band(gr_obs_up)[4]
    Sigma1_x_min_exp_down =sigma_band(gr_exp_down)[0]
    Sigma1_x_max_exp_down =sigma_band(gr_exp_down)[1]
    Sigma2_x_min_exp_down =sigma_band(gr_exp_down)[2]
    Sigma2_x_max_exp_down =sigma_band(gr_exp_down)[3]
    best_exp_down         =sigma_band(gr_exp_down)[4]
    Sigma1_x_min_obs_down =sigma_band(gr_obs_down)[0]
    Sigma1_x_max_obs_down =sigma_band(gr_obs_down)[1]
    Sigma2_x_min_obs_down =sigma_band(gr_obs_down)[2]
    Sigma2_x_max_obs_down =sigma_band(gr_obs_down)[3]
    best_obs_down         =sigma_band(gr_obs_down)[4]
            
    canvas = ROOT.TCanvas('canvas','',900, 900)
    canvas.cd()
    canvas.SetTickx()
    canvas.SetTicky()
    canvas.SetLeftMargin(0.13)
    canvas.SetBottomMargin(0.13)
    y_min=0
    y_max=y_min+4.1
    y_max=y_min+4.8
#    y_max=y_min+0.1
    x_min=0.4
    x_max=1.6
    if coulp=="Cphiq":
        x_title="C_{#phiq}^{(3)}#font[22]{/}#Lambda^{2} [TeV^{-2}]"
        x_min=-12
        x_max=6
        if "ee" in chan or "mumu" in chan:
            x_min=-14
            x_max=6
        elif "combined" in chan:
            #x_min=-11
            #x_max=2.5
            x_min=-5
            x_max=2
    elif coulp=="Ctw":
        x_title="C_{tW}#font[22]{/}#Lambda^{2} [TeV^{-2}]"
        #x_min=-11
        #x_max=8
        x_min=-3
        x_max=8
        if "combined" not in chan :
            x_min=-15
            x_max=10
    elif coulp=="Ctg":
        x_title="C_{tG}#font[22]{/}#Lambda^{2} [TeV^{-2}]"
        x_min=-0.9
        x_max=0.6
        if "mumu" in chan:
            x_min=-1.7
            x_max=0.8
            if "_1j1t" == region:
                x_min=-1.4
                x_max=0.8
        elif "emu" in chan:
            x_min=-1.5
            x_max=0.6
            if  region in ["_1j1t","_1j0t_1j1t"]:
                x_min=-1.4
                x_max=0.8
        elif "ee" in chan:
            x_min=-1.5
            x_max=0.6
            if  region in ["_1j1t"]:
                x_min=-1.2
                x_max=0.8
        elif "combined" in chan:
            #x_min=-1.5
            #x_max=0.6
            x_min=-0.6
            x_max=0.5
            if  region in ["_1j1t"]:
                x_min=-1.6
                x_max=0.8
    elif coulp=="Cg":
        x_title="C_{G}#font[22]{/}#Lambda^{2} [TeV^{-2}]"
        x_min=-3.5
        x_max=1.3
        if "combined" in chan:
            x_min=-1.5
            x_max=1.3
    elif coulp=="Cug":
        x_title="C_{uG}#font[22]{/}#Lambda^{2} [TeV^{-2}]"
        x_min=-1.8
        x_max=0.6
        if "combined" in chan:
            #x_min=-0.9
            #x_max=0.36
            x_min=-0.34
            x_max=0.34
    elif coulp=="Ccg":
        x_title="C_{cG}#font[22]{/}#Lambda^{2} [TeV^{-2}]"
        x_min=-3
        x_max=1.2
        if "combined" in chan:
            #x_min=-2.1
            #x_max=0.75
            x_min=-0.68
            x_max=0.68
    dummy = ROOT.TH2D("dummy","",1,x_min,x_max,1,y_min,y_max)
    dummy.SetStats(ROOT.kFALSE)
    dummy.GetYaxis().SetTitle("-2 #Deltaln L")
    dummy.GetXaxis().SetTitle("%s"%x_title)
    dummy.GetXaxis().SetTitleSize(0.05)
    dummy.GetYaxis().SetTitleSize(0.05)
    dummy.GetYaxis().SetLabelSize(0.04)
    dummy.GetXaxis().SetLabelSize(0.04)
    dummy.GetYaxis().SetLabelOffset(0.01)
    dummy.GetXaxis().SetLabelOffset(0.015)
    dummy.GetYaxis().SetTitleOffset(1.1)
    dummy.GetXaxis().SetTitleOffset(1.1)
    dummy.GetXaxis().SetMoreLogLabels()
    dummy.GetXaxis().SetNoExponent()
#    dummy.GetXaxis().CenterTitle()
#    dummy.GetYaxis().CenterTitle()
    dummy.Draw()
#    gr_exp.Draw("pc")
#    gr_exp_up.Draw("pc")
#    gr_exp_down.Draw("pc")
#    gr_exp.Draw("pl")
    if Unblind:
        str_tmp=str(coulp+"_"+chan+region)
        if Add_up_down:
            if str_tmp =="Ctg_combined":
                gr_obs_down.Fit("pol2","0","",-0.15,0.3)
                Function=gr_obs_down.GetFunction("pol2")
                Function.SetRange(-0.5,0.5)
                Function.SetLineColor(gr_obs_down.GetLineColor())
                Function.SetLineWidth(gr_obs_down.GetLineWidth())
                Function.SetLineStyle(gr_obs_down.GetLineStyle())
                Function.Draw("same")
                gr_obs_up.Draw("pl")
                Sigma1_x_min_obs_down =sigma_band_Fun(fun=Function, low=-0.5, up=0.5, points=200)[0]
                Sigma1_x_max_obs_down =sigma_band_Fun(fun=Function, low=-0.5, up=0.5, points=200)[1]
                Sigma2_x_min_obs_down =sigma_band_Fun(fun=Function, low=-0.5, up=0.5, points=200)[2]
                Sigma2_x_max_obs_down =sigma_band_Fun(fun=Function, low=-0.5, up=0.5, points=200)[3]
                best_obs_down         =sigma_band_Fun(fun=Function, low=-0.5, up=0.5, points=200)[4]
            elif str_tmp =="Ctg_emu":
                gr_obs_down.Fit("pol2","0","",0,0.21)
                Function=gr_obs_down.GetFunction("pol2")
                Function.SetRange(-0.5,0.5)
                Function.SetLineColor(gr_obs_down.GetLineColor())
                Function.SetLineWidth(gr_obs_down.GetLineWidth())
                Function.SetLineStyle(gr_obs_down.GetLineStyle())
                Function.Draw("same")
                gr_obs_up.Draw("pl")
                Sigma1_x_min_obs_down =sigma_band_Fun(fun=Function, low=-0.6, up=0.6, points=200)[0]
                Sigma1_x_max_obs_down =sigma_band_Fun(fun=Function, low=-0.6, up=0.6, points=200)[1]
                Sigma2_x_min_obs_down =sigma_band_Fun(fun=Function, low=-0.6, up=0.6, points=200)[2]
                Sigma2_x_max_obs_down =sigma_band_Fun(fun=Function, low=-0.6, up=0.6, points=200)[3]
                best_obs_down         =sigma_band_Fun(fun=Function, low=-0.6, up=0.6, points=200)[4]
            elif str_tmp =="Ctg_combined_1j1t":
                gr_obs_down.SetPoint(gr_obs_down.GetN(),0.207634,0)##set point from fit
                gr_obs_down.Fit("pol2","0","",-0.3,0.20764)
                Function=gr_obs_down.GetFunction("pol2")
                Function.SetRange(-0.5,0.8)
                Function.SetLineColor(gr_obs_down.GetLineColor())
                Function.SetLineWidth(gr_obs_down.GetLineWidth())
                Function.SetLineStyle(gr_obs_down.GetLineStyle())
                Function.Draw("same")
                gr_obs_up.Draw("pl")
                Sigma1_x_min_obs_down =sigma_band_Fun(fun=Function, low=-0.5, up=0.7, points=200)[0]
                Sigma1_x_max_obs_down =sigma_band_Fun(fun=Function, low=-0.5, up=0.7, points=200)[1]
                Sigma2_x_min_obs_down =sigma_band_Fun(fun=Function, low=-0.5, up=0.7, points=200)[2]
                Sigma2_x_max_obs_down =sigma_band_Fun(fun=Function, low=-0.5, up=0.7, points=200)[3]
                best_obs_down         =sigma_band_Fun(fun=Function, low=-0.5, up=0.7, points=200)[4]
            elif str_tmp =="Ctg_emu_1j1t":
                gr_obs_down.Fit("pol2","0","",-0.2,0.3)
                Function=gr_obs_down.GetFunction("pol2")
                Function.SetRange(-0.5,0.7)
                Function.SetLineColor(gr_obs_down.GetLineColor())
                Function.SetLineWidth(gr_obs_down.GetLineWidth())
                Function.SetLineStyle(gr_obs_down.GetLineStyle())
                Function.Draw("same")
                gr_obs_up.Draw("pl")
                Sigma1_x_min_obs_down =sigma_band_Fun(fun=Function, low=-0.6, up=0.7, points=200)[0]
                Sigma1_x_max_obs_down =sigma_band_Fun(fun=Function, low=-0.6, up=0.7, points=200)[1]
                Sigma2_x_min_obs_down =sigma_band_Fun(fun=Function, low=-0.6, up=0.7, points=200)[2]
                Sigma2_x_max_obs_down =sigma_band_Fun(fun=Function, low=-0.6, up=0.7, points=200)[3]
                best_obs_down         =sigma_band_Fun(fun=Function, low=-0.6, up=0.7, points=200)[4]
            elif str_tmp =="Cg_combined":
                gr_obs_up.Fit("pol2","0","",-0.5,0.05)
                Function=gr_obs_up.GetFunction("pol2")
                Function.SetRange(-1,1)
                Function.SetLineColor(gr_obs_up.GetLineColor())
                Function.SetLineWidth(gr_obs_up.GetLineWidth())
                Function.SetLineStyle(gr_obs_up.GetLineStyle())
                Function.Draw("same")
                gr_obs_down.Draw("pl")
                Sigma1_x_min_obs_up =sigma_band_Fun(fun=Function, low=-1.0, up=0.8, points=300)[0]
                Sigma1_x_max_obs_up =sigma_band_Fun(fun=Function, low=-1.0, up=0.8, points=300)[1]
                Sigma2_x_min_obs_up =sigma_band_Fun(fun=Function, low=-1.0, up=0.8, points=300)[2]
                Sigma2_x_max_obs_up =sigma_band_Fun(fun=Function, low=-1.0, up=0.8, points=300)[3]
                best_obs_up         =sigma_band_Fun(fun=Function, low=-1.0, up=0.8, points=300)[4]
            else:
                gr_obs_up  .Draw("pl")
                gr_obs_down.Draw("pl")
        if str_tmp !="Ctg_combined":
            gr_obs.Draw("pl")
        if str_tmp =="Ctg_combined":
            gr_obs.Fit("pol2","0","",-0.4,0.15)
            Function=gr_obs.GetFunction("pol2")
            Function.SetRange(-0.6,0.5)
            Function.SetLineColor(gr_obs.GetLineColor())
            Function.SetLineWidth(gr_obs.GetLineWidth())
            Function.SetLineStyle(gr_obs.GetLineStyle())
            Function.Draw("same")
    gr_exp.Draw("pc")
    dummy.Draw("AXISSAME")
    line_1sigma =ROOT.TLine(x_min,1,x_max,1)
    line_2sigma =ROOT.TLine(x_min,3.84,x_max,3.84)
    line_1sigma.SetLineColor(sigma_color)
    line_1sigma.SetLineStyle(2)
    line_1sigma.SetLineWidth(3)
    line_2sigma.SetLineColor(sigma_color)
    line_2sigma.SetLineStyle(2)
    line_2sigma.SetLineWidth(3)
#    line_1sigma.Draw()
#    line_2sigma.Draw()
    print "exp:%-5s_%-8s%-15s| best: %.2f | 1sigma:%.2f to %.2f | 2sigma:%.2f to %.2f|"%(coulp,chan,region,float(0),float(Sigma1_x_min_exp),float(Sigma1_x_max_exp),float(Sigma2_x_min_exp),float(Sigma2_x_max_exp))
    if Unblind:
        print "obs:%-5s_%-8s%-15s| best: %.3f | 1sigma:%.2f to %.2f | 2sigma:%.2f to %.2f|"%(coulp,chan,region,float(best_obs),float(Sigma1_x_min_obs),float(Sigma1_x_max_obs),float(Sigma2_x_min_obs),float(Sigma2_x_max_obs))
        print "obs up:%-5s_%-8s%-15s| best: %.3f | 1sigma:%.2f to %.2f | 2sigma:%.2f to %.2f|"%(coulp,chan,region,float(best_obs_up),float(Sigma1_x_min_obs_up),float(Sigma1_x_max_obs_up),float(Sigma2_x_min_obs_up),float(Sigma2_x_max_obs_up))
        print "obs down:%-5s_%-8s%-15s| best: %.3f | 1sigma:%.2f to %.2f | 2sigma:%.2f to %.2f|"%(coulp,chan,region,float(best_obs_down),float(Sigma1_x_min_obs_down),float(Sigma1_x_max_obs_down),float(Sigma2_x_min_obs_down),float(Sigma2_x_max_obs_down))
#    legend = ROOT.TLegend(0.15,0.4,0.35,0.75)
    legend = ROOT.TLegend(0.35,0.746,0.7,0.896)
    legend.AddEntry(gr_exp,'Exp.','l')
#    legend.AddEntry(gr_exp,'Expected','l')
#    legend.AddEntry(gr_exp_up  ,'Expected (+theory sys.)','l')
#    legend.AddEntry(gr_exp_down,'Expected (-theory sys.)','l')
    if Unblind:
        #legend.AddEntry(gr_obs,'Observed','l')
        legend.AddEntry(gr_obs,'Obs.','l')
        if Add_up_down:
            #legend.AddEntry(gr_obs_up  ,'Observed (#plus theory sys.)','l')
            #legend.AddEntry(gr_obs_down,'Observed (#minus theory sys.)','l')
            #legend.AddEntry(gr_obs_down,'Observed (#pm theory sys.)','l')
            legend.AddEntry(gr_obs_up  ,'Obs. (#plus theory sys.)','l')
            legend.AddEntry(gr_obs_down,'Obs. (#minus theory sys.)','l')
    legend.SetBorderSize(0)
    #legend.SetTextSize(0.03)
    legend.SetTextFont(42)
    #legend.SetFillStyle(0)
    legend.Draw()
    line_1sigma.Draw()
    line_2sigma.Draw()
    label_lamda = ROOT.TLatex(0.15,0.78,"#Lambda = 1 TeV")
    label_lamda.SetNDC(ROOT.kTRUE)
    #label_lamda.Draw()
    #label_1sigma = ROOT.TLatex(0.92,0.26,"1 #sigma")
    label_1sigma = ROOT.TLatex(0.905,0.275,"68%")
    label_1sigma.SetNDC(ROOT.kTRUE)
    label_1sigma.SetTextColor(sigma_color)
    label_1sigma.Draw()
    #label_2sigma = ROOT.TLatex(0.92,0.61,"2 #sigma")
    label_2sigma = ROOT.TLatex(0.905,0.735,"95%")
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
        label.DrawLatex(0.15,0.2, "ee%s"%str_region)
    elif chan=="emu":
        label.DrawLatex(0.15,0.2, "e#mu%s"%str_region)
    elif chan=="mumu":
        label.DrawLatex(0.15,0.2, "#mu#mu%s"%str_region)
    elif chan=="combined":
        label.DrawLatex(0.15,0.2, "%s"%str_region)
    Label_cms_prelim = ROOT.TPaveText(0.11,0.905,0.4,0.945,"NDC")
    Label_cms_prelim.SetLineColor(10)
    Label_cms_prelim.SetFillColor(10)
    #Label_cms_prelim.SetTextSize(0.075)
    Label_cms_prelim.SetTextSize(0.05)
    Label_cms_prelim.SetTextAlign(12)
    Label_cms_prelim.SetTextFont(61)
    Label_cms_prelim.SetFillStyle(0)

    label_cms    = ROOT.TPaveLabel(0.13, 0.9, 0.2, 0.94, "CMS", "brNDC")
    label_prelim = ROOT.TPaveLabel(0.22, 0.9, 0.36, 0.94, "Preliminary", "brNDC")
    Label_lumi = ROOT.TPaveText(0.61,0.905,0.81,0.945,"NDC")
    if for_paper_style:
        Label_cms_prelim.AddText("CMS")
        Label_cms_prelim.SetShadowColor(10)
        Label_cms_prelim.Draw()
        Label_lumi.SetLineColor(10)
        Label_lumi.SetFillColor(10)
        #Label_lumi.SetTextSize(0.06)
        #Label_lumi.SetTextSize(0.05)
        Label_lumi.SetTextSize(0.04)
        Label_lumi.SetTextAlign(12)
        Label_lumi.SetTextFont(42)
        Label_lumi.AddText("35.9 fb^{-1} (13 TeV)")
        Label_lumi.SetShadowColor(10)
        Label_lumi.Draw()
    else:
        label_cms.SetBorderSize(0)
        label_cms.SetFillColor(0)
        label_cms.SetFillStyle(0)
        label_cms.SetTextFont(61)
        label_cms.SetTextSize(1)
        label_cms.Draw()
        label_prelim.SetBorderSize(0)
        label_prelim.SetFillColor(0)
        label_prelim.SetFillStyle(0)
        label_prelim.SetTextFont(51)
        label_prelim.SetTextSize(1* 0.8)
        label_prelim.Draw()
        Label_lumi = ROOT.TPaveText(0.65,0.9,0.85,0.94,"NDC")
        Label_lumi.SetBorderSize(0)
        Label_lumi.SetFillColor(0)
        Label_lumi.SetFillStyle(0)
        Label_lumi.SetTextSize(0.035)
        Label_lumi.SetTextAlign(12)
        Label_lumi.SetTextFont(42)
        Label_lumi.AddText("35.9 fb^{-1} (13 TeV)")
        Label_lumi.SetShadowColor(10)
        Label_lumi.Draw()

    canvas.Print('./scan_plot/%s_%s%s_scan.png'%(coulp,chan,region))
    canvas.Print('./scan_plot/%s_%s%s_scan.pdf'%(coulp,chan,region))

#Dir="./scan_both/"##for FCNC final
Dir="./scan_NoTopPtReW/"##for No top pt reweighting check
#Dir="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/scan_script/output/"##for EFT final
for_paper_style=True
Unblind=True
Add_up_down=False ## true for noimial
transfer_to_coulping=True 
For_FCNC=True
for coup in ["Ctg","Ctw","Cphiq","Cg","Cug","Ccg"]:
    for chan in["ee","emu","mumu","combined"]:
        for region in ["_1j1t","_1j0t_1j1t","_1j1t_2j1t","_1j1t_2j1t_2j2t",""]:
            if For_FCNC:
                draw(Dir+"higgsCombineexp_%s_%s%s.MultiDimFit.mH125.7.root"%(str(chan),str(coup),str(region)),Dir+"higgsCombineexp_%s_%s%s.MultiDimFit.mH125.7.root"%(str(chan),str(coup),str(region)),Dir+"higgsCombineexp_%s_%s%s.MultiDimFit.mH125.7.root"%(str(chan),str(coup),str(region)),Dir+"higgsCombineobs_%s_%s%s.MultiDimFit.mH125.7.root"%(str(chan),str(coup),str(region)),Dir+"higgsCombineobs_%s_%s%s.MultiDimFit.mH125.7.root"%(str(chan),str(coup),str(region)),Dir+"higgsCombineobs_%s_%s%s.MultiDimFit.mH125.7.root"%(str(chan),str(coup),str(region)),str(chan),str(region),str(coup))
            else:
                draw(Dir+"higgsCombineexp_%s_%s%s.MultiDimFit.mH125.7.root"%(str(chan),str(coup),str(region)),Dir+"higgsCombineexp_%s_%s%s.MultiDimFit.mH125.7.root"%(str(chan),str(coup),str(region+"_up")),Dir+"higgsCombineexp_%s_%s%s.MultiDimFit.mH125.7.root"%(str(chan),str(coup),str(region+"_down")),Dir+"higgsCombineobs_%s_%s%s.MultiDimFit.mH125.7.root"%(str(chan),str(coup),str(region)),Dir+"higgsCombineobs_%s_%s%s.MultiDimFit.mH125.7.root"%(str(chan),str(coup),str(region+"_up")),Dir+"higgsCombineobs_%s_%s%s.MultiDimFit.mH125.7.root"%(str(chan),str(coup),str(region+"_down")),str(chan),str(region),str(coup))
