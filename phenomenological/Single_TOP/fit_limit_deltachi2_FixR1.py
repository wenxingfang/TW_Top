######### Note #################
# This is used for fix R study, the only difference is in vtb,vts,vtd loop squence and the output file name #
################################
import ROOT
import math
from array import array
import gc
import numpy as np
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gSystem.Load("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/mod_limit_C.so")

#ROOT.RooAbsReal.defaultIntegratorConfig().Print("v")
ROOT.RooAbsReal.defaultIntegratorConfig().setEpsAbs(1e-10) 
ROOT.RooAbsReal.defaultIntegratorConfig().setEpsRel(1e-10) 

from optparse import OptionParser
parser=OptionParser()

parser.add_option("-m","--method",dest="str_method",default="chi2",type="str")
parser.add_option("-e","--exp",dest="str_type",default="obs",type="str")
parser.add_option("-c","--cat",dest="str_cat",default="",type="str")
parser.add_option("-L","--lumi",dest="str_lumi",default="",type="str")
parser.add_option("-i","--indiv",dest="str_indiv",default="",type="str")
parser.add_option("-M", action="store_true", dest="bool_marg",default=False)
parser.add_option("-R", "--Fixed_R", dest="Fixed_R",default=-1,type=float)
(options,args)=parser.parse_args()

print "method:%s"%(options.str_method)
print "type:%s"  %(options.str_type  )
print "cat:%s"   %(options.str_cat   )
print "lumi:%s"   %(options.str_lumi )
print "indiv:%s" %(options.str_indiv )
print "margin:%s"%(options.bool_marg )
str_method=options.str_method
str_type=options.str_type
str_cat=options.str_cat
str_lumi=options.str_lumi
str_indiv=options.str_indiv
marginlized=options.bool_marg
Fixed_R = options.Fixed_R
do_Fix_R = False if Fixed_R==-1 else True
print "do_Fix_R: %d, Fixed_R:%f" %(int(do_Fix_R), Fixed_R)
data_hist_name=""
if options.str_type == "exp":
    data_hist_name="_exp"

class cat_object:
    def __init__(self, name, min_chi2, bin_min, bin_max, ndof, Vtb_low,Vtb_up,Vtb_bin,Vts_low,Vts_up,Vts_bin,Vtd_low,Vtd_up,Vtd_bin):
        self.name   =name
        self.min_chi2 = min_chi2
        self.ndof   =ndof   
        self.bin_min=bin_min
        self.bin_max=bin_max
        self.Vtb_low=Vtb_low
        self.Vtb_up =Vtb_up 
        self.Vtb_bin=Vtb_bin
        self.Vts_low=Vts_low
        self.Vts_up =Vts_up 
        self.Vts_bin=Vts_bin
        self.Vtd_low=Vtd_low
        self.Vtd_up =Vtd_up 
        self.Vtd_bin=Vtd_bin

def plot_dicti(Dict,out_name):
    x=[]
    y=[]
    for i in Dict:
        x.append(float(i))
        y.append(float(Dict[i]))
    gr_tmp=ROOT.TGraph(len(x),np.array(x),np.array(y))
    tmp_dir="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/limit_out/"
    f_tmp=ROOT.TFile("%smarg_probe.root"%(tmp_dir),"UPDATE")
    f_tmp.cd()
    gr_tmp.Write(out_name,ROOT.TObject.kOverwrite)
    f_tmp.Close()
 

def margin_value(Dict1,name,sigma):## from best fit to get interval
    Dict={}
    for key in Dict1:
        if key >=0: Dict[key]=Dict1[key]
     
    sum_value=sum(Dict.values())
    sort_key=sorted(Dict.keys())
    limit=float(sum_value*sigma)
    max_value=0
    max_key=0
    for key in Dict:
        if Dict[key]>max_value:
            max_value=Dict[key]
            max_key  =key
   
    max_index=sort_key.index(max_key)
    lim=[max_key,-999,-999]
    if name=="Vtd" or name=="Vts":
        lim[1]=0
        tmp=0
        for key in sort_key:
            tmp=tmp+Dict[key]
            if tmp>limit:
                lim[2]=(key+sort_key[sort_key.index(key)-1])/2
                return lim
    else:
        tmp=0
        for i in range(max_index,len(sort_key)):
            tmp=tmp+Dict[sort_key[i]]
            if tmp>(limit/2):
                lim[2]=(sort_key[i]+sort_key[i-1])/2
                break   
        tmp=0
        for i in range(max_index-1,-1,-1):
            tmp=tmp+Dict[sort_key[i]]
            if tmp>(limit/2):
                lim[1]=(sort_key[i]+sort_key[i+1])/2
                break   
        return lim

def margin_value_v1(Dict1,name,sigma):## from low or up to get interval
    Dict={}
    for key in Dict1:
        if key >=0: Dict[key]=Dict1[key]
     
    sum_value=sum(Dict.values())
    sort_key=sorted(Dict.keys())
    limit=float(sum_value*(1-sigma))
    max_value=0
    max_key=0
    for key in Dict:
        if Dict[key]>max_value:
            max_value=Dict[key]
            max_key  =key
   
    lim=[max_key,-999,-999]
    if name=="Vtd" or name=="Vts":
        lim[1]=0
        tmp=0
        for i in range(len(sort_key)-1,-1,-1):
            tmp=tmp+Dict[sort_key[i]]
            if tmp>limit:
                lim[2]=(sort_key[i]+sort_key[i+1])/2
                if i==(len(sort_key)-1):print "last bin over up limit"
                return lim
    else:
        tmp=0
        for i in range(len(sort_key)-1,-1,-1):
            tmp=tmp+Dict[sort_key[i]]
            if tmp>(limit/2):
                lim[2]=(sort_key[i]+sort_key[i+1])/2
                if i==(len(sort_key)-1):print "last bin over up limit"
                break   
        tmp=0
        for i in range(0,len(sort_key)):
            tmp=tmp+Dict[sort_key[i]]
            if tmp>(limit/2):
                lim[1]=(sort_key[i]+sort_key[i-1])/2
                if i==0:print "fisrt bin over low limit"
                break   
        return lim

def SigmaBand(result_list, vtx):
    x=0
    y=0
    if vtx=="VtbVts":
        x=0
        y=1
    elif vtx=="VtbVtd":
        x=0
        y=2
    elif vtx=="VtsVtd":
        x=1
        y=2
    else:
        print "wrong vtx"
    dicti={}
    for ilist in result_list:
        tmp_x=float(ilist[x])
        tmp_y=float(ilist[y])
        if tmp_x not in dicti:
            dicti[tmp_x]=[]
        dicti[tmp_x].append(tmp_y)
    list_x=[]
    list_y_up=[]
    list_y_down=[]
    for ix in sorted(dicti):
        list_x.append(ix)
        list_y_up.append(np.max(dicti[ix]))
        list_y_down.append(np.min(dicti[ix]))
    out_x=[]
    out_y=[]
    for ii in range(0,len(list_x)):
        out_x.append(list_x[ii])
        out_y.append(list_y_up[ii])
    for ii in range(len(list_x)-1,0-1,-1):
        out_x.append(list_x[ii])
        out_y.append(list_y_down[ii])
    if len(out_x)!=0:
        out_x.append(list_x[0])     # in order to make it close
        out_y.append(list_y_up[0])  #
    if len(out_x)==0:
        out_x.append(999)
        out_y.append(999)
    return [out_x,out_y]    


def Integral_2D(v1_low,v1_up,v1_bin,v2_low,v2_up,v2_bin, result_list, vtx):
    Inte_list=[]
    index1=0
    index2=0
    if vtx=="Vtb":
        index1=1
        index2=2
    elif vtx=="Vts":
        index1=0
        index2=2
    elif vtx=="Vtd":
        index1=0
        index2=1
    else:print "wrong name!!"
    for v1 in np.linspace(v1_low,v1_up,v1_bin): 
        for v2 in np.linspace(v2_low,v2_up,v2_bin):
            inte_chi2=0
            for value in result_list:
                if value[index1]==v1 and value[index2]==v2:
                    inte_chi2=inte_chi2+value[3] 
        Inte_list.append([v1,v2,inte_chi2])
    return Inte_list





Vts_Vtd_8TeV_uncert={'Vts': [0.04395504227138255, 0.039870200469597356, 0.014387298718914508, 0.01947704200683578, 0.04812299473874714, 0.04208920417053782, 0.041173270343239025, 0.0156253977809811, 0.03940912804684313, 0.011548528694792348, 0.02883151414906353, 0.023041622816338963, 0.02185742652037801, 0.016178832101673986, 0.02687423374395859, 0.024474289829419568, 0.044250860485868036, 0.013659854505874258, 0.02859308859124197, 0.03078655869244504, 0.016751890805435408, 0.01969912378478502, 0.01986057169116168, 0.013197013516322588, 0.02085854365869654, 0.022052125082873825, 0.061567368902981645, 0.030495236201795492, 0.0556003170534961, 0.01565078373125331, 0.050360216601641, 0.04091304632771059, 0.011973044553633677, 0.013311580716033139, 0.010434942088840904, 0.01066046720763699, 0.019302912101432396, 0.021236134482665057, 0.029862831515898674, 0.02454346089009116, 0.03530429468606024, 0.022780100653831493, 0.03262330783284554, 0.02531668609072936, 0.041639759425393504, 0.01821879922127982, 0.0436374518529902, 0.032243086487886125, 0.02097460168310003, 0.03489306031573572, 0.027154634625235614], 'Vtb': [0.07114089559484875, 0.0783751961364897, 0.037415946887750885, 0.05101764922573859, 0.03788824656759494, 0.0775647673628361, 0.042724912270416616, 0.04975043255616447, 0.05906691871106207, 0.025890158317952227, 0.020635487404921188, 0.04473482942793604, 0.024878262020556575, 0.04446935124842909, 0.033717611053845895, 0.03933918770153642, 0.04875009086869429, 0.08157154055223807, 0.039337634576278625, 0.08588103967315368, 0.02123734562394866, 0.11993336375349067, 0.06066929396566057, 0.042863064312329786, 0.023059006584475208, 0.04938286228663706, 0.05046217577559997, 0.04656911213491116, 0.028843368613441285, 0.07414856044730206, 0.03712844874970954, 0.06838243161960647, 0.03848586686181305, 0.04639527121923742, 0.021996520326874016, 0.03978012517650329, 0.04505326282158504, 0.05648876007312237, 0.0394890272940215, 0.04049306070372625, 0.046469121306118404, 0.026612384547218933, 0.02918703385162895, 0.05216252499067642, 0.023524573210826873, 0.03974188318419391, 0.034004331990745644, 0.038890929449838345, 0.059904169353828, 0.05218387154469037, 0.06459998629230333], 'Vtd': [0.07657562985535, 0.04465033684644957, 0.027696141367434136, 0.02510434434170673, 0.015572544849350231, 0.03900124672622287, 0.0531179475370572, 0.04697104692546301, 0.021413991686978984, 0.017270986922062085, 0.026599646652362932, 0.016572694848142288, 0.011203730480824832, 0.021256644678799723, 0.0362601165902752, 0.03358152701093658, 0.018243091347809916, 0.025333176925462438, 0.01613142403616025, 0.03347446889499411, 0.02392309525252478, 0.03565165609726555, 0.015921945654881565, 0.016332470715387404, 0.030613364669338578, 0.04192370950935216, 0.047769064807327045, 0.018458457679508503, 0.01746551258900286, 0.02219300876769542, 0.01737939464366101, 0.04397733065968247, 0.03363368750819541, 0.02962450274575771, 0.026947020499131443, 0.04701293242915176, 0.03194933037685177, 0.013361976072923755, 0.011881415529995063, 0.03700166587768256, 0.02660818473581827, 0.03930019811619778, 0.009679465255861898, 0.020054725746801824, 0.03577158754178641, 0.01472198980606653, 0.025949083555222907, 0.02565711274936633, 0.033997191036616206, 0.022770919971643898, 0.04357971267277413]}




