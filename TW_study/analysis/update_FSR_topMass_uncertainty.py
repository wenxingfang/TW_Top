import ROOT
import os
import numpy
import math
ROOT.TH1.AddDirectory(ROOT.kFALSE)


cat={}
#cat["ST_tW_mtop1755"]           =["TW_antitop","TW_top"  ]##
#cat["ST_tW_mtop1695"]           =["TW_antitop","TW_top"  ]##
#cat["ST_tW_fsrdown" ]           =["TW_antitop","TW_top"  ]##
#cat["ST_tW_fsrup"   ]           =["TW_antitop","TW_top"  ]##
cat["TT_fsrdown"    ]           =["TTTo2L2Nu"            ]##
cat["TT_fsrup"      ]           =["TTTo2L2Nu"            ]##
cat["TT_mtop1695"   ]           =["TTTo2L2Nu"            ]##
cat["TT_mtop1755"   ]           =["TTTo2L2Nu"            ]##

Dir   ="./ntuples/saved_hist/Step2_20180623_top_pt_reweight/"
##Dir_SS="./ntuples/saved_hist/Step2_SameSign_1013_xjet_1bjet/"## not used

sample_event={}
sample_event["nominal__TW_top"    ]        =8609398/19.47
sample_event["nominal__TW_antitop"]        =8681265/19.47
sample_event["nominal__TTTo2L2Nu" ]        =64910035/87.31
sample_event["ST_tW_mtop1755__TW_antitop" ]=3194626/19.47
sample_event["ST_tW_mtop1695__TW_antitop" ]=2968744/19.47
sample_event["ST_tW_fsrdown__TW_antitop"  ]=3234964/19.47
sample_event["ST_tW_fsrup__TW_antitop"    ]=3001527/19.47
sample_event["ST_tW_mtop1755__TW_top"     ]=2938402/19.47
sample_event["ST_tW_mtop1695__TW_top"     ]=3178900/19.47
sample_event["ST_tW_fsrdown__TW_top"      ]=2935595/19.47
sample_event["ST_tW_fsrup__TW_top"        ]=3192325/19.47
sample_event["TT_mtop1695__TTTo2L2Nu"     ]=58281931/831.76
sample_event["TT_mtop1755__TTTo2L2Nu"     ]=38909457/831.76
sample_event["TT_fsrdown__TTTo2L2Nu"      ]=57563666/831.76
sample_event["TT_fsrup__TTTo2L2Nu"        ]=58475264/831.76

f_nominal=ROOT.TFile(Dir+"emu_nominal_.root","read")

for idir in [Dir]:
#for idir in [Dir,Dir_SS]:
    for chan in ["ee","emu","mumu"]:
    #for chan in ["emu"]:
        f_nominal=ROOT.TFile(Dir+"%s_nominal_.root"%(chan),"read")
        for icat in cat:
            f_sys=ROOT.TFile(Dir+"%s_%s_.root"%(chan,icat),"update")
            scale=1
            if "fsr" in icat:
                scale=1/math.sqrt(2.0)
                #print "for %s"%(icat)
            elif "mtop" in icat:
                scale=1.0/6.0##very import to be float
                #print "for %s"%(icat)
            for ihist in cat[icat]:
                for ih in range(0,f_nominal.GetListOfKeys().GetSize()):
                    hname=f_nominal.GetListOfKeys()[ih].GetName()
                    if str("_"+ihist+"_") in hname and type(f_nominal.Get(hname)) == ROOT.TH1D:
                        h_nominal=f_nominal.Get(hname)
                        h_nominal.Scale(float(sample_event[icat+"__"+ihist])/float(sample_event["nominal__"+ihist]))
                        #print "%s,event:%f"%(h_nominal.GetName(),h_nominal.GetSumOfWeights())
                        h_sys=f_sys.Get(hname.replace("nominal",icat))
                        #print "%s,event:%f"%(h_sys.GetName(),h_sys.GetSumOfWeights())
                        h_sys.Add(h_nominal,-1)
                        h_sys.Scale(scale)
                        #print "scaled event:%f"%(h_sys.GetSumOfWeights())
                        h_nominal.Add(h_sys)
                        f_sys.cd()
                        #print "write %s,event:%f"%(hname.replace("nominal",icat),h_nominal.GetSumOfWeights())
                        h_nominal.Write(hname.replace("nominal",icat),ROOT.TObject.kOverwrite) 
            f_sys.Close()
            print "%s %s updated %s "%(idir,chan,icat)
        f_nominal.Close()
