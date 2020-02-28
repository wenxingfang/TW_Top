import os 

from HiggsAnalysis.CombinedLimit.PhysicsModel import *
class TopEFT_TW(PhysicsModel):
    def __init__(self, TW_AinttoAsm, TW_AbsmtoAsm, TW_AsmnlomlotoAlo):
        self.poiMap = []
        self.pois = {}
        self.verbose = False
        self.TW_AinttoAsm      = float(TW_AinttoAsm)
        self.TW_AbsmtoAsm      = float(TW_AbsmtoAsm)
        self.TW_AsmnlomlotoAlo = float(TW_AsmnlomlotoAlo)
    def setModelBuilder(self, modelBuilder):
        PhysicsModel.setModelBuilder(self,modelBuilder)
        self.modelBuilder.doModelBOnly = False
 
    def getYieldScale(self,bin,process):
        if process == "TW": return "TW_s_func"
        else:
            return 1

    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""
        self.modelBuilder.doVar("CMS_TW_mu[0.,-10,10]") 
        poi = "CMS_TW_mu"

        self.modelBuilder.factory_( "expr::TW_s_func(\"(1)+(@0)*%f + pow(@0,2)*%f + %f \", CMS_TW_mu)"%(self.TW_AinttoAsm,self.TW_AbsmtoAsm,self.TW_AsmnlomlotoAlo))

        self.modelBuilder.doSet("POI",poi)
       
class TopEFT_TWTT(PhysicsModel):
    def __init__(self, TW_AinttoAsm, TW_AbsmtoAsm, TW_AsmnlomlotoAlo, TT_AinttoAsm, TT_AbsmtoAsm, TT_AsmnnlomnlotoAnlo):
        self.poiMap = []
        self.pois = {}
        self.verbose = False
        self.TW_AinttoAsm         = float(TW_AinttoAsm)
        self.TW_AbsmtoAsm         = float(TW_AbsmtoAsm)
        self.TW_AsmnlomlotoAlo    = float(TW_AsmnlomlotoAlo)
        self.TT_AinttoAsm         = float(TT_AinttoAsm)
        self.TT_AbsmtoAsm         = float(TT_AbsmtoAsm)
        self.TT_AsmnnlomnlotoAnlo = float(TT_AsmnnlomnlotoAnlo)
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
        self.modelBuilder.doVar("CMS_TWTT_mu[0.,-10,10]") 
        poi = "CMS_TWTT_mu"

        self.modelBuilder.factory_( "expr::TW_s_func(\"(1)+(@0)*%f + pow(@0,2)*%f + %f \", CMS_TWTT_mu)"%(self.TW_AinttoAsm,self.TW_AbsmtoAsm,self.TW_AsmnlomlotoAlo))
        self.modelBuilder.factory_( "expr::TT_s_func(\"(1)+(@0)*%f + pow(@0,2)*%f + %f \", CMS_TWTT_mu)"%(self.TT_AinttoAsm,self.TT_AbsmtoAsm,self.TT_AsmnnlomnlotoAnlo))

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
        self.modelBuilder.doVar("CMS_FCNC_mu[0.,-10,10]") 
        poi = "CMS_FCNC_mu"

        self.modelBuilder.factory_( "expr::FCNC_func(\"pow(@0,2)\", CMS_FCNC_mu)")

        self.modelBuilder.doSet("POI",poi)

Model_Ctw  =TopEFT_TW(-4.45/55.24,1/55.24   ,(71.7-55.24)/55.24)
Model_Cphiq=TopEFT_TW(  6.7/55.24,0.21/55.24,(71.7-55.24)/55.24)
Model_Ctg=TopEFT_TWTT( 6.65/55.24,4.99/55.24,(71.7-55.24)/55.24,405.66/730.7,94.18/730.7,(831.76-730.7)/730.7)

Model_FCNC=TopEFT_FCNC()
