import ROOT
import gc
ROOT.gROOT.SetBatch(ROOT.kTRUE)


def draw_marg_indiv(F_in,ic, gr1,gr2):
        canvas = ROOT.TCanvas('canvas','',900, 600)
        canvas.cd()
        canvas.SetTickx()
        canvas.SetTicky()
        canvas.SetBottomMargin(0.15)
        canvas.SetLeftMargin(0.15)
        y_min=0
        y_max=3
        x_min=0.959
        x_max=1.08
        dummy = ROOT.TH2D("dummy_%s"%ic,"",1,x_min,x_max,3,y_min,y_max)
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
        #dummy.GetXaxis().SetNdivisions(505)
        dummy.GetXaxis().SetNdivisions(6,ROOT.kTRUE)
        dummy.GetXaxis().CenterTitle()
        dummy.GetYaxis().CenterTitle()
        dummy.Draw()
        ############Clone resut for negative #################
        #gr_margin_neg   =gr_margin   .Clone("Vtx_margin_negative")
        #gr_Vtb_indiv_neg=gr_Vtb_indiv.Clone("Vtb_indiv_negative")
        #gr_Vts_indiv_neg=gr_Vts_indiv.Clone("Vts_indiv_negative")
        #gr_Vtd_indiv_neg=gr_Vtd_indiv.Clone("Vtd_indiv_negative")
        #for ibin in range(0,gr_margin_neg.GetN()):
        #    gr_margin_neg.SetPoint(ibin,-1*gr_margin_neg.GetX()[ibin],gr_margin_neg.GetY()[ibin])
        #    gr_margin_neg.SetPointEXlow(ibin,gr_margin.GetEXhigh()[ibin])
        #    gr_margin_neg.SetPointEXhigh(ibin,gr_margin.GetEXlow()[ibin])
        #gr_Vtb_indiv_neg.SetPoint(0,-1*gr_Vtb_indiv_neg.GetX()[0],gr_Vtb_indiv_neg.GetY()[0])
        #gr_Vtb_indiv_neg.SetPointEXlow(0,gr_Vtb_indiv.GetEXhigh()[0])
        #gr_Vtb_indiv_neg.SetPointEXhigh(0,gr_Vtb_indiv.GetEXlow()[0])
        #gr_Vts_indiv_neg.SetPoint(0,-1*gr_Vts_indiv_neg.GetX()[0],gr_Vts_indiv_neg.GetY()[0])
        #gr_Vts_indiv_neg.SetPointEXlow(0,gr_Vts_indiv.GetEXhigh()[0])
        #gr_Vts_indiv_neg.SetPointEXhigh(0,gr_Vts_indiv.GetEXlow()[0])
        #gr_Vtd_indiv_neg.SetPoint(0,-1*gr_Vtd_indiv_neg.GetX()[0],gr_Vtd_indiv_neg.GetY()[0])
        #gr_Vtd_indiv_neg.SetPointEXlow(0,gr_Vtd_indiv.GetEXhigh()[0])
        #gr_Vtd_indiv_neg.SetPointEXhigh(0,gr_Vtd_indiv.GetEXlow()[0])
        ###################### one line ############################
        line_1 =ROOT.TLine(1,y_min,1,y_max)
        line_1.SetLineColor(ROOT.kBlack)
        line_1.SetLineStyle(2)
        line_1.SetLineWidth(2)
        line_1.Draw()
        ####################  Draw result #######################################
        gr1.Draw("pez")
        gr2.Draw("pez")
        dummy.Draw("AXISSAME")
        #lx_min=0.4
        #ly_min=0.6
        #lx_max=0.6
        #ly_max=0.8
        lx_min=0.62
        ly_min=0.6
        lx_max=0.83
        ly_max=0.8
        legend = ROOT.TLegend(lx_min,ly_min,lx_max,ly_max)
        legend.AddEntry(gr2,'%s'%(gr2.GetName())  ,'pl')
        legend.AddEntry(gr1,'%s'%(gr1.GetName()),'pl')
        legend.SetBorderSize(0)
        legend.SetTextFont(42)
        legend.SetTextSize(0.06)
        legend.Draw()
        label = ROOT.TLatex()
        label.SetTextAlign(12)
        label.SetTextFont(42)
        label.SetTextSize(0.05)
        label.SetNDC(ROOT.kTRUE)
        #label.DrawLatex(0.2,0.85,label_sigma)
        label.DrawLatex(0.6,0.86,label_sigma)
        label.Draw()
        label_chan = ROOT.TLatex()
        label_chan.SetTextAlign(12)
        label_chan.SetTextFont(42)
        label_chan.SetTextSize(0.05)
        label_chan.SetNDC(ROOT.kTRUE)
        label_chan.DrawLatex(0.15,0.93, chan)
        canvas.Print('./summary_limit_plot/%s.png'%(ic)) 
        canvas.Print('./summary_limit_plot/%s.pdf'%(ic)) 
        del canvas
        gc.collect()