Vts_Vtd_7TeV_uncert={'Vts': [0.014510426667812286, 0.018670217941836962, 0.013824410005545327, 0.027235152143910726, 0.026172873399492563, 0.0079686443422907, 0.004499981012853105, 0.004931477276267838, 0.006593416789659163, 0.01494616290808857, 0.0075852502056749475, 0.012904007251510743, 0.027015065372350298, 0.049901546092979816, 0.012161859491987793, 0.008808654696056979, 0.0046735082606708155, 0.0067906718488956325], 'Vtd': [0.010379551291915224, 0.006155319166191686, 0.007886253804342604, 0.013577137342603617, 0.020396735919505873, 0.009637507469347823, 0.005292686331174062, 0.007077097977266686, 0.004513836159277158, 0.014173605624555614, 0.008215794488848323, 0.010061768812414829, 0.022446900306757667, 0.041275458697762994, 0.006247658970508582, 0.006971596886783427, 0.004078938351060619, 0.006539465557376379]}


F_in_8TeV=ROOT.TFile("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/Limit_hist_8TeV.root","read")
hist_8TeV_data=F_in_8TeV.Get("data%s"%data_hist_name)
hist_8TeV_Vtb =F_in_8TeV.Get("Vtb")
hist_8TeV_Vts =F_in_8TeV.Get("Vts")
hist_8TeV_Vtd =F_in_8TeV.Get("Vtd")
if "13TeV" in str_cat:
    F_in_8TeV=ROOT.TFile("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/Limit_hist_13TeV_%s.root"%(str_lumi),"read")
    hist_8TeV_data=F_in_8TeV.Get("data%s"%data_hist_name)
    hist_8TeV_Vtb =F_in_8TeV.Get("Vtb")
    hist_8TeV_Vts =F_in_8TeV.Get("Vts")
    hist_8TeV_Vtd =F_in_8TeV.Get("Vtd")
    print "replace by 13TeV %s file"%(str_lumi)

F_in_7TeV=ROOT.TFile("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/Limit_hist_7TeV.root","read")
hist_7TeV_data=F_in_7TeV.Get("data%s"%data_hist_name)
hist_7TeV_Vtb =F_in_7TeV.Get("Vtb")
hist_7TeV_Vts =F_in_7TeV.Get("Vts")
hist_7TeV_Vtd =F_in_7TeV.Get("Vtd")
Nbins=hist_8TeV_data.GetNbinsX()+hist_7TeV_data.GetNbinsX()
hist_data=ROOT.TH1D("data","",Nbins,0,Nbins)
hist_Vtb =ROOT.TH1D("Vtb" ,"",Nbins,0,Nbins)
hist_Vts =ROOT.TH1D("Vts" ,"",Nbins,0,Nbins)
hist_Vtd =ROOT.TH1D("Vtd" ,"",Nbins,0,Nbins)
hist_Vtb_sys_uncert =ROOT.TH1D("Vtb_sys" ,"",Nbins,0,Nbins)
hist_Vts_sys_uncert =ROOT.TH1D("Vts_sys" ,"",Nbins,0,Nbins)
hist_Vtd_sys_uncert =ROOT.TH1D("Vtd_sys" ,"",Nbins,0,Nbins)
if( (len(Vts_Vtd_8TeV_uncert['Vts'])+len(Vts_Vtd_7TeV_uncert['Vts'])) != Nbins) : print "wrong bin number"
for ibin in range(1,Nbins+1):
    if ibin<=hist_8TeV_data.GetNbinsX():
        hist_data.SetBinContent(ibin,hist_8TeV_data.GetBinContent(ibin))
        hist_data.SetBinError  (ibin,hist_8TeV_data.GetBinError  (ibin))
        hist_Vtb .SetBinContent(ibin,hist_8TeV_Vtb .GetBinContent(ibin))
        hist_Vtb .SetBinError  (ibin,hist_8TeV_Vtb .GetBinError  (ibin))
        hist_Vts .SetBinContent(ibin,hist_8TeV_Vts .GetBinContent(ibin))
        hist_Vts .SetBinError  (ibin,hist_8TeV_Vts .GetBinError  (ibin))
        hist_Vtd .SetBinContent(ibin,hist_8TeV_Vtd .GetBinContent(ibin))
        hist_Vtd .SetBinError  (ibin,hist_8TeV_Vtd .GetBinError  (ibin))
        Vtb_sys=math.sqrt(math.pow(Vts_Vtd_8TeV_uncert['Vtb'][ibin-1],2)+math.pow(0.00,2))##adding 0% uncert
        Vts_sys=math.sqrt(math.pow(Vts_Vtd_8TeV_uncert['Vts'][ibin-1],2)+math.pow(0.00,2))##adding 0% uncert
        Vtd_sys=math.sqrt(math.pow(Vts_Vtd_8TeV_uncert['Vtd'][ibin-1],2)+math.pow(0.00,2))##adding 0% uncert
        if str_lumi=="3000fb":########## for 13 TeV 3000fb scale theory uncert by 0.5
           hist_Vtb_sys_uncert.SetBinContent(ibin,Vtb_sys/2)
           hist_Vts_sys_uncert.SetBinContent(ibin,Vts_sys/2)
           hist_Vtd_sys_uncert.SetBinContent(ibin,Vtd_sys/2)
        else:
           hist_Vtb_sys_uncert.SetBinContent(ibin,Vtb_sys)
           hist_Vts_sys_uncert.SetBinContent(ibin,Vts_sys)
           hist_Vtd_sys_uncert.SetBinContent(ibin,Vtd_sys)
    else:
        hist_data.SetBinContent(ibin,hist_7TeV_data.GetBinContent(ibin-hist_8TeV_data.GetNbinsX()))
        hist_data.SetBinError  (ibin,hist_7TeV_data.GetBinError  (ibin-hist_8TeV_data.GetNbinsX()))
        hist_Vtb .SetBinContent(ibin,hist_7TeV_Vtb .GetBinContent(ibin-hist_8TeV_data.GetNbinsX()))
        hist_Vtb .SetBinError  (ibin,hist_7TeV_Vtb .GetBinError  (ibin-hist_8TeV_data.GetNbinsX()))
        hist_Vts .SetBinContent(ibin,hist_7TeV_Vts .GetBinContent(ibin-hist_8TeV_data.GetNbinsX()))
        hist_Vts .SetBinError  (ibin,hist_7TeV_Vts .GetBinError  (ibin-hist_8TeV_data.GetNbinsX()))
        hist_Vtd .SetBinContent(ibin,hist_7TeV_Vtd .GetBinContent(ibin-hist_8TeV_data.GetNbinsX()))
        hist_Vtd .SetBinError  (ibin,hist_7TeV_Vtd .GetBinError  (ibin-hist_8TeV_data.GetNbinsX()))
        Vts_sys=math.sqrt(math.pow(Vts_Vtd_7TeV_uncert['Vts'][ibin-hist_8TeV_data.GetNbinsX()-1],2)+math.pow(0.00,2))##adding 0% uncert
        Vtd_sys=math.sqrt(math.pow(Vts_Vtd_7TeV_uncert['Vtd'][ibin-hist_8TeV_data.GetNbinsX()-1],2)+math.pow(0.00,2))##adding 0% uncert
        hist_Vtb_sys_uncert.SetBinContent(ibin,0.02)## %2 for vtb 7TeV
        hist_Vts_sys_uncert.SetBinContent(ibin,Vts_sys)
        hist_Vtd_sys_uncert.SetBinContent(ibin,Vtd_sys)

if False:
    for hist in [hist_data,hist_Vtb,hist_Vts,hist_Vtd]:
        canvas = ROOT.TCanvas('canvas','',900, 600)
        canvas.cd()
        canvas.SetLogy()
        hist.Draw("pe")
        canvas.Print('/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/check_plot/%s.png'%(hist.GetName())) 
        del canvas
        gc.collect()


