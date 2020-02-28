import ROOT
import gc
ROOT.gROOT.SetBatch(ROOT.kTRUE)


def draw_marg_indiv(keys, gr_dict, chan):
        canvas = ROOT.TCanvas('canvas','',900, 600)
        canvas.cd()
        canvas.SetTickx()
        canvas.SetTicky()
        canvas.SetBottomMargin(0.15)
        canvas.SetLeftMargin(0.15)
        y_min=0
        y_max=3
        #x_min=0.7
        #x_max=1.3
        x_min=0.9
        x_max=1.25
        if chan=="Marginalized":
            #x_min=0.96
            x_min=0.97
            x_max=1.12
        elif chan=="Individual":
            #x_min=0.985
            x_min=0.97
            #x_max=1.1
            x_max=1.12

        dummy = ROOT.TH2D("dummy_%s"%chan,"",1,x_min,x_max,3,y_min,y_max)
        dummy.SetStats(ROOT.kFALSE)
        dummy.GetYaxis().SetTitle("")
        dummy.GetXaxis().SetTitle("")
        dummy.GetXaxis().SetTitleSize(0.07)
        dummy.GetYaxis().SetTitleSize(0.07)
        dummy.GetYaxis().SetLabelSize(0.08)
        dummy.GetYaxis().SetBinLabel(1,"|V_{tb}|")
        dummy.GetYaxis().SetBinLabel(2,"1+|V_{ts}|")
        dummy.GetYaxis().SetBinLabel(3,"1+|V_{td}|")
        dummy.GetXaxis().SetLabelSize(0.06)
        dummy.GetYaxis().SetLabelOffset(0.01)
        dummy.GetXaxis().SetLabelOffset(0.015)
        dummy.GetYaxis().SetTitleOffset(1)
        dummy.GetXaxis().SetTitleOffset(1)
        dummy.GetXaxis().SetMoreLogLabels()
        dummy.GetXaxis().SetNoExponent()
        dummy.GetXaxis().CenterTitle()
        dummy.GetYaxis().CenterTitle()
        dummy.GetXaxis().SetNdivisions(505)
        dummy.Draw()
        line_1 =ROOT.TLine(1,y_min,1,y_max)
        line_1.SetLineColor(ROOT.kBlack)
        line_1.SetLineStyle(2)
        line_1.SetLineWidth(2)
        line_1.Draw()
        lx_min=0.65
        ly_min=0.68
        lx_max=0.85
        ly_max=0.88
        legend = ROOT.TLegend(lx_min,ly_min,lx_max,ly_max)
        legend.SetBorderSize(0)
        legend.SetFillStyle(4000)
        legend.SetTextFont(42)
        legend.SetTextSize(0.04)
        ####################  Draw result #######################################
        for ikey in keys: 
            tmp="" if ikey not in text_leg else text_leg[ikey]
            gr_dict[ikey][chan].Draw("pez")
            legend.AddEntry(gr_dict[ikey][chan],'%s'%(tmp),'pl')
        dummy.Draw("AXISSAME")
        legend.Draw()
        label = ROOT.TLatex()
        label.SetTextAlign(12)
        label.SetTextFont(42)
        label.SetTextSize(0.05)
        label.SetNDC(ROOT.kTRUE)
        label.DrawLatex(0.35,0.85,label_sigma)
        label.Draw()
        label_chan = ROOT.TLatex()
        label_chan.SetTextAlign(12)
        label_chan.SetTextFont(42)
        label_chan.SetTextSize(0.05)
        label_chan.SetNDC(ROOT.kTRUE)
        label_chan.DrawLatex(0.15,0.93, channel)
        label_M = ROOT.TLatex()
        label_M.SetTextAlign(12)
        label_M.SetTextFont(42)
        label_M.SetTextSize(0.05)
        label_M.SetNDC(ROOT.kTRUE)
        if chan=="Marginalized":
            label_M.DrawLatex(0.73,0.93,chan)
        elif chan=="Individual":
            label_M.DrawLatex(0.775,0.93,chan)
        label_M.Draw()
        canvas.Print('./summary_limit_plot/%s.png'%(chan)) 
        canvas.Print('./summary_limit_plot/%s.pdf'%(chan)) 
        del canvas
        gc.collect()


