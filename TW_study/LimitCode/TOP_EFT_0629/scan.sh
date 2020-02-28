combine -M MultiDimFit ws_0724_search/combined_Cphiq_1.00.root -m 125.7 -n combined_Cphiq --algo=grid --points=400 --setPhysicsModelParameterRanges CMS_TW_mu=-10,10
combine -M MultiDimFit ws_0724_search/combined_Ctg_1.00.root   -m 125.7 -n combined_Ctg   --algo=grid --points=150 --setPhysicsModelParameterRanges CMS_TWTT_mu=-1,1
combine -M MultiDimFit ws_0724_search/combined_Ctw_1.00.root   -m 125.7 -n combined_Ctw   --algo=grid --points=400 --setPhysicsModelParameterRanges CMS_TW_mu=-6,6
combine -M MultiDimFit ws_0724_search/ee_Cphiq_1.00.root       -m 125.7 -n ee_Cphiq       --algo=grid --points=400 --setPhysicsModelParameterRanges CMS_TW_mu=-10,10
combine -M MultiDimFit ws_0724_search/ee_Ctg_1.00.root         -m 125.7 -n ee_Ctg         --algo=grid --points=150 --setPhysicsModelParameterRanges CMS_TWTT_mu=-1,1
combine -M MultiDimFit ws_0724_search/ee_Ctw_1.00.root         -m 125.7 -n ee_Ctw         --algo=grid --points=400 --setPhysicsModelParameterRanges CMS_TW_mu=-6,6
combine -M MultiDimFit ws_0724_search/emu_Cphiq_1.00.root      -m 125.7 -n emu_Cphiq      --algo=grid --points=400 --setPhysicsModelParameterRanges CMS_TW_mu=-10,10
combine -M MultiDimFit ws_0724_search/emu_Ctg_1.00.root        -m 125.7 -n emu_Ctg        --algo=grid --points=150 --setPhysicsModelParameterRanges CMS_TWTT_mu=-1,1
combine -M MultiDimFit ws_0724_search/emu_Ctw_1.00.root        -m 125.7 -n emu_Ctw        --algo=grid --points=400 --setPhysicsModelParameterRanges CMS_TW_mu=-6,6
combine -M MultiDimFit ws_0724_search/mumu_Cphiq_1.00.root     -m 125.7 -n mumu_Cphiq     --algo=grid --points=400 --setPhysicsModelParameterRanges CMS_TW_mu=-10,10
combine -M MultiDimFit ws_0724_search/mumu_Ctg_1.00.root       -m 125.7 -n mumu_Ctg       --algo=grid --points=150 --setPhysicsModelParameterRanges CMS_TWTT_mu=-1,1
combine -M MultiDimFit ws_0724_search/mumu_Ctw_1.00.root       -m 125.7 -n mumu_Ctw       --algo=grid --points=400 --setPhysicsModelParameterRanges CMS_TW_mu=-6,6
echo "scan done"
