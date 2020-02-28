import os

def get_value(chan_region,coulp,sf,opposite):
    opp="" if opposite==False else "_opposite"
    TW=0
    TWNLO=0
    TWSignal=0
    TWSignalonly=0
    TT=0
    TTNNLO=0
    TTSignal=0
    TTSignalonly=0
    f_info = open(info_path+"info.txt",'r')
    lines = f_info.readlines()
    for ic in chan_region:
        name=str(ic)+"_"+str(coulp)+"_"+str(sf)+opp
        for li in lines:
            li =li.strip('\n')
            if name in li:
                if (name+"_TW:") in li :
                    TW=float(TW)+float(li.split(":")[-1])
                elif (name+"_TWNLO:") in li:
                    TWNLO=float(TWNLO)+float(li.split(":")[-1])
                elif (name+"_TWSignal:") in li:
                    TWSignal=float(TWSignal)+float(li.split(":")[-1])
                elif (name+"_TWSignalonly:") in li:
                    TWSignalonly=float(TWSignalonly)+float(li.split(":")[-1])
                elif (name+"_TT:") in li :
                    TT=float(TT)+float(li.split(":")[-1])
                elif (name+"_TTNNLO:") in li:
                    TTNNLO=float(TTNNLO)+float(li.split(":")[-1])
                elif (name+"_TTSignal:") in li:
                    TTSignal=float(TTSignal)+float(li.split(":")[-1])
                elif (name+"_TTSignalonly:") in li:
                    TTSignalonly=float(TTSignalonly)+float(li.split(":")[-1])
    TW_AbsmtoAsm        =0 if float(TW)==0 else float(TWSignalonly/TW)
    TW_AbsmpsmtoAsm     =0 if float(TW)==0 else float(TWSignal    /TW) 
    TW_AsmnlomlotoAlo   =0 if float(TW)==0 else float(TWNLO       /TW) 
    TT_AbsmtoAsm        =0 if float(TT)==0 else float(TTSignalonly/TT)
    TT_AbsmpsmtoAsm     =0 if float(TT)==0 else float(TTSignal    /TT)
    TT_AsmnnlomnlotoAnlo=0 if float(TT)==0 else float(TTNNLO      /TT)
#    if(str(ic)+"_"+str(coulp)+"_"+str(sf)+opp)== "ee_1jet_1bjet_Ctg_1.00_opposite":
#    if chan_region == ["emu_1jet_0bjet","emu_1jet_1bjet","emu_2jet_1bjet","emu_2jet_2bjet"]:
#        print "%s, %s, %s, TT:%s, TTSignal:%s"%(str(coulp),str(sf),str(opp),str(TT),str(TTSignal))
    return [TW_AbsmtoAsm,TW_AbsmpsmtoAsm,TW_AsmnlomlotoAlo,TT_AbsmtoAsm,TT_AbsmpsmtoAsm,TT_AsmnnlomnlotoAnlo]

template_model='''
from HiggsAnalysis.CombinedLimit.PhysicsModel import *
class TopEFT_TW(PhysicsModel):
    def __init__(self, TW_AbsmtoAsm, TW_AbsmpsmtoAsm, TW_AsmnlomlotoAlo):
        self.poiMap = []
        self.pois = {}
        self.verbose = False
        self.TW_AbsmtoAsm      = TW_AbsmtoAsm
        self.TW_AbsmpsmtoAsm   = TW_AbsmpsmtoAsm
        self.TW_AsmnlomlotoAlo = TW_AsmnlomlotoAlo
    def setModelBuilder(self, modelBuilder):
        PhysicsModel.setModelBuilder(self,modelBuilder)
        self.modelBuilder.doModelBOnly = False
 
    def getYieldScale(self,bin,process):
        if process == "TW": return "TW_s_func"
        else:
            return 1

    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""
        self.modelBuilder.doVar("CMS_TW_mu[0.,0.,100.0]") 
        poi = "CMS_TW_mu"

        self.modelBuilder.factory_( "expr::TW_s_func(\\"(1-sqrt(@0))+(@0-sqrt(@0))*%f + sqrt(@0)*%f + %f \\", CMS_TW_mu)"%(self.TW_AbsmtoAsm,self.TW_AbsmpsmtoAsm,self.TW_AsmnlomlotoAlo))

        self.modelBuilder.doSet("POI",poi)
       
class TopEFT_TWTT(PhysicsModel):
    def __init__(self, TW_AbsmtoAsm, TW_AbsmpsmtoAsm, TW_AsmnlomlotoAlo, TT_AbsmtoAsm, TT_AbsmpsmtoAsm, TT_AsmnnlomnlotoAnlo):
        self.poiMap = []
        self.pois = {}
        self.verbose = False
        self.TW_AbsmtoAsm         =TW_AbsmtoAsm        
        self.TW_AbsmpsmtoAsm      =TW_AbsmpsmtoAsm     
        self.TW_AsmnlomlotoAlo    =TW_AsmnlomlotoAlo   
        self.TT_AbsmtoAsm         =TT_AbsmtoAsm        
        self.TT_AbsmpsmtoAsm      =TT_AbsmpsmtoAsm     
        self.TT_AsmnnlomnlotoAnlo =TT_AsmnnlomnlotoAnlo
    def setModelBuilder(self, modelBuilder):
        PhysicsModel.setModelBuilder(self,modelBuilder)
        self.modelBuilder.doModelBOnly = False
 
    def getYieldScale(self,bin,process):
        if process == "TW": return "TW_s_func"
        elif process == "TT": return "TT_s_func"
        else:
            return 1

    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""
        self.modelBuilder.doVar("CMS_TWTT_mu[0.,0.,100.0]") 
        poi = "CMS_TWTT_mu"

        self.modelBuilder.factory_( "expr::TW_s_func(\\"(1-sqrt(@0))+(@0-sqrt(@0))*%f + sqrt(@0)*%f + %f \\", CMS_TWTT_mu)"%(self.TW_AbsmtoAsm,self.TW_AbsmpsmtoAsm,self.TW_AsmnlomlotoAlo))
        self.modelBuilder.factory_( "expr::TT_s_func(\\"(1-sqrt(@0))+(@0-sqrt(@0))*%f + sqrt(@0)*%f + %f\\", CMS_TWTT_mu)"%(self.TT_AbsmtoAsm,self.TT_AbsmpsmtoAsm,self.TT_AsmnnlomnlotoAnlo))

        self.modelBuilder.doSet("POI",poi)
'''

