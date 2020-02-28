import ROOT





#F_in=["Limit_hist_7TeV.root","Limit_hist_8TeV.root","Limit_hist_13TeV_100fb.root","Limit_hist_13TeV_300fb.root","Limit_hist_13TeV_3000fb.root"]
F_in=["Limit_hist_13TeV_300fb.root","Limit_hist_13TeV_3000fb.root"]

for str_f in F_in:
    f_tmp=ROOT.TFile(str_f,"UPDATE")
    h_data=f_tmp.Get("Vtb")
    h_scale=f_tmp.Get("data")
    #for str_toy in ["toy_up","toy_down"]:
    for str_toy in ["exp"]:
        h_data_tmp=h_data.Clone("data_%s"%str_toy)
        if str_toy == "toy_up":
            for ibin in range(1,h_data_tmp.GetNbinsX()+1):
                #h_data_tmp.SetBinContent(ibin,h_data_tmp.GetBinContent(ibin)+h_scale.GetBinError(ibin))
                h_data_tmp.SetBinError  (ibin,h_scale.GetBinError(ibin))
        elif str_toy == "toy_down":
            for ibin in range(1,h_data_tmp.GetNbinsX()+1):
                #h_data_tmp.SetBinContent(ibin,h_data_tmp.GetBinContent(ibin)-h_scale.GetBinError(ibin))
                h_data_tmp.SetBinError  (ibin,h_scale.GetBinError(ibin))
        elif str_toy == "exp":
            for ibin in range(1,h_data_tmp.GetNbinsX()+1):
                h_data_tmp.SetBinError  (ibin,h_scale.GetBinError(ibin))
        else:print "wrong name"
        f_tmp.cd() 
        h_data_tmp.Write("data_%s"%str_toy,ROOT.TObject.kOverwrite)
    f_tmp.Close()
print "make toy done"
