cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/scan_script/output/
eval `scramv1 runtime -sh`
combine -M MultiDimFit /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901_emu_1j1t/emu_Ctg_1.00_down.root          -m 125.7 -n obs_emu_Ctg_1j1t_down              --algo=grid --points=100  --setPhysicsModelParameterRanges r=-1,1
echo "AllCompleted"
