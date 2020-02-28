import ROOT
from make_script import channel,uncertainty

class mc_object:
    def __init__(self, name, event, crosssection, color):
        self.name = name
        self.event= event
        self.crosssection = crosssection
        self.lumi = float(self.event)/float(self.crosssection)
        self.color = color

MC_Sample={}
MC_Sample["TW_top"                ]=mc_object("TW_top"                ,8609398  ,19.47  ,ROOT.kOrange-3)
MC_Sample["TW_antitop"            ]=mc_object("TW_antitop"            ,8681265  ,19.47  ,ROOT.kOrange-3)
MC_Sample["TTTo2L2Nu"             ]=mc_object("TTTo2L2Nu"             ,64910035 ,87.31  ,ROOT.kRed-4)
MC_Sample["DYJetsToLL_M10to50_amc"]=mc_object("DYJetsToLL_M10to50_amc",29332494 ,18610  ,ROOT.kBlue-3)
MC_Sample["DYJetsToLL_M50_amc"    ]=mc_object("DYJetsToLL_M50_amc"    ,68009629 ,5765.4 ,ROOT.kBlue-3)
MC_Sample["TTWJetsToQQ"           ]=mc_object("TTWJetsToQQ"           ,72339    ,0.4062 ,ROOT.kGreen)
MC_Sample["TTWJetsToLNu"          ]=mc_object("TTWJetsToLNu"          ,1552336  ,0.2043 ,ROOT.kGreen)
MC_Sample["TTZToLLNuNu"           ]=mc_object("TTZToLLNuNu"           ,678038   ,0.2529 ,ROOT.kGreen)
MC_Sample["TTZToQQ"               ]=mc_object("TTZToQQ"               ,90425    ,0.5297 ,ROOT.kGreen)
MC_Sample["TTGJets"               ]=mc_object("TTGJets"               ,1771676  ,3.697  ,ROOT.kGreen)
MC_Sample["WJet_mad"              ]=mc_object("WJet_mad"              ,51285955 ,61526.7,ROOT.kGreen)
MC_Sample["WWTo2L2Nu"             ]=mc_object("WWTo2L2Nu"             ,1671947  ,12.178 ,ROOT.kGreen)
MC_Sample["WZ_3LNu"               ]=mc_object("WZ_3LNu"               ,1993154  ,4.42965,ROOT.kGreen)
MC_Sample["WZ_2L2Q"               ]=mc_object("WZ_2L2Q"               ,10254393 ,5.595  ,ROOT.kGreen)
MC_Sample["ZZ_2L2Nu"              ]=mc_object("ZZ_2L2Nu"              ,7819554  ,0.564  ,ROOT.kGreen)
MC_Sample["ZZ_4L"                 ]=mc_object("ZZ_4L"                 ,6544107  ,1.212  ,ROOT.kGreen)
MC_Sample["WG_LNuG"               ]=mc_object("WG_LNuG"               ,6304489  ,489    ,ROOT.kGreen)

