
#combine -M MultiDimFit ws_search_tug_20180625/combined_FCNC_0.10.root  -m 125.7 -n obs_combined_Cug        --algo=grid --points=80    --setPhysicsModelParameterRanges r=-2,2
#combine -M MultiDimFit ws_search_tug_20180625/ee_FCNC_0.10.root        -m 125.7 -n obs_ee_Cug              --algo=grid --points=80    --setPhysicsModelParameterRanges r=-2,2
#combine -M MultiDimFit ws_search_tug_20180625/emu_FCNC_0.10.root       -m 125.7 -n obs_emu_Cug             --algo=grid --points=80    --setPhysicsModelParameterRanges r=-2,2
#combine -M MultiDimFit ws_search_tug_20180625/mumu_FCNC_0.10.root      -m 125.7 -n obs_mumu_Cug            --algo=grid --points=80    --setPhysicsModelParameterRanges r=-2,2
#combine -M MultiDimFit ws_search_tcg_20180625/combined_FCNC_0.10.root  -m 125.7 -n obs_combined_Ccg        --algo=grid --points=80    --setPhysicsModelParameterRanges r=-2,2
#combine -M MultiDimFit ws_search_tcg_20180625/ee_FCNC_0.10.root        -m 125.7 -n obs_ee_Ccg              --algo=grid --points=80    --setPhysicsModelParameterRanges r=-2,2
#combine -M MultiDimFit ws_search_tcg_20180625/emu_FCNC_0.10.root       -m 125.7 -n obs_emu_Ccg             --algo=grid --points=80    --setPhysicsModelParameterRanges r=-2,2
#combine -M MultiDimFit ws_search_tcg_20180625/mumu_FCNC_0.10.root      -m 125.7 -n obs_mumu_Ccg            --algo=grid --points=80    --setPhysicsModelParameterRanges r=-2,2

########################## check ###########33
combine -M MultiDimFit ws_search_tug_20190608_NoTopPtReW/combined_FCNC_0.10.root  -m 125.7 -n obs_combined_Cug        --algo=grid --points=80    --setPhysicsModelParameterRanges r=-2,2
combine -M MultiDimFit ws_search_tug_20190608_NoTopPtReW/combined_FCNC_0.10.root  -m 125.7 -n obs_combined_Ccg        --algo=grid --points=80    --setPhysicsModelParameterRanges r=-2,2
echo "obs scan done"
