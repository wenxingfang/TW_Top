import os
class card_object:
    def __init__(self,name,coulping,channel,sf,opposite, Dict, out_name):
        self.name=name
        self.coulping=coulping
        self.channel =channel
        self.sf =sf
        self.opposite=opposite
        self.template=''''''
        self.Dict=Dict
        self.out_name=out_name
    def make_template(self):
        if self.coulping == "Ctw" or self.coulping=="Cphiq":
            if "emu" in self.name:
                if "1jet_0bjet" in self.name:
                    self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
---------------------------------------------------------------------------------------------------------
bin                                            %(cname)s        %(cname)s        %(cname)s    %(cname)s       %(cname)s
process                                        0                1                2            3               4              
process                                        TW               TT               DY           other           jets          
rate                                           %(n_TW)s         %(n_TT)s         %(n_DY)s     %(n_other)s     %(n_jets)s       
-------------------------------------------------------------  -------------    ----                                            
Luminosity                         lnN         1.025            1.025            1.025        1.025           -          
TT_normalisation                   lnN         -                1.05             -            -               -               
%(region)s_DY_normalisation        lnN         -                -                1.15         -               -               
Other_normalisation                lnN         -                -                -            1.50            -               
Jets_normalisation                 lnN         -                -                -            -               1.50               
%(chan_region)s_TW_stat_bin1_      shape       1                -                -            -               -
%(chan_region)s_TT_stat_bin1_      shape       -                1                -            -               -
%(chan_region)s_DY_stat_bin1_      shape       -                -                1            -               -
%(chan_region)s_other_stat_bin1_   shape       -                -                -            1               -
PileUp_                            shape       1                1                1            1               -           
TriggerSF_                         shape       1                1                1            1               -           
JetEnergyResolution_               shape       1                1                1            1               -                
JetEnergyScale_                    shape       1                1                1            1               -              
BtagScaleFactor_udsg_              shape       1                1                1            1               -              
BtagScaleFactor_bc_                shape       1                1                1            1               -                 
ElectronIDIsoScaleFactor_          shape       1                1                1            1               -               
ElectronReconstructionScaleFactor_ shape       1                1                1            1               -              
MuonTrackEfficiencyScaleFactor_    shape       1                1                1            1               -             
MuonIDScaleFactor_                 shape       1                1                1            1               -             
MuonIsoScaleFactor_                shape       1                1                1            1               -              
DY_PDF_                            shape       -                -                1            -               -
DY_QCD_                            shape       -                -                1            -               -
TT_Tune_                           shape       -                1                -            -               -
TT_PDF_                            shape       -                1                -            -               -
TT_QCD_                            shape       -                1                -            -               -
TT_CR_                             shape       -                1                -            -               -
FSR_                               shape       1                1                -            -               -
TT_hdamp_                          shape       -                1                -            -               -
ISR_                               shape       1                1                -            -               -
TT_TopMass_                        shape       -                1                -            -               -
tw_DS_                             shape       1                -                -            -               -
tw_MEscale_                        shape       1                -                -            -               -
tw_TopMass_                        shape       1                -                -            -               -
'''
                else:
                    self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
---------------------------------------------------------------------------------------------------------
bin                                            %(cname)s        %(cname)s        %(cname)s    %(cname)s       %(cname)s
process                                        0                1                2            3               4              
process                                        TW               TT               DY           other           jets          
rate                                           %(n_TW)s         %(n_TT)s         %(n_DY)s     %(n_other)s     %(n_jets)s       
-------------------------------------------------------------  -------------    ----                                            
Luminosity                         lnN         1.025            1.025            1.025        1.025           -          
TT_normalisation                   lnN         -                1.05             -            -               -               
%(region)s_DY_normalisation        lnN         -                -                1.50         -               -               
Other_normalisation                lnN         -                -                -            1.50            -               
Jets_normalisation                 lnN         -                -                -            -               1.50               
%(chan_region)s_TW_stat_bin1_      shape       1                -                -            -               -
%(chan_region)s_TT_stat_bin1_      shape       -                1                -            -               -
%(chan_region)s_DY_stat_bin1_      shape       -                -                1            -               -
%(chan_region)s_other_stat_bin1_   shape       -                -                -            1               -
PileUp_                            shape       1                1                1            1               -           
TriggerSF_                         shape       1                1                1            1               -           
JetEnergyResolution_               shape       1                1                1            1               -                
JetEnergyScale_                    shape       1                1                1            1               -              
BtagScaleFactor_udsg_              shape       1                1                1            1               -              
BtagScaleFactor_bc_                shape       1                1                1            1               -                 
ElectronIDIsoScaleFactor_          shape       1                1                1            1               -               
ElectronReconstructionScaleFactor_ shape       1                1                1            1               -              
MuonTrackEfficiencyScaleFactor_    shape       1                1                1            1               -             
MuonIDScaleFactor_                 shape       1                1                1            1               -             
MuonIsoScaleFactor_                shape       1                1                1            1               -              
TT_Tune_                           shape       -                1                -            -               -
TT_PDF_                            shape       -                1                -            -               -
TT_QCD_                            shape       -                1                -            -               -
TT_CR_                             shape       -                1                -            -               -
FSR_                               shape       1                1                -            -               -
TT_hdamp_                          shape       -                1                -            -               -
ISR_                               shape       1                1                -            -               -
TT_TopMass_                        shape       -                1                -            -               -
tw_DS_                             shape       1                -                -            -               -
tw_MEscale_                        shape       1                -                -            -               -
tw_TopMass_                        shape       1                -                -            -               -
'''
            elif "ee" in self.name:
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
---------------------------------------------------------------------------------------------------------
bin                                            %(cname)s        %(cname)s        %(cname)s    %(cname)s       %(cname)s
process                                        0                1                2            3               4              
process                                        TW               TT               DY           other           jets          
rate                                           %(n_TW)s         %(n_TT)s         %(n_DY)s     %(n_other)s     %(n_jets)s       
-------------------------------------------------------------  -------------    ----                                            
Luminosity                         lnN         1.025            1.025            1.025        1.025           -          
TT_normalisation                   lnN         -                1.05             -            -               -               
%(region)s_DY_normalisation        lnN         -                -                1.30         -               -               
Other_normalisation                lnN         -                -                -            1.50            -               
Jets_normalisation                 lnN         -                -                -            -               1.50               
%(chan_region)s_TW_stat_bin1_      shape       1                -                -            -               -
%(chan_region)s_TT_stat_bin1_      shape       -                1                -            -               -
%(chan_region)s_DY_stat_bin1_      shape       -                -                1            -               -
%(chan_region)s_other_stat_bin1_   shape       -                -                -            1               -
PileUp_                            shape       1                1                1            1               -           
TriggerSF_                         shape       1                1                1            1               -           
JetEnergyResolution_               shape       1                1                1            1               -                
JetEnergyScale_                    shape       1                1                1            1               -              
BtagScaleFactor_udsg_              shape       1                1                1            1               -              
BtagScaleFactor_bc_                shape       1                1                1            1               -                 
ElectronIDIsoScaleFactor_          shape       1                1                1            1               -               
ElectronReconstructionScaleFactor_ shape       1                1                1            1               -              
UnclusteredEn_                     shape       1                1                1            1               -              
TT_Tune_                           shape       -                1                -            -               -
TT_PDF_                            shape       -                1                -            -               -
TT_QCD_                            shape       -                1                -            -               -
TT_CR_                             shape       -                1                -            -               -
FSR_                               shape       1                1                -            -               -
TT_hdamp_                          shape       -                1                -            -               -
ISR_                               shape       1                1                -            -               -
TT_TopMass_                        shape       -                1                -            -               -
tw_DS_                             shape       1                -                -            -               -
tw_MEscale_                        shape       1                -                -            -               -
tw_TopMass_                        shape       1                -                -            -               -
'''
            elif "mumu" in self.name:
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
---------------------------------------------------------------------------------------------------------
bin                                            %(cname)s        %(cname)s        %(cname)s    %(cname)s       %(cname)s
process                                        0                1                2            3               4              
process                                        TW               TT               DY           other           jets          
rate                                           %(n_TW)s         %(n_TT)s         %(n_DY)s     %(n_other)s     %(n_jets)s       
-------------------------------------------------------------  -------------    ----                                            
Luminosity                         lnN         1.025            1.025            1.025        1.025           -          
TT_normalisation                   lnN         -                1.05             -            -               -               
%(region)s_DY_normalisation        lnN         -                -                1.30         -               -               
Other_normalisation                lnN         -                -                -            1.50            -               
Jets_normalisation                 lnN         -                -                -            -               1.50               
%(chan_region)s_TW_stat_bin1_      shape       1                -                -            -               -
%(chan_region)s_TT_stat_bin1_      shape       -                1                -            -               -
%(chan_region)s_DY_stat_bin1_      shape       -                -                1            -               -
%(chan_region)s_other_stat_bin1_   shape       -                -                -            1               -
PileUp_                            shape       1                1                1            1               -           
TriggerSF_                         shape       1                1                1            1               -           
JetEnergyResolution_               shape       1                1                1            1               -                
JetEnergyScale_                    shape       1                1                1            1               -              
BtagScaleFactor_udsg_              shape       1                1                1            1               -              
BtagScaleFactor_bc_                shape       1                1                1            1               -                 
MuonTrackEfficiencyScaleFactor_    shape       1                1                1            1               -             
MuonIDScaleFactor_                 shape       1                1                1            1               -             
MuonIsoScaleFactor_                shape       1                1                1            1               -              
UnclusteredEn_                     shape       1                1                1            1               -              
TT_Tune_                           shape       -                1                -            -               -
TT_PDF_                            shape       -                1                -            -               -
TT_QCD_                            shape       -                1                -            -               -
TT_CR_                             shape       -                1                -            -               -
FSR_                               shape       1                1                -            -               -
TT_hdamp_                          shape       -                1                -            -               -
ISR_                               shape       1                1                -            -               -
TT_TopMass_                        shape       -                1                -            -               -
tw_DS_                             shape       1                -                -            -               -
tw_MEscale_                        shape       1                -                -            -               -
tw_TopMass_                        shape       1                -                -            -               -
'''
        elif self.coulping == "Ctg":
            if "emu" in self.name:
                if "1jet_0bjet" in self.name:
                    self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s           %(cname)s        %(cname)s    %(cname)s     %(cname)s
