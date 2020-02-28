import os
import math


def get_uncert(coupling):
    best_value=0
    uncert={}
    real_effect={}
    for ifile in os.listdir(path):
        if ".txt" not in ifile or coupling not in ifile:continue
        #if ".txt" not in ifile :continue
        name1=ifile.split(".txt")[0]
        name = name1.split("%s_"%coupling)[-1]
        print name
        v_uncert=0
        fname=path+ifile
        f_in=open(fname,"r")
        lines=f_in.readlines()
        if Method=="MaxLikelihoodFit":
            for line in lines:
                if "Best fit r:" in line:
                    #print line
                    b1=line.split(":")[-1]
                    b2=b1.split("  ")[0]
                    #print b2
                    best_value=float(b2)
                    tmp=line.split("(68% CL)")[0]
                    tmp1=tmp.split("-")[-1]
                    down=tmp1.split("/")[0]
                    up1 =tmp1.split("/")[-1]
                    up  =up1.split("+")[-1] 
                    #if float(up)>float(down):v_uncert=float(up)
                    #else                    :v_uncert=float(down)
                    v_uncert=(float(up)+float(down))/2
                    #if float(up)>0.5: 
                    #    v_uncert=float(down)
                    #if float(down)>0.5: 
                    #    v_uncert=float(up)
        elif Method=="MultiDimFit":
            for line in lines:
                if "RooRealVar::r" in line:
                    b1=line.split("=")[-1]
                    b2=b1.split("+/-")[0]
                    best_value=float(b2)
                    tmp=line.split("+/-")[-1]
                    tmp1=tmp.split("L")[0]
                    v_uncert=float(tmp1)
        uncert[name]=v_uncert
    best_value = abs(best_value)
    if "Total" in uncert:
        if False: ############## uncertainty for tw measurement#######################
            for iu in uncert:
                if iu == "Total":
                    real_effect[iu]=100*uncert[iu]/best_value
                elif iu == "Remove_all":##data statistic
                    real_effect[iu]=100*uncert[iu]/best_value
                else:
                    if uncert[iu]>uncert["Total"]:
                        print "%s:total=%f,it=%f"%(iu,uncert["Total"],uncert[iu])
                        real_effect[iu]=0
                    else:
                        real_effect[iu]=100*math.sqrt(math.pow(uncert["Total"],2)-math.pow(uncert[iu],2))/best_value
        if True: ############## uncertainty for coupling   pow(U_i,2)/sum(pow(U_i,2))=pow(U_i,2)/pow(U_tot,2)#######################
            for iu in uncert:
                if iu == "Total":
                    real_effect[iu]=100
                elif iu == "Remove_all":##data statistic
                    real_effect[iu]=100*math.pow(uncert[iu],2)/math.pow(uncert['Total'],2)
                else:
                    if uncert[iu]>uncert["Total"]:
                        print "%s:total=%f,it=%f"%(iu,uncert["Total"],uncert[iu])
                        real_effect[iu]=0
                        continue
                    real_effect[iu]=100*(math.pow(uncert["Total"],2)-math.pow(uncert[iu],2))/math.pow(uncert['Total'],2)
    else:
        print "missing Total"
        exit()

    return real_effect
        

Method="MaxLikelihoodFit"
#Method="MultiDimFit"
path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/output/"
dict_uncert_tot={}
dict_uncert={}
dict_uncert['Cg']   =get_uncert('Cg')
dict_uncert['Cphiq']=get_uncert('Cphiq')
dict_uncert['Ctw']  =get_uncert('Ctw')
dict_uncert['Ctg']  =get_uncert('Ctg')
dict_uncert['Cug']  =get_uncert('Cug')
dict_uncert['Ccg']  =get_uncert('Ccg')
for ic in dict_uncert:
    for iu in dict_uncert[ic]:
        dict_uncert_tot["%s_%s"%(ic,iu)]=dict_uncert[ic][iu]
print dict_uncert_tot
#la_head='''
#\\begin{table}[]
#\centering
#\caption{My caption}
#\label{my-label}
#\\begin{tabular}{|c|c|}
#\hline
#Source & Uncertainty \\\ \hline \hline
#'''
#print la_head
#for ie in real_effect:
#    print "%s & %.3f\\%% \\\\ \hline "%(ie,real_effect[ie])
#
#la_end='''
#\end{tabular}
#\end{table}
#'''
#print la_end