hist_list_8TeV=["H_top_pt_fine","H_top_Rap_fine","H_top_jet_pt_fine","H_top_jet_Rap_fine","H_atop_pt_fine","H_atop_Rap_fine","H_atop_jet_pt_fine","H_atop_jet_Rap_fine"]
hist_list_7TeV=["H_top_pt_fine","H_top_Rap_fine","H_atop_pt_fine","H_atop_Rap_fine"]
'''
Stat_correlation_matrix={}
#################### 8TeV top pt #######################################################################
Stat_correlation_matrix["1"]={"1":1    ,"2":-0.36,"3":0.04 ,"4":0.01 ,"5":0    ,"6":-0.01,"7":0    }
Stat_correlation_matrix["2"]={"1":-0.36,"2":1    ,"3":-0.3 ,"4":0.03 ,"5":0.02 ,"6":0.02 ,"7":-0.01}
Stat_correlation_matrix["3"]={"1":0.04 ,"2":-0.3 ,"3":1    ,"4":-0.27,"5":0.02 ,"6":0    ,"7":-0.01}
Stat_correlation_matrix["4"]={"1":0.01 ,"2":0.03 ,"3":-0.27,"4":1    ,"5":-0.23,"6":0    ,"7":0.01 }
Stat_correlation_matrix["5"]={"1":0    ,"2":0.02 ,"3":0.02 ,"4":-0.23,"5":1    ,"6":-0.17,"7":0.02 }
Stat_correlation_matrix["6"]={"1":-0.01,"2":0.02 ,"3":0    ,"4":0    ,"5":-0.17,"6":1    ,"7":-0.2 }
Stat_correlation_matrix["7"]={"1":0    ,"2":-0.01,"3":-0.01,"4":0.01 ,"5":0.02 ,"6":-0.20,"7":1    }
#################### 8TeV top rap #######################################################################
Stat_correlation_matrix["8"]={"8":1     ,"9":-0.12,"10":0.01 ,"11":0.01 ,"12":0.01 ,"13":-0.01,"14":0    }
Stat_correlation_matrix["9"]={"8":-0.12 ,"9":1    ,"10":-0.13,"11":0    ,"12":-0.02,"13":0    ,"14":0    }
Stat_correlation_matrix["10"]={"8":0.01 ,"9":-0.13,"10":1    ,"11":-0.12,"12":0.01 ,"13":0.02 ,"14":0    }
Stat_correlation_matrix["11"]={"8":0.01 ,"9":0    ,"10":-0.12,"11":1    ,"12":-0.07,"13":0    ,"14":0    }
Stat_correlation_matrix["12"]={"8":0.01 ,"9":-0.02,"10":0.01 ,"11":-0.07,"12":1    ,"13":-0.07,"14":0.01 }
Stat_correlation_matrix["13"]={"8":-0.01,"9":0    ,"10":0.02 ,"11":0    ,"12":-0.07,"13":1    ,"14":-0.04}
Stat_correlation_matrix["14"]={"8":0    ,"9":0    ,"10":0    ,"11":0    ,"12":0.01 ,"13":-0.04,"14":1    }
####################8TeV top jet pt #######################################################################
Stat_correlation_matrix["15"]={"15":1    ,"16":-0.37,"17":0.06    ,"18":0    ,"19":-0.01 ,"20":0.01  }
Stat_correlation_matrix["16"]={"15":-0.37,"16":1    ,"17":-0.33   ,"18":0.05 ,"19":0.01  ,"20":0     }
Stat_correlation_matrix["17"]={"15":0.06 ,"16":-0.33,"17":1       ,"18":-0.33,"19":0.04  ,"20":0     }
Stat_correlation_matrix["18"]={"15":0    ,"16":0.05 ,"17":-0.33   ,"18":1    ,"19":-0.22 ,"20":0.03  }
Stat_correlation_matrix["19"]={"15":-0.01,"16":0.01 ,"17":0.04    ,"18":-0.22,"19":1     ,"20":-0.14 }
Stat_correlation_matrix["20"]={"15":0.01 ,"16":0    ,"17":0       ,"18":0.03 ,"19":-0.14 ,"20":1     }
####################8TeV top jet rap #######################################################################
Stat_correlation_matrix["21"]={"21":1     ,"22":-0.02  ,"23":0.01       ,"24":0     ,"25":-0.02 ,"26":0     }
Stat_correlation_matrix["22"]={"21":-0.02 ,"22":1      ,"23":-0.01      ,"24":-0.01 ,"25":0.01  ,"26":0     }
Stat_correlation_matrix["23"]={"21":0.01  ,"22":-0.01  ,"23":1          ,"24":-0.02 ,"25":0     ,"26":0.01  }
Stat_correlation_matrix["24"]={"21":0     ,"22":-0.01  ,"23":-0.02      ,"24":1     ,"25":-0.02 ,"26":0     }
Stat_correlation_matrix["25"]={"21":-0.02 ,"22":0.01   ,"23":0          ,"24":-0.02 ,"25":1     ,"26":-0.03 }
Stat_correlation_matrix["26"]={"21":0     ,"22":0      ,"23":0.01       ,"24":0     ,"25":-0.03 ,"26":1     }
####################8TeV atop pt #######################################################################
Stat_correlation_matrix["27"]={"27":1     ,"28":-0.36  ,"29":0.05       ,"30":0     ,"31":0     ,"32":-0.01 }
Stat_correlation_matrix["28"]={"27":-0.36 ,"28":1      ,"29":-0.31      ,"30":0.05  ,"31":0     ,"32":0     }
Stat_correlation_matrix["29"]={"27":0.05  ,"28":-0.31  ,"29":1          ,"30":-0.26 ,"31":0.02  ,"32":0.02  }
Stat_correlation_matrix["30"]={"27":0     ,"28":0.05   ,"29":-0.26      ,"30":1     ,"31":-0.23 ,"32":0.01  }
Stat_correlation_matrix["31"]={"27":0     ,"28":0      ,"29":0.02       ,"30":-0.23 ,"31":1     ,"32":-0.15 }
Stat_correlation_matrix["32"]={"27":-0.01 ,"28":0      ,"29":0.02       ,"30":0.01  ,"31":-0.15 ,"32":1     }
####################8TeV atop rap #######################################################################
Stat_correlation_matrix["33"]={"33":1     ,"34":-0.13,"35":0.02 ,"36":0     ,"37":0.01 ,"38":0     ,"39":-0.01    }
Stat_correlation_matrix["34"]={"33":-0.13 ,"34":1    ,"35":-0.11,"36":0     ,"37":0    ,"38":-0.01 ,"39":0        }
Stat_correlation_matrix["35"]={"33":0.02  ,"34":-0.11,"35":1.00 ,"36":-0.11 ,"37":0    ,"38":-0.01 ,"39":-0.01    }
Stat_correlation_matrix["36"]={"33":0.00  ,"34":0.00 ,"35":-0.11,"36":1.00  ,"37":-0.09,"38":0.00  ,"39":-0.01    }
Stat_correlation_matrix["37"]={"33":0.01  ,"34":0.00 ,"35":0.00 ,"36":-0.09 ,"37":1.00 ,"38":-0.06 ,"39": 0.01    }
Stat_correlation_matrix["38"]={"33":0.00  ,"34":-0.01,"35":-0.01,"36": 0.00 ,"37":-0.06,"38":1.00  ,"39":-0.04    }
Stat_correlation_matrix["39"]={"33":-0.01 ,"34":0.00 ,"35":-0.01,"36":-0.01 ,"37":0.01 ,"38":-0.04 ,"39":1.00     }
####################8TeV atop jet pt #######################################################################
Stat_correlation_matrix["40"]={"40": 1.00,"41":-0.36,"42": 0.06,"43": 0.00,"44": 0.01,"45": 0.00 }
Stat_correlation_matrix["41"]={"40":-0.36,"41": 1.00,"42":-0.36,"43": 0.05,"44": 0.02,"45": 0.00 }
Stat_correlation_matrix["42"]={"40": 0.06,"41":-0.36,"42": 1.00,"43":-0.34,"44": 0.04,"45": 0.01 }
Stat_correlation_matrix["43"]={"40": 0.00,"41": 0.05,"42":-0.34,"43": 1.00,"44":-0.22,"45": 0.01 }
Stat_correlation_matrix["44"]={"40": 0.01,"41": 0.02,"42": 0.04,"43":-0.22,"44": 1.00,"45":-0.11 }
Stat_correlation_matrix["45"]={"40": 0.00,"41": 0.00,"42": 0.01,"43": 0.01,"44":-0.11,"45": 1.00 }
####################8TeV atop jet rap  #######################################################################
Stat_correlation_matrix["46"]={"46": 1.00,"47":-0.02,"48": 0.00,"49": 0.01,"50": 0.00,"51": 0.00 }
Stat_correlation_matrix["47"]={"46":-0.02,"47": 1.00,"48":-0.03,"49": 0.00,"50":-0.01,"51":-0.01 }
Stat_correlation_matrix["48"]={"46":-0.00,"47":-0.03,"48": 1.00,"49":-0.02,"50":-0.00,"51": 0.01 }
Stat_correlation_matrix["49"]={"46": 0.01,"47":-0.00,"48":-0.02,"49": 1.00,"50":-0.02,"51": 0.01 }
Stat_correlation_matrix["50"]={"46": 0.00,"47":-0.01,"48":-0.00,"49":-0.02,"50": 1.00,"51":-0.03 }
Stat_correlation_matrix["51"]={"46": 0.00,"47":-0.01,"48": 0.01,"49": 0.01,"50":-0.03,"51": 1.00 }
#################### 7TeV top pt #######################################################################
Stat_correlation_matrix["52"]={"52": 1.00,"53": 0.48,"54": 0.49,"55": 0.43,"56": 0.35 }
Stat_correlation_matrix["53"]={"52": 0.48,"53": 1.00,"54": 0.51,"55": 0.43,"56": 0.37 }
Stat_correlation_matrix["54"]={"52": 0.49,"53": 0.51,"54": 1.00,"55": 0.34,"56": 0.31 }
Stat_correlation_matrix["55"]={"52": 0.43,"53": 0.43,"54": 0.34,"55": 1.00,"56": 0.14 }
Stat_correlation_matrix["56"]={"52": 0.35,"53": 0.37,"54": 0.31,"55": 0.14,"56": 1.00 }
#################### 7TeV top rap #######################################################################
Stat_correlation_matrix["57"]={"57": 1.00,"58":-0.12,"59":-0.14,"60":-0.02 }
Stat_correlation_matrix["58"]={"57":-0.12,"58": 1.00,"59":-0.19,"60":-0.09 }
Stat_correlation_matrix["59"]={"57":-0.14,"58":-0.19,"59": 1.00,"60":-0.18 }
Stat_correlation_matrix["60"]={"57":-0.02,"58":-0.09,"59":-0.18,"60": 1.00 }
#################### 7TeV atop pt #######################################################################
Stat_correlation_matrix["61"]={"61": 1.00,"62": 0.34,"63": 0.26,"64": 0.13,"65": 0.13 }
Stat_correlation_matrix["62"]={"61": 0.34,"62": 1.00,"63": 0.32,"64": 0.03,"65": 0.15 }
Stat_correlation_matrix["63"]={"61": 0.26,"62": 0.32,"63": 1.00,"64": 0.09,"65": 0.05 }
Stat_correlation_matrix["64"]={"61": 0.13,"62": 0.03,"63": 0.09,"64": 1.00,"65":-0.06 }
Stat_correlation_matrix["65"]={"61": 0.13,"62": 0.15,"63": 0.05,"64":-0.06,"65": 1.00 }
#################### 7TeV atop rap #######################################################################
Stat_correlation_matrix["66"]={"66": 1.00,"67":-0.05,"68":-0.17,"69": 0.11 }
Stat_correlation_matrix["67"]={"66":-0.05,"67": 1.00,"68":-0.01,"69":-0.06 }
Stat_correlation_matrix["68"]={"66":-0.17,"67":-0.01,"68": 1.00,"69":-0.23 }
Stat_correlation_matrix["69"]={"66": 0.11,"67":-0.06,"68":-0.23,"69": 1.00 }
'''

#F_in=ROOT.TFile("Limit_hist_8TeV.root","read")
#hist_data=F_in.Get("data")
#hist_Vtb =F_in.Get("Vtb")
#hist_Vts =F_in.Get("Vts")
#hist_Vtd =F_in.Get("Vtd")
#N_Vtb=hist_Vtb.GetSumOfWeights()
#N_Vts=hist_Vts.GetSumOfWeights()
#N_Vtd=hist_Vtd.GetSumOfWeights()
#print "N_Vtb=%f,N_Vts=%f,N_Vtd=%f"%(N_Vtb,N_Vts,N_Vtd)