label_sigma="68% CL Expected"
channel="#sigma_{diff}^{t-ch} (LHC)"
cat=[]
cat.append("Diff_8TeV_Ratio")
cat.append("Diff_13TeV_Ratio300fb")
cat.append("Diff_13TeV_Ratio3000fb")
color={"Diff_8TeV_Ratio":ROOT.TColor.GetColor("#0000ff"),"Diff_13TeV_Ratio300fb":ROOT.TColor.GetColor("#00ff00"),"Diff_13TeV_Ratio3000fb":ROOT.TColor.GetColor("#ffd700")}
text_leg={"Diff_8TeV_Ratio":"8TeV","Diff_13TeV_Ratio300fb":"13TeV 300fb^{-1}","Diff_13TeV_Ratio3000fb":"13TeV 3000fb^{-1}"}
do_marg_indiv=True
do_marg      =False
gr_dict={}
if do_marg_indiv:
    for ic in cat:
        gr_dict[ic]={}
        F_in=ROOT.TFile("limit_out/limit_1D_dchi2_%s_exp.root"%(ic),"read")
        gr_margin=None
        gr_Vtb_indiv=None
        gr_Vts_indiv=None
        gr_Vtd_indiv=None
        gr_margin=F_in.Get("%s_correct_marginal"%ic)
        gr_Vtb_indiv=F_in.Get("%s_individual_Vtb"%ic)
        gr_Vts_indiv=F_in.Get("%s_individual_Vts"%ic)
        gr_Vtd_indiv=F_in.Get("%s_individual_Vtd"%ic)
        line_width=25
        marker_size=2
        icolor=1 if ic not in color else color[ic]
        gr_margin.SetLineColor(icolor)
        gr_margin.SetLineWidth(line_width)
        gr_margin.SetMarkerColor(ROOT.TColor.GetColor("#ff0000"))
        gr_margin.SetMarkerStyle(8)
        gr_margin.SetMarkerSize(marker_size)
        gr_margin.SetName("Marginalized")
        gr_margin.SetPoint(0,1                    ,gr_margin.GetY()[0])##set vtb==1
        gr_margin.SetPoint(1,1+gr_margin.GetX()[1],gr_margin.GetY()[1])
        gr_margin.SetPoint(2,1+gr_margin.GetX()[2],gr_margin.GetY()[2])
        gr_indivi=ROOT.TGraphAsymmErrors()
        gr_indivi.SetName("Individual")
        #gr_indivi.SetPoint(0,gr_Vtb_indiv.GetX()[0],gr_Vtb_indiv.GetY()[0]+0.2)
        #gr_indivi.SetPoint(1,1+gr_Vts_indiv.GetX()[0],gr_Vts_indiv.GetY()[0]+0.2)
        #gr_indivi.SetPoint(2,1+gr_Vtd_indiv.GetX()[0],gr_Vtd_indiv.GetY()[0]+0.2)
        gr_indivi.SetPoint(0,gr_Vtb_indiv.GetX()[0],gr_Vtb_indiv.GetY()[0]  )
        gr_indivi.SetPoint(1,1+gr_Vts_indiv.GetX()[0],gr_Vts_indiv.GetY()[0])
        gr_indivi.SetPoint(2,1+gr_Vtd_indiv.GetX()[0],gr_Vtd_indiv.GetY()[0])
        gr_indivi.SetPointEXlow(0,gr_Vtb_indiv.GetErrorXlow(0))
        gr_indivi.SetPointEXlow(1,gr_Vts_indiv.GetErrorXlow(0))
        gr_indivi.SetPointEXlow(2,gr_Vtd_indiv.GetErrorXlow(0))
        gr_indivi.SetPointEXhigh(0,gr_Vtb_indiv.GetErrorXhigh(0))
        gr_indivi.SetPointEXhigh(1,gr_Vts_indiv.GetErrorXhigh(0))
        gr_indivi.SetPointEXhigh(2,gr_Vtd_indiv.GetErrorXhigh(0))
        gr_indivi.SetLineColor(icolor)
        gr_indivi.SetLineWidth(line_width)
        gr_indivi.SetMarkerColor(ROOT.TColor.GetColor("#ff0000"))
        gr_indivi.SetMarkerStyle(8)
        gr_indivi.SetMarkerSize(marker_size)
        gr_dict[ic]={"Marginalized":gr_margin,"Individual":gr_indivi}
        print "%s marginalized:%.4f+%.4f-%.4f,%.4f+%.4f-%.4f,%.4f+%.4f-%.4f"%(ic,gr_margin.GetX()[0],gr_margin.GetErrorXhigh(0),gr_margin.GetErrorXlow(0),gr_margin.GetX()[1],gr_margin.GetErrorXhigh(1),gr_margin.GetErrorXlow(1),gr_margin.GetX()[2],gr_margin.GetErrorXhigh(2),gr_margin.GetErrorXlow(2))
        print "%s individual  :%.4f+%.4f-%.4f,%.4f+%.4f-%.4f,%.4f+%.4f-%.4f"%(ic,gr_indivi.GetX()[0],gr_indivi.GetErrorXhigh(0),gr_indivi.GetErrorXlow(0),gr_indivi.GetX()[1],gr_indivi.GetErrorXhigh(1),gr_indivi.GetErrorXlow(1),gr_indivi.GetX()[2],gr_indivi.GetErrorXhigh(2),gr_indivi.GetErrorXlow(2))
    draw_marg_indiv(cat,gr_dict, "Marginalized")
    draw_marg_indiv(cat,gr_dict, "Individual")
    print "done"
'''
if do_marg:
    gr_margin1=F_in.Get("Diff_7TeV_Inclusive_marginalized")
    gr_margin2=F_in.Get("Diff_8TeV_7TeV_Inclusive_marginalized")
    gr_margin2.SetPoint(0,gr_margin2.GetX()[0],gr_margin2.GetY()[0]+0.2)
    gr_margin2.SetPoint(1,gr_margin2.GetX()[1],gr_margin2.GetY()[1]+0.2)
    gr_margin2.SetPoint(2,gr_margin2.GetX()[2],gr_margin2.GetY()[2]+0.2)
   
    gr_margin1.SetName("7TeV differential + Inclusive")
    gr_margin2.SetName("all")
    line_width=2
    gr_margin1.SetLineColor(ROOT.kBlue)
    gr_margin1.SetLineWidth(line_width)
    gr_margin1.SetMarkerColor(ROOT.kBlue)
    gr_margin1.SetMarkerStyle(8)
    gr_margin2.SetLineColor(ROOT.kRed)
    gr_margin2.SetLineWidth(line_width)
    gr_margin2.SetMarkerColor(ROOT.kRed)
    gr_margin2.SetMarkerStyle(8)
    ic="margin_"
    draw_marg_indiv(F_in,ic,gr_margin1,gr_margin2)
'''
