split -l 1 all_scripts.txt -d -a 4 split_ # split file, details(http://blog.csdn.net/mxgsgtc/article/details/12048919)
find ./ -name "split*" -exec mv "{}" "{}.sh" \;
find ./ -name "split_*"  -exec sed -i '1i eval `scramv1 runtime -sh`' {} \; #write echo "AllCompleted" in last
find ./ -name "split_*"  -exec sed -i '1i cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_limit/HybridNew/output/' {} \; #write echo "AllCompleted" in last
find ./ -name "split_*"  -exec sed -i '$a echo "AllCompleted"' {} \; #write echo "AllCompleted" in last