process                                        -1                  0                1            2             3              
process                                        TW                  TT               DY           other         jets          
rate                                           %(n_TW)s            %(n_TT)s         %(n_DY)s     %(n_other)s   %(n_jets)s       
-------------------------------------------------------------  ----------------    ----                                          
Luminosity                         lnN         1.025               1.025            1.025        1.025         -          
%(region)s_DY_normalisation        lnN         -                   -                1.15         -             -               
Other_normalisation                lnN         -                   -                -            1.50          -               
Jets_normalisation                 lnN         -                   -                -            -             1.50               
%(chan_region)s_TW_stat_bin1_      shape       1                   -                -            -             -
%(chan_region)s_TT_stat_bin1_      shape       -                   1                -            -             -
%(chan_region)s_DY_stat_bin1_      shape       -                   -                1            -             -
%(chan_region)s_other_stat_bin1_   shape       -                   -                -            1             -
PileUp_                            shape       1                   1                1            1             -           
TriggerSF_                         shape       1                   1                1            1             -           
JetEnergyResolution_               shape       1                   1                1            1             -                
JetEnergyScale_                    shape       1                   1                1            1             -              
BtagScaleFactor_udsg_              shape       1                   1                1            1             -              
BtagScaleFactor_bc_                shape       1                   1                1            1             -                 
ElectronIDIsoScaleFactor_          shape       1                   1                1            1             -               
ElectronReconstructionScaleFactor_ shape       1                   1                1            1             -              
MuonTrackEfficiencyScaleFactor_    shape       1                   1                1            1             -             
MuonIDScaleFactor_                 shape       1                   1                1            1             -             
MuonIsoScaleFactor_                shape       1                   1                1            1             -              
DY_PDF_                            shape       -                   -                1            -             -
DY_QCD_                            shape       -                   -                1            -             -
TT_Tune_                           shape       -                   1                -            -             -
TT_PDF_                            shape       -                   1                -            -             -
TT_QCD_                            shape       -                   1                -            -             -
TT_CR_                             shape       -                   1                -            -             -
FSR_                               shape       1                   1                -            -             -
TT_hdamp_                          shape       -                   1                -            -             -
ISR_                               shape       1                   1                -            -             -
TT_TopMass_                        shape       -                   1                -            -             -
tw_DS_                             shape       1                   -                -            -             -
tw_MEscale_                        shape       1                   -                -            -             -
tw_TopMass_                        shape       1                   -                -            -             -
'''
                else:
                    self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s           %(cname)s        %(cname)s    %(cname)s     %(cname)s
process                                        -1                  0                1            2             3              
process                                        TW                  TT               DY           other         jets          
rate                                           %(n_TW)s            %(n_TT)s         %(n_DY)s     %(n_other)s   %(n_jets)s       
-------------------------------------------------------------  ----------------    ----                                          
Luminosity                         lnN         1.025               1.025            1.025        1.025         -          
%(region)s_DY_normalisation        lnN         -                   -                1.50         -             -               
Other_normalisation                lnN         -                   -                -            1.50          -               
Jets_normalisation                 lnN         -                   -                -            -             1.50               
%(chan_region)s_TW_stat_bin1_      shape       1                   -                -            -             -
%(chan_region)s_TT_stat_bin1_      shape       -                   1                -            -             -
%(chan_region)s_DY_stat_bin1_      shape       -                   -                1            -             -
%(chan_region)s_other_stat_bin1_   shape       -                   -                -            1             -
PileUp_                            shape       1                   1                1            1             -           
TriggerSF_                         shape       1                   1                1            1             -           
JetEnergyResolution_               shape       1                   1                1            1             -                
JetEnergyScale_                    shape       1                   1                1            1             -              
BtagScaleFactor_udsg_              shape       1                   1                1            1             -              
BtagScaleFactor_bc_                shape       1                   1                1            1             -                 
ElectronIDIsoScaleFactor_          shape       1                   1                1            1             -               
ElectronReconstructionScaleFactor_ shape       1                   1                1            1             -              
MuonTrackEfficiencyScaleFactor_    shape       1                   1                1            1             -             
MuonIDScaleFactor_                 shape       1                   1                1            1             -             
MuonIsoScaleFactor_                shape       1                   1                1            1             -              
TT_Tune_                           shape       -                   1                -            -             -
TT_PDF_                            shape       -                   1                -            -             -
TT_QCD_                            shape       -                   1                -            -             -
TT_CR_                             shape       -                   1                -            -             -
FSR_                               shape       1                   1                -            -             -
TT_hdamp_                          shape       -                   1                -            -             -
ISR_                               shape       1                   1                -            -             -
TT_TopMass_                        shape       -                   1                -            -             -
tw_DS_                             shape       1                   -                -            -             -
tw_MEscale_                        shape       1                   -                -            -             -
tw_TopMass_                        shape       1                   -                -            -             -
'''
            elif "ee" in self.name:
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s           %(cname)s        %(cname)s    %(cname)s     %(cname)s
process                                        -1                  0                1            2             3              
process                                        TW                  TT               DY           other         jets          
rate                                           %(n_TW)s            %(n_TT)s         %(n_DY)s     %(n_other)s   %(n_jets)s       
-------------------------------------------------------------  ----------------    ----                                          
Luminosity                         lnN         1.025               1.025            1.025        1.025         -          
%(region)s_DY_normalisation        lnN         -                   -                1.30         -             -               
Other_normalisation                lnN         -                   -                -            1.50          -               
Jets_normalisation                 lnN         -                   -                -            -             1.50               
%(chan_region)s_TW_stat_bin1_      shape       1                   -                -            -             -
%(chan_region)s_TT_stat_bin1_      shape       -                   1                -            -             -
%(chan_region)s_DY_stat_bin1_      shape       -                   -                1            -             -
%(chan_region)s_other_stat_bin1_   shape       -                   -                -            1             -
PileUp_                            shape       1                   1                1            1             -           
TriggerSF_                         shape       1                   1                1            1             -           
JetEnergyResolution_               shape       1                   1                1            1             -                
JetEnergyScale_                    shape       1                   1                1            1             -              
BtagScaleFactor_udsg_              shape       1                   1                1            1             -              
BtagScaleFactor_bc_                shape       1                   1                1            1             -                 
ElectronIDIsoScaleFactor_          shape       1                   1                1            1             -               
ElectronReconstructionScaleFactor_ shape       1                   1                1            1             -              
UnclusteredEn_                     shape       1                   1                1            1             -              
TT_Tune_                           shape       -                   1                -            -             -
TT_PDF_                            shape       -                   1                -            -             -
TT_QCD_                            shape       -                   1                -            -             -
TT_CR_                             shape       -                   1                -            -             -
FSR_                               shape       1                   1                -            -             -
TT_hdamp_                          shape       -                   1                -            -             -
ISR_                               shape       1                   1                -            -             -
TT_TopMass_                        shape       -                   1                -            -             -
tw_DS_                             shape       1                   -                -            -             -
tw_MEscale_                        shape       1                   -                -            -             -
tw_TopMass_                        shape       1                   -                -            -             -
'''
            elif "mumu" in self.name:
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s           %(cname)s        %(cname)s    %(cname)s     %(cname)s
process                                        -1                  0                1            2             3              
process                                        TW                  TT               DY           other         jets          
rate                                           %(n_TW)s            %(n_TT)s         %(n_DY)s     %(n_other)s   %(n_jets)s       
-------------------------------------------------------------  ----------------    ----                                          
Luminosity                         lnN         1.025               1.025            1.025        1.025         -          
%(region)s_DY_normalisation        lnN         -                   -                1.30         -             -               
Other_normalisation                lnN         -                   -                -            1.50          -               
Jets_normalisation                 lnN         -                   -                -            -             1.50               
%(chan_region)s_TW_stat_bin1_      shape       1                   -                -            -             -
%(chan_region)s_TT_stat_bin1_      shape       -                   1                -            -             -
%(chan_region)s_DY_stat_bin1_      shape       -                   -                1            -             -
%(chan_region)s_other_stat_bin1_   shape       -                   -                -            1             -
PileUp_                            shape       1                   1                1            1             -           
TriggerSF_                         shape       1                   1                1            1             -           
JetEnergyResolution_               shape       1                   1                1            1             -                
JetEnergyScale_                    shape       1                   1                1            1             -              
BtagScaleFactor_udsg_              shape       1                   1                1            1             -              
BtagScaleFactor_bc_                shape       1                   1                1            1             -                 
MuonTrackEfficiencyScaleFactor_    shape       1                   1                1            1             -             
MuonIDScaleFactor_                 shape       1                   1                1            1             -             
MuonIsoScaleFactor_                shape       1                   1                1            1             -              
UnclusteredEn_                     shape       1                   1                1            1             -              
TT_Tune_                           shape       -                   1                -            -             -
TT_PDF_                            shape       -                   1                -            -             -
TT_QCD_                            shape       -                   1                -            -             -
TT_CR_                             shape       -                   1                -            -             -
FSR_                               shape       1                   1                -            -             -
TT_hdamp_                          shape       -                   1                -            -             -
ISR_                               shape       1                   1                -            -             -
TT_TopMass_                        shape       -                   1                -            -             -
tw_DS_                             shape       1                   -                -            -             -
tw_MEscale_                        shape       1                   -                -            -             -
tw_TopMass_                        shape       1                   -                -            -             -
'''
        elif self.coulping == "Cg" or  self.coulping == "Cphig":
            if "emu" in self.name:
                if "1jet_0bjet" in self.name:
                    self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s    %(cname)s      %(cname)s    %(cname)s     %(cname)s