if False:
    x_lower=hist_data.GetXaxis().GetXmin()
    x_upper=hist_data.GetXaxis().GetXmax()
    x = ROOT.RooRealVar('x','x', x_lower, x_upper)
    H_data = ROOT.RooDataHist('H_data', '', ROOT.RooArgList(x), hist_data)
    H_Vtb  = ROOT.RooDataHist('H_Vtb' , '', ROOT.RooArgList(x), hist_Vtb )
    H_Vts  = ROOT.RooDataHist('H_Vts' , '', ROOT.RooArgList(x), hist_Vts )
    H_Vtd  = ROOT.RooDataHist('H_Vtd' , '', ROOT.RooArgList(x), hist_Vtd )
    pdf_Vtb=ROOT.RooHistPdf('pdf_Vtb','',ROOT.RooArgSet(x),H_Vtb,0)
    pdf_Vts=ROOT.RooHistPdf('pdf_Vts','',ROOT.RooArgSet(x),H_Vts,0)
    pdf_Vtd=ROOT.RooHistPdf('pdf_Vtd','',ROOT.RooArgSet(x),H_Vtd,0)
    #f_Vtb = ROOT.RooRealVar('f_Vtb', 'f_Vtb', 0.9 , 0, 1)
    #f_Vts = ROOT.RooRealVar('f_Vts', 'f_Vts', 0.01, 0, 1)
    #f_Vtd = ROOT.RooRealVar('f_Vtd', 'f_Vtd', 0.01, 0, 1)
    ##model = ROOT.RooAddPdf('model', 'Vtb*pdf1+Vts*pdf2+(1-Vtb-Vts)*pdf3', ROOT.RooArgList(pdf_Vtb, pdf_Vts, pdf_Vtd), ROOT.RooArgList(f_Vtb,f_Vts))
    ##model = ROOT.RooAddPdf('model', 'Vtb*pdf1+Vtd*pdf2+(1-Vtb-Vtd)*pdf3', ROOT.RooArgList(pdf_Vtb, pdf_Vtd, pdf_Vts), ROOT.RooArgList(f_Vtb,f_Vtd))
    #model = ROOT.RooAddPdf('model', 'Vts*pdf1+Vtd*pdf2+%*pdf3', ROOT.RooArgList(pdf_Vts, pdf_Vtd, pdf_Vtb), ROOT.RooArgList(f_Vts,f_Vtd))
    #result = model.fitTo(H_data, ROOT.RooFit.Range(x_lower, x_upper), ROOT.RooFit.Save(True),ROOT.RooFit.SumW2Error(False))##use this give same error 
    #f_Vtb = ROOT.RooRealVar('f_Vtb', 'f_Vtb', 0.9 , 0, 100)
    #f_Vts = ROOT.RooRealVar('f_Vts', 'f_Vts', 0.01, 0, 100)
    #f_Vtd = ROOT.RooRealVar('f_Vtd', 'f_Vtd', 0.01, 0, 100)
    f_Vtb = ROOT.RooRealVar('f_Vtb', 'f_Vtb', 0.9 , 0, 1)
    f_Vts = ROOT.RooRealVar('f_Vts', 'f_Vts', 0.01, 0, 1)
    f_Vtd = ROOT.RooRealVar('f_Vtd', 'f_Vtd', 0.01, 0, 1)
    model = ROOT.RooAddPdf('model', 'vtb*pdf1+vts*pdf2+vtd*pdf3'        , ROOT.RooArgList(pdf_Vtb, pdf_Vts, pdf_Vtd), ROOT.RooArgList(f_Vtb,f_Vts,f_Vtd))
    #model = ROOT.RooGenericPdf("model","","32.33*TMath::Power(@0,2)*@1+116.23*TMath::Power(@2,2)*@3+242.57*TMath::Power(@4,2)*@5",ROOT.RooArgList(f_Vtb,pdf_Vtb,f_Vts,pdf_Vts,f_Vtd,pdf_Vtd))
    #modelxy = model.createProjection(ROOT.RooArgSet(f_Vtb))
    #modelx  = model.createProjection(ROOT.RooArgSet(f_Vtb,f_Vtd))
    #result = modelx.fitTo(H_data, ROOT.RooFit.Extended(False),ROOT.RooFit.Minos(False), ROOT.RooFit.Save(True),ROOT.RooFit.SumW2Error(False))##use this give same error 
    #result = modelxy.fitTo(H_data, ROOT.RooFit.Extended(False),ROOT.RooFit.Minos(False), ROOT.RooFit.Save(True),ROOT.RooFit.SumW2Error(False))##use this give same error 
    result = model.fitTo(H_data, ROOT.RooFit.Extended(False),ROOT.RooFit.Minos(False), ROOT.RooFit.Save(True),ROOT.RooFit.SumW2Error(False))##use this give same error 
    #result = model.fitTo(H_data, ROOT.RooFit.Extended(True),ROOT.RooFit.Minos(False), ROOT.RooFit.Save(True),ROOT.RooFit.SumW2Error(False))##use this give same error 
    #result = model.fitTo(H_data, ROOT.RooFit.Range(x_lower, x_upper), ROOT.RooFit.Save(True),ROOT.RooFit.SumW2Error(True))
    #result = model.fitTo(H_data, ROOT.RooFit.Range(x_lower, x_upper), ROOT.RooFit.Save(True),ROOT.RooFit.SumW2Error(False),ROOT.RooFit.PrintLevel(-1))
    fit_status=ROOT.gMinuit.fCstatu
    min_Nll   =result.minNll()
    #Vtb_value=f_Vtb.getValV()  
    #Vtb_error=f_Vtb.getError() 
    #Vts_value=f_Vts.getValV()  
    #Vts_error=f_Vts.getError() 
    #print "minNll %f"%(result.minNll())
    #print "vtb=%f+-%f"%(Vtb_value,Vtb_error)
    #print "vts=%f+-%f"%(Vts_value,Vts_error)
    #print "precentage vtb=%f+-%f"%(Vtb_value/hist_data.GetSumOfWeights(),Vtb_error/hist_data.GetSumOfWeights())
    #print "precentage vts=%f+-%f"%(Vts_value/hist_data.GetSumOfWeights(),Vts_error/hist_data.GetSumOfWeights())
    
    canvas=ROOT.TCanvas("canvas","",600,800)
    #canvas.SetGridx(False)
    #canvas.SetGridy(False)
    #canvas.SetRightMargin(0.05)
    canvas.SetLeftMargin(0.1)
    canvas.SetLogy()
    frame = x.frame()
    H_data.plotOn(frame,ROOT.RooFit.DataError(ROOT.RooAbsData.SumW2))
    model.plotOn(frame)
    model.plotOn(frame, ROOT.RooFit.Components('pdf_Vtb'), ROOT.RooFit.LineStyle(ROOT.kDashed), ROOT.RooFit.LineColor(ROOT.kRed))
    model.plotOn(frame, ROOT.RooFit.Components('pdf_Vts'), ROOT.RooFit.LineStyle(ROOT.kDashed), ROOT.RooFit.LineColor(ROOT.kGreen))
    model.plotOn(frame, ROOT.RooFit.Components('pdf_Vtd'), ROOT.RooFit.LineStyle(ROOT.kDashed), ROOT.RooFit.LineColor(ROOT.kYellow))
    H_data.plotOn(frame,ROOT.RooFit.DataError(ROOT.RooAbsData.SumW2))
    model.paramOn(frame, ROOT.RooFit.Layout(0.7,0.95,0.9))##plot parameter
    frame.getAttText().SetTextSize(0.02)
    #Chi2 =ROOT.RooChi2Var("chi2","",model,H_data)
    #value=Chi2.getVal() 
    #NDof = hist_data.GetNbinsX()-model.getParameters(H_data).getSize()
    #chi2OverNDof = 0 if NDof==0 else value/NDof
    #str_chi2ONDF="#chi^{2}/NDF=%.1f/%d=%.1f"%(value,NDof,chi2OverNDof)
    frame.SetTitle('')
    frame.GetXaxis().SetTitle('Bin')
    frame.GetXaxis().SetTitleSize(0.05)
    frame.GetXaxis().SetLabelSize(0.04)
    frame.GetXaxis().SetTitleOffset(0.8)
    frame.GetYaxis().SetTitle('XS')
    frame.GetYaxis().SetTitleSize(0.06)
    frame.GetYaxis().SetLabelSize(0.04)
    frame.GetYaxis().SetTitleOffset(1)
    str_fit_status="status=%s"%(str(fit_status))
    str_minNll="minNll=%s"%(str(min_Nll))
    #label_chi2oNDF=ROOT.TLatex(0.7, 0.45 , "%s, %s"%(str(str_chi2ONDF),str_fit_status))
    #label_chi2oNDF.SetTextSize(0.02)
    #label_chi2oNDF.SetNDC()
    #frame.addObject(label_chi2oNDF)
    label_status=ROOT.TLatex(0.5, 0.45 , "%s, %s"%(str(str_minNll),str_fit_status))
    label_status.SetTextSize(0.02)
    label_status.SetNDC()
    frame.addObject(label_status)
    frame.SetMaximum(10)
    frame.SetMinimum(1e-9)
    frame.Draw()
    canvas.Print("./fit_resut.pdf")

############################# NLL ########################
if False:
    N_try=0
    F_out=ROOT.TFile("limit.root","RECREATE")
    x_low=0.9
    x_up =1
    x_bin=11
    y_low=0
    y_up =1e-1
    y_bin=101
    z_low=0
    z_up =1e-1
    z_bin=101
    Hist_out=ROOT.TH3D("Hist","",x_bin,x_low,x_up,y_bin,y_low,y_up,z_bin,z_low,z_up)
    for vtb in np.linspace(x_low,x_up,x_bin): 
        vtb_tmp=str(vtb).replace(".","p")
        Hist2D_out=ROOT.TH2D("Hist_Vtb_%s"%(str(vtb_tmp)),"",y_bin,y_low,y_up,z_bin,z_low,z_up)
        for vts in np.linspace(y_low,y_up,y_bin): 
            for vtd in np.linspace(z_low,z_up,z_bin): 
                N_try+=1
                if (N_try%10000)==0:print"process %f"%(float(N_try)/(x_bin*y_bin*z_bin))
                if(vtb+vts+vtd)>1:continue 
                f_Vtb_1 = ROOT.RooRealVar('f_Vtb_1', 'f_Vtb_1', vtb)
                f_Vts_1 = ROOT.RooRealVar('f_Vts_1', 'f_Vts_1', vts)
                f_Vtd_1 = ROOT.RooRealVar('f_Vtd_1', 'f_Vtd_1', vtd)
                model_1 = ROOT.RooAddPdf('model_1', 'Vtb*pdf1+Vts*pdf2+Vtd*pdf3', ROOT.RooArgList(pdf_Vtb, pdf_Vts, pdf_Vtd), ROOT.RooArgList(f_Vtb_1,f_Vts_1,f_Vtd_1))
                nll     = ROOT.RooNLLVar("nll","nll",model_1,H_data) 
                #print "Nll=%f"%(nll.getVal())
                Hist_out.Fill(vtb,vts,vtd,2*2.303*(nll.getVal()-min_Nll))
                Hist2D_out.Fill(vts,vtd  ,2*2.303*(nll.getVal()-min_Nll))
                del f_Vtb_1 
                del f_Vts_1 
                del f_Vtd_1 
                del model_1 
                del nll     
                gc.collect()
        F_out.cd()
        Hist2D_out.Write()
    F_out.cd()
    Hist_out.Write()
    F_out.Close()
    print "saved limit plot"

############################# Chi2 ########################




