import os
class card_object:
    def __init__(self,name,channel,Dict, out_name):
        self.name=name
        self.channel =channel
        self.template=''''''
        self.Dict=Dict
        self.out_name=out_name
    def make_template(self):
        if "1jet_0bjet" in self.name:
            if self.channel=="emu":
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-----------------------------------------------------------------------------------------------------------
bin                                            %(cname)s          %(cname)s         %(cname)s          %(cname)s            %(cname)s
process                                         0                    1                 2                   3                     4
process                                         TW                   TT               DY                  other                 jets
rate                                           %(n_TW)s            %(n_TT)s         %(n_DY)s            %(n_other)s           %(n_jets)s
---------------------------------------------------------------------------------------------------- -----------------------------------------------
Luminosity                         lnN          1.025                 1.025            1.025              1.025                 -
TT_normalisation                   lnN          -                     1.05             -                   -                    -
%(region)s_DY_normalisation_Norm   lnN          -                     -                1.15                -                    -
Othernormalisation_Norm            lnN          -                     -                -                   1.50                 -
Jets_normalisation_Norm            lnN          -                     -                -                   -                    1.50
%(cname)s_TW_stat_bin1_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin2_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin3_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin4_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin5_            shape        1                     -                -                   -                    -
%(cname)s_TT_stat_bin1_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin2_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin3_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin4_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin5_            shape        -                     1                -                   -                    -
%(cname)s_DY_stat_bin1_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin2_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin3_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin4_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin5_            shape        -                     -                1                   -                    -
%(cname)s_other_stat_bin1_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin2_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin3_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin4_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin5_         shape        -                     -                -                   1                    -
PileUp_                            shape        1                     1                1                   1                    -
TriggerSF_                         shape        1                     1                1                   1                    -
JetEnergyResolution_               shape        1                     1                1                   1                    -
JetEnergyScale_                    shape        1                     1                1                   1                    -
BtagScaleFactor_udsg_              shape        1                     1                1                   1                    -
BtagScaleFactor_bc_                shape        1                     1                1                   1                    -
ElectronIDIsoScaleFactor_          shape        1                     1                1                   1                    -
ElectronReconstructionScaleFactor_ shape        1                     1                1                   1                    -
MuonIsoScaleFactor_                shape        1                     1                1                   1                    -
MuonTrackEfficiencyScaleFactor_    shape        1                     1                1                   1                    -
MuonIDScaleFactor_                 shape        1                     1                1                   1                    -
UnclusteredEn_                     shape        1                     1                1                   1                    -
DY_PDF_                            shape        -                     -                1                   -                    -  
DY_QCD_                            shape        -                     -                1                   -                    -  
TT_Tune_                           shape        -                     1                -                   -                    -  
TT_PDF_                            shape        -                     1                -                   -                    -  
TT_QCD_                            shape        -                     1                -                   -                    -  
TT_CR_                             shape        -                     1                -                   -                    -  
FSR_                               shape        1                     1                -                   -                    -  
TT_hdamp_                          shape        -                     1                -                   -                    -  
ISR_                               shape        1                     1                -                   -                    -  
TT_TopMass_                        shape        -                     1                -                   -                    -  
tw_DS_                             shape        1                     -                -                   -                    -  
tw_MEscale_                        shape        1                     -                -                   -                    -  
tw_TopMass_                        shape        1                     -                -                   -                    -  
'''
            elif self.channel=="ee":
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-----------------------------------------------------------------------------------------------------------
bin                                            %(cname)s          %(cname)s         %(cname)s          %(cname)s            %(cname)s
process                                         0                    1                 2                   3                     4
process                                         TW                   TT               DY                  other                 jets
rate                                           %(n_TW)s            %(n_TT)s         %(n_DY)s            %(n_other)s           %(n_jets)s
---------------------------------------------------------------------------------------------------- -----------------------------------------------
Luminosity                         lnN          1.025                 1.025            1.025              1.025                 -
TT_normalisation                   lnN          -                     1.05             -                   -                    -
%(region)s_DY_normalisation_Norm   lnN          -                     -                1.30                -                    -
Othernormalisation_Norm            lnN          -                     -                -                   1.50                 -
Jets_normalisation_Norm            lnN          -                     -                -                   -                    1.50
%(cname)s_TW_stat_bin1_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin2_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin3_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin4_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin5_            shape        1                     -                -                   -                    -
%(cname)s_TT_stat_bin1_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin2_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin3_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin4_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin5_            shape        -                     1                -                   -                    -
%(cname)s_DY_stat_bin1_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin2_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin3_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin4_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin5_            shape        -                     -                1                   -                    -
%(cname)s_other_stat_bin1_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin2_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin3_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin4_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin5_         shape        -                     -                -                   1                    -
PileUp_                            shape        1                     1                1                   1                    -
TriggerSF_                         shape        1                     1                1                   1                    -
JetEnergyResolution_               shape        1                     1                1                   1                    -
JetEnergyScale_                    shape        1                     1                1                   1                    -
BtagScaleFactor_udsg_              shape        1                     1                1                   1                    -
BtagScaleFactor_bc_                shape        1                     1                1                   1                    -
ElectronIDIsoScaleFactor_          shape        1                     1                1                   1                    -
ElectronReconstructionScaleFactor_ shape        1                     1                1                   1                    -
UnclusteredEn_                     shape        1                     1                1                   1                    -
TT_Tune_                           shape        -                     1                -                   -                    -  
TT_PDF_                            shape        -                     1                -                   -                    -  
TT_QCD_                            shape        -                     1                -                   -                    -  
TT_CR_                             shape        -                     1                -                   -                    -  
FSR_                               shape        1                     1                -                   -                    -  
TT_hdamp_                          shape        -                     1                -                   -                    -  
ISR_                               shape        1                     1                -                   -                    -  
TT_TopMass_                        shape        -                     1                -                   -                    -  
tw_DS_                             shape        1                     -                -                   -                    -  
tw_MEscale_                        shape        1                     -                -                   -                    -  
tw_TopMass_                        shape        1                     -                -                   -                    -  
'''
            elif self.channel=="mumu":
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-----------------------------------------------------------------------------------------------------------
bin                                            %(cname)s          %(cname)s         %(cname)s          %(cname)s            %(cname)s
process                                         0                    1                 2                   3                     4
process                                         TW                   TT               DY                  other                 jets
rate                                           %(n_TW)s            %(n_TT)s         %(n_DY)s            %(n_other)s           %(n_jets)s
---------------------------------------------------------------------------------------------------- -----------------------------------------------
Luminosity                         lnN          1.025                 1.025            1.025              1.025                 -
TT_normalisation                   lnN          -                     1.05             -                   -                    -
%(region)s_DY_normalisation_Norm   lnN          -                     -                1.30                -                    -
Othernormalisation_Norm            lnN          -                     -                -                   1.50                 -
Jets_normalisation_Norm            lnN          -                     -                -                   -                    1.50
%(cname)s_TW_stat_bin1_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin2_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin3_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin4_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin5_            shape        1                     -                -                   -                    -
%(cname)s_TT_stat_bin1_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin2_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin3_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin4_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin5_            shape        -                     1                -                   -                    -
%(cname)s_DY_stat_bin1_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin2_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin3_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin4_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin5_            shape        -                     -                1                   -                    -
%(cname)s_other_stat_bin1_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin2_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin3_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin4_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin5_         shape        -                     -                -                   1                    -
PileUp_                            shape        1                     1                1                   1                    -
TriggerSF_                         shape        1                     1                1                   1                    -
JetEnergyResolution_               shape        1                     1                1                   1                    -
JetEnergyScale_                    shape        1                     1                1                   1                    -
BtagScaleFactor_udsg_              shape        1                     1                1                   1                    -
BtagScaleFactor_bc_                shape        1                     1                1                   1                    -
MuonIsoScaleFactor_                shape        1                     1                1                   1                    -
MuonTrackEfficiencyScaleFactor_    shape        1                     1                1                   1                    -
MuonIDScaleFactor_                 shape        1                     1                1                   1                    -
UnclusteredEn_                     shape        1                     1                1                   1                    -
TT_Tune_                           shape        -                     1                -                   -                    -  
TT_PDF_                            shape        -                     1                -                   -                    -  
TT_QCD_                            shape        -                     1                -                   -                    -  
TT_CR_                             shape        -                     1                -                   -                    -  
FSR_                               shape        1                     1                -                   -                    -  
TT_hdamp_                          shape        -                     1                -                   -                    -  
ISR_                               shape        1                     1                -                   -                    -  
TT_TopMass_                        shape        -                     1                -                   -                    -  
tw_DS_                             shape        1                     -                -                   -                    -  
tw_MEscale_                        shape        1                     -                -                   -                    -  
tw_TopMass_                        shape        1                     -                -                   -                    -  
'''
        elif "1jet_1bjet" in self.name:
            if self.channel=="emu":
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-----------------------------------------------------------------------------------------------------------
bin                                            %(cname)s          %(cname)s         %(cname)s          %(cname)s            %(cname)s
process                                         0                    1                 2                   3                     4
process                                         TW                   TT               DY                  other                 jets
rate                                           %(n_TW)s            %(n_TT)s         %(n_DY)s            %(n_other)s           %(n_jets)s
---------------------------------------------------------------------------------------------------- -----------------------------------------------
Luminosity                         lnN          1.025                 1.025            1.025              1.025                 -
TT_normalisation                   lnN          -                     1.05             -                   -                    -
%(region)s_DY_normalisation_Norm   lnN          -                     -                1.50                -                    -
Othernormalisation_Norm            lnN          -                     -                -                   1.50                 -
Jets_normalisation_Norm            lnN          -                     -                -                   -                    1.50
%(cname)s_TW_stat_bin1_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin2_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin3_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin4_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin5_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin6_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin7_            shape        1                     -                -                   -                    -
%(cname)s_TT_stat_bin1_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin2_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin3_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin4_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin5_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin6_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin7_            shape        -                     1                -                   -                    -
%(cname)s_DY_stat_bin1_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin2_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin3_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin4_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin5_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin6_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin7_            shape        -                     -                1                   -                    -
%(cname)s_other_stat_bin1_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin2_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin3_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin4_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin5_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin6_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin7_         shape        -                     -                -                   1                    -
PileUp_                            shape        1                     1                1                   1                    -
TriggerSF_                         shape        1                     1                1                   1                    -
JetEnergyResolution_               shape        1                     1                1                   1                    -
JetEnergyScale_                    shape        1                     1                1                   1                    -
BtagScaleFactor_udsg_              shape        1                     1                1                   1                    -
BtagScaleFactor_bc_                shape        1                     1                1                   1                    -
ElectronIDIsoScaleFactor_          shape        1                     1                1                   1                    -
ElectronReconstructionScaleFactor_ shape        1                     1                1                   1                    -
MuonIsoScaleFactor_                shape        1                     1                1                   1                    -
MuonTrackEfficiencyScaleFactor_    shape        1                     1                1                   1                    -
MuonIDScaleFactor_                 shape        1                     1                1                   1                    -
UnclusteredEn_                     shape        1                     1                1                   1                    -
TT_Tune_                           shape        -                     1                -                   -                    -  
TT_PDF_                            shape        -                     1                -                   -                    -  
TT_QCD_                            shape        -                     1                -                   -                    -  
TT_CR_                             shape        -                     1                -                   -                    -  
FSR_                               shape        1                     1                -                   -                    -  
TT_hdamp_                          shape        -                     1                -                   -                    -  
ISR_                               shape        1                     1                -                   -                    -  
TT_TopMass_                        shape        -                     1                -                   -                    -  
tw_DS_                             shape        1                     -                -                   -                    -  
tw_MEscale_                        shape        1                     -                -                   -                    -  
tw_TopMass_                        shape        1                     -                -                   -                    -  
'''
            elif self.channel=="ee":
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-----------------------------------------------------------------------------------------------------------
bin                                            %(cname)s          %(cname)s         %(cname)s          %(cname)s            %(cname)s
process                                         0                    1                 2                   3                     4
process                                         TW                   TT               DY                  other                 jets
rate                                           %(n_TW)s            %(n_TT)s         %(n_DY)s            %(n_other)s           %(n_jets)s
---------------------------------------------------------------------------------------------------- -----------------------------------------------
Luminosity                         lnN          1.025                 1.025            1.025              1.025                 -
TT_normalisation                   lnN          -                     1.05             -                   -                    -
%(region)s_DY_normalisation_Norm   lnN          -                     -                1.30                -                    -
Othernormalisation_Norm            lnN          -                     -                -                   1.50                 -
Jets_normalisation_Norm            lnN          -                     -                -                   -                    1.50
%(cname)s_TW_stat_bin1_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin2_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin3_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin4_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin5_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin6_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin7_            shape        1                     -                -                   -                    -
%(cname)s_TT_stat_bin1_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin2_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin3_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin4_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin5_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin6_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin7_            shape        -                     1                -                   -                    -
%(cname)s_DY_stat_bin1_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin2_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin3_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin4_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin5_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin6_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin7_            shape        -                     -                1                   -                    -
%(cname)s_other_stat_bin1_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin2_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin3_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin4_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin5_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin6_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin7_         shape        -                     -                -                   1                    -
PileUp_                            shape        1                     1                1                   1                    -
TriggerSF_                         shape        1                     1                1                   1                    -
JetEnergyResolution_               shape        1                     1                1                   1                    -
JetEnergyScale_                    shape        1                     1                1                   1                    -
BtagScaleFactor_udsg_              shape        1                     1                1                   1                    -
BtagScaleFactor_bc_                shape        1                     1                1                   1                    -
ElectronIDIsoScaleFactor_          shape        1                     1                1                   1                    -
ElectronReconstructionScaleFactor_ shape        1                     1                1                   1                    -
UnclusteredEn_                     shape        1                     1                1                   1                    -
TT_Tune_                           shape        -                     1                -                   -                    -  
TT_PDF_                            shape        -                     1                -                   -                    -  
TT_QCD_                            shape        -                     1                -                   -                    -  
TT_CR_                             shape        -                     1                -                   -                    -  
FSR_                               shape        1                     1                -                   -                    -  
TT_hdamp_                          shape        -                     1                -                   -                    -  
ISR_                               shape        1                     1                -                   -                    -  
TT_TopMass_                        shape        -                     1                -                   -                    -  
tw_DS_                             shape        1                     -                -                   -                    -  
tw_MEscale_                        shape        1                     -                -                   -                    -  
tw_TopMass_                        shape        1                     -                -                   -                    -  
'''
            elif self.channel=="mumu":
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-----------------------------------------------------------------------------------------------------------
bin                                            %(cname)s          %(cname)s         %(cname)s          %(cname)s            %(cname)s
process                                         0                    1                 2                   3                     4
process                                         TW                   TT               DY                  other                 jets
rate                                           %(n_TW)s            %(n_TT)s         %(n_DY)s            %(n_other)s           %(n_jets)s
---------------------------------------------------------------------------------------------------- -----------------------------------------------
Luminosity                         lnN          1.025                 1.025            1.025              1.025                 -
TT_normalisation                   lnN          -                     1.05             -                   -                    -
%(region)s_DY_normalisation_Norm   lnN          -                     -                1.30                -                    -
Othernormalisation_Norm            lnN          -                     -                -                   1.50                 -
Jets_normalisation_Norm            lnN          -                     -                -                   -                    1.50
%(cname)s_TW_stat_bin1_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin2_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin3_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin4_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin5_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin6_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin7_            shape        1                     -                -                   -                    -
%(cname)s_TT_stat_bin1_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin2_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin3_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin4_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin5_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin6_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin7_            shape        -                     1                -                   -                    -
%(cname)s_DY_stat_bin1_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin2_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin3_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin4_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin5_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin6_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin7_            shape        -                     -                1                   -                    -
%(cname)s_other_stat_bin1_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin2_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin3_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin4_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin5_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin6_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin7_         shape        -                     -                -                   1                    -
PileUp_                            shape        1                     1                1                   1                    -
TriggerSF_                         shape        1                     1                1                   1                    -
JetEnergyResolution_               shape        1                     1                1                   1                    -
JetEnergyScale_                    shape        1                     1                1                   1                    -
BtagScaleFactor_udsg_              shape        1                     1                1                   1                    -
BtagScaleFactor_bc_                shape        1                     1                1                   1                    -
MuonIsoScaleFactor_                shape        1                     1                1                   1                    -
MuonTrackEfficiencyScaleFactor_    shape        1                     1                1                   1                    -
MuonIDScaleFactor_                 shape        1                     1                1                   1                    -
UnclusteredEn_                     shape        1                     1                1                   1                    -
TT_Tune_                           shape        -                     1                -                   -                    -  
TT_PDF_                            shape        -                     1                -                   -                    -  
TT_QCD_                            shape        -                     1                -                   -                    -  
TT_CR_                             shape        -                     1                -                   -                    -  
FSR_                               shape        1                     1                -                   -                    -  
TT_hdamp_                          shape        -                     1                -                   -                    -  
ISR_                               shape        1                     1                -                   -                    -  
TT_TopMass_                        shape        -                     1                -                   -                    -  
tw_DS_                             shape        1                     -                -                   -                    -  
tw_MEscale_                        shape        1                     -                -                   -                    -  
tw_TopMass_                        shape        1                     -                -                   -                    -  
'''
        elif "2jet_1bjet" in self.name:
            if self.channel=="emu":
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-----------------------------------------------------------------------------------------------------------
bin                                            %(cname)s          %(cname)s         %(cname)s          %(cname)s            %(cname)s
process                                         0                    1                 2                   3                     4
process                                         TW                   TT               DY                  other                 jets
rate                                           %(n_TW)s            %(n_TT)s         %(n_DY)s            %(n_other)s           %(n_jets)s
---------------------------------------------------------------------------------------------------- -----------------------------------------------
Luminosity                         lnN          1.025                 1.025            1.025              1.025                 -
TT_normalisation                   lnN          -                     1.05             -                   -                    -
%(region)s_DY_normalisation_Norm   lnN          -                     -                1.50                -                    -
Othernormalisation_Norm            lnN          -                     -                -                   1.50                 -
Jets_normalisation_Norm            lnN          -                     -                -                   -                    1.50
%(cname)s_TW_stat_bin1_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin2_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin3_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin4_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin5_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin6_            shape        1                     -                -                   -                    -
%(cname)s_TT_stat_bin1_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin2_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin3_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin4_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin5_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin6_            shape        -                     1                -                   -                    -
%(cname)s_DY_stat_bin1_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin2_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin3_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin4_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin5_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin6_            shape        -                     -                1                   -                    -
%(cname)s_other_stat_bin1_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin2_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin3_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin4_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin5_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin6_         shape        -                     -                -                   1                    -
PileUp_                            shape        1                     1                1                   1                    -
TriggerSF_                         shape        1                     1                1                   1                    -
JetEnergyResolution_               shape        1                     1                1                   1                    -
JetEnergyScale_                    shape        1                     1                1                   1                    -
BtagScaleFactor_udsg_              shape        1                     1                1                   1                    -
BtagScaleFactor_bc_                shape        1                     1                1                   1                    -
ElectronIDIsoScaleFactor_          shape        1                     1                1                   1                    -
ElectronReconstructionScaleFactor_ shape        1                     1                1                   1                    -
MuonIsoScaleFactor_                shape        1                     1                1                   1                    -
MuonTrackEfficiencyScaleFactor_    shape        1                     1                1                   1                    -
MuonIDScaleFactor_                 shape        1                     1                1                   1                    -
UnclusteredEn_                     shape        1                     1                1                   1                    -
TT_Tune_                           shape        -                     1                -                   -                    -  
TT_PDF_                            shape        -                     1                -                   -                    -  
TT_QCD_                            shape        -                     1                -                   -                    -  
TT_CR_                             shape        -                     1                -                   -                    -  
FSR_                               shape        1                     1                -                   -                    -  
TT_hdamp_                          shape        -                     1                -                   -                    -  
ISR_                               shape        1                     1                -                   -                    -  
TT_TopMass_                        shape        -                     1                -                   -                    -  
tw_DS_                             shape        1                     -                -                   -                    -  
tw_MEscale_                        shape        1                     -                -                   -                    -  
tw_TopMass_                        shape        1                     -                -                   -                    -  
'''
            elif self.channel=="ee":
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-----------------------------------------------------------------------------------------------------------
bin                                            %(cname)s          %(cname)s         %(cname)s          %(cname)s            %(cname)s
process                                         0                    1                 2                   3                     4
process                                         TW                   TT               DY                  other                 jets
rate                                           %(n_TW)s            %(n_TT)s         %(n_DY)s            %(n_other)s           %(n_jets)s
---------------------------------------------------------------------------------------------------- -----------------------------------------------
Luminosity                         lnN          1.025                 1.025            1.025              1.025                 -
TT_normalisation                   lnN          -                     1.05             -                   -                    -
%(region)s_DY_normalisation_Norm   lnN          -                     -                1.30                -                    -
Othernormalisation_Norm            lnN          -                     -                -                   1.50                 -
Jets_normalisation_Norm            lnN          -                     -                -                   -                    1.50
%(cname)s_TW_stat_bin1_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin2_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin3_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin4_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin5_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin6_            shape        1                     -                -                   -                    -
%(cname)s_TT_stat_bin1_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin2_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin3_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin4_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin5_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin6_            shape        -                     1                -                   -                    -
%(cname)s_DY_stat_bin1_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin2_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin3_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin4_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin5_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin6_            shape        -                     -                1                   -                    -
%(cname)s_other_stat_bin1_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin2_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin3_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin4_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin5_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin6_         shape        -                     -                -                   1                    -
PileUp_                            shape        1                     1                1                   1                    -
TriggerSF_                         shape        1                     1                1                   1                    -
JetEnergyResolution_               shape        1                     1                1                   1                    -
JetEnergyScale_                    shape        1                     1                1                   1                    -
BtagScaleFactor_udsg_              shape        1                     1                1                   1                    -
BtagScaleFactor_bc_                shape        1                     1                1                   1                    -
ElectronIDIsoScaleFactor_          shape        1                     1                1                   1                    -
ElectronReconstructionScaleFactor_ shape        1                     1                1                   1                    -
UnclusteredEn_                     shape        1                     1                1                   1                    -
TT_Tune_                           shape        -                     1                -                   -                    -  
TT_PDF_                            shape        -                     1                -                   -                    -  
TT_QCD_                            shape        -                     1                -                   -                    -  
TT_CR_                             shape        -                     1                -                   -                    -  
FSR_                               shape        1                     1                -                   -                    -  
TT_hdamp_                          shape        -                     1                -                   -                    -  
ISR_                               shape        1                     1                -                   -                    -  
TT_TopMass_                        shape        -                     1                -                   -                    -  
tw_DS_                             shape        1                     -                -                   -                    -  
tw_MEscale_                        shape        1                     -                -                   -                    -  
tw_TopMass_                        shape        1                     -                -                   -                    -  
'''
            elif self.channel=="mumu":
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-----------------------------------------------------------------------------------------------------------
bin                                            %(cname)s          %(cname)s         %(cname)s          %(cname)s            %(cname)s
process                                         0                    1                 2                   3                     4
process                                         TW                   TT               DY                  other                 jets
rate                                           %(n_TW)s            %(n_TT)s         %(n_DY)s            %(n_other)s           %(n_jets)s
---------------------------------------------------------------------------------------------------- -----------------------------------------------
Luminosity                         lnN          1.025                 1.025            1.025              1.025                 -
TT_normalisation                   lnN          -                     1.05             -                   -                    -
%(region)s_DY_normalisation_Norm   lnN          -                     -                1.30                -                    -
Othernormalisation_Norm            lnN          -                     -                -                   1.50                 -
Jets_normalisation_Norm            lnN          -                     -                -                   -                    1.50
%(cname)s_TW_stat_bin1_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin2_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin3_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin4_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin5_            shape        1                     -                -                   -                    -
%(cname)s_TW_stat_bin6_            shape        1                     -                -                   -                    -
%(cname)s_TT_stat_bin1_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin2_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin3_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin4_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin5_            shape        -                     1                -                   -                    -
%(cname)s_TT_stat_bin6_            shape        -                     1                -                   -                    -
%(cname)s_DY_stat_bin1_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin2_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin3_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin4_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin5_            shape        -                     -                1                   -                    -
%(cname)s_DY_stat_bin6_            shape        -                     -                1                   -                    -
%(cname)s_other_stat_bin1_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin2_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin3_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin4_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin5_         shape        -                     -                -                   1                    -
%(cname)s_other_stat_bin6_         shape        -                     -                -                   1                    -
PileUp_                            shape        1                     1                1                   1                    -
TriggerSF_                         shape        1                     1                1                   1                    -
JetEnergyResolution_               shape        1                     1                1                   1                    -
JetEnergyScale_                    shape        1                     1                1                   1                    -
BtagScaleFactor_udsg_              shape        1                     1                1                   1                    -
BtagScaleFactor_bc_                shape        1                     1                1                   1                    -
MuonIsoScaleFactor_                shape        1                     1                1                   1                    -
MuonTrackEfficiencyScaleFactor_    shape        1                     1                1                   1                    -
MuonIDScaleFactor_                 shape        1                     1                1                   1                    -
UnclusteredEn_                     shape        1                     1                1                   1                    -
TT_Tune_                           shape        -                     1                -                   -                    -  
TT_PDF_                            shape        -                     1                -                   -                    -  
TT_QCD_                            shape        -                     1                -                   -                    -  
TT_CR_                             shape        -                     1                -                   -                    -  
FSR_                               shape        1                     1                -                   -                    -  
TT_hdamp_                          shape        -                     1                -                   -                    -  
ISR_                               shape        1                     1                -                   -                    -  
TT_TopMass_                        shape        -                     1                -                   -                    -  
tw_DS_                             shape        1                     -                -                   -                    -  
tw_MEscale_                        shape        1                     -                -                   -                    -  
tw_TopMass_                        shape        1                     -                -                   -                    -  
'''
        elif "2jet_2bjet" in self.name:
            if self.channel=="emu":
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-----------------------------------------------------------------------------------------------------------
bin                                            %(cname)s          %(cname)s         %(cname)s          %(cname)s            %(cname)s
process                                         0                    1                 2                   3                     4
process                                         TW                   TT               DY                  other                 jets
rate                                           %(n_TW)s            %(n_TT)s         %(n_DY)s            %(n_other)s           %(n_jets)s
---------------------------------------------------------------------------------------------------- -----------------------------------------------
Luminosity                         lnN          1.025                 1.025            1.025              1.025                 -
TT_normalisation                   lnN          -                     1.05             -                   -                    -
%(region)s_DY_normalisation_Norm   lnN          -                     -                1.50                -                    -
Othernormalisation_Norm            lnN          -                     -                -                   1.50                 -
Jets_normalisation_Norm            lnN          -                     -                -                   -                    1.50
%(cname)s_TW_stat_bin1_            shape        1                     -                -                   -                    -
%(cname)s_TT_stat_bin1_            shape        -                     1                -                   -                    -
%(cname)s_DY_stat_bin1_            shape        -                     -                1                   -                    -
%(cname)s_other_stat_bin1_         shape        -                     -                -                   1                    -
PileUp_                            shape        1                     1                1                   1                    -
TriggerSF_                         shape        1                     1                1                   1                    -
JetEnergyResolution_               shape        1                     1                1                   1                    -
JetEnergyScale_                    shape        1                     1                1                   1                    -
BtagScaleFactor_udsg_              shape        1                     1                1                   1                    -
BtagScaleFactor_bc_                shape        1                     1                1                   1                    -
ElectronIDIsoScaleFactor_          shape        1                     1                1                   1                    -
ElectronReconstructionScaleFactor_ shape        1                     1                1                   1                    -
MuonIsoScaleFactor_                shape        1                     1                1                   1                    -
MuonTrackEfficiencyScaleFactor_    shape        1                     1                1                   1                    -
MuonIDScaleFactor_                 shape        1                     1                1                   1                    -
UnclusteredEn_                     shape        1                     1                1                   1                    -
TT_Tune_                           shape        -                     1                -                   -                    -  
TT_PDF_                            shape        -                     1                -                   -                    -  
TT_QCD_                            shape        -                     1                -                   -                    -  
TT_CR_                             shape        -                     1                -                   -                    -  
FSR_                               shape        1                     1                -                   -                    -  
TT_hdamp_                          shape        -                     1                -                   -                    -  
ISR_                               shape        1                     1                -                   -                    -  
TT_TopMass_                        shape        -                     1                -                   -                    -  
tw_DS_                             shape        1                     -                -                   -                    -  
tw_MEscale_                        shape        1                     -                -                   -                    -  
tw_TopMass_                        shape        1                     -                -                   -                    -  
'''
            elif self.channel=="ee":
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-----------------------------------------------------------------------------------------------------------
bin                                            %(cname)s          %(cname)s         %(cname)s          %(cname)s            %(cname)s
process                                         0                    1                 2                   3                     4
process                                         TW                   TT               DY                  other                 jets
rate                                           %(n_TW)s            %(n_TT)s         %(n_DY)s            %(n_other)s           %(n_jets)s
---------------------------------------------------------------------------------------------------- -----------------------------------------------
Luminosity                         lnN          1.025                 1.025            1.025              1.025                 -
TT_normalisation                   lnN          -                     1.05             -                   -                    -
%(region)s_DY_normalisation_Norm   lnN          -                     -                1.30                -                    -
Othernormalisation_Norm            lnN          -                     -                -                   1.50                 -
Jets_normalisation_Norm            lnN          -                     -                -                   -                    1.50
%(cname)s_TW_stat_bin1_            shape        1                     -                -                   -                    -
%(cname)s_TT_stat_bin1_            shape        -                     1                -                   -                    -
%(cname)s_DY_stat_bin1_            shape        -                     -                1                   -                    -
%(cname)s_other_stat_bin1_         shape        -                     -                -                   1                    -
PileUp_                            shape        1                     1                1                   1                    -
TriggerSF_                         shape        1                     1                1                   1                    -
JetEnergyResolution_               shape        1                     1                1                   1                    -
JetEnergyScale_                    shape        1                     1                1                   1                    -
BtagScaleFactor_udsg_              shape        1                     1                1                   1                    -
BtagScaleFactor_bc_                shape        1                     1                1                   1                    -
ElectronIDIsoScaleFactor_          shape        1                     1                1                   1                    -
ElectronReconstructionScaleFactor_ shape        1                     1                1                   1                    -
UnclusteredEn_                     shape        1                     1                1                   1                    -
TT_Tune_                           shape        -                     1                -                   -                    -  
TT_PDF_                            shape        -                     1                -                   -                    -  
TT_QCD_                            shape        -                     1                -                   -                    -  
TT_CR_                             shape        -                     1                -                   -                    -  
FSR_                               shape        1                     1                -                   -                    -  
TT_hdamp_                          shape        -                     1                -                   -                    -  
ISR_                               shape        1                     1                -                   -                    -  
TT_TopMass_                        shape        -                     1                -                   -                    -  
tw_DS_                             shape        1                     -                -                   -                    -  
tw_MEscale_                        shape        1                     -                -                   -                    -  
tw_TopMass_                        shape        1                     -                -                   -                    -  
'''
            elif self.channel=="mumu":
                self.template='''
