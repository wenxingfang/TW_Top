import ROOT

def cout_combine():
    for sf in ["1.00", "0.05", "0.10", "0.15", "0.20", "0.25", "0.30","0.02","0.50"]:
        for do_opposite in [True,False]:
            for choose_C in ["Ctg","Ctw","Cphiq"]:
                str_extra=""
                str_sf=str(sf)
                for_Ctg  =False
                for_Cphiq=False
                for_Ctw  =False
                no_signal=True
                if choose_C == "Ctg":for_Ctg=True
                elif choose_C == "Ctw":for_Ctw=True
                elif choose_C == "Cphiq":for_Cphiq=True
                else: print "wrong"
                if   for_Cphiq:str_extra="_Cphiq"
                elif for_Ctw:str_extra="_Ctw"
                elif for_Ctg:str_extra="_Ctg"
                str_extra=str_extra+"_"+str_sf
                if no_signal:str_extra=str_extra+"_noSignal"
                if do_opposite:str_extra=str_extra+"_opposite"
                dir_out="./Final_Limit_out/"
                channel=["ee","emu","mumu","combined"]
                sample=["data_obs","Signal","Signalonly","TT","TTNNLO","TW","TWNLO","DY","other","jets"]
                for ch in channel:
                    f_in=ROOT.TFile(dir_out+ch+str_extra+".root","READ")
                    for sname in sample:
                        if f_in.Get(sname):
                            print "%s:%.4f"%(ch+str_extra+"_"+sname,f_in.Get(sname).GetSumOfWeights())
                    f_in.Close()
    print "done!"

def cout_separate():
    for sf in ["1.00", "0.05", "0.10", "0.15", "0.20", "0.25", "0.30","0.02","0.50"]:
        for do_opposite in [True,False]:
            #for choose_C in ["Ctg","Ctw","Cphiq"]:
            for choose_C in ["Ctg","Ctw","Cphiq","Cg"]:
                for region in ["0jet_0bjet","1jet_0bjet","1jet_1bjet","2jet_1bjet","2jet_2bjet"]:
                    str_extra="_"+str(region)
                    str_sf=str(sf)
                    no_signal=False######################### change here , True for tw, False for EFT
                    str_extra=str_extra+"_"+str(choose_C)
                    str_extra=str_extra+"_"+str_sf
                    if no_signal:str_extra=str_extra+"_noSignal"
                    if do_opposite:str_extra=str_extra+"_opposite"
                    dir_out="./Limit_out/"
                    channel=["ee","emu","mumu"]
                    #channel=["emu"]
                    sample=["data_obs","TTSignal","TTSignalonly","TWSignal","TWSignalonly","TT","TTNNLO","TW","TWNLO","DY","other","jets"]
                    for ch in channel:
                        f_in=ROOT.TFile(dir_out+ch+str_extra+".root","READ")
                        for sname in sample:
                            if f_in.Get(sname):
                                print "%s:%.4f"%(ch+str_extra+"_"+sname,f_in.Get(sname).GetSumOfWeights())
                        f_in.Close()
    print "done!"


def cout_FCNC():
    #for region in ["0jet_0bjet","1jet_0bjet","1jet_1bjet","2jet_1bjet","2jet_2bjet"]:
    for region in ["xjet_1bjet"]:
        for sf in ["1.00", "0.05", "0.10", "0.15", "0.20", "0.25", "0.30","0.02","0.50"]:
            str_extra="_"+str(region)+"_FCNC"+"_"+str(sf)
            dir_out="./Limit_out/"
            channel=["ee","emu","mumu"]
            sample=["data_obs","TTSignal","TTSignalonly","TWSignal","TWSignalonly","TT","TTNNLO","TW","TWNLO","DY","other","jets","FCNCSignal"]
            for ch in channel:
                f_in=ROOT.TFile(dir_out+ch+str_extra+".root","READ")
                for sname in sample:
                    if f_in.Get(sname):
                        print "%s:%.4f"%(ch+str_extra+"_"+sname,f_in.Get(sname).GetSumOfWeights())
                f_in.Close()
    print "done!"



#cout_separate()
cout_FCNC()