if True:
    
    indiv_Vtb=True  if str_indiv=="iVtb" else False
    indiv_Vts=True  if str_indiv=="iVts" else False
    indiv_Vtd=True  if str_indiv=="iVtd" else False
    NDOF=hist_data.GetNbinsX()
    print "N bins data=%d"%NDOF
    ############## For ttbar channel R value ###########
    CMS_R=[1.014,0.003,0.032]
    D0_R=[0.9,0.04]
    CDF_R_1=[0.87,0.07]
    CDF_R_2=[0.94,0.09]
    NDOF=NDOF+4
    ############# For ttbar channel top width ##########
    G_F=1.16637e-5
    MT=172.5
    MW=80.385
    aphi_s=0.118
    top_width_scale=G_F*math.pow(MT,3)*math.pow((1-math.pow(MW/MT,2)),2)*(1+2*math.pow(MW/MT,2))*(1-((2*aphi_s)/(3*math.pi))*((2*math.pi*math.pi/3)-(5/2)))/(8*math.pi*math.sqrt(2))
    ATLAS_W=[1.76,0.33,0.79]
    CDF_W=[1.10,4.05]
    D0_W=[0.3,4.4]
    NDOF=NDOF+3    
    ############# For TW cross section ##########
    ATLAS_TW_7=[16.8,2.9,4.9]
    ATLAS_TW_8=[23.0,1.3,3.5,1.1]
    ATLAS_TW_13=[94,10,28,2]
    CMS_TW_7=[16,5]
    CMS_TW_8=[23.4,5.4]
    NDOF=NDOF+5    
    ############# For t-channel inclusive XS and Rt ##########
    ATLAS_7_Rt=[2.04,0.18] 
    ATLAS_8_Rt=[1.72,0.09] 
    ATLAS_13_t   =[156,5,27,3] 
    ATLAS_13_tbar=[91,4,18,2] 
    ATLAS_13_Rt=[1.72,0.09,0.18] 
    CMS_7_ttbar=[67.2,6.1]
    CMS_8_t=[53.8,1.5,4.4]
    CMS_8_tbar=[27.6,1.3,3.7]
    CMS_8_Rt=[1.95,0.10,0.19]
    CMS_13_t   =[154,22] 
    CMS_13_tbar=[85,16] 
    CMS_13_Rt=[1.81,0.18,0.15] 
    D0_ttbar=[2.9,0.59]
    NDOF=NDOF+13    
    #################### some cards for different situation ##  
    NPara=3
    icat=str_cat
    Cats={}
    Cats["obs"]={}
    Cats["exp"]={}
    Cats["exp"]["Ratio_8TeV"]                    =cat_object( "exp_Ratio_8TeV"                    , 0    , 0 , 0 , 1               , 0.0 ,2.0 ,401,0 ,0.8 ,201,0 ,0.8 ,201)
    Cats["exp"]["Width_8TeV"]                    =cat_object( "exp_Width_8TeV"                    , 0    , 0 , 0 , 1               , 0.0 ,2.0 ,401,0 ,2.0 ,401,0 ,2.0 ,401)
    Cats["exp"]["Rt_8TeV"]                       =cat_object( "exp_Rt_8TeV"                       , 0    , 0 , 0 , 1               , 0.0 ,2.0 ,401,0 ,2.0 ,401,0 ,1.0 ,201)
    Cats["exp"]["tW_8TeV"]                       =cat_object( "exp_tW_8TeV"                       , 0    , 0 , 0 , 1               , 0.0 ,1.4 ,201,0 ,2.0 ,201,0 ,2.0 ,201)
    Cats["exp"]["tW_Ratio_8TeV"]                 =cat_object( "exp_tW_Ratio_8TeV"                 , 0    , 0 , 0 , 2               , 0.0 ,1.4 ,201,0 ,2.0 ,201,0 ,2.0 ,201)
    Cats["exp"]["ST_8TeV"]                       =cat_object( "exp_ST_8TeV"                       , 0    , 0 , 0 , 2               , 0.0 ,1.2 ,201,0 ,2.0 ,201,0 ,2.0 ,201)
    Cats["exp"]["ST_Ratio_8TeV"]                 =cat_object( "exp_ST_Ratio_8TeV"                 , 0    , 0 , 0 , 3               , 0.0 ,1.2 ,201,0 ,2.0 ,201,0 ,2.0 ,201)
    Cats["exp"]["Diff_13TeV"]                    =cat_object( "exp_Diff_13TeV"                    , 0    , 1 , 51, 51-NPara        , 0.4 ,1.2 ,201,0 ,2   ,401,0 ,0.6 ,401)##for 13 TeV expection
    Cats["exp"]["Diff_13TeV_Ratio"]              =cat_object( "exp_Diff_13TeV_Ratio"              , 0    , 1 , 51, 52-NPara        , 0.9 ,1.05,401,0 ,0.3 ,401,0 ,0.3 ,401)##for 13 TeV expection
    Cats["exp"]["Diff_8TeV"]                     =cat_object( "exp_Diff_8TeV"                     , 0    , 1 , 51, 51-NPara        , 0.4 ,1.2 ,201,0 ,2   ,401,0 ,0.6 ,201)
    Cats["exp"]["Diff_8TeV_Ratio"]               =cat_object( "exp_Diff_8TeV_Ratio"               , 0    , 1 , 51, 52-NPara        , 0.6 ,1.2 ,301,0 ,0.5 ,201,0 ,0.3 ,201)
#    Cats["exp"]["Diff_8TeV_Ratio"]               =cat_object( "exp_Diff_8TeV_Ratio"               , 0.189949    , 1 , 51, 52-NPara        , 0.6 ,1.2 ,301,0 ,0.5 ,201,0 ,0.3 ,201)## fix R to CMS value
    Cats["exp"]["8TeV_Ratio_st_fid"]             =cat_object( "exp_8TeV_Ratio_st_fid"             , 0    , 0 , 0 , 3-NPara         , 0.8 ,1.1 ,301,0 ,0.4 ,301,0 ,0.4 ,301)## check R+fid
    Cats["exp"]["Diff_8TeV_tW_ST_Width_Ratio_Rt"]=cat_object( "exp_Diff_8TeV_tW_ST_Width_Ratio_Rt", 0    , 1 , 51, 59-NPara        , 0.6 ,1.2 ,301,0 ,0.5 ,201,0 ,0.3 ,201)
    Cats["exp"]["Diff_8TeV_7TeV_Inclusive"]      =cat_object( "exp_Diff_8TeV_7TeV_Inclusive"      , 0    , 1 , 69, NDOF-NPara-11   , 0.85,1.05,201,0 ,0.4 ,201,0 ,0.2 ,201)##for expected all
#    Cats["exp"]["Diff_8TeV_7TeV_Inclusive"]      =cat_object( "exp_Diff_8TeV_7TeV_Inclusive"      , 0.190325    , 1 , 69, NDOF-NPara-11   , 0.85,1.05,201,0 ,0.4 ,201,0 ,0.2 ,201)##for expected all, fix R to CMS value

    Cats["obs"]["Inclusive"]                     =cat_object( "obs_Inclusive"                     , -1   , 0 , 0 , NDOF-51-18-NPara, 0.8 ,1.1 ,201,0 ,0.4 ,201,0 ,0.25,201)
    Cats["obs"]["Diff_7TeV"]                     =cat_object( "obs_Diff_7TeV"                     , -1   , 52, 69, 18-NPara        , 0.8 ,1.1 ,101,0 ,0.4 ,101,0 ,0.25,101)
    Cats["obs"]["Diff_8TeV"]                     =cat_object( "obs_Diff_8TeV"                     , 52.81, 1 , 51, 51-NPara        , 0.85 ,1.05,201,0 ,0.45,201,0 ,0.15,201)##for compare
    Cats["obs"]["Diff_13TeV"]                    =cat_object( "obs_Diff_13TeV"                    , 0    , 1 , 51, 51-NPara        , 0.4  ,1.2 ,201,0 ,2   ,401,0 ,0.6 ,201)##no result now,only 13 TeV expection
    Cats["obs"]["Diff_8TeV_Ratio"]               =cat_object( "obs_Diff_8TeV_Ratio"               , 53.0 , 1 , 51, 52-NPara        , 0.85 ,1.05,201,0 ,0.45,201,0 ,0.15,201)##for compare
#    Cats["obs"]["Diff_8TeV_Ratio"]               =cat_object( "obs_Diff_8TeV_Ratio"               , 52.807113 , 1 , 51, 52-NPara        , 0.85 ,1.05,201,0 ,0.45,201,0 ,0.15,201)##for fix R to CMS
    Cats["obs"]["8TeV_Ratio_st_fid"]             =cat_object( "obs_8TeV_Ratio_st_fid"             , 0.590749  , 0 , 0, 3-NPara          , 0.8 ,1.1 ,301,0 ,0.3 ,301,0 ,0.4,301)##check R+fid
    Cats["obs"]["Diff_8TeV_7TeV_Ratio"]          =cat_object( "obs_Diff_8TeV_7TeV_Ratio"          , 0    , 1 , 69, 70-NPara        , 0.85 ,1.05,201,0 ,0.45,201,0 ,0.15,201)##for check
    Cats["obs"]["Diff_13TeV_Ratio"]              =cat_object( "obs_Diff_13TeV_Ratio"              , 0    , 1 , 51, 52-NPara        , 0.85 ,1.05,201,0 ,0.45,201,0 ,0.15,201)##no result now,only 13 TeV expection
    Cats["obs"]["Diff_7TeV_Inclusive"]           =cat_object( "obs_Diff_7TeV_Inclusive"           , -1   , 52, 69, NDOF-51-NPara   , 0.8 ,1.1 ,301,0 ,0.4 ,201,0 ,0.25,201)##for compare
    Cats["obs"]["Diff_8TeV_Inclusive"]           =cat_object( "obs_Diff_8TeV_Inclusive"           , 0    , 1 , 51, NDOF-18-NPara   , 0.8 ,1.1 ,301,0 ,0.4 ,201,0 ,0.25,201)##for check
    #Cats["obs"]["Diff_8TeV_7TeV_Inclusive"]      =cat_object( "obs_Diff_8TeV_7TeV_Inclusive"      , 96.96, 1 , 69, NDOF-NPara      , 0.85,1.05,201,0 ,0.4 ,201,0 ,0.2 ,201)##for final result
    Cats["obs"]["Diff_8TeV_7TeV_Inclusive"]      =cat_object( "obs_Diff_8TeV_7TeV_Inclusive"      , 86.87 , 1 , 69, NDOF-NPara-3    , 0.85,1.05,201,0 ,0.4 ,201,0 ,0.2 ,201)##for final result, no D0,CDF R