max    1     number of categories
jmax   4     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-----------------------------------------------------------------------------------------------------------
bin                                            %(cname)s          %(cname)s         %(cname)s          %(cname)s            %(cname)s
process                                         0                    1                 2                   3                     4
process                                         TW                   TT               DY                  other                 jets
rate                                           %(n_TW)s            %(n_TT)s         %(n_DY)s            %(n_other)s           %(n_jets)s
---------------------------------------------------------------------------------------------------- -----------------------------------------------
Luminosity                         lnN          1.025                 1.025            1.025              1.025                 -
TT_normalisation                   lnN          -                     1.05             -                   -                    -
%(region)s_DY_normalisation_Norm   lnN          -                     -                1.30                -                    -
Othernormalisation_Norm            lnN          -                     -                -                   1.50                 -
Jets_normalisation_Norm            lnN          -                     -                -                   -                    1.50
%(cname)s_TW_stat_bin1_            shape        1                     -                -                   -                    -
%(cname)s_TT_stat_bin1_            shape        -                     1                -                   -                    -
%(cname)s_DY_stat_bin1_            shape        -                     -                1                   -                    -
%(cname)s_other_stat_bin1_         shape        -                     -                -                   1                    -
PileUp_                            shape        1                     1                1                   1                    -
TriggerSF_                         shape        1                     1                1                   1                    -
JetEnergyResolution_               shape        1                     1                1                   1                    -
JetEnergyScale_                    shape        1                     1                1                   1                    -
BtagScaleFactor_udsg_              shape        1                     1                1                   1                    -
BtagScaleFactor_bc_                shape        1                     1                1                   1                    -
MuonIsoScaleFactor_                shape        1                     1                1                   1                    -
MuonTrackEfficiencyScaleFactor_    shape        1                     1                1                   1                    -
MuonIDScaleFactor_                 shape        1                     1                1                   1                    -
UnclusteredEn_                     shape        1                     1                1                   1                    -
TT_Tune_                           shape        -                     1                -                   -                    -  
TT_PDF_                            shape        -                     1                -                   -                    -  
TT_QCD_                            shape        -                     1                -                   -                    -  
TT_CR_                             shape        -                     1                -                   -                    -  
FSR_                               shape        1                     1                -                   -                    -  
TT_hdamp_                          shape        -                     1                -                   -                    -  
ISR_                               shape        1                     1                -                   -                    -  
TT_TopMass_                        shape        -                     1                -                   -                    -  
tw_DS_                             shape        1                     -                -                   -                    -  
tw_MEscale_                        shape        1                     -                -                   -                    -  
tw_TopMass_                        shape        1                     -                -                   -                    -  
'''

    def writeCard(self):
        text_file = open("%s.txt" % (self.out_name), "w")
        text_file.write(self.template % (self.Dict))
        text_file.close()
        print "write card: %s"%(self.out_name)



input_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/input/"
output_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/"
info_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/"
if not os.path.exists(output_path):
    os.makedirs(output_path)
Cards=[]
for chan in ["ee","emu","mumu"]:
    for region in ["1jet_0bjet","1jet_1bjet","2jet_1bjet","2jet_2bjet"]:
                c_name=str(chan)+"_"+str(region)
                dir_tmp={}
                dir_tmp["cname"]=c_name
                dir_tmp["input_root"]=input_path+c_name
                dir_tmp["region"]="is"+str(region)
                f_info = open(info_path+"info.txt",'r')
                lines = f_info.readlines()
                for li in lines:
                    li =li.strip('\n')
                    if c_name in li:
                        if "data_obs" in li:
                            dir_tmp["n_observation"]=str(li.split(":")[-1])
                        elif "TW" in li :
                            dir_tmp["n_TW"]=str(li.split(":")[-1])
                        elif "TT" in li:
                            dir_tmp["n_TT"]=str(li.split(":")[-1])
                        elif "DY" in li:
                            dir_tmp["n_DY"]=str(li.split(":")[-1])
                        elif "other" in li:
                            dir_tmp["n_other"]=str(li.split(":")[-1])
                        elif "jets" in li:
                            dir_tmp["n_jets"]=str(li.split(":")[-1])
                Cards.append(card_object(c_name,str(chan),dir_tmp, output_path+c_name))    
for icard in Cards:
    icard.make_template()
    icard.writeCard()
