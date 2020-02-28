import os
import copy
Method="MultiDimFit"

system={}
system["Ctg"]  ={}
system["Cphiq"]={}
system["Ctw"]  ={}
system["Cg"]   ={}
system["Ccg"]  ={}
system["Cug"]  ={}

system["Ctg"]['BtagScaleFactor_bc_']=['BtagScaleFactor_bc_']
system["Ctg"]['BtagScaleFactor_udsg_']=['BtagScaleFactor_udsg_']
system["Ctg"]['DY_PDF_']=['DY_PDF_'] 
system["Ctg"]['DY_QCD_']=['DY_QCD_'] 
system["Ctg"]['ElectronIDIsoScaleFactor_']=['ElectronIDIsoScaleFactor_']
system["Ctg"]['ElectronReconstructionScaleFactor_']=['ElectronReconstructionScaleFactor_']
system["Ctg"]['FSR_']=['FSR_']    
system["Ctg"]['ISR_']=['ISR_']    
system["Ctg"]['JetEnergyResolution_']=['JetEnergyResolution_']
system["Ctg"]['JetEnergyScale_']=['JetEnergyScale_']
system["Ctg"]['Jets_normalisation']=['Jets_normalisation']
system["Ctg"]['Luminosity']=['Luminosity']
system["Ctg"]['MuonIDScaleFactor_']=['MuonIDScaleFactor_']
system["Ctg"]['MuonIsoScaleFactor_']=['MuonIsoScaleFactor_']
system["Ctg"]['MuonTrackEfficiencyScaleFactor_']=['MuonTrackEfficiencyScaleFactor_']
system["Ctg"]['Other_normalisation']=['Other_normalisation']
system["Ctg"]['is1jet_0bjet_DY_normalisation']=['is1jet_0bjet_DY_normalisation']
system["Ctg"]['is1jet_1bjet_DY_normalisation']=['is1jet_1bjet_DY_normalisation']
system["Ctg"]['is2jet_1bjet_DY_normalisation']=['is2jet_1bjet_DY_normalisation']
system["Ctg"]['is2jet_2bjet_DY_normalisation']=['is2jet_2bjet_DY_normalisation']
system["Ctg"]['PileUp_']=['PileUp_'] 
system["Ctg"]['TT_CR_']=['TT_CR_']  
system["Ctg"]['TT_PDF_']=['TT_PDF_'] 
system["Ctg"]['TT_QCD_']=['TT_QCD_'] 
system["Ctg"]['TT_TopMass_']=['TT_TopMass_']
system["Ctg"]['TT_Tune_']=['TT_Tune_']
system["Ctg"]['TT_hdamp_']=['TT_hdamp_']
system["Ctg"]['TriggerSF_']=['TriggerSF_']
system["Ctg"]['UnclusteredEn_']=['UnclusteredEn_']
system["Ctg"]['tw_DS_']=['tw_DS_']  
system["Ctg"]['tw_MEscale_']=['tw_MEscale_']
system["Ctg"]['tw_TopMass_']=['tw_TopMass_']
system["Ctg"]['MC_stat']=[]
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_DY_stat_bin1_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_DY_stat_bin2_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_DY_stat_bin3_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_DY_stat_bin4_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_DY_stat_bin5_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_TT_stat_bin1_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_TT_stat_bin2_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_TT_stat_bin3_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_TT_stat_bin4_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_TT_stat_bin5_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_TW_stat_bin1_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_TW_stat_bin2_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_TW_stat_bin3_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_TW_stat_bin4_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_TW_stat_bin5_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_other_stat_bin1_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_other_stat_bin2_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_other_stat_bin3_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_other_stat_bin4_')
system["Ctg"]['MC_stat'].append('ee_1jet_1bjet_other_stat_bin5_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_DY_stat_bin1_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_DY_stat_bin2_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_DY_stat_bin3_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_DY_stat_bin4_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_DY_stat_bin5_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_DY_stat_bin6_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_TT_stat_bin1_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_TT_stat_bin2_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_TT_stat_bin3_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_TT_stat_bin4_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_TT_stat_bin5_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_TT_stat_bin6_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_TW_stat_bin1_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_TW_stat_bin2_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_TW_stat_bin3_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_TW_stat_bin4_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_TW_stat_bin5_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_TW_stat_bin6_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_other_stat_bin1_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_other_stat_bin2_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_other_stat_bin3_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_other_stat_bin4_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_other_stat_bin5_')
system["Ctg"]['MC_stat'].append('ee_2jet_1bjet_other_stat_bin6_')
system["Ctg"]['MC_stat'].append('ee_2jet_2bjet_DY_stat_bin1_')
system["Ctg"]['MC_stat'].append('ee_2jet_2bjet_TT_stat_bin1_')
system["Ctg"]['MC_stat'].append('ee_2jet_2bjet_TW_stat_bin1_')
system["Ctg"]['MC_stat'].append('ee_2jet_2bjet_other_stat_bin1_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_DY_stat_bin1_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_DY_stat_bin2_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_DY_stat_bin3_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_DY_stat_bin4_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_DY_stat_bin5_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_TT_stat_bin1_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_TT_stat_bin2_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_TT_stat_bin3_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_TT_stat_bin4_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_TT_stat_bin5_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_TW_stat_bin1_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_TW_stat_bin2_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_TW_stat_bin3_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_TW_stat_bin4_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_TW_stat_bin5_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_other_stat_bin1_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_other_stat_bin2_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_other_stat_bin3_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_other_stat_bin4_')
system["Ctg"]['MC_stat'].append('emu_1jet_0bjet_other_stat_bin5_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_DY_stat_bin1_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_DY_stat_bin2_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_DY_stat_bin3_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_DY_stat_bin4_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_DY_stat_bin5_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_TT_stat_bin1_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_TT_stat_bin2_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_TT_stat_bin3_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_TT_stat_bin4_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_TT_stat_bin5_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_TW_stat_bin1_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_TW_stat_bin2_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_TW_stat_bin3_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_TW_stat_bin4_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_TW_stat_bin5_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_other_stat_bin1_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_other_stat_bin2_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_other_stat_bin3_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_other_stat_bin4_')
system["Ctg"]['MC_stat'].append('emu_1jet_1bjet_other_stat_bin5_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_DY_stat_bin1_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_DY_stat_bin2_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_DY_stat_bin3_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_DY_stat_bin4_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_DY_stat_bin5_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_DY_stat_bin6_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_TT_stat_bin1_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_TT_stat_bin2_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_TT_stat_bin3_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_TT_stat_bin4_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_TT_stat_bin5_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_TT_stat_bin6_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_TW_stat_bin1_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_TW_stat_bin2_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_TW_stat_bin3_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_TW_stat_bin4_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_TW_stat_bin5_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_TW_stat_bin6_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_other_stat_bin1_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_other_stat_bin2_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_other_stat_bin3_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_other_stat_bin4_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_other_stat_bin5_')
system["Ctg"]['MC_stat'].append('emu_2jet_1bjet_other_stat_bin6_')
system["Ctg"]['MC_stat'].append('emu_2jet_2bjet_DY_stat_bin1_')
system["Ctg"]['MC_stat'].append('emu_2jet_2bjet_TT_stat_bin1_')
system["Ctg"]['MC_stat'].append('emu_2jet_2bjet_TW_stat_bin1_')
system["Ctg"]['MC_stat'].append('emu_2jet_2bjet_other_stat_bin1_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_DY_stat_bin1_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_DY_stat_bin2_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_DY_stat_bin3_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_DY_stat_bin4_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_DY_stat_bin5_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_TT_stat_bin1_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_TT_stat_bin2_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_TT_stat_bin3_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_TT_stat_bin4_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_TT_stat_bin5_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_TW_stat_bin1_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_TW_stat_bin2_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_TW_stat_bin3_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_TW_stat_bin4_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_TW_stat_bin5_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_other_stat_bin1_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_other_stat_bin2_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_other_stat_bin3_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_other_stat_bin4_')
system["Ctg"]['MC_stat'].append('mumu_1jet_1bjet_other_stat_bin5_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_DY_stat_bin1_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_DY_stat_bin2_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_DY_stat_bin3_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_DY_stat_bin4_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_DY_stat_bin5_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_DY_stat_bin6_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_TT_stat_bin1_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_TT_stat_bin2_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_TT_stat_bin3_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_TT_stat_bin4_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_TT_stat_bin5_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_TT_stat_bin6_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_TW_stat_bin1_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_TW_stat_bin2_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_TW_stat_bin3_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_TW_stat_bin4_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_TW_stat_bin5_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_TW_stat_bin6_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_other_stat_bin1_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_other_stat_bin2_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_other_stat_bin3_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_other_stat_bin4_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_other_stat_bin5_')
system["Ctg"]['MC_stat'].append('mumu_2jet_1bjet_other_stat_bin6_')
system["Ctg"]['MC_stat'].append('mumu_2jet_2bjet_DY_stat_bin1_')
system["Ctg"]['MC_stat'].append('mumu_2jet_2bjet_TT_stat_bin1_')
system["Ctg"]['MC_stat'].append('mumu_2jet_2bjet_TW_stat_bin1_')
system["Ctg"]['MC_stat'].append('mumu_2jet_2bjet_other_stat_bin1_')

