import os 
import math
from HiggsAnalysis.CombinedLimit.PhysicsModel import *
class TopEFT_TW(PhysicsModel):
    def __init__(self, TW_Constant ,TW_AinttoAsm, TW_AbsmtoAsm):
        self.poiMap = []
        self.pois = {}
        self.verbose = False
        self.TW_Constant       = float(TW_Constant)
        self.TW_AinttoAsm      = float(TW_AinttoAsm)
        self.TW_AbsmtoAsm      = float(TW_AbsmtoAsm)
    def setModelBuilder(self, modelBuilder):
        PhysicsModel.setModelBuilder(self,modelBuilder)
        self.modelBuilder.doModelBOnly = False
 
    def getYieldScale(self,bin,process):
        if process == "TW": return "TW_s_func"
        else:
            return 1

    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""
        self.modelBuilder.doVar("r[0.,-10,10]") 
        poi = "r"

        self.modelBuilder.factory_( "expr::TW_s_func(\"(%f)+(@0)*%f + pow(@0,2)*%f  \", r)"%(self.TW_Constant,self.TW_AinttoAsm,self.TW_AbsmtoAsm))

        self.modelBuilder.doSet("POI",poi)
       
class TopEFT_TWTT(PhysicsModel):
    def __init__(self, TW_Constant,TW_AinttoAsm, TW_AbsmtoAsm,TT_Constant ,TT_AinttoAsm, TT_AbsmtoAsm):
        self.poiMap = []
        self.pois = {}
        self.verbose = False
        self.TW_Constant          = float(TW_Constant)
        self.TW_AinttoAsm         = float(TW_AinttoAsm)
        self.TW_AbsmtoAsm         = float(TW_AbsmtoAsm)
        self.TT_Constant          = float(TT_Constant)
        self.TT_AinttoAsm         = float(TT_AinttoAsm)
        self.TT_AbsmtoAsm         = float(TT_AbsmtoAsm)
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
        self.modelBuilder.doVar("r[0.,-10,10]") 
        poi = "r"

        self.modelBuilder.factory_( "expr::TW_s_func(\"(%f)+(@0)*%f + pow(@0,2)*%f \", r)"%(self.TW_Constant,self.TW_AinttoAsm,self.TW_AbsmtoAsm))
        self.modelBuilder.factory_( "expr::TT_s_func(\"(%f)+(@0)*%f + pow(@0,2)*%f \", r)"%(self.TT_Constant,self.TT_AinttoAsm,self.TT_AbsmtoAsm))

        self.modelBuilder.doSet("POI",poi)

class TopEFT_TT(PhysicsModel):
    def __init__(self, TT_Constant,TT_AinttoAsm, TT_AbsmtoAsm):
        self.poiMap = []
        self.pois = {}
        self.verbose = False
        self.TT_Constant          = float(TT_Constant)
        self.TT_AinttoAsm         = float(TT_AinttoAsm)
        self.TT_AbsmtoAsm         = float(TT_AbsmtoAsm)
    def setModelBuilder(self, modelBuilder):
        PhysicsModel.setModelBuilder(self,modelBuilder)
        self.modelBuilder.doModelBOnly = False
 
    def getYieldScale(self,bin,process):
        if process == "TT": return "TT_s_func"
        else:
            return 1

    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""
        self.modelBuilder.doVar("r[0.,-10,10]") 
        poi = "r"

        self.modelBuilder.factory_( "expr::TT_s_func(\"(%f)+(@0)*%f + pow(@0,2)*%f \", r)"%(self.TT_Constant,self.TT_AinttoAsm,self.TT_AbsmtoAsm))

        self.modelBuilder.doSet("POI",poi)

class TopEFT_FCNC(PhysicsModel):
    def __init__(self):
        self.poiMap = []
        self.pois = {}
        self.verbose = False
    def setModelBuilder(self, modelBuilder):
        PhysicsModel.setModelBuilder(self,modelBuilder)
        self.modelBuilder.doModelBOnly = False
 
    def getYieldScale(self,bin,process):
        if process == "FCNCSignal": return "FCNC_func"
        else:
            return 1

    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""
        self.modelBuilder.doVar("r[0.,-2,2]") 
        poi = "r"

        self.modelBuilder.factory_( "expr::FCNC_func(\"pow(@0,2)\", r)")

        self.modelBuilder.doSet("POI",poi)
