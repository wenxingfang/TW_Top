
combine -M MultiDimFit ../ws_20180325_Ptll/combined_Cphiq_1.00.root                -m 125.7 -n exp_combined_Cphiq            --algo=grid --points=40 -t -1 --expectSignal=0 --setPhysicsModelParameterRanges r=-4,4
combine -M MultiDimFit ../ws_20180325_Ptll/combined_Ctg_1.00.root                  -m 125.7 -n exp_combined_Ctg              --algo=grid --points=30 -t -1 --expectSignal=0 --setPhysicsModelParameterRanges r=-0.3,0.3
combine -M MultiDimFit ../ws_20180325_Ptll/combined_Ctw_1.00.root                  -m 125.7 -n exp_combined_Ctw              --algo=grid --points=40 -t -1 --expectSignal=0 --setPhysicsModelParameterRanges r=-10,10