process                                        0            1              2            3             4              
process                                        TT           TW             DY           other         jets          
rate                                           %(n_TT)s     %(n_TW)s       %(n_DY)s     %(n_other)s   %(n_jets)s       
------------------------------------------------------------------------------------------------------------------                                        
Luminosity                         lnN         1.025        1.025          1.025        1.025         -          
Signal_extra                       lnN         1.03         -              -            -             -               
TW_normalisation                   lnN         -            1.10           -            -             -               
%(region)s_DY_normalisation        lnN         -            -              1.15         -             -               
Other_normalisation                lnN         -            -              -            1.50          -               
Jets_normalisation                 lnN         -            -              -            -             1.50               
%(chan_region)s_TW_stat_bin1_      shape       -            1              -            -             -
%(chan_region)s_TT_stat_bin1_      shape       1            -              -            -             -
%(chan_region)s_DY_stat_bin1_      shape       -            -              1            -             -
%(chan_region)s_other_stat_bin1_   shape       -            -              -            1             -
PileUp_                            shape       1            1              1            1             -           
TriggerSF_                         shape       1            1              1            1             -           
JetEnergyResolution_               shape       1            1              1            1             -                
JetEnergyScale_                    shape       1            1              1            1             -              
BtagScaleFactor_udsg_              shape       1            1              1            1             -              
BtagScaleFactor_bc_                shape       1            1              1            1             -                 
ElectronIDIsoScaleFactor_          shape       1            1              1            1             -               
ElectronReconstructionScaleFactor_ shape       1            1              1            1             -              
MuonTrackEfficiencyScaleFactor_    shape       1            1              1            1             -             
MuonIDScaleFactor_                 shape       1            1              1            1             -             
MuonIsoScaleFactor_                shape       1            1              1            1             -              
DY_PDF_                            shape       -            -              1            -             -
DY_QCD_                            shape       -            -              1            -             -
TT_Tune_                           shape       1            -              -            -             -
TT_PDF_                            shape       1            -              -            -             -
TT_QCD_                            shape       1            -              -            -             -
TT_CR_                             shape       1            -              -            -             -
FSR_                               shape       1            1              -            -             -
TT_hdamp_                          shape       1            -              -            -             -
ISR_                               shape       1            1              -            -             -
TT_TopMass_                        shape       1            -              -            -             -
tw_DS_                             shape       -            1              -            -             -
tw_MEscale_                        shape       -            1              -            -             -
tw_TopMass_                        shape       -            1              -            -             -
'''
                else:
                    self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s    %(cname)s      %(cname)s    %(cname)s     %(cname)s
process                                        0            1              2            3             4              
process                                        TT           TW             DY           other         jets          
rate                                           %(n_TT)s     %(n_TW)s       %(n_DY)s     %(n_other)s   %(n_jets)s       
------------------------------------------------------------------------------------------------------------------                                        
Luminosity                         lnN         1.025        1.025          1.025        1.025         -          
Signal_extra                       lnN         1.03         -              -            -             -               
TW_normalisation                   lnN         -            1.10           -            -             -               
%(region)s_DY_normalisation        lnN         -            -              1.50         -             -               
Other_normalisation                lnN         -            -              -            1.50          -               
Jets_normalisation                 lnN         -            -              -            -             1.50               
%(chan_region)s_TW_stat_bin1_      shape       -            1              -            -             -
%(chan_region)s_TT_stat_bin1_      shape       1            -              -            -             -
%(chan_region)s_DY_stat_bin1_      shape       -            -              1            -             -
%(chan_region)s_other_stat_bin1_   shape       -            -              -            1             -
PileUp_                            shape       1            1              1            1             -           
TriggerSF_                         shape       1            1              1            1             -           
JetEnergyResolution_               shape       1            1              1            1             -                
JetEnergyScale_                    shape       1            1              1            1             -              
BtagScaleFactor_udsg_              shape       1            1              1            1             -              
BtagScaleFactor_bc_                shape       1            1              1            1             -                 
ElectronIDIsoScaleFactor_          shape       1            1              1            1             -               
ElectronReconstructionScaleFactor_ shape       1            1              1            1             -              
MuonTrackEfficiencyScaleFactor_    shape       1            1              1            1             -             
MuonIDScaleFactor_                 shape       1            1              1            1             -             
MuonIsoScaleFactor_                shape       1            1              1            1             -              
TT_Tune_                           shape       1            -              -            -             -
TT_PDF_                            shape       1            -              -            -             -
TT_QCD_                            shape       1            -              -            -             -
TT_CR_                             shape       1            -              -            -             -
FSR_                               shape       1            1              -            -             -
TT_hdamp_                          shape       1            -              -            -             -
ISR_                               shape       1            1              -            -             -
TT_TopMass_                        shape       1            -              -            -             -
tw_DS_                             shape       -            1              -            -             -
tw_MEscale_                        shape       -            1              -            -             -
tw_TopMass_                        shape       -            1              -            -             -
'''
            elif "ee" in self.name:
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s    %(cname)s      %(cname)s    %(cname)s     %(cname)s
process                                        0            1              2            3             4              
process                                        TT           TW             DY           other         jets          
rate                                           %(n_TT)s     %(n_TW)s       %(n_DY)s     %(n_other)s   %(n_jets)s       
------------------------------------------------------------------------------------------------------------------                                        
Luminosity                         lnN         1.025        1.025          1.025        1.025         -          
Signal_extra                       lnN         1.03         -              -            -             -               
TW_normalisation                   lnN         -            1.10           -            -             -               
%(region)s_DY_normalisation        lnN         -            -              1.50         -             -               
Other_normalisation                lnN         -            -              -            1.50          -               
Jets_normalisation                 lnN         -            -              -            -             1.50               
%(chan_region)s_TW_stat_bin1_      shape       -            1              -            -             -
%(chan_region)s_TT_stat_bin1_      shape       1            -              -            -             -
%(chan_region)s_DY_stat_bin1_      shape       -            -              1            -             -
%(chan_region)s_other_stat_bin1_   shape       -            -              -            1             -
PileUp_                            shape       1            1              1            1             -           
TriggerSF_                         shape       1            1              1            1             -           
JetEnergyResolution_               shape       1            1              1            1             -                
JetEnergyScale_                    shape       1            1              1            1             -              
BtagScaleFactor_udsg_              shape       1            1              1            1             -              
BtagScaleFactor_bc_                shape       1            1              1            1             -                 
ElectronIDIsoScaleFactor_          shape       1            1              1            1             -               
ElectronReconstructionScaleFactor_ shape       1            1              1            1             -              
TT_Tune_                           shape       1            -              -            -             -
TT_PDF_                            shape       1            -              -            -             -
TT_QCD_                            shape       1            -              -            -             -
TT_CR_                             shape       1            -              -            -             -
FSR_                               shape       1            1              -            -             -
TT_hdamp_                          shape       1            -              -            -             -
ISR_                               shape       1            1              -            -             -
TT_TopMass_                        shape       1            -              -            -             -
tw_DS_                             shape       -            1              -            -             -
tw_MEscale_                        shape       -            1              -            -             -
tw_TopMass_                        shape       -            1              -            -             -
'''
            elif "mumu" in self.name:
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s    %(cname)s      %(cname)s    %(cname)s     %(cname)s
process                                        0            1              2            3             4              
process                                        TT           TW             DY           other         jets          
rate                                           %(n_TT)s     %(n_TW)s       %(n_DY)s     %(n_other)s   %(n_jets)s       
------------------------------------------------------------------------------------------------------------------                                        
Luminosity                         lnN         1.025        1.025          1.025        1.025         -          
Signal_extra                       lnN         1.03         -              -            -             -               
TW_normalisation                   lnN         -            1.10           -            -             -               
%(region)s_DY_normalisation        lnN         -            -              1.50         -             -               
Other_normalisation                lnN         -            -              -            1.50          -               
Jets_normalisation                 lnN         -            -              -            -             1.50               
%(chan_region)s_TW_stat_bin1_      shape       -            1              -            -             -
%(chan_region)s_TT_stat_bin1_      shape       1            -              -            -             -
%(chan_region)s_DY_stat_bin1_      shape       -            -              1            -             -
%(chan_region)s_other_stat_bin1_   shape       -            -              -            1             -
PileUp_                            shape       1            1              1            1             -           
TriggerSF_                         shape       1            1              1            1             -           
JetEnergyResolution_               shape       1            1              1            1             -                
JetEnergyScale_                    shape       1            1              1            1             -              
BtagScaleFactor_udsg_              shape       1            1              1            1             -              
BtagScaleFactor_bc_                shape       1            1              1            1             -                 
MuonTrackEfficiencyScaleFactor_    shape       1            1              1            1             -             
MuonIDScaleFactor_                 shape       1            1              1            1             -             
MuonIsoScaleFactor_                shape       1            1              1            1             -              
TT_Tune_                           shape       1            -              -            -             -
TT_PDF_                            shape       1            -              -            -             -
TT_QCD_                            shape       1            -              -            -             -
TT_CR_                             shape       1            -              -            -             -
FSR_                               shape       1            1              -            -             -
TT_hdamp_                          shape       1            -              -            -             -
ISR_                               shape       1            1              -            -             -
TT_TopMass_                        shape       1            -              -            -             -
tw_DS_                             shape       -            1              -            -             -
tw_MEscale_                        shape       -            1              -            -             -
tw_TopMass_                        shape       -            1              -            -             -
'''

        else: print "wrong coulping"
    def writeCard(self):
        text_file = open("%s.txt" % (self.out_name), "w")
        text_file.write(self.template % (self.Dict))
        text_file.close()
        print "write card: %s"%(self.out_name)