#    Cats["obs"]["Diff_8TeV_7TeV_Inclusive"]      =cat_object( "obs_Diff_8TeV_7TeV_Inclusive"      , 87.364266 , 1 , 69, NDOF-NPara-3    , 0.85,1.05,201,0 ,0.4 ,201,0 ,0.2 ,201)##for final result, no D0,CDF R, fix R to CMS
    Cats["obs"]["Diff_8TeV_top_pt"]              =cat_object( "obs_Diff_8TeV_top_pt"              , -1   , 1 , 7 , 7               , 0.6 ,1.2,101,0 ,0.4,101,0 ,0.2,101)
    Cats["obs"]["Diff_8TeV_top_y"]               =cat_object( "obs_Diff_8TeV_top_y"               , -1   , 8 , 14, 7               , 0.6 ,1.2,101,0 ,0.4,101,0 ,0.2,101)
    Cats["obs"]["Diff_8TeV_top_jet_pt"]          =cat_object( "obs_Diff_8TeV_top_jet_pt"          , -1   , 15, 20, 6               , 0.6 ,1.2,101,0 ,0.4,101,0 ,0.2,101)
    Cats["obs"]["Diff_8TeV_top_jet_y"]           =cat_object( "obs_Diff_8TeV_top_jet_y"           , -1   , 21, 26, 6               , 0.6 ,1.2,101,0 ,0.4,101,0 ,0.2,101)
    Cats["obs"]["Diff_8TeV_atop_pt"]             =cat_object( "obs_Diff_8TeV_atop_pt"             , -1   , 27 ,32 ,6               , 0.6 ,1.2,101,0 ,0.4,101,0 ,0.2,101)
    Cats["obs"]["Diff_8TeV_atop_y"]              =cat_object( "obs_Diff_8TeV_atop_y"              , -1   , 33 ,39, 7               , 0.6 ,1.2,101,0 ,0.4,101,0 ,0.2,101)
    Cats["obs"]["Diff_8TeV_atop_jet_pt"]         =cat_object( "obs_Diff_8TeV_atop_jet_pt"         , -1   , 40, 45, 6               , 0.6 ,1.2,101,0 ,0.4,101,0 ,0.2,101)
    Cats["obs"]["Diff_8TeV_atop_jet_y"]          =cat_object( "obs_Diff_8TeV_atop_jet_y"          , -1   , 46, 51, 6               , 0.6 ,1.2,101,0 ,0.4,101,0 ,0.2,101)

    if Fixed_R==0.9:
        Cats["exp"]["Diff_8TeV_Ratio"]            =cat_object( "exp_Diff_8TeV_Ratio"               ,12.532487 , 1 , 51, 52-NPara       , 0.8 ,1.0 ,401,0.25 ,0.35 ,401,0 ,0.15 ,401)
        Cats["exp"]["Diff_8TeV_7TeV_Inclusive"]   =cat_object( "exp_Diff_8TeV_7TeV_Inclusive"      ,14.907341 , 1 , 69, NDOF-NPara-11  , 0.8 ,1.0 ,401,0.25 ,0.35 ,401,0 ,0.15 ,401)
        Cats["obs"]["Diff_8TeV_Ratio"]           =cat_object( "obs_Diff_8TeV_Ratio"               , 81.429889 , 1 , 51, 52-NPara       , 0.8 ,1.0 ,401,0.25 ,0.35 ,401,0 ,0.15 ,401)
        Cats["obs"]["Diff_8TeV_7TeV_Inclusive"]  =cat_object( "obs_Diff_8TeV_7TeV_Inclusive"      , 121.370952, 1 , 69, NDOF-NPara-3   , 0.8 ,1.0 ,401,0.25 ,0.35 ,401,0 ,0.15 ,401)
    if Fixed_R==0.95:
        Cats["exp"]["Diff_8TeV_Ratio"]            =cat_object( "exp_Diff_8TeV_Ratio"               ,3.212733 , 1 , 51, 52-NPara        , 0.85 ,1.05 ,401,0.12 ,0.26 ,401,0 ,0.2 ,401)
        Cats["exp"]["Diff_8TeV_7TeV_Inclusive"]   =cat_object( "exp_Diff_8TeV_7TeV_Inclusive"      ,3.887127 , 1 , 69, NDOF-NPara-11   , 0.85 ,1.05 ,401,0.12 ,0.26 ,401,0 ,0.2 ,401)
        Cats["obs"]["Diff_8TeV_Ratio"]           =cat_object( "obs_Diff_8TeV_Ratio"               , 64.646454 , 1 , 51, 52-NPara       , 0.85 ,1.05 ,401,0.12 ,0.26 ,401,0 ,0.2 ,401)
        Cats["obs"]["Diff_8TeV_7TeV_Inclusive"]  =cat_object( "obs_Diff_8TeV_7TeV_Inclusive"      , 99.867181 , 1 , 69, NDOF-NPara-3   , 0.85 ,1.05 ,401,0.12 ,0.26 ,401,0 ,0.2 ,401)
    if Fixed_R==0.99:
        Cats["exp"]["Diff_8TeV_Ratio"]            =cat_object( "exp_Diff_8TeV_Ratio"               ,0.132553 , 1 , 51, 52-NPara        , 0.85 ,1.05 ,401,0.0 ,0.15 ,401,0 ,0.15 ,401)
        Cats["exp"]["Diff_8TeV_7TeV_Inclusive"]   =cat_object( "exp_Diff_8TeV_7TeV_Inclusive"      ,0.163180 , 1 , 69, NDOF-NPara-11   , 0.85 ,1.05 ,401,0.0 ,0.15 ,401,0 ,0.15 ,401)
        Cats["obs"]["Diff_8TeV_Ratio"]           =cat_object( "obs_Diff_8TeV_Ratio"               , 54.906328 , 1 , 51, 52-NPara       , 0.85 ,1.05 ,401,0.0 ,0.15 ,401,0 ,0.15 ,401)
        Cats["obs"]["Diff_8TeV_7TeV_Inclusive"]  =cat_object( "obs_Diff_8TeV_7TeV_Inclusive"      , 88.746315 , 1 , 69, NDOF-NPara-3   , 0.85 ,1.05 ,401,0.0 ,0.15 ,401,0 ,0.15 ,401)


    if icat not in Cats[str_type]:
        print "wrong not find: %s %s"%(str_type,icat)
        exit()
    print "for %s"%icat
    Indiv_minChi2={}
    Indiv_minChi2["obs"]={}
    Indiv_minChi2["obs"]["Diff_8TeV_7TeV_Inclusive"]={}
    Indiv_minChi2["obs"]["Diff_8TeV_Ratio"]={}
    Indiv_minChi2["obs"]["Diff_8TeV_7TeV_Inclusive"]["iVtb"]=86.872052
    Indiv_minChi2["obs"]["Diff_8TeV_7TeV_Inclusive"]["iVts"]=90.027558
    Indiv_minChi2["obs"]["Diff_8TeV_7TeV_Inclusive"]["iVtd"]=90.027558
    Indiv_minChi2["obs"]["Diff_8TeV_Ratio"]["iVtb"]=52.996654
    Indiv_minChi2["obs"]["Diff_8TeV_Ratio"]["iVts"]=57.093447
    Indiv_minChi2["obs"]["Diff_8TeV_Ratio"]["iVtd"]=57.093447
    #########################################################
    N_try=0
    result_list_1sigma=[]
    result_list_2sigma=[]
    result_list_3sigma=[]
    Vtx_x=array('f')
    Vtx_xel=array('f')
    Vtx_xeh=array('f')
    Vtx_y=array('f')
    Vtx_yel=array('f')
    Vtx_yeh=array('f')
    Vtb_best=array('f')
    Vts_best=array('f')
    Vtd_best=array('f')
    ndof   =Cats[str_type][icat].ndof   
    Min_chi2=Cats[str_type][icat].min_chi2
    delta_chi2_cut_1=[1   ,3.84,6.63]##for fit parameters=1, 68.3%,95%,99%#http://www.reid.ai/2012/09/chi-squared-distribution-table-with.html
    delta_chi2_cut_2=[2.30,5.99,9.21]##for fit parameters=2, 68.3%,95%,99%
    delta_chi2_cut_3=[3.53,7.82,11.3]##for fit parameters=3  68.3%,95%,99%
    delta_chi2_cut_68=delta_chi2_cut_3[0]
    delta_chi2_cut_95=delta_chi2_cut_3[1]
    delta_chi2_cut_99=delta_chi2_cut_3[2]
    if indiv_Vtb or indiv_Vts or indiv_Vtd:
        delta_chi2_cut_68=delta_chi2_cut_1[0]
        delta_chi2_cut_95=delta_chi2_cut_1[1]
        delta_chi2_cut_99=delta_chi2_cut_1[2]
        if str_type=="exp":
            Min_chi2=0
        elif Indiv_minChi2[str_type][icat][str_indiv] is not None:
            Min_chi2=Indiv_minChi2[str_type][icat][str_indiv]
        else:print "wrong..."
    if do_Fix_R :
       delta_chi2_cut_68=delta_chi2_cut_2[0]
       delta_chi2_cut_95=delta_chi2_cut_2[1]
       delta_chi2_cut_99=delta_chi2_cut_2[2]

    bin_min=Cats[str_type][icat].bin_min
    bin_max=Cats[str_type][icat].bin_max
    Vtb_low=Cats[str_type][icat].Vtb_low
    Vtb_up =Cats[str_type][icat].Vtb_up 
    Vtb_bin=Cats[str_type][icat].Vtb_bin
    Vts_low=Cats[str_type][icat].Vts_low
    Vts_up =Cats[str_type][icat].Vts_up 
    Vts_bin=Cats[str_type][icat].Vts_bin
    Vtd_low=Cats[str_type][icat].Vtd_low
    Vtd_up =Cats[str_type][icat].Vtd_up 
    Vtd_bin=Cats[str_type][icat].Vtd_bin
    if marginlized:
        Vtb_low=0.92
        Vtb_up =1.04
        Vtb_bin=121
        #Vtb_bin=19
        Vts_low=-0.3
        Vts_up =0.3
        #Vts_bin=301
        Vts_bin=101
        Vtd_low=-0.13
        Vtd_up =0.13
        #Vtd_bin=301
        Vtd_bin=101
    elif indiv_Vtb:
        Vtb_low=0.8
        Vtb_up =1.2
        Vtb_bin=10001
        Vts_low=0
        Vts_up =0
        Vts_bin=1
        Vtd_low=0
        Vtd_up =0
        Vtd_bin=1
    elif indiv_Vts:
        Vts_low=0
        Vts_up =0.5
        Vts_bin=10001
        Vtb_low=1
        Vtb_up =1
        Vtb_bin=1
        Vtd_low=0
        Vtd_up =0
        Vtd_bin=1
    elif indiv_Vtd:
        Vtb_low=1
        Vtb_up =1
        Vtb_bin=1
        Vts_low=0
        Vts_up =0
        Vts_bin=1
        Vtd_low=0
        Vtd_up =0.25
        Vtd_bin=10001
    best_fit=[]
    min_chi2=float(1e5)
    max_Prob=float(0)
    ma_Vtb=[]
    ma_Vts=[]
    ma_Vtd=[]
    ma_Prob=[]
    Lumi=float(1)
    if str_lumi==""        :Lumi=float(1)
    elif str_lumi=="100fb" :Lumi=float(100.0)
    elif str_lumi=="300fb" :Lumi=float(300.0)
    elif str_lumi=="3000fb":Lumi=float(3000.0)
    else:
        print "wrong Lumi"
        exit()
    vtb_array=np.linspace(Vtb_low,Vtb_up,Vtb_bin)
    vts_array=np.linspace(Vts_low,Vts_up,Vts_bin)
    vtd_array=np.linspace(Vtd_low,Vtd_up,Vtd_bin)
    vtb_array1=np.linspace(Vtb_low,Vtb_up,Vtb_bin)
    vts_array1=np.linspace(Vts_low,Vts_up,Vts_bin)
    vtd_array1=np.linspace(Vtd_low,Vtd_up,Vtd_bin)
    
    if len(np.where(vtb_array==1)[0])==0:vtb_array1=np.insert(vtb_array,0,values=[[1.0]],axis=0)
    if len(np.where(vts_array==0)[0])==0:vts_array1=np.insert(vts_array,0,values=[[0.0]],axis=0)
    if len(np.where(vtd_array==0)[0])==0:vtd_array1=np.insert(vtd_array,0,values=[[0.0]],axis=0)
    for vtb in vtb_array1: 
        for vts in vts_array1: 
            if do_Fix_R : 
                tmp0 = ((1-Fixed_R)*vtb*vtb/Fixed_R) - (vts*vts)
                if tmp0<0:continue
                vtd_array1 = [math.sqrt(tmp0)]
            for vtd in vtd_array1: 
              #  if(vtb*vtb+vts*vts+vtd*vtd)>1:continue## cut 
                N_try+=1
                if (N_try%100000)==0:print"process %f"%(float(N_try)/(Vtb_bin*Vts_bin*Vtd_bin))
                if (vtb*vtb+vts*vts+vtd*vtd==0): continue
                Prob_chi2=ROOT.mod_limit(vtb, vts, vtd, icat, bin_min, bin_max, hist_Vtb, hist_Vts, hist_Vtd, hist_Vtb_sys_uncert, hist_Vts_sys_uncert, hist_Vtd_sys_uncert, hist_data, ndof, str_type, Lumi, do_Fix_R, Fixed_R)
                Prob_calc=Prob_chi2.first
                tmp_chi2 =Prob_chi2.second
                #print Prob_calc.first
                #print Prob_calc.second
                if tmp_chi2<min_chi2:
                    min_chi2=tmp_chi2
                    best_fit=[vtb,vts,vtd]
                    max_Prob=Prob_calc
                if marginlized:
                    ma_Vtb.append(vtb)
                    ma_Vts.append(vts)
                    ma_Vtd.append(vtd)
                    ma_Prob.append(math.exp(-tmp_chi2/2))
                else:
                    if str_method == "chi2":
                        if Prob_calc>0.32:
                            result_list_1sigma.append([vtb,vts,vtd])
                            result_list_2sigma.append([vtb,vts,vtd])
                            result_list_3sigma.append([vtb,vts,vtd])
                        elif Prob_calc>0.05:
                            result_list_2sigma.append([vtb,vts,vtd])
                            result_list_3sigma.append([vtb,vts,vtd])
                        elif Prob_calc>0.01:
                            result_list_3sigma.append([vtb,vts,vtd])
                    elif str_method == "dchi2":
                        if (tmp_chi2-Min_chi2)<delta_chi2_cut_68:
                            result_list_1sigma.append([vtb,vts,vtd])
                            result_list_2sigma.append([vtb,vts,vtd])
                            result_list_3sigma.append([vtb,vts,vtd])
                        elif (tmp_chi2-Min_chi2)<delta_chi2_cut_95:
                            result_list_2sigma.append([vtb,vts,vtd])
                            result_list_3sigma.append([vtb,vts,vtd])
                        elif (tmp_chi2-Min_chi2)<delta_chi2_cut_99:
                            result_list_3sigma.append([vtb,vts,vtd])
                    else:
                        print "wrong!!!"
                        exit()
    Prob_sum=sum(ma_Prob)
