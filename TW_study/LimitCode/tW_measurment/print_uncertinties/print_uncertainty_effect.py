import os
import math

Method="MaxLikelihoodFit"
#Method="MultiDimFit"
path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/print_uncertinties/output/"

best_value=0
uncert={}
real_effect={}
for ifile in os.listdir(path):
    name=ifile.split(".txt")[0]
    v_uncert=0
    fname=path+ifile
    if ".txt" not in ifile:continue
    f_in=open(fname,"r")
    lines=f_in.readlines()
    if Method=="MaxLikelihoodFit":
        for line in lines:
            if "Best fit r:" in line:
                b1=line.split(":")[-1]
                b2=b1.split("-")[0]
                best_value=float(b2)
                tmp=line.split("(68% CL)")[0]
                tmp1=tmp.split("-")[-1]
                down=tmp1.split("/")[0]
                up1 =tmp1.split("/")[-1]
                up  =up1.split("+")[-1] 
                #if float(up)>float(down):v_uncert=float(up)
                #else                    :v_uncert=float(down)
                v_uncert=(float(up)+float(down))/2
                if float(up)>0.5: 
                    v_uncert=float(down)
                if float(down)>0.5: 
                    v_uncert=float(up)
    elif Method=="MultiDimFit":
        for line in lines:
            if "RooRealVar::r" in line:
                b1=line.split("=")[-1]
                b2=b1.split("+/-")[0]
                best_value=float(b2)
                tmp=line.split("+/-")[-1]
                tmp1=tmp.split("L")[0]
                v_uncert=float(tmp1)
    uncert[name]=v_uncert
if "Total" in uncert:
    for iu in uncert:
        if iu == "Total":
            real_effect[iu]=100*uncert[iu]/best_value
        elif iu == "Remove_all":##data statistic
            real_effect[iu]=100*uncert[iu]/best_value
        else:
            if uncert[iu]>uncert["Total"]:
                print "%s:total=%f,it=%f"%(iu,uncert["Total"],uncert[iu])
                continue
            real_effect[iu]=100*math.sqrt(math.pow(uncert["Total"],2)-math.pow(uncert[iu],2))/best_value
else:
    print "missing Total"
#print real_effect
la_head='''
\\begin{table}[]
\centering
\caption{My caption}
\label{my-label}
\\begin{tabular}{|c|c|}
\hline
Source & Uncertainty \\\ \hline \hline
'''
print la_head
for ie in real_effect:
    print "%s & %.3f\\%% \\\\ \hline "%(ie,real_effect[ie])

la_end='''
\end{tabular}
\end{table}
'''
print la_end