template='''
Ucertainty         & Cg     & Cphiq     & Ctw      & Ctg      & Cug     & Ccg                         \hline
Trigger            & %(Cg_Trigger)-8.3f& %(Cphiq_Trigger)-8.3f& %(Ctw_Trigger)-8.3f& %(Ctg_Trigger)-8.3f& %(Cug_Trigger)-8.3f& %(Ccg_Trigger)-8.3f\hline
PileUp             & %(Cg_PileUp)-8.3f& %(Cphiq_PileUp)-8.3f& %(Ctw_PileUp)-8.3f& %(Ctg_PileUp)-8.3f& %(Cug_PileUp)-8.3f& %(Ccg_PileUp)-8.3f\hline
UnclusteredEn      & %(Cg_UnclusteredEn)-8.3f& %(Cphiq_UnclusteredEn)-8.3f& %(Ctw_UnclusteredEn)-8.3f& %(Ctg_UnclusteredEn)-8.3f& %(Cug_UnclusteredEn)-8.3f& %(Ccg_UnclusteredEn)-8.3f\hline
Btag               & %(Cg_Btag)-8.3f& %(Cphiq_Btag)-8.3f& %(Ctw_Btag)-8.3f& %(Ctg_Btag)-8.3f& %(Cug_Btag)-8.3f& %(Ccg_Btag)-8.3f\hline
Missingtag         & %(Cg_Missingtag)-8.3f& %(Cphiq_Missingtag)-8.3f& %(Ctw_Missingtag)-8.3f& %(Ctg_Missingtag)-8.3f& %(Cug_Missingtag)-8.3f& %(Ccg_Missingtag)-8.3f\hline
JER                & %(Cg_JER)-8.3f& %(Cphiq_JER)-8.3f& %(Ctw_JER)-8.3f& %(Ctg_JER)-8.3f& %(Cug_JER)-8.3f& %(Ccg_JER)-8.3f\hline
JES                & %(Cg_JES)-8.3f& %(Cphiq_JES)-8.3f& %(Ctw_JES)-8.3f& %(Ctg_JES)-8.3f& %(Cug_JES)-8.3f& %(Ccg_JES)-8.3f\hline
ElectronIDIso      & %(Cg_ElectronIDIso)-8.3f& %(Cphiq_ElectronIDIso)-8.3f& %(Ctw_ElectronIDIso)-8.3f& %(Ctg_ElectronIDIso)-8.3f& %(Cug_ElectronIDIso)-8.3f& %(Ccg_ElectronIDIso)-8.3f\hline
ElectronReco       & %(Cg_ElectronReco)-8.3f& %(Cphiq_ElectronReco)-8.3f& %(Ctw_ElectronReco)-8.3f& %(Ctg_ElectronReco)-8.3f& %(Cug_ElectronReco)-8.3f& %(Ccg_ElectronReco)-8.3f\hline
MuonID             & %(Cg_MuonID)-8.3f& %(Cphiq_MuonID)-8.3f& %(Ctw_MuonID)-8.3f& %(Ctg_MuonID)-8.3f& %(Cug_MuonID)-8.3f& %(Ccg_MuonID)-8.3f\hline
MuonIso            & %(Cg_MuonIso)-8.3f& %(Cphiq_MuonIso)-8.3f& %(Ctw_MuonIso)-8.3f& %(Ctg_MuonIso)-8.3f& %(Cug_MuonIso)-8.3f& %(Ccg_MuonIso)-8.3f\hline
MuonTrack          & %(Cg_MuonTrack)-8.3f& %(Cphiq_MuonTrack)-8.3f& %(Ctw_MuonTrack)-8.3f& %(Ctg_MuonTrack)-8.3f& %(Cug_MuonTrack)-8.3f& %(Ccg_MuonTrack)-8.3f\hline
FSR                & %(Cg_FSR)-8.3f& %(Cphiq_FSR)-8.3f& %(Ctw_FSR)-8.3f& %(Ctg_FSR)-8.3f& %(Cug_FSR)-8.3f& %(Ccg_FSR)-8.3f\hline
ISR                & %(Cg_ISR)-8.3f& %(Cphiq_ISR)-8.3f& %(Ctw_ISR)-8.3f& %(Ctg_ISR)-8.3f& %(Cug_ISR)-8.3f& %(Ccg_ISR)-8.3f\hline
TT_CR              & %(Cg_TT_CR)-8.3f& %(Cphiq_TT_CR)-8.3f& %(Ctw_TT_CR)-8.3f& %(Ctg_TT_CR)-8.3f& %(Cug_TT_CR)-8.3f& %(Ccg_TT_CR)-8.3f\hline
TT_PDF             & %(Cg_TT_PDF)-8.3f& %(Cphiq_TT_PDF)-8.3f& %(Ctw_TT_PDF)-8.3f& %(Ctg_TT_PDF)-8.3f& %(Cug_TT_PDF)-8.3f& %(Ccg_TT_PDF)-8.3f\hline
TT_QCD             & %(Cg_TT_QCD)-8.3f& %(Cphiq_TT_QCD)-8.3f& %(Ctw_TT_QCD)-8.3f& %(Ctg_TT_QCD)-8.3f& %(Cug_TT_QCD)-8.3f& %(Ccg_TT_QCD)-8.3f\hline
TT_Tune            & %(Cg_TT_Tune)-8.3f& %(Cphiq_TT_Tune)-8.3f& %(Ctw_TT_Tune)-8.3f& %(Ctg_TT_Tune)-8.3f& %(Cug_TT_Tune)-8.3f& %(Ccg_TT_Tune)-8.3f\hline
TT_hdamp           & %(Cg_TT_hdamp)-8.3f& %(Cphiq_TT_hdamp)-8.3f& %(Ctw_TT_hdamp)-8.3f& %(Ctg_TT_hdamp)-8.3f& %(Cug_TT_hdamp)-8.3f& %(Ccg_TT_hdamp)-8.3f\hline
TT_mtop            & %(Cg_TT_mtop)-8.3f& %(Cphiq_TT_mtop)-8.3f& %(Ctw_TT_mtop)-8.3f& %(Ctg_TT_mtop)-8.3f& %(Cug_TT_mtop)-8.3f& %(Ccg_TT_mtop)-8.3f\hline
TW_DS              & %(Cg_TW_DS)-8.3f& %(Cphiq_TW_DS)-8.3f& %(Ctw_TW_DS)-8.3f& %(Ctg_TW_DS)-8.3f& %(Cug_TW_DS)-8.3f& %(Ccg_TW_DS)-8.3f\hline
TW_ME              & %(Cg_TW_ME)-8.3f& %(Cphiq_TW_ME)-8.3f& %(Ctw_TW_ME)-8.3f& %(Ctg_TW_ME)-8.3f& %(Cug_TW_ME)-8.3f& %(Ccg_TW_ME)-8.3f\hline
TW_mtop            & %(Cg_TW_mtop)-8.3f& %(Cphiq_TW_mtop)-8.3f& %(Ctw_TW_mtop)-8.3f& %(Ctg_TW_mtop)-8.3f& %(Cug_TW_mtop)-8.3f& %(Ccg_TW_mtop)-8.3f\hline
DY_PDF             & %(Cg_DY_PDF)-8.3f& %(Cphiq_DY_PDF)-8.3f& %(Ctw_DY_PDF)-8.3f& %(Ctg_DY_PDF)-8.3f& %(Cug_DY_PDF)-8.3f& %(Ccg_DY_PDF)-8.3f\hline
DY_QCD             & %(Cg_DY_QCD)-8.3f& %(Cphiq_DY_QCD)-8.3f& %(Ctw_DY_QCD)-8.3f& %(Ctg_DY_QCD)-8.3f& %(Cug_DY_QCD)-8.3f& %(Ccg_DY_QCD)-8.3f\hline
TW_normalisation   & %(Cg_TW_normalisation)-8.3f& %(Cphiq_TW_normalisation)-8.3f& %(Ctw_TW_normalisation)-8.3f& %(Ctg_TW_normalisation)-8.3f& %(Cug_TW_normalisation)-8.3f& %(Ccg_TW_normalisation)-8.3f\hline
TT_normalisation   & %(Cg_TT_normalisation)-8.3f& %(Cphiq_TT_normalisation)-8.3f& %(Ctw_TT_normalisation)-8.3f& %(Ctg_TT_normalisation)-8.3f& %(Cug_TT_normalisation)-8.3f& %(Ccg_TT_normalisation)-8.3f\hline
DY_normalisation   & %(Cg_DY_normalisation)-8.3f& %(Cphiq_DY_normalisation)-8.3f& %(Ctw_DY_normalisation)-8.3f& %(Ctg_DY_normalisation)-8.3f& %(Cug_DY_normalisation)-8.3f& %(Ccg_DY_normalisation)-8.3f\hline
Other_normalisation& %(Cg_Other_normalisation)-8.3f& %(Cphiq_Other_normalisation)-8.3f& %(Ctw_Other_normalisation)-8.3f& %(Ctg_Other_normalisation)-8.3f& %(Cug_Other_normalisation)-8.3f& %(Ccg_Other_normalisation)-8.3f\hline
Jets_normalisation & %(Cg_Jets_normalisation)-8.3f& %(Cphiq_Jets_normalisation)-8.3f& %(Ctw_Jets_normalisation)-8.3f& %(Ctg_Jets_normalisation)-8.3f& %(Cug_Jets_normalisation)-8.3f& %(Ccg_Jets_normalisation)-8.3f\hline
Luminosity         & %(Cg_Luminosity)-8.3f& %(Cphiq_Luminosity)-8.3f& %(Ctw_Luminosity)-8.3f& %(Ctg_Luminosity)-8.3f& %(Cug_Luminosity)-8.3f& %(Ccg_Luminosity)-8.3f\hline
MC_stat            & %(Cg_MC_stat)-8.3f& %(Cphiq_MC_stat)-8.3f& %(Ctw_MC_stat)-8.3f& %(Ctg_MC_stat)-8.3f& %(Cug_MC_stat)-8.3f& %(Ccg_MC_stat)-8.3f\hline
Remove_all         & %(Cg_Remove_all)-8.3f& %(Cphiq_Remove_all)-8.3f& %(Ctw_Remove_all)-8.3f& %(Ctg_Remove_all)-8.3f& %(Cug_Remove_all)-8.3f& %(Ccg_Remove_all)-8.3f\hline
Total              & %(Cg_Total)-8.3f& %(Cphiq_Total)-8.3f& %(Ctw_Total)-8.3f& %(Ctg_Total)-8.3f& %(Cug_Total)-8.3f& %(Ccg_Total)-8.3f\hline
'''
print template%dict_uncert_tot
