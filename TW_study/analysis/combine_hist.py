
import ROOT
for sf in ["1.00", "0.05", "0.10", "0.15", "0.20", "0.25", "0.30","0.02","0.50", "1.50", "2.00", "2.50","3.00","4.00","5.00"]:
    for do_opposite in [True,False]:
        for choose_C in ["Ctg","Ctw","Cphiq"]:
            str_extra=""
            str_sf=str(sf)
            for_Ctg  =False
            for_Cphiq=False
            for_Ctw  =False
            no_signal=False
            if choose_C == "Ctg":for_Ctg=True
            elif choose_C == "Ctw":for_Ctw=True
            elif choose_C == "Cphiq":for_Cphiq=True
            else: print "wrong"
            if for_Cphiq:str_extra="_Cphiq"
            elif for_Ctw:str_extra="_Ctw"
            elif for_Ctg:str_extra="_Ctg"
            str_extra=str_extra+"_"+str_sf
            if no_signal:str_extra=str_extra+"_noSignal"
            if do_opposite:str_extra=str_extra+"_opposite"
            
            dir_out="./Limit_out/"
            F_ee  =ROOT.TFile(dir_out+"ee"+str_extra+".root","READ")
            F_emu =ROOT.TFile(dir_out+"emu"+str_extra+".root","READ")
            F_mumu=ROOT.TFile(dir_out+"mumu"+str_extra+".root","READ")
            F_out =ROOT.TFile(dir_out+"combined"+str_extra+".root","RECREATE")
            for ih in range(0,F_ee.GetListOfKeys().GetSize()):
                hname=F_ee.GetListOfKeys()[ih].GetName()
                nbin=F_ee.Get(hname).GetNbinsX()+F_emu.Get(hname).GetNbinsX()+F_mumu.Get(hname).GetNbinsX()
                if F_ee.Get(hname).GetNbinsX()!=3 or F_emu.Get(hname).GetNbinsX()!=4 or F_mumu.Get(hname).GetNbinsX()!=3:
                    print "wrong bin %s : ee %d, emu %d, mumu %d"%(hname,F_ee.Get(hname).GetNbinsX(),F_emu.Get(hname).GetNbinsX(),F_mumu.Get(hname).GetNbinsX())
                h_combine=ROOT.TH1D(hname,"",nbin,0,nbin)
                for ibin in range(1,nbin+1):
                    if ibin<=F_emu.Get(hname).GetNbinsX():
                        h_combine.SetBinContent(ibin,F_emu.Get(hname).GetBinContent(ibin))
                        h_combine.SetBinError  (ibin,F_emu.Get(hname).GetBinError  (ibin))
                    elif ibin<=(F_emu.Get(hname).GetNbinsX()+F_ee.Get(hname).GetNbinsX()):
                        h_combine.SetBinContent(ibin,F_ee.Get(hname).GetBinContent(ibin-F_emu.Get(hname).GetNbinsX()))
                        h_combine.SetBinError  (ibin,F_ee.Get(hname).GetBinError  (ibin-F_emu.Get(hname).GetNbinsX()))
                    elif ibin<=nbin:
                        h_combine.SetBinContent(ibin,F_mumu.Get(hname).GetBinContent(ibin-(F_emu.Get(hname).GetNbinsX()+F_ee.Get(hname).GetNbinsX())))
                        h_combine.SetBinError  (ibin,F_mumu.Get(hname).GetBinError  (ibin-(F_emu.Get(hname).GetNbinsX()+F_ee.Get(hname).GetNbinsX())))
                F_out.cd()
                h_combine.Write()
            F_out.Close()
            print "done! %s is saved"%(F_out.GetName()) 