system["Ctw"]=copy.deepcopy(system["Ctg"])
system["Ctw"]['TT_normalisation']=['TT_normalisation']
system["Cphiq"]=system["Ctw"]


system["Cg"]['BtagScaleFactor_bc_'               ]=['BtagScaleFactor_bc_'                 ]
system["Cg"]['BtagScaleFactor_udsg_'             ]=['BtagScaleFactor_udsg_'               ]
system["Cg"]['DY_PDF_'                           ]=['DY_PDF_'                             ]
system["Cg"]['DY_QCD_'                           ]=['DY_QCD_'                             ]
system["Cg"]['ElectronIDIsoScaleFactor_'         ]=['ElectronIDIsoScaleFactor_'           ]
system["Cg"]['ElectronReconstructionScaleFactor_']=['ElectronReconstructionScaleFactor_'  ]
system["Cg"]['FSR_'                              ]=['FSR_'                                ]
system["Cg"]['ISR_'                              ]=['ISR_'                                ]
system["Cg"]['JetEnergyResolution_'              ]=['JetEnergyResolution_'                ]
system["Cg"]['JetEnergyScale_'                   ]=['JetEnergyScale_'                     ]
system["Cg"]['Jets_normalisation'                ]=['Jets_normalisation'                  ]
system["Cg"]['Luminosity'                        ]=['Luminosity'                          ]
system["Cg"]['MuonIDScaleFactor_'                ]=['MuonIDScaleFactor_'                  ]
system["Cg"]['MuonIsoScaleFactor_'               ]=['MuonIsoScaleFactor_'                 ]
system["Cg"]['MuonTrackEfficiencyScaleFactor_'   ]=['MuonTrackEfficiencyScaleFactor_'     ]
system["Cg"]['Other_normalisation'               ]=['Other_normalisation'                 ]
system["Cg"]['PileUp_'                           ]=['PileUp_'                             ]
system["Cg"]['Signal_extra'                      ]=['Signal_extra'                        ]
system["Cg"]['TT_CR_'                            ]=['TT_CR_'                              ]
system["Cg"]['TT_PDF_'                           ]=['TT_PDF_'                             ]
system["Cg"]['TT_QCD_'                           ]=['TT_QCD_'                             ]
system["Cg"]['TT_TopMass_'                       ]=['TT_TopMass_'                         ]
system["Cg"]['TT_Tune_'                          ]=['TT_Tune_'                            ]
system["Cg"]['TT_hdamp_'                         ]=['TT_hdamp_'                           ]
system["Cg"]['TW_normalisation'                  ]=['TW_normalisation'                    ]
system["Cg"]['TriggerSF_'                        ]=['TriggerSF_'                          ]
system["Cg"]['is1jet_0bjet_DY_normalisation'     ]=['is1jet_0bjet_DY_normalisation'       ]
system["Cg"]['is1jet_1bjet_DY_normalisation'     ]=['is1jet_1bjet_DY_normalisation'       ]
system["Cg"]['is2jet_1bjet_DY_normalisation'     ]=['is2jet_1bjet_DY_normalisation'       ]
system["Cg"]['is2jet_2bjet_DY_normalisation'     ]=['is2jet_2bjet_DY_normalisation'       ]
system["Cg"]['tw_DS_'                            ]=['tw_DS_'                              ]
system["Cg"]['tw_MEscale_'                       ]=['tw_MEscale_'                         ]
system["Cg"]['tw_TopMass_'                       ]=['tw_TopMass_'                         ]
system["Cg"]['MC_stat']=[]
system["Cg"]['MC_stat'].append('ee_1jet_1bjet_DY_stat_bin1_')
system["Cg"]['MC_stat'].append('ee_1jet_1bjet_TT_stat_bin1_')
system["Cg"]['MC_stat'].append('ee_1jet_1bjet_TW_stat_bin1_')
system["Cg"]['MC_stat'].append('ee_1jet_1bjet_other_stat_bin1_')
system["Cg"]['MC_stat'].append('ee_2jet_1bjet_DY_stat_bin1_')
system["Cg"]['MC_stat'].append('ee_2jet_1bjet_TT_stat_bin1_')
system["Cg"]['MC_stat'].append('ee_2jet_1bjet_TW_stat_bin1_')
system["Cg"]['MC_stat'].append('ee_2jet_1bjet_other_stat_bin1_')
system["Cg"]['MC_stat'].append('ee_2jet_2bjet_DY_stat_bin1_')
system["Cg"]['MC_stat'].append('ee_2jet_2bjet_TT_stat_bin1_')
system["Cg"]['MC_stat'].append('ee_2jet_2bjet_TW_stat_bin1_')
system["Cg"]['MC_stat'].append('ee_2jet_2bjet_other_stat_bin1_')
system["Cg"]['MC_stat'].append('emu_1jet_0bjet_DY_stat_bin1_')
system["Cg"]['MC_stat'].append('emu_1jet_0bjet_TT_stat_bin1_')
system["Cg"]['MC_stat'].append('emu_1jet_0bjet_TW_stat_bin1_')
system["Cg"]['MC_stat'].append('emu_1jet_0bjet_other_stat_bin1_')
system["Cg"]['MC_stat'].append('emu_1jet_1bjet_DY_stat_bin1_')
system["Cg"]['MC_stat'].append('emu_1jet_1bjet_TT_stat_bin1_')
system["Cg"]['MC_stat'].append('emu_1jet_1bjet_TW_stat_bin1_')
system["Cg"]['MC_stat'].append('emu_1jet_1bjet_other_stat_bin1_')
system["Cg"]['MC_stat'].append('emu_2jet_1bjet_DY_stat_bin1_')
system["Cg"]['MC_stat'].append('emu_2jet_1bjet_TT_stat_bin1_')
system["Cg"]['MC_stat'].append('emu_2jet_1bjet_TW_stat_bin1_')
system["Cg"]['MC_stat'].append('emu_2jet_1bjet_other_stat_bin1_')
system["Cg"]['MC_stat'].append('emu_2jet_2bjet_DY_stat_bin1_')
system["Cg"]['MC_stat'].append('emu_2jet_2bjet_TT_stat_bin1_')
system["Cg"]['MC_stat'].append('emu_2jet_2bjet_TW_stat_bin1_')
system["Cg"]['MC_stat'].append('emu_2jet_2bjet_other_stat_bin1_')
system["Cg"]['MC_stat'].append('mumu_1jet_1bjet_DY_stat_bin1_')
system["Cg"]['MC_stat'].append('mumu_1jet_1bjet_TT_stat_bin1_')
system["Cg"]['MC_stat'].append('mumu_1jet_1bjet_TW_stat_bin1_')
system["Cg"]['MC_stat'].append('mumu_1jet_1bjet_other_stat_bin1_')
system["Cg"]['MC_stat'].append('mumu_2jet_1bjet_DY_stat_bin1_')
system["Cg"]['MC_stat'].append('mumu_2jet_1bjet_TT_stat_bin1_')
system["Cg"]['MC_stat'].append('mumu_2jet_1bjet_TW_stat_bin1_')
system["Cg"]['MC_stat'].append('mumu_2jet_1bjet_other_stat_bin1_')
system["Cg"]['MC_stat'].append('mumu_2jet_2bjet_DY_stat_bin1_')
system["Cg"]['MC_stat'].append('mumu_2jet_2bjet_TT_stat_bin1_')
system["Cg"]['MC_stat'].append('mumu_2jet_2bjet_TW_stat_bin1_')
system["Cg"]['MC_stat'].append('mumu_2jet_2bjet_other_stat_bin1_')

