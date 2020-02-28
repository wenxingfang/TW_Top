cd /user/wenxing/ST_TW_channel/CMSSW_8_0_25/src
eval `scramv1 runtime -sh`
python /user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/fit_limit_deltachi2.py -m "dchi2" -e "obs" -c "Diff_8TeV_7TeV_Inclusive"  -R 0.9
python /user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/fit_limit_deltachi2_FixR1.py -m "dchi2" -e "obs" -c "Diff_8TeV_7TeV_Inclusive"  -R 0.9
python /user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/fit_limit_deltachi2_FixR2.py -m "dchi2" -e "obs" -c "Diff_8TeV_7TeV_Inclusive"  -R 0.9