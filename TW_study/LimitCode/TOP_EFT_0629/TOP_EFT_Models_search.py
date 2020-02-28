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
        self.modelBuilder.doVar("r[0.,-10,10]") 
        poi = "r"

        self.modelBuilder.factory_( "expr::TW_s_func(\"(1)+(@0)*%f + pow(@0,2)*%f + %f \", r)"%(self.TW_AinttoAsm,self.TW_AbsmtoAsm,self.TW_AsmnlomlotoAlo))

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
        self.modelBuilder.doVar("r[0.,-10,10]") 
        poi = "r"

        self.modelBuilder.factory_( "expr::TW_s_func(\"(1)+(@0)*%f + pow(@0,2)*%f + %f \", r)"%(self.TW_AinttoAsm,self.TW_AbsmtoAsm,self.TW_AsmnlomlotoAlo))
        self.modelBuilder.factory_( "expr::TT_s_func(\"(1)+(@0)*%f + pow(@0,2)*%f + %f \", r)"%(self.TT_AinttoAsm,self.TT_AbsmtoAsm,self.TT_AsmnnlomnlotoAnlo))

        self.modelBuilder.doSet("POI",poi)

class TopEFT_TT(PhysicsModel):
    def __init__(self, TT_AinttoAsm, TT_AbsmtoAsm, TT_AsmnnlomnlotoAnlo):
        self.poiMap = []
        self.pois = {}
        self.verbose = False
        self.TT_AinttoAsm         = float(TT_AinttoAsm)
        self.TT_AbsmtoAsm         = float(TT_AbsmtoAsm)
        self.TT_AsmnnlomnlotoAnlo = float(TT_AsmnnlomnlotoAnlo)
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

        self.modelBuilder.factory_( "expr::TT_s_func(\"(1)+(@0)*%f + pow(@0,2)*%f + %f \", r)"%(self.TT_AinttoAsm,self.TT_AbsmtoAsm,self.TT_AsmnnlomnlotoAnlo))

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

Model_Ctw  =TopEFT_TW(-4.45*1.27/55.24,1*1.18/55.24   ,(71.7-55.24)/55.24)
Model_Cphiq=TopEFT_TW(  6.7*1.32/55.24,0.21*1.31/55.24,(71.7-55.24)/55.24)
Model_Ctg  =TopEFT_TWTT( 6.65*1.27*0.5/55.24,4.99*1.06*0.25/55.24,(71.7-55.24)/55.24,405.66*0.5/730.7,94.18*0.25/730.7,(831.76-730.7)/730.7)
Model_Cg   =TopEFT_TT(25.33/730.7,80.3/730.7,(831.76-730.7)/730.7)
Model_Cphig=TopEFT_TT(25.33/730.7,80.3/730.7,(831.76-730.7)/730.7)

Model_FCNC=TopEFT_FCNC()