system["Ccg"]['BtagScaleFactor_bc_'                   ]=['BtagScaleFactor_bc_'                     ]
system["Ccg"]['BtagScaleFactor_udsg_'                 ]=['BtagScaleFactor_udsg_'                   ]
system["Ccg"]['ElectronIDIsoScaleFactor_'             ]=['ElectronIDIsoScaleFactor_'               ]
system["Ccg"]['ElectronReconstructionScaleFactor_'    ]=['ElectronReconstructionScaleFactor_'      ]
system["Ccg"]['FCNC_PDF_'                             ]=['FCNC_PDF_'                               ]
system["Ccg"]['FCNC_PS_'                              ]=['FCNC_PS_'                                ]
system["Ccg"]['FCNC_QCD_'                             ]=['FCNC_QCD_'                               ]
system["Ccg"]['FSR_'                                  ]=['FSR_'                                    ]
system["Ccg"]['ISR_'                                  ]=['ISR_'                                    ]
system["Ccg"]['JetEnergyResolution_'                  ]=['JetEnergyResolution_'                    ]
system["Ccg"]['JetEnergyScale_'                       ]=['JetEnergyScale_'                         ]
system["Ccg"]['Jets_normalisation_Norm'               ]=['Jets_normalisation_Norm'                 ]
system["Ccg"]['Luminosity'                            ]=['Luminosity'                              ]
system["Ccg"]['MuonIDScaleFactor_'                    ]=['MuonIDScaleFactor_'                      ]
system["Ccg"]['MuonIsoScaleFactor_'                   ]=['MuonIsoScaleFactor_'                     ]
system["Ccg"]['MuonTrackEfficiencyScaleFactor_'       ]=['MuonTrackEfficiencyScaleFactor_'         ]
system["Ccg"]['Othernormalisation_Norm'               ]=['Othernormalisation_Norm'                 ]
system["Ccg"]['PileUp_'                               ]=['PileUp_'                                 ]
system["Ccg"]['TT_CR_'                                ]=['TT_CR_'                                  ]
system["Ccg"]['TT_PDF_'                               ]=['TT_PDF_'                                 ]
system["Ccg"]['TT_QCD_'                               ]=['TT_QCD_'                                 ]
system["Ccg"]['TT_TopMass_'                           ]=['TT_TopMass_'                             ]
system["Ccg"]['TT_Tune_'                              ]=['TT_Tune_'                                ]
system["Ccg"]['TT_hdamp_'                             ]=['TT_hdamp_'                               ]
system["Ccg"]['TT_normalisation_Norm'                 ]=['TT_normalisation_Norm'                   ]
system["Ccg"]['TW_normalisation_Norm'                 ]=['TW_normalisation_Norm'                   ]
system["Ccg"]['TriggerSF_'                            ]=['TriggerSF_'                              ]
system["Ccg"]['UnclusteredEn_'                        ]=['UnclusteredEn_'                          ]
system["Ccg"]['tw_DS_'                                ]=['tw_DS_'                                  ]
system["Ccg"]['tw_MEscale_'                           ]=['tw_MEscale_'                             ]
system["Ccg"]['tw_TopMass_'                           ]=['tw_TopMass_'                             ]
system["Ccg"]['isxjet_1bjet_DY_normalisation_Norm'    ]=['isxjet_1bjet_DY_normalisation_Norm'      ]
system["Ccg"]['MC_stat']=[]
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_DY_stat_bin10_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_DY_stat_bin1_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_DY_stat_bin2_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_DY_stat_bin3_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_DY_stat_bin4_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_DY_stat_bin5_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_DY_stat_bin6_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_DY_stat_bin7_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_DY_stat_bin8_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_DY_stat_bin9_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_FCNCSignal_stat_bin10_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_FCNCSignal_stat_bin1_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_FCNCSignal_stat_bin2_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_FCNCSignal_stat_bin3_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_FCNCSignal_stat_bin4_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_FCNCSignal_stat_bin5_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_FCNCSignal_stat_bin6_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_FCNCSignal_stat_bin7_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_FCNCSignal_stat_bin8_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_FCNCSignal_stat_bin9_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TT_stat_bin10_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TT_stat_bin1_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TT_stat_bin2_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TT_stat_bin3_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TT_stat_bin4_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TT_stat_bin5_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TT_stat_bin6_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TT_stat_bin7_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TT_stat_bin8_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TT_stat_bin9_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TW_stat_bin10_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TW_stat_bin1_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TW_stat_bin2_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TW_stat_bin3_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TW_stat_bin4_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TW_stat_bin5_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TW_stat_bin6_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TW_stat_bin7_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TW_stat_bin8_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_TW_stat_bin9_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_other_stat_bin10_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_other_stat_bin1_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_other_stat_bin2_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_other_stat_bin3_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_other_stat_bin4_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_other_stat_bin5_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_other_stat_bin6_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_other_stat_bin7_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_other_stat_bin8_')
system["Ccg"]['MC_stat'].append('ee_xjet_1bjet_other_stat_bin9_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_DY_stat_bin10_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_DY_stat_bin1_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_DY_stat_bin2_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_DY_stat_bin3_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_DY_stat_bin4_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_DY_stat_bin5_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_DY_stat_bin6_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_DY_stat_bin7_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_DY_stat_bin8_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_DY_stat_bin9_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_FCNCSignal_stat_bin10_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_FCNCSignal_stat_bin1_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_FCNCSignal_stat_bin2_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_FCNCSignal_stat_bin3_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_FCNCSignal_stat_bin4_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_FCNCSignal_stat_bin5_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_FCNCSignal_stat_bin6_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_FCNCSignal_stat_bin7_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_FCNCSignal_stat_bin8_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_FCNCSignal_stat_bin9_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TT_stat_bin10_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TT_stat_bin1_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TT_stat_bin2_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TT_stat_bin3_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TT_stat_bin4_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TT_stat_bin5_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TT_stat_bin6_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TT_stat_bin7_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TT_stat_bin8_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TT_stat_bin9_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TW_stat_bin10_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TW_stat_bin1_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TW_stat_bin2_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TW_stat_bin3_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TW_stat_bin4_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TW_stat_bin5_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TW_stat_bin6_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TW_stat_bin7_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TW_stat_bin8_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_TW_stat_bin9_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_other_stat_bin10_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_other_stat_bin1_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_other_stat_bin2_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_other_stat_bin3_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_other_stat_bin4_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_other_stat_bin5_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_other_stat_bin6_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_other_stat_bin7_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_other_stat_bin8_')
system["Ccg"]['MC_stat'].append('emu_xjet_1bjet_other_stat_bin9_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_DY_stat_bin10_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_DY_stat_bin1_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_DY_stat_bin2_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_DY_stat_bin3_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_DY_stat_bin4_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_DY_stat_bin5_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_DY_stat_bin6_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_DY_stat_bin7_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_DY_stat_bin8_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_DY_stat_bin9_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_FCNCSignal_stat_bin10_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_FCNCSignal_stat_bin1_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_FCNCSignal_stat_bin2_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_FCNCSignal_stat_bin3_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_FCNCSignal_stat_bin4_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_FCNCSignal_stat_bin5_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_FCNCSignal_stat_bin6_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_FCNCSignal_stat_bin7_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_FCNCSignal_stat_bin8_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_FCNCSignal_stat_bin9_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TT_stat_bin10_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TT_stat_bin1_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TT_stat_bin2_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TT_stat_bin3_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TT_stat_bin4_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TT_stat_bin5_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TT_stat_bin6_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TT_stat_bin7_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TT_stat_bin8_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TT_stat_bin9_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TW_stat_bin10_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TW_stat_bin1_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TW_stat_bin2_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TW_stat_bin3_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TW_stat_bin4_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TW_stat_bin5_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TW_stat_bin6_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TW_stat_bin7_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TW_stat_bin8_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_TW_stat_bin9_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_other_stat_bin10_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_other_stat_bin1_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_other_stat_bin2_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_other_stat_bin3_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_other_stat_bin4_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_other_stat_bin5_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_other_stat_bin6_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_other_stat_bin7_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_other_stat_bin8_')
system["Ccg"]['MC_stat'].append('mumu_xjet_1bjet_other_stat_bin9_')