info_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/"


file_in=open("TOP_EFT_Models.py","w")
file_in.write("import os \n")
file_in.write(template_model)
region={}
region["ee"]   =["ee_1jet_1bjet","ee_2jet_1bjet","ee_2jet_2bjet"]
region["emu"]  =["emu_1jet_0bjet","emu_1jet_1bjet","emu_2jet_1bjet","emu_2jet_2bjet"]
region["mumu"] =["mumu_1jet_1bjet","mumu_2jet_1bjet","mumu_2jet_2bjet"]

#region["ee"]   =["ee_1jet_1bjet"]
#region["emu"]  =["emu_1jet_1bjet"]
#region["mumu"] =["mumu_1jet_1bjet"]


combined=[]
combined.extend(region["ee"])
combined.extend(region["emu"])
combined.extend(region["mumu"])
region["combined"]=combined
for chan in ["ee","emu","mumu","combined"]:
    for ic in ["Ctw","Ctg","Cphiq"]:
        for sf in ["1.00", "0.05", "0.10", "0.15", "0.20", "0.25", "0.30","0.02","0.50"]:
            for do_opposite in [True,False]:
                str_opp=""if do_opposite==False else "_opposite"
                if ic == "Ctg":
                    if chan == "combined":
                        for ir in region[chan]:
                            chan_region_list=[str(ir)]
                            value=get_value(chan_region_list,ic,sf,do_opposite)
                            model_name_1=ir+"_"+str(ic)+"_"+str(sf)+str_opp
                            model_name=model_name_1.replace(".","p")
                            str_model="TWTT_%s=TopEFT_TWTT(%s,%s,%s,%s,%s,%s)"%(str(model_name),str(value[0]),str(value[1]),str(value[2]),str(value[3]),str(value[4]),str(value[5]))
                            file_in.write(str_model+"\n")
                        value=get_value(region[chan],ic,sf,do_opposite)
                        model_name_1="combined_"+str(ic)+"_"+str(sf)+str_opp
                        model_name=model_name_1.replace(".","p")
                        str_model="TWTT_%s=TopEFT_TWTT(%s,%s,%s,%s,%s,%s)"%(str(model_name),str(value[0]),str(value[1]),str(value[2]),str(value[3]),str(value[4]),str(value[5]))
                        file_in.write(str_model+"\n")
                    else:       
                        value=get_value(region[chan],ic,sf,do_opposite)
                        model_name_1="%s_"%(str(chan))+str(ic)+"_"+str(sf)+str_opp
                        model_name=model_name_1.replace(".","p")
                        str_model="TWTT_%s=TopEFT_TWTT(%s,%s,%s,%s,%s,%s)"%(str(model_name),str(value[0]),str(value[1]),str(value[2]),str(value[3]),str(value[4]),str(value[5]))
                        file_in.write(str_model+"\n")
                        
                else:
                    if chan == "combined":
                        for ir in region[chan]:
                            chan_region_list=[str(ir)]
                            value=get_value(chan_region_list,ic,sf,do_opposite)
                            model_name_1=ir+"_"+str(ic)+"_"+str(sf)+str_opp
                            model_name=model_name_1.replace(".","p")
                            str_model="TW_%s=TopEFT_TW(%s,%s,%s)"%(str(model_name),str(value[0]),str(value[1]),str(value[2]))
                            file_in.write(str_model+"\n")
                        value=get_value(region[chan],ic,sf,do_opposite)
                        model_name_1="combined_"+str(ic)+"_"+str(sf)+str_opp
                        model_name=model_name_1.replace(".","p")
                        str_model="TW_%s=TopEFT_TW(%s,%s,%s)"%(str(model_name),str(value[0]),str(value[1]),str(value[2]))
                        file_in.write(str_model+"\n")
                    else:       
                        value=get_value(region[chan],ic,sf,do_opposite)
                        model_name_1="%s_"%(str(chan))+str(ic)+"_"+str(sf)+str_opp
                        model_name=model_name_1.replace(".","p")
                        str_model="TW_%s=TopEFT_TW(%s,%s,%s)"%(str(model_name),str(value[0]),str(value[1]),str(value[2]))
                        file_in.write(str_model+"\n")

print "done!"

