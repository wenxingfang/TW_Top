split -l 10 sub_ws.txt -d -a 4 split_ # split file, details(http://blog.csdn.net/mxgsgtc/article/details/12048919)
find ./ -name "split*" -exec mv "{}" "{}.sh" \;
find ./ -name "split_*"  -exec sed -i '$a echo "AllCompleted"' {} \; #write echo "AllCompleted" in last