system["Cug"]=system["Ccg"]

system["Ctg"]  ['Total']      =[]
system["Ctw"]  ['Total']      =[]
system["Cphiq"]['Total']      =[]
system["Cg"]   ['Total']      =[]
system["Cug"]  ['Total']      =[]
system["Cug"]  ['Total']      =[]
system["Ctg"]  ['Freeze_all'] =[]
system["Ctw"]  ['Freeze_all'] =[]
system["Cphiq"]['Freeze_all'] =[]
system["Cg"]   ['Freeze_all'] =[]
system["Cug"]  ['Freeze_all'] =[]
system["Cug"]  ['Freeze_all'] =[]


r_Range={}
r_Range['Cg']   = [-1, 1]
r_Range['Ctg']  = [-0.5, 0.5]
r_Range['Ctw']  = [-2, 7]
r_Range['Cphiq']= [-4, 2]
r_Range['Cug']  = [-2, 2]
r_Range['Ccg']  = [-2, 2]

script_path = "/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para_new/scripts/"
str_evn = 'eval `scramv1 runtime -sh`'
for cat in ['obs','exp']:
    print '########## %s ##########'%cat
    str1='-t -1 --expectSignal=0' if cat=="exp" else " "
    for ic in ['Cg','Cphiq','Ctw','Ctg','Cug','Ccg']:
        print '------------ %s ------------'%ic
        savedworkspace="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/%s/higgsCombine%s.MultiDimFit.mH120.root"%(cat,ic)
        action_other="--freezeNuisances "
        first=True
        for isys in system[ic]:
            f_out=open(script_path+"%s_%s_%s.sh"%(cat,ic,isys),"w")
            str_cd = 'cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/by_freeze_para_new/%s/%s'%(cat, ic)
            f_out.write(str_cd +'\n')
            f_out.write(str_evn+'\n')
            points = '50'
            action_1=""
            if isys=="Freeze_all":
                action_1="--freezeNuisances all --fastScan"
            elif isys=="Total":
                action_1=""
            else:
                print isys
                for i in system[ic][isys]:
                    if first:
                        action_other=action_other+str(i)
                        first=False
                    else:
                        action_other=action_other+","+str(i)
            str_log = '%s_%s_%s.log'%(cat,ic,isys)
            outname=isys
            action = action_1 if (isys=='Freeze_all' or isys=='Total') else action_other
            f_out.write("logsave  %s combine %s -M %s --setPhysicsModelParameterRanges r=%f,%f   --algo grid --points %s %s -n %s --snapshotName MultiDimFit %s "%(str_log,savedworkspace,Method,r_Range[ic][0],r_Range[ic][1],points,str1,outname,action))
            f_out.close()
print "done"
