from HiggsAnalysis.CombinedLimit.PhysicsModel import *
 
### This is the base python class to study the Top EFT
 
class FCNC_Model(PhysicsModel):
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
        self.modelBuilder.doVar("CMS_TW_mu[0.,0.,100.0]") 
        poi = "CMS_TW_mu"
        self.modelBuilder.factory_( "expr::FCNC_func(\"@0\", CMS_TW_mu)")
             
        self.modelBuilder.doSet("POI",poi)
       
FCNC = FCNC_Model()
 