tW_NLO_up  =1+float(math.sqrt(1.8*1.8+3.4*3.4)/71.7)##Qscale + PDF
tW_NLO_down=1-float(math.sqrt(1.8*1.8+3.4*3.4)/71.7)
tW_Ctw_s1Dsmnlo_up  =1+float( 0.00078/-0.053)   
tW_Ctw_s1Dsmnlo_down=1+float(-0.00058/-0.053)
tW_Ctw_s2Dsmnlo_up  =1+float( 0.00022/0.00918)
tW_Ctw_s2Dsmnlo_down=1+float(-0.0002 /0.00918)
tW_Ctg_s1Dsmnlo_up  =1+float( 0.00048/0.0689)
tW_Ctg_s1Dsmnlo_down=1+float(-0.00065/0.0689)
tW_Ctg_s2Dsmnlo_up  =1+float( 0.0013 /0.0308)
tW_Ctg_s2Dsmnlo_down=1+float(-0.00078/0.0308)
tW_Cphiq_s1Dsmnlo_up  =1+float( 0.0/0.119)
tW_Cphiq_s1Dsmnlo_down=1+float(-0.0/0.119)
tW_Cphiq_s2Dsmnlo_up  =1+float( 0.0/0.00357)
tW_Cphiq_s2Dsmnlo_down=1+float(-0.0/0.00357)
tt_NNLO_up  =1+float(math.sqrt(19.77*19.77+35.06*35.06)/831.76)## Qscale + PDF
tt_NNLO_down=1-float(math.sqrt(29.20*29.20+35.06*35.06)/831.76)
tt_Ctg_s1Dsmnnlo_up  =1+float( 0.121)
tt_Ctg_s1Dsmnnlo_down=1+float(-0.133)
tt_Ctg_s2Dsmnnlo_up  =1+float( 0.0/0.0308)
tt_Ctg_s2Dsmnnlo_down=1+float(-0.0/0.0308)


##################### Nominal ##################################################
Model_Ctw  =TopEFT_TW  (1.0,-4.45*1.27/71.7    ,1*1.18/71.7         )
Model_Cphiq=TopEFT_TW  (1.0,  6.7*1.32/71.7    ,0.21*1.31/71.7      )
Model_Ctg  =TopEFT_TWTT(1.0, 6.65*1.27*0.5/71.7,4.99*1.06*0.25/71.7, 1.0,405.66*0.5/831.76,94.18*0.25/831.76)
#Model_Cg   =TopEFT_TT  (1.0, 25.33/831.76      ,80.3/831.76         )
Model_Cg   =TopEFT_TT  (1.0, 31.9/831.76      ,102.3/831.76         )
Model_FCNC=TopEFT_FCNC()

Model_CtgTTOnly  =TopEFT_TT( 1.0, 405.66*0.5/831.76, 94.18*0.25/831.76 )## used for check

##################### Scale up ##################################################
Model_Ctw_up  =TopEFT_TW  (1.0*tW_NLO_up ,tW_Ctw_s1Dsmnlo_up  *-4.45*1.27/71.7    ,tW_Ctw_s2Dsmnlo_up  *1*1.18/71.7         )
Model_Cphiq_up=TopEFT_TW  (1.0*tW_NLO_up ,tW_Cphiq_s1Dsmnlo_up*  6.7*1.32/71.7    ,tW_Cphiq_s2Dsmnlo_up*0.21*1.31/71.7      )
Model_Ctg_up  =TopEFT_TWTT(1.0*tW_NLO_up ,tW_Ctg_s1Dsmnlo_up  * 6.65*1.27*0.5/71.7,tW_Ctg_s2Dsmnlo_up  *4.99*1.06*0.25/71.7, 1.0*tt_NNLO_up,tt_Ctg_s1Dsmnnlo_up*405.66*0.5/831.76,tt_Ctg_s2Dsmnnlo_up*94.18*0.25/831.76)
Model_Cg_up   =TopEFT_TT  (1.0*tt_NNLO_up , 40/831.76      ,125/831.76         )
Model_FCNC_up =TopEFT_FCNC()
##################### Scale down ##################################################
Model_Ctw_down  =TopEFT_TW  (1.0*tW_NLO_down ,tW_Ctw_s1Dsmnlo_down  *-4.45*1.27/71.7    ,tW_Ctw_s2Dsmnlo_down  *1*1.18/71.7         )
Model_Cphiq_down=TopEFT_TW  (1.0*tW_NLO_down ,tW_Cphiq_s1Dsmnlo_down*  6.7*1.32/71.7    ,tW_Cphiq_s2Dsmnlo_down*0.21*1.31/71.7      )
Model_Ctg_down  =TopEFT_TWTT(1.0*tW_NLO_down ,tW_Ctg_s1Dsmnlo_down  * 6.65*1.27*0.5/71.7,tW_Ctg_s2Dsmnlo_down  *4.99*1.06*0.25/71.7, 1.0*tt_NNLO_down,tt_Ctg_s1Dsmnnlo_down*405.66*0.5/831.76,tt_Ctg_s2Dsmnnlo_down*94.18*0.25/831.76)
Model_Cg_down   =TopEFT_TT  (1.0*tt_NNLO_down, 25/831.76      ,87/831.76         )
Model_FCNC_down =TopEFT_FCNC()