#    print ma_Prob
    print Prob_sum
    Vtb_marg=[]
    Vts_marg=[]
    Vtd_marg=[]
    Limit_CL=float(0.68)
    if marginlized:
        Vtb_dict={}
        Vts_dict={}
        Vtd_dict={}
        for vtb in vtb_array1: 
            if vtb not in Vtb_dict:
                Vtb_dict[vtb]=0
            for iv in enumerate(ma_Vtb):
                if vtb==iv[1]:Vtb_dict[vtb]=Vtb_dict[vtb]+ma_Prob[iv[0]]/Prob_sum
        for vts in vts_array1: 
            if vts not in Vts_dict:
                Vts_dict[vts]=0
            for iv in enumerate(ma_Vts):
                if vts==iv[1]:Vts_dict[vts]=Vts_dict[vts]+ma_Prob[iv[0]]/Prob_sum
        for vtd in vtd_array1: 
            if vtd not in Vtd_dict:
                Vtd_dict[vtd]=0
            for iv in enumerate(ma_Vtd):
                if vtd==iv[1]:Vtd_dict[vtd]=Vtd_dict[vtd]+ma_Prob[iv[0]]/Prob_sum
                    #print "vtd:%f,index:%f,ma_prob:%e,sum:%e,prob:%e"%(iv[1],iv[0],ma_Prob[iv[0]],Prob_sum,ma_Prob[iv[0]]/Prob_sum)
        #print Vtd_dict       
        tmp_dir="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/limit_out/"
        plot_dicti(Vtb_dict,str_type+"_"+str_cat+str_lumi+"_"+"prob_vtb")    
        plot_dicti(Vts_dict,str_type+"_"+str_cat+str_lumi+"_"+"prob_vts")    
        plot_dicti(Vtd_dict,str_type+"_"+str_cat+str_lumi+"_"+"prob_vtd")    
        #Vtb_marg=margin_value(Vtb_dict,"Vtb",0.95)
        #Vts_marg=margin_value(Vts_dict,"Vts",0.95)
        #Vtd_marg=margin_value(Vtd_dict,"Vtd",0.95)
        Vtb_marg=margin_value_v1(Vtb_dict,"Vtb",Limit_CL)
        Vts_marg=margin_value_v1(Vts_dict,"Vts",Limit_CL)
        Vtd_marg=margin_value_v1(Vtd_dict,"Vtd",Limit_CL)
        print "marg Vtb best fit:%f,low:%f,up:%f"%(Vtb_marg[0],Vtb_marg[1],Vtb_marg[2])
        print "marg Vts best fit:%f,low:%f,up:%f"%(Vts_marg[0],Vts_marg[1],Vts_marg[2])
        print "marg Vtd best fit:%f,low:%f,up:%f"%(Vtd_marg[0],Vtd_marg[1],Vtd_marg[2])

    VtbVts_1sigma=SigmaBand(result_list_1sigma, "VtbVts")
    VtbVtd_1sigma=SigmaBand(result_list_1sigma, "VtbVtd")
    VtsVtd_1sigma=SigmaBand(result_list_1sigma, "VtsVtd")
    VtbVts_2sigma=SigmaBand(result_list_2sigma, "VtbVts")
    VtbVtd_2sigma=SigmaBand(result_list_2sigma, "VtbVtd")
    VtsVtd_2sigma=SigmaBand(result_list_2sigma, "VtsVtd")
    VtbVts_3sigma=SigmaBand(result_list_3sigma, "VtbVts")
    VtbVtd_3sigma=SigmaBand(result_list_3sigma, "VtbVtd")
    VtsVtd_3sigma=SigmaBand(result_list_3sigma, "VtsVtd")
#    print VtbVts_1sigma
#    print VtbVtd_1sigma
#    print VtsVtd_1sigma
#    print VtbVts_2sigma
#    print VtbVtd_2sigma
#    print VtsVtd_2sigma
    Vtb_limit_up  =np.array(VtbVts_1sigma[0]).max() 
    Vtb_limit_down=np.array(VtbVts_1sigma[0]).min() 
    Vts_limit_up  =np.array(VtsVtd_1sigma[0]).max() 
    Vts_limit_down=np.array(VtsVtd_1sigma[0]).min() 
    Vtd_limit_up  =np.array(VtbVtd_1sigma[1]).max() 
    Vtd_limit_down=np.array(VtbVtd_1sigma[1]).min() 
    if Limit_CL==float(0.68):
        Vtb_limit_up  =np.array(VtbVts_1sigma[0]).max() 
        Vtb_limit_down=np.array(VtbVts_1sigma[0]).min() 
        Vts_limit_up  =np.array(VtsVtd_1sigma[0]).max() 
        Vts_limit_down=np.array(VtsVtd_1sigma[0]).min() 
        Vtd_limit_up  =np.array(VtbVtd_1sigma[1]).max() 
        Vtd_limit_down=np.array(VtbVtd_1sigma[1]).min() 
    elif Limit_CL==float(0.95):
        Vtb_limit_up  =np.array(VtbVts_2sigma[0]).max() 
        Vtb_limit_down=np.array(VtbVts_2sigma[0]).min() 
        Vts_limit_up  =np.array(VtsVtd_2sigma[0]).max() 
        Vts_limit_down=np.array(VtsVtd_2sigma[0]).min() 
        Vtd_limit_up  =np.array(VtbVtd_2sigma[1]).max() 
        Vtd_limit_down=np.array(VtbVtd_2sigma[1]).min() 
    else:print "wrong C.L."
    Vtb_best.append(best_fit[0])
    Vts_best.append(best_fit[1])
    Vtd_best.append(best_fit[2])


    if indiv_Vtb:
        Vtx_x.append(best_fit[0])
        Vtx_y.append(0.4)
        Vtx_xel.append(best_fit[0]-Vtb_limit_down)
        Vtx_xeh.append(Vtb_limit_up-best_fit[0])
        Vtx_yel.append(0)
        Vtx_yeh.append(0)
        print "Vtb=%f+%f-%f"%(Vtx_x[0],Vtx_xeh[0],Vtx_xel[0])
        print "max_probe=%f"%(max_Prob)
        print "min_chi2 =%f"%(min_chi2)
    elif indiv_Vts:
        Vtx_x.append(best_fit[1])
        Vtx_y.append(1.4)
        Vtx_xel.append(best_fit[1]-Vts_limit_down)
        Vtx_xeh.append(Vts_limit_up-best_fit[1])
        Vtx_yel.append(0)
        Vtx_yeh.append(0)
        print "Vts=%f+%f-%f"%(Vtx_x[0],Vtx_xeh[0],Vtx_xel[0])
        print "max_probe=%f"%(max_Prob)
        print "min_chi2 =%f"%(min_chi2)
    elif indiv_Vtd:
        Vtx_x.append(best_fit[2])
        Vtx_y.append(2.4)
        Vtx_xel.append(best_fit[2]-Vtd_limit_down)
        Vtx_xeh.append(Vtd_limit_up-best_fit[2])
        Vtx_yel.append(0)
        Vtx_yeh.append(0)
        print "Vtd=%f+%f-%f"%(Vtx_x[0],Vtx_xeh[0],Vtx_xel[0])
        print "max_probe=%f"%(max_Prob)
        print "min_chi2 =%f"%(min_chi2)
    elif marginlized:
        Vtx_x.append(Vtb_marg[0])
        Vtx_x.append(Vts_marg[0])
        Vtx_x.append(Vtd_marg[0])
        Vtx_y.append(0.4)
        Vtx_y.append(1.4)
        Vtx_y.append(2.4)
        Vtx_xel.append(Vtb_marg[0]-Vtb_marg[1])
        Vtx_xel.append(Vts_marg[0]-Vts_marg[1])
        Vtx_xel.append(Vtd_marg[0]-Vtd_marg[1])
        Vtx_xeh.append(Vtb_marg[2]-Vtb_marg[0])
        Vtx_xeh.append(Vts_marg[2]-Vts_marg[0])
        Vtx_xeh.append(Vtd_marg[2]-Vtd_marg[0])
        Vtx_yel.append(0)
        Vtx_yel.append(0)
        Vtx_yel.append(0)
        Vtx_yeh.append(0)
        Vtx_yeh.append(0)
        Vtx_yeh.append(0)
        print "Vtb=%f+%f-%f,Vts=%f+%f-%f,Vtd=%f+%f-%f"%(Vtx_x[0],Vtx_xeh[0],Vtx_xel[0],Vtx_x[1],Vtx_xeh[1],Vtx_xel[1],Vtx_x[2],Vtx_xeh[2],Vtx_xel[2])
        print "max_probe=%f"%(max_Prob)
        print "min_chi2 =%f"%(min_chi2)
    else:
        Vtx_x.append(best_fit[0])
        Vtx_x.append(best_fit[1])
        Vtx_x.append(best_fit[2])
        Vtx_y.append(0.4)
        Vtx_y.append(1.4)
        Vtx_y.append(2.4)
        Vtx_xel.append(best_fit[0]-Vtb_limit_down)
        Vtx_xel.append(best_fit[1]-Vts_limit_down)
        Vtx_xel.append(best_fit[2]-Vtd_limit_down)
        Vtx_xeh.append(Vtb_limit_up-best_fit[0])
        Vtx_xeh.append(Vts_limit_up-best_fit[1])
        Vtx_xeh.append(Vtd_limit_up-best_fit[2])
        Vtx_yel.append(0)
        Vtx_yel.append(0)
        Vtx_yel.append(0)
        Vtx_yeh.append(0)
        Vtx_yeh.append(0)
        Vtx_yeh.append(0)
        print "Vtb=%f+%f-%f,Vts=%f+%f-%f,Vtd=%f+%f-%f"%(Vtx_x[0],Vtx_xeh[0],Vtx_xel[0],Vtx_x[1],Vtx_xeh[1],Vtx_xel[1],Vtx_x[2],Vtx_xeh[2],Vtx_xel[2])
        print "max_probe=%f"%(max_Prob)
        print "min_chi2 =%f"%(min_chi2)
    ############ graph for out#############
    str_fix_R = "_R"+str(Fixed_R) if do_Fix_R else ""
    gr_VtbVtsVtd=ROOT.TGraphAsymmErrors(int(len(Vtx_x)),Vtx_x,Vtx_y,Vtx_xel,Vtx_xeh,Vtx_yel,Vtx_yeh)
    gr_VtbVtsVtd.SetName("%s%s_old_marginalized"%(icat,str_lumi))
    if indiv_Vtb:
        gr_VtbVtsVtd.SetName("%s%s_individual_Vtb"%(icat,str_lumi))
    elif indiv_Vts:
        gr_VtbVtsVtd.SetName("%s%s_individual_Vts"%(icat,str_lumi))
    elif indiv_Vtd:
        gr_VtbVtsVtd.SetName("%s%s_individual_Vtd"%(icat,str_lumi))
    elif marginlized:
        gr_VtbVtsVtd.SetName("%s%s_correct_marginal"%(icat,str_lumi))
    if indiv_Vtb or indiv_Vts or indiv_Vtd or marginlized:
        F_out=ROOT.TFile("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/limit_out/FixR1_limit_1D_%s_%s%s_%s%s.root"%(str_method,icat,str_lumi,str_type,str_fix_R),"UPDATE")
        F_out.cd()
        gr_VtbVtsVtd.Write("",ROOT.TObject.kOverwrite)
        F_out.Close()
        exit()###stop here
    gr_VtbVts_best=ROOT.TGraph(int(1),Vtb_best,Vts_best)
    gr_VtbVtd_best=ROOT.TGraph(int(1),Vtb_best,Vtd_best)
    gr_VtsVtd_best=ROOT.TGraph(int(1),Vts_best,Vtd_best)
    gr_VtbVts_1s=ROOT.TGraph(len(VtbVts_1sigma[0]),np.array(VtbVts_1sigma[0]),np.array(VtbVts_1sigma[1]))
    gr_VtbVtd_1s=ROOT.TGraph(len(VtbVtd_1sigma[0]),np.array(VtbVtd_1sigma[0]),np.array(VtbVtd_1sigma[1]))
    gr_VtsVtd_1s=ROOT.TGraph(len(VtsVtd_1sigma[0]),np.array(VtsVtd_1sigma[0]),np.array(VtsVtd_1sigma[1]))
    gr_VtbVts_2s=ROOT.TGraph(len(VtbVts_2sigma[0]),np.array(VtbVts_2sigma[0]),np.array(VtbVts_2sigma[1]))
    gr_VtbVtd_2s=ROOT.TGraph(len(VtbVtd_2sigma[0]),np.array(VtbVtd_2sigma[0]),np.array(VtbVtd_2sigma[1]))
    gr_VtsVtd_2s=ROOT.TGraph(len(VtsVtd_2sigma[0]),np.array(VtsVtd_2sigma[0]),np.array(VtsVtd_2sigma[1]))
    gr_VtbVts_3s=ROOT.TGraph(len(VtbVts_3sigma[0]),np.array(VtbVts_3sigma[0]),np.array(VtbVts_3sigma[1]))
    gr_VtbVtd_3s=ROOT.TGraph(len(VtbVtd_3sigma[0]),np.array(VtbVtd_3sigma[0]),np.array(VtbVtd_3sigma[1]))
    gr_VtsVtd_3s=ROOT.TGraph(len(VtsVtd_3sigma[0]),np.array(VtsVtd_3sigma[0]),np.array(VtsVtd_3sigma[1]))