Sys_MC_Sample={}
Sys_MC_Sample["TT_TuneCUETP8M2T4down"    ]=mc_object("TT_TuneCUETP8M2T4down"           ,27877257 ,831.76 ,ROOT.kRed-4)
Sys_MC_Sample["TT_TuneCUETP8M2T4up"      ]=mc_object("TT_TuneCUETP8M2T4up"             ,28701616 ,831.76 ,ROOT.kRed-4)
########### for color reconnection : envelope 
Sys_MC_Sample["TT_QCDbasedCRTune_erdON"  ]=mc_object("TT_QCDbasedCRTune_erdON"         ,28789634 ,831.76 ,ROOT.kRed-4)
Sys_MC_Sample["TT_GluonMoveCRTune"       ]=mc_object("TT_GluonMoveCRTune"              ,56456001 ,831.76 ,ROOT.kRed-4)
Sys_MC_Sample["TT_erdON"                 ]=mc_object("TT_erdON"                        ,28550174 ,831.76 ,ROOT.kRed-4)
#############################################
Sys_MC_Sample["TT_fsrdown"               ]=mc_object("TT_fsrdown"                      ,29156223 ,831.76 ,ROOT.kRed-4)
Sys_MC_Sample["TT_fsrup"                 ]=mc_object("TT_fsrup"                        ,29022611 ,831.76 ,ROOT.kRed-4)
Sys_MC_Sample["TT_hdampDOWN"             ]=mc_object("TT_hdampDOWN"                    ,28003470 ,831.76 ,ROOT.kRed-4)
Sys_MC_Sample["TT_hdampUP"               ]=mc_object("TT_hdampUP"                      ,29151802 ,831.76 ,ROOT.kRed-4)
Sys_MC_Sample["TT_isrdown"               ]=mc_object("TT_isrdown"                      ,28744718 ,831.76 ,ROOT.kRed-4)
Sys_MC_Sample["TT_isrup"                 ]=mc_object("TT_isrup"                        ,57577179 ,831.76 ,ROOT.kRed-4)
Sys_MC_Sample["TT_mtop1695"              ]=mc_object("TT_mtop1695"                     ,19295090 ,831.76 ,ROOT.kRed-4)
Sys_MC_Sample["TT_mtop1755"              ]=mc_object("TT_mtop1755"                     ,28979681 ,831.76 ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_DS_top"             ]=mc_object("ST_tW_DS_top"                    ,3192538 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_MEscaledown_top"    ]=mc_object("ST_tW_MEscaledown_top"           ,3051991 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_MEscaleup_top"      ]=mc_object("ST_tW_MEscaleup_top"             ,3188665 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_PSscaledown_top"    ]=mc_object("ST_tW_PSscaledown_top"           ,3181559 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_PSscaleup_top"      ]=mc_object("ST_tW_PSscaleup_top"             ,3124846 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_fsrdown_top"        ]=mc_object("ST_tW_fsrdown_top"               ,2935595 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_fsrup_top"          ]=mc_object("ST_tW_fsrup_top"                 ,3192325 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_herwigpp_top"       ]=mc_object("ST_tW_herwigpp_top"              ,3200997 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_isrdown_top"        ]=mc_object("ST_tW_isrdown_top"               ,3181500 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_isrup_top"          ]=mc_object("ST_tW_isrup_top"                 ,3110339 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_mtop1695_top"       ]=mc_object("ST_tW_mtop1695_top"              ,3178900 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_mtop1755_top"       ]=mc_object("ST_tW_mtop1755_top"              ,2938402 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_DS_antitop"         ]=mc_object("ST_tW_DS_antitop"                ,3098002 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_MEscaledown_antitop"]=mc_object("ST_tW_MEscaledown_antitop"       ,1575142 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_MEscaleup_antitop"  ]=mc_object("ST_tW_MEscaleup_antitop"         ,1606961 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_PSscaledown_antitop"]=mc_object("ST_tW_PSscaledown_antitop"       ,1568912 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_PSscaleup_antitop"  ]=mc_object("ST_tW_PSscaleup_antitop"         ,1608419 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_fsrdown_antitop"    ]=mc_object("ST_tW_fsrdown_antitop"           ,3234964 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_fsrup_antitop"      ]=mc_object("ST_tW_fsrup_antitop"             ,3001527 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_isrdown_antitop"    ]=mc_object("ST_tW_isrdown_antitop"           ,3101321 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_isrup_antitop"      ]=mc_object("ST_tW_isrup_antitop"             ,3076275 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_mtop1695_antitop"   ]=mc_object("ST_tW_mtop1695_antitop"          ,2968744 ,19.47   ,ROOT.kRed-4)
Sys_MC_Sample["ST_tW_mtop1755_antitop"   ]=mc_object("ST_tW_mtop1755_antitop"          ,3194626 ,19.47   ,ROOT.kRed-4)



Lumi=35867

input_path  ="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/ntuples/saved_hist/Step2_sys_MVA_0616_SameSign/"
output_path ="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/ee_channel/ntuples/saved_hist/Step2_sys_MVA_QCD_0616/"
ROOT.TH1.AddDirectory(ROOT.kFALSE)
hist_list=[]

f_nominal_ee=ROOT.TFile(input_path+"ee_nominal_.root","read")
for ih in range(0,f_nominal_ee.GetListOfKeys().GetSize()):
    hname=f_nominal_ee.GetListOfKeys()[ih].GetName()
    h_tmp=f_nominal_ee.Get(hname)
    if type(h_tmp)==ROOT.TH2D:continue
    if "__" not in hname:continue
    if "data" not in hname:continue
    hist_name=hname.split("__")[-1]
    hist_list.append(hist_name)
f_nominal_ee.Close()
#print hist_list
for nhist in hist_list:
    print nhist
    for chan in channel:
        f_nominal=ROOT.TFile(input_path+chan+"_nominal_.root","read")
        h_data=f_nominal.Get("nominal__data__"+nhist).Clone(chan+"_nominal__data__"+nhist)
        for uncert in uncertainty:
            h_ss  =h_data.Clone(chan+"_"+uncert+"__ss__"+nhist)
            h_ss.Scale(0)
            h_ss.Add(h_data,-1)
            f_in=ROOT.TFile(input_path+chan+"_"+uncert+"_.root","read")
            for ih in range(0,f_in.GetListOfKeys().GetSize()):
                hname=f_in.GetListOfKeys()[ih].GetName()
                #print hname.split("__")
                if "__" not in hname:continue
                hist_name=hname.split("__")[-1]
                sname    =hname.split("__")[1]
                if hist_name != nhist:continue
                if sname == "data" or sname == "WJet_mad":continue
                h_tmp=f_in.Get(hname)
                scale=float(Lumi)/float(MC_Sample[sname].lumi)
                if "TT_" in uncert and sname == "TTTo2L2Nu":
                    scale=float(Lumi)/float(Sys_MC_Sample[uncert].lumi)
                if "ST_" in uncert and "TW_" in sname:
                    scale=float(Lumi)/float(Sys_MC_Sample[uncert+"_"+sname.split("TW_")[-1]].lumi)
                h_tmp.Scale(scale)
                h_ss.Add(h_tmp)
            for ibin in range(1,h_ss.GetNbinsX()+1):
                h_ss.SetBinError(ibin,0)
                if h_ss.GetBinContent(ibin)<0:h_ss.SetBinContent(ibin,0)
            f_out=ROOT.TFile(output_path+chan+"_"+uncert+"_.root","update")
            f_out.cd()
            h_ss.Write(uncert+"__WJet_mad__"+nhist,ROOT.TObject.kOverwrite)    
            f_out.Close()
            f_in.Close()
        f_nominal.Close()
print "replaced wjet with same sign !"
