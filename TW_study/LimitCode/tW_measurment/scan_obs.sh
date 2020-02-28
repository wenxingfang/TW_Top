#combine -M MultiDimFit data_card_ttbar_DY/emu_1jet_1bjet.root    -n obs_emu_1j1t           --algo=grid  --points=90  --setPhysicsModelParameterRanges r=0,2  
#combine -M MultiDimFit data_card_ttbar_DY/emu_11_21_card.root    -n obs_emu_1j1t_2j1t      --algo=grid  --points=200  --setPhysicsModelParameterRanges r=0,2     
#combine -M MultiDimFit data_card_ttbar_DY/emu_11_21_22_card.root -n obs_emu_1j1t_2j1t_2j2t --algo=grid  --points=200  --setPhysicsModelParameterRanges r=0,2       
#combine -M MultiDimFit data_card_ttbar_DY/emu_card.root          -n obs_emu                --algo=grid  --points=80  --setPhysicsModelParameterRanges r=0,2       
#combine -M MultiDimFit data_card_ttbar_DY/ee_card.root           -n obs_ee                 --algo=grid  --points=200  --setPhysicsModelParameterRanges r=0,2      
#combine -M MultiDimFit data_card_ttbar_DY/mumu_card.root         -n obs_mumu               --algo=grid  --points=30  --setPhysicsModelParameterRanges r=0,2    
#combine -M MultiDimFit data_card_ttbar_DY/ee_emu_mumu_card.root  -n obs_combined           --algo=grid  --points=200  --setPhysicsModelParameterRanges r=0,2      

echo "scan obs done"
#combine -M MultiDimFit data_card_ttbar_DY/emu_1jet_1bjet.root    -n obs_emu_1j1t           --algo=grid  --points=90  --setPhysicsModelParameterRanges r=0,2  
#combine -M MultiDimFit data_card_ttbar_DY/emu_card.root          -n obs_emu                --algo=grid  --points=80  --setPhysicsModelParameterRanges r=0,2       
#combine -M MultiDimFit data_card_ttbar_DY/mumu_card.root         -n obs_mumu               --algo=grid  --points=30  --setPhysicsModelParameterRanges r=0,2    