################ save it for comparation ############################################
    gr_VtbVts_best.SetName("VtbVts_best")
    gr_VtbVtd_best.SetName("VtbVtd_best")
    gr_VtsVtd_best.SetName("VtsVtd_best")
    gr_VtbVts_1s  .SetName("VtbVts_1s")
    gr_VtbVtd_1s  .SetName("VtbVtd_1s")
    gr_VtsVtd_1s  .SetName("VtsVtd_1s")
    gr_VtbVts_2s  .SetName("VtbVts_2s")
    gr_VtbVtd_2s  .SetName("VtbVtd_2s")
    gr_VtsVtd_2s  .SetName("VtsVtd_2s")
    gr_VtbVts_3s  .SetName("VtbVts_3s")
    gr_VtbVtd_3s  .SetName("VtbVtd_3s")
    gr_VtsVtd_3s  .SetName("VtsVtd_3s")
    f_out=ROOT.TFile("/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/limit_out/FixR1_limit_2D_%s_%s%s_%s%s.root"%(str_method,icat,str_lumi,str_type,str_fix_R),"UPDATE")
    f_out.cd()
    gr_VtbVts_best.Write("",ROOT.TObject.kOverwrite)
    gr_VtbVtd_best.Write("",ROOT.TObject.kOverwrite)
    gr_VtsVtd_best.Write("",ROOT.TObject.kOverwrite)
    gr_VtbVts_1s  .Write("",ROOT.TObject.kOverwrite)
    gr_VtbVtd_1s  .Write("",ROOT.TObject.kOverwrite)
    gr_VtsVtd_1s  .Write("",ROOT.TObject.kOverwrite)
    gr_VtbVts_2s  .Write("",ROOT.TObject.kOverwrite)
    gr_VtbVtd_2s  .Write("",ROOT.TObject.kOverwrite)
    gr_VtsVtd_2s  .Write("",ROOT.TObject.kOverwrite)
    gr_VtbVts_3s  .Write("",ROOT.TObject.kOverwrite)
    gr_VtbVtd_3s  .Write("",ROOT.TObject.kOverwrite)
    gr_VtsVtd_3s  .Write("",ROOT.TObject.kOverwrite)
    f_out.Close()
################ Draw ############################################
    if False:
        gr_dicti={}
        gr_dicti["VtbVts"]=[gr_VtbVts_best,gr_VtbVts_1s,gr_VtbVts_2s,gr_VtbVts_3s]
        gr_dicti["VtbVtd"]=[gr_VtbVtd_best,gr_VtbVtd_1s,gr_VtbVtd_2s,gr_VtbVtd_3s]
        gr_dicti["VtsVtd"]=[gr_VtsVtd_best,gr_VtsVtd_1s,gr_VtsVtd_2s,gr_VtsVtd_3s]
        for igr in gr_dicti:
            canvas = ROOT.TCanvas('canvas','',900, 600)
            canvas.cd()
            canvas.SetTickx()
            canvas.SetTicky()
            canvas.SetBottomMargin(0.17)
            canvas.SetLeftMargin(0.15)
            y_min=0
            y_max=1
            x_min=0
            x_max=1
            x_title=""
            y_title=""
            if igr == "VtbVts":
                x_min=Vtb_low
                x_max=Vtb_up
                y_min=Vts_low
                y_max=Vts_up
                x_title="|V_{tb}|"
                y_title="|V_{ts}|"
            elif igr == "VtbVtd":
                x_min=Vtb_low
                x_max=Vtb_up
                y_min=Vtd_low
                y_max=Vtd_up
                x_title="|V_{tb}|"
                y_title="|V_{td}|"
            elif igr == "VtsVtd":
                x_min=Vts_low
                x_max=Vts_up
                y_min=Vtd_low
                y_max=Vtd_up
                x_title="|V_{ts}|"
                y_title="|V_{td}|"
            dummy = ROOT.TH2D("dummy","",1,x_min,x_max,1,y_min,y_max)
            dummy.SetStats(ROOT.kFALSE)
            dummy.GetYaxis().SetTitle("%s"%y_title)
            dummy.GetXaxis().SetTitle("%s"%x_title)
            dummy.GetXaxis().SetTitleSize(0.07)
            dummy.GetYaxis().SetTitleSize(0.07)
            dummy.GetYaxis().SetLabelSize(0.06)
            dummy.GetXaxis().SetLabelSize(0.06)
            dummy.GetYaxis().SetLabelOffset(0.01)
            dummy.GetXaxis().SetLabelOffset(0.015)
            dummy.GetYaxis().SetTitleOffset(1)
            dummy.GetXaxis().SetTitleOffset(1)
            dummy.GetXaxis().SetMoreLogLabels()
            dummy.GetXaxis().SetNoExponent()
            dummy.GetXaxis().CenterTitle()
            dummy.GetYaxis().CenterTitle()
            dummy.Draw()
            gr_dicti[igr][0].SetMarkerColor(ROOT.TColor.GetColor("#ff00ff"))
            gr_dicti[igr][0].SetFillColor  (ROOT.TColor.GetColor("#ff00ff"))
            gr_dicti[igr][0].SetLineColor  (ROOT.TColor.GetColor("#ff00ff"))
            gr_dicti[igr][0].SetMarkerStyle(22)
            gr_dicti[igr][0].SetMarkerSize(1.5)
            gr_dicti[igr][1].SetMarkerColor(ROOT.TColor.GetColor("#0000ff"))
            gr_dicti[igr][1].SetFillColor  (ROOT.TColor.GetColor("#0000ff"))
            gr_dicti[igr][1].SetLineColor  (ROOT.TColor.GetColor("#0000ff"))
            gr_dicti[igr][1].SetMarkerStyle(8)
            gr_dicti[igr][2].SetMarkerColor(ROOT.TColor.GetColor("#00ffff"))
            gr_dicti[igr][2].SetFillColor  (ROOT.TColor.GetColor("#00ffff"))
            gr_dicti[igr][2].SetLineColor  (ROOT.TColor.GetColor("#00ffff"))
            gr_dicti[igr][2].SetMarkerStyle(8)
            gr_dicti[igr][3].SetMarkerColor(ROOT.TColor.GetColor("#ffa500"))
            gr_dicti[igr][3].SetFillColor  (ROOT.TColor.GetColor("#ffa500"))
            gr_dicti[igr][3].SetLineColor  (ROOT.TColor.GetColor("#ffa500"))
            gr_dicti[igr][3].SetMarkerStyle(8)
            gr_dicti[igr][3].Draw("F")
            gr_dicti[igr][2].Draw("F")
            gr_dicti[igr][1].Draw("F")
            gr_dicti[igr][0].Draw("p")
            dummy.Draw("AXISSAME")
            legend = ROOT.TLegend(0.7,0.66,0.85,0.85)
            legend.AddEntry(gr_dicti[igr][0],'best-fit','p')
            legend.AddEntry(gr_dicti[igr][1],'68%','f')
            legend.AddEntry(gr_dicti[igr][2],'95%','f')
            legend.AddEntry(gr_dicti[igr][3],'99%','f')
            legend.SetBorderSize(0)
            legend.SetTextFont(42)
            legend.SetTextSize(0.06)
            legend.Draw()
            canvas.Print('/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/limit_plot/%s_%s%s_%s_%s.png'%(str_method,icat,str_lumi,igr,str_type)) 
            del canvas
            gc.collect()
        print "saved limit plot"
