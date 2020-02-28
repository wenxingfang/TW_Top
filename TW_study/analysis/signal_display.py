import ROOT
import gc
ROOT.gROOT.SetBatch(ROOT.kTRUE)

Ctw_Cphiq_SM_list=["TW"     ,"TWNLO","TT","DY","other"]
Ctw_Cphiq_BSM_list=["Signal","TWNLO","TT","DY","other"]
Ctg_SM_list=["TW"     ,"TWNLO","TTNNLO","DY","other"]
Ctg_BSM_list=["Signal","TWNLO","TTNNLO","DY","other"]


#C_Ctw=[-1.00,-2.00,1.00,2.00]
C_Ctw=["1.00","2.00","3.00","5.00"]
C_Ctg=["0.10","0.20","0.30"]
C_Cphiq=["2.00","3.00","4.00","5.00"]
for iCtw in C_Ctw:
    str_op="" if float(iCtw)>0 else "_opposite"
    f_Ctw=ROOT.TFile("./Limit_out/combined_Ctw_"+str(iCtw).strip("-")+str_op+".root")
    for iCtg in C_Ctg:
        str_op="" if float(iCtg)>0 else "_opposite"
        f_Ctg=ROOT.TFile("./Limit_out/combined_Ctg_"+str(iCtg).strip("-")+str_op+".root")
        for iCphiq in C_Cphiq:
            str_op="" if float(iCphiq)>0 else "_opposite"
            f_Cphiq=ROOT.TFile("./Limit_out/combined_Cphiq_"+str(iCphiq).strip("-")+str_op+".root")
            h_data     =f_Cphiq.Get("data_obs")
            h_SM       =f_Cphiq.Get(Ctw_Cphiq_SM_list[0]).Clone("SM_%s_%s_%s"%(str(iCtw),str(iCtg),str(iCphiq)))
            h_BSM_Cphiq=f_Cphiq.Get(Ctw_Cphiq_BSM_list[0]).Clone("BSM_Cphiq_%s"%(str(iCphiq)))
            h_BSM_Ctw  =f_Ctw  .Get(Ctw_Cphiq_BSM_list[0]).Clone("BSM_Ctw_%s"  %(str(iCtw)  ))
            h_BSM_Ctg  =f_Ctg  .Get(Ctg_BSM_list[0])      .Clone("BSM_Ctg_%s"  %(str(iCtg)  ))
            h_SM       .Scale(0)
            h_BSM_Cphiq.Scale(0)
            h_BSM_Ctw  .Scale(0)
            h_BSM_Ctg  .Scale(0)
            for hname in Ctw_Cphiq_SM_list:
                h_SM       .Add(f_Cphiq.Get(hname))
            for hname in Ctw_Cphiq_BSM_list: 
                h_BSM_Cphiq.Add(f_Cphiq.Get(hname))
            for hname in Ctw_Cphiq_BSM_list: 
                h_BSM_Ctw  .Add(f_Ctw.Get(hname))
            for hname in Ctg_BSM_list: 
                h_BSM_Ctg  .Add(f_Ctg.Get(hname))

            canvas = ROOT.TCanvas('canvas_Ctw%s_Ctg%s_Cphiq%s'%(str(iCtw),str(iCtg),str(iCphiq)),'',50,50,865,780)
            canvas.SetLeftMargin(0.5)
            canvas.cd()
            pad1=ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 0.99 , 0)#used for the hist plot
            pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.3 , 0)#used for the ratio plot
            pad1.Draw()
            pad2.Draw()
            pad2.SetGridy()
            pad2.SetTickx()
            pad1.SetBottomMargin(0.04)
            pad1.SetLeftMargin(0.12)
            pad1.SetRightMargin(0.05)
            pad2.SetTopMargin(0.0)
            pad2.SetBottomMargin(0.3)
            pad2.SetLeftMargin(0.12)
            pad2.SetRightMargin(0.05)
            pad1.cd()
            nbins=h_SM.GetNbinsX()
            x_min=h_SM.GetXaxis().GetXmin()
            x_max=h_SM.GetXaxis().GetXmax()
            y_min=0
            y_max=2*h_SM.GetBinContent(h_SM.GetMaximumBin())
            dummy = ROOT.TH2D("dummy_%s"%(canvas.GetName()),"",nbins,x_min,x_max,1,y_min,y_max)
            dummy.SetStats(ROOT.kFALSE)
            dummy.GetYaxis().SetTitle('Events')
            dummy.GetXaxis().SetLabelSize(0)
            dummy.GetXaxis().SetMoreLogLabels()
            dummy.GetXaxis().SetNoExponent()
            dummy.GetYaxis().SetTitleOffset(0.7)
            dummy.GetYaxis().SetTitleSize(0.08)
            dummy.GetYaxis().SetLabelSize(0.04/0.7)
            dummy.Draw()
            line_width=2
            h_data.SetMarkerStyle(8)
            h_data.SetLineColor(ROOT.kBlack)
            h_SM.SetLineWidth(line_width)
            h_BSM_Ctw.SetLineWidth(line_width)
            h_BSM_Ctg.SetLineWidth(line_width)
            h_BSM_Cphiq.SetLineWidth(line_width)
            h_SM.SetLineColor       (ROOT.TColor.GetColor("#ff0000"))
            h_BSM_Ctw.SetLineColor  (ROOT.TColor.GetColor("#0000ff"))
            h_BSM_Ctg.SetLineColor  (ROOT.TColor.GetColor("#008000"))
            #h_BSM_Cphiq.SetLineColor(ROOT.TColor.GetColor("#800080"))
            h_BSM_Cphiq.SetLineColor(ROOT.TColor.GetColor("#ffa500"))
            h_SM.Draw("same:hist")
            h_BSM_Ctw.Draw("same:hist")
            h_BSM_Ctg.Draw("same:hist")
            h_BSM_Cphiq.Draw("same:hist")
            h_data.Draw("same:pe")
            dummy.Draw("AXISSAME")
            legend = ROOT.TLegend(0.16,0.55,0.93,0.88)
            legend.SetBorderSize(0)
            #legend.SetNColumns(5)
            legend.AddEntry(h_data,'Data','pel')
            legend.AddEntry(h_SM,'SM','l')
            legend.AddEntry(h_BSM_Ctw  ,'BSM+SM:C_{tW}=%s'%(str(iCtw)),'l')
            legend.AddEntry(h_BSM_Ctg  ,'BSM+SM:C_{tg}=%s'%(str(iCtg)),'l')
            legend.AddEntry(h_BSM_Cphiq,'BSM+SM:C_{#phiq}=%s'%(str(iCphiq)),'l')
            legend.Draw()
            Label_cms_prelim = ROOT.TPaveText(0.6,0.83,0.9,0.83,"NDC")
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
            Label_lumi.AddText("%.1f fb^{-1} (13 TeV)"%(float(35867)/1000))
            Label_lumi.SetShadowColor(10)
            Label_lumi.Draw()

            pad2.cd()
            ratio_y_min=0.96
            ratio_y_max=1.12
            dummy_ratio = ROOT.TH2F("ratio_%s"%(dummy.GetName()),"",nbins,x_min,x_max,1,ratio_y_min,ratio_y_max)
            dummy_ratio.SetStats(ROOT.kFALSE)
            dummy_ratio.GetYaxis().SetTitle('(BSM+SM)/SM')
            dummy_ratio.GetYaxis().CenterTitle()
            dummy_ratio.GetXaxis().SetTitle("(nJets,nBtags)")
            dummy_ratio.GetXaxis().SetMoreLogLabels()
            dummy_ratio.GetXaxis().SetNoExponent()
            dummy_ratio.GetXaxis().SetTitleSize(0.04/0.3)
            dummy_ratio.GetYaxis().SetTitleSize(0.04/0.3)
            dummy_ratio.GetXaxis().SetTitleFont(42)
            dummy_ratio.GetYaxis().SetTitleFont(42)
            dummy_ratio.GetXaxis().SetTickLength(0.05)
            dummy_ratio.GetYaxis().SetTickLength(0.05)
            dummy_ratio.GetXaxis().SetLabelSize(0.04/0.3)
            dummy_ratio.GetYaxis().SetLabelSize(0.04/0.3)
            dummy_ratio.GetXaxis().SetLabelOffset(0.02)
            dummy_ratio.GetYaxis().SetLabelOffset(0.01)
            dummy_ratio.GetYaxis().SetTitleOffset(0.4)
            dummy_ratio.GetXaxis().SetTitleOffset(0.25/0.25)
            dummy_ratio.GetYaxis().SetNdivisions(504)
            
            Xaxis_label_emu=["e#mu(1,0)","e#mu(1,1)","e#mu(#geq2,1)","e#mu(#geq2,2)"]
            Xaxis_label_ee =["ee(1,1)","ee(#geq2,1)","ee(#geq2,2)"]
            Xaxis_label_mumu =["#mu#mu(1,1)","#mu#mu(#geq2,1)","#mu#mu(#geq2,2)"]
            Xaxis_label_emu.extend(Xaxis_label_ee)
            Xaxis_label_emu.extend(Xaxis_label_mumu)
            if nbins == len(Xaxis_label_emu):
                for ibin in range(1,nbins+1):
                    dummy_ratio.GetXaxis().SetBinLabel(ibin,Xaxis_label_emu[ibin-1])
            dummy_ratio.GetXaxis().CenterLabels()
            dummy_ratio.Draw()
            h_ratio_Ctw  =h_BSM_Ctw.Clone("ratio_%s"%(h_BSM_Ctw.GetName()))
            h_ratio_Ctg  =h_BSM_Ctg.Clone("ratio_%s"%(h_BSM_Ctg.GetName()))
            h_ratio_Cphiq=h_BSM_Cphiq.Clone("ratio_%s"%(h_BSM_Cphiq.GetName()))
            h_ratio_Ctw  .Divide(h_SM)
            h_ratio_Ctg  .Divide(h_SM)
            h_ratio_Cphiq.Divide(h_SM)
            h_ratio_Ctw  .Draw("same:hist")
            h_ratio_Ctg  .Draw("same:hist")
            h_ratio_Cphiq.Draw("same:hist")
            dummy_ratio.Draw("AXISSAME")
            canvas.Print('./Signal_plot/signal_Ctw%s_Ctg%s_Cphiq%s.png'%(str(iCtw),str(iCtg),str(iCphiq)))
            del canvas
            gc.collect() 

           