input_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/input_file_1bin/"
output_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/data_card_1bin/"
info_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/"

if not os.path.exists(output_path):
    os.makedirs(output_path)


Cards=[]
for chan in ["ee","emu","mumu"]:
    for region in ["1jet_0bjet","1jet_1bjet","2jet_1bjet","2jet_2bjet"]:
        #for ic in ["Ctw","Ctg","Cphiq"]:
        for ic in ["Cg"]:
            for sf in ["1.00", "0.05", "0.10", "0.15", "0.20", "0.25", "0.30","0.02","0.50"]:
                for do_opposite in [True,False]:
                    c_name=str(chan)+"_"+str(region)+"_"+str(ic)+"_"+str(sf)
                    if do_opposite==True:
                        c_name=c_name+"_opposite"
                    dir_tmp={}
                    dir_tmp["input_root"]=input_path+c_name
                    dir_tmp["region"]="is"+str(region)
                    dir_tmp["cname"]     =c_name
                    dir_tmp["chan_region"]=str(chan)+"_"+str(region)
                    f_info = open(info_path+"info_1bin.txt",'r')
                    lines = f_info.readlines()
                    for li in lines:
                        li =li.strip('\n')
                        if c_name in li:
                            if "data_obs" in li:
                                dir_tmp["n_observation"]=str(li.split(":")[-1])
                            elif "TW" in li and "TWNLO" not in li:
                                dir_tmp["n_TW"]=str(li.split(":")[-1])
                            elif "TT" in li and "TTNNLO" not in li:
                                dir_tmp["n_TT"]=str(li.split(":")[-1])
                            elif "DY" in li:
                                dir_tmp["n_DY"]=str(li.split(":")[-1])
                            elif "other" in li:
                                dir_tmp["n_other"]=str(li.split(":")[-1])
                            elif "jets" in li:
                                dir_tmp["n_jets"]=str(li.split(":")[-1])
                    Cards.append(card_object(c_name,str(ic),str(chan),str(sf),do_opposite, dir_tmp, output_path+c_name))    
for icard in Cards:
    icard.make_template()
    icard.writeCard()
