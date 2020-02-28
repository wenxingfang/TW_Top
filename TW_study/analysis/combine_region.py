import ROOT
ROOT.TH1.AddDirectory(ROOT.kFALSE)

def combine_files(files,output):
    f_out=ROOT.TFile(output,"RECREATE")
    N=0
    for ifile in files:
        N=N+files[ifile].Get("data_obs").GetNbinsX()
    h_out=ROOT.TH1D("out","",N,0,N)
    f_tmp=files.values()[0]
    hist_list=[]
    for ih in range(0,f_tmp.GetListOfKeys().GetSize()):
        hname=f_tmp.GetListOfKeys()[ih].GetName()
        hist_list.append(hname)
    for hname in hist_list:
        Nbin=0
        for ifile in files:
            h_tmp=files[ifile].Get(hname)
            for ibin in range(1,h_tmp.GetNbinsX()+1):
                Nbin=Nbin+1 
                h_out.SetBinContent(Nbin,h_tmp.GetBinContent(ibin))
                h_out.SetBinError  (Nbin,h_tmp.GetBinError  (ibin))
        if Nbin !=h_out.GetNbinsX():print "wrong, different bin!"
        f_out.cd()
        h_out.Write(hname)
    f_out.Close()
    for ifile in files:
        files[ifile].Close()
    print "%s is combined !"%(output)

channels=["ee","emu","mumu","combined"]
region_list_emu = ["0jet_0bjet","1jet_0bjet","1jet_1bjet","2jet_1bjet","2jet_2bjet"]
region_list_ee_mumu = ["1jet_1bjet","2jet_1bjet","2jet_2bjet"]

dir_in="./Limit_out/"
dir_out="./Final_Limit_out/"
noSignal=True
str_noSignal="_noSignal" if noSignal==True else ""
for sf in ["1.00", "0.05", "0.10", "0.15", "0.20", "0.25", "0.30","0.02","0.50"]:
    for do_opposite in [True,False]:
        for choose_C in ["Ctg","Ctw","Cphiq"]:
            for chan in channels:
                str_opp="" if do_opposite==False else "_opposite"
                dicti_file={}
                if chan == "combined":
                    for ir in region_list_emu:
                        name="emu_"+str(ir)+"_"+str(choose_C)+"_"+str(sf)+str_noSignal+str_opp
                        dicti_file[name]=ROOT.TFile(dir_in+name+".root","READ")   
                    for ir in region_list_ee_mumu:
                        name="ee_"+str(ir)+"_"+str(choose_C)+"_"+str(sf)+str_noSignal+str_opp
                        dicti_file[name]=ROOT.TFile(dir_in+name+".root","READ")   
                    for ir in region_list_ee_mumu:
                        name="mumu_"+str(ir)+"_"+str(choose_C)+"_"+str(sf)+str_noSignal+str_opp
                        dicti_file[name]=ROOT.TFile(dir_in+name+".root","READ")   
                elif chan == "emu": 
                    for ir in region_list_emu:
                        name="emu_"+str(ir)+"_"+str(choose_C)+"_"+str(sf)+str_noSignal+str_opp
                        dicti_file[name]=ROOT.TFile(dir_in+name+".root","READ")   
                elif chan == "ee": 
                    for ir in region_list_ee_mumu:
                        name="ee_"+str(ir)+"_"+str(choose_C)+"_"+str(sf)+str_noSignal+str_opp
                        dicti_file[name]=ROOT.TFile(dir_in+name+".root","READ")   
                elif chan == "mumu": 
                    for ir in region_list_ee_mumu:
                        name="mumu_"+str(ir)+"_"+str(choose_C)+"_"+str(sf)+str_noSignal+str_opp
                        dicti_file[name]=ROOT.TFile(dir_in+name+".root","READ")   
                out_name=str(chan)+"_"+str(choose_C)+"_"+str(sf)+str_noSignal+str_opp
                combine_files(dicti_file,dir_out+out_name+".root")

     