cat=[]
label_sigma="68% CL Observed"
#F_in=ROOT.TFile("limit_out/limit_1D_dchi2_Diff_8TeV_7TeV_Inclusive_obs.root","read")
#chan="LHC + Tevatron"
#cat.append("Diff_8TeV_7TeV_Inclusive")
#F_in=ROOT.TFile("limit_out/limit_1D_dchi2_Diff_8TeV_Ratio_obs.root","read")
F_in=ROOT.TFile("limit_out_final/limit_1D_dchi2_Diff_8TeV_Ratio_obs.root","read")
chan="#sigma_{diff}^{t-ch} (LHC)                                   #sqrt{s} = 8 TeV, 20.2 fb^{-1}"
cat.append("Diff_8TeV_Ratio")
do_marg_indiv=True
do_marg      =False
if do_marg_indiv:
    for ic in cat:
        gr_margin=F_in.Get("%s_correct_marginal"%ic)
        gr_Vtb_indiv=F_in.Get("%s_individual_Vtb"%ic)
        gr_Vts_indiv=F_in.Get("%s_individual_Vts"%ic)
        gr_Vtd_indiv=F_in.Get("%s_individual_Vtd"%ic)
        line_width=25
        marker_size=2
        gr_margin.SetLineColor  (ROOT.TColor.GetColor("#0000ff"))
        gr_margin.SetMarkerColor(ROOT.TColor.GetColor("#ff0000"))
        gr_margin.SetLineWidth(line_width)
        gr_margin.SetMarkerStyle(8)
        #gr_margin.SetMarkerStyle(21)
        gr_margin.SetMarkerSize(marker_size)
        gr_margin.SetName("Marginalized")
        gr_margin.SetPoint(1,1+gr_margin.GetX()[1],gr_margin.GetY()[1])
        gr_margin.SetPoint(2,1+gr_margin.GetX()[2],gr_margin.GetY()[2])
        gr_indivi=ROOT.TGraphAsymmErrors()
        gr_indivi.SetName("Individual")
        gr_indivi.SetPoint(0,gr_Vtb_indiv.GetX()[0],gr_Vtb_indiv.GetY()[0]+0.2)
        gr_indivi.SetPoint(1,1+gr_Vts_indiv.GetX()[0],gr_Vts_indiv.GetY()[0]+0.2)
        gr_indivi.SetPoint(2,1+gr_Vtd_indiv.GetX()[0],gr_Vtd_indiv.GetY()[0]+0.2)
        gr_indivi.SetPointEXlow(0,gr_Vtb_indiv.GetErrorXlow(0))
        gr_indivi.SetPointEXlow(1,gr_Vts_indiv.GetErrorXlow(0))
        gr_indivi.SetPointEXlow(2,gr_Vtd_indiv.GetErrorXlow(0))
        gr_indivi.SetPointEXhigh(0,gr_Vtb_indiv.GetErrorXhigh(0))
        gr_indivi.SetPointEXhigh(1,gr_Vts_indiv.GetErrorXhigh(0))
        gr_indivi.SetPointEXhigh(2,gr_Vtd_indiv.GetErrorXhigh(0))
        gr_indivi.SetLineColor  (ROOT.TColor.GetColor("#00ff00"))
        gr_indivi.SetMarkerColor(ROOT.TColor.GetColor("#ff0000"))
        gr_indivi.SetLineWidth(line_width)
        gr_indivi.SetMarkerStyle(8)
        gr_indivi.SetMarkerSize(marker_size)
        draw_marg_indiv(F_in,ic,gr_margin,gr_indivi)
        print "marginalized:%.3f+%.3f-%.3f,%.3f+%.3f-%.3f,%.3f+%.3f-%.3f"%(gr_margin.GetX()[0],gr_margin.GetErrorXhigh(0),gr_margin.GetErrorXlow(0),gr_margin.GetX()[1],gr_margin.GetErrorXhigh(1),gr_margin.GetErrorXlow(1),gr_margin.GetX()[2],gr_margin.GetErrorXhigh(2),gr_margin.GetErrorXlow(2))
        print "individual  :%.3f+%.3f-%.3f,%.3f+%.3f-%.3f,%.3f+%.3f-%.3f"%(gr_indivi.GetX()[0],gr_indivi.GetErrorXhigh(0),gr_indivi.GetErrorXlow(0),gr_indivi.GetX()[1],gr_indivi.GetErrorXhigh(1),gr_indivi.GetErrorXlow(1),gr_indivi.GetX()[2],gr_indivi.GetErrorXhigh(2),gr_indivi.GetErrorXlow(2))
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
