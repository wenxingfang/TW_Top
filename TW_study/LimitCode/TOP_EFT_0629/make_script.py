import os

do_search=True

path_workspace="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_0803_search/"
path_script   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/script_0803_search/"
path_result   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/result_0803_search/"

#path_workspace="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT/ws_1bin/"
#path_script="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT/script_0622_10Toy_1bin/"
#path_result="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT/result_0622_10Toy_1bin/"
if not os.path.exists(path_script):
        os.makedirs(path_script)
if not os.path.exists(path_result):
        os.makedirs(path_result)



Method="Asymptotic"
#Method="HybridNew"
#Method="MarkovChainMC"
CPU="1"

#cat=["obs","exp"]
cat=["exp"]

channel=["ee","emu","mumu","combined"]

signal=["Ctw","Cphiq","Ctg"]
#signal=["Ctg"]

#sf=["1.00", "0.05", "0.10", "0.15", "0.20", "0.25", "0.30","0.02","0.50", "1.50", "2.00", "2.50","3.00","4.00","5.00"]
sf=["1.00", "0.05", "0.10", "0.15", "0.20", "0.25", "0.30","0.02","0.50"]
if do_search:
    sf=["1.00"]
for ic in cat:
    for chan in channel:
        for isig in signal:
            for isf in sf:
                for Add_opposite in [True,False]:
                    str_opp=""
                    if Add_opposite:str_opp="_opposite"
                    f = open(path_script+str(ic)+"_"+str(chan)+"_"+str(isig)+"_"+str(isf)+str_opp+".sh",'w')
                    f.write("cd /user/wenxing/Limits/CMSSW_7_4_7/src")
                    f.write("\n")
                    f.write("eval `scramv1 runtime -sh`")
                    f.write("\n")
                    str_ws=path_workspace+str(chan)+"_"+str(isig)+"_"+str(isf)+str_opp+".root"
                    log_name=str(ic)+"_"+str(chan)+"_"+str(isig)+"_"+str(isf)+str_opp+".log"
                    log_name=path_result+log_name
                    if ic =="obs":
                        if Method=="Asymptotic":
                            f.write("combine -M Asymptotic "+ str_ws+ " > " + log_name)
                        elif Method=="HybridNew":
                            f.write("combine -M HybridNew --frequentist --testStat LHC "+str_ws+" -H ProfileLikelihood --fork "+CPU+ " > " + log_name)
                        elif Method=="MarkovChainMC":
                            f.write("combine -M MarkovChainMC -H --tries 10 "+str_ws+" > " + log_name)
                    elif ic =="exp":
                        if Method=="Asymptotic":
                            f.write("combine -M Asymptotic "+ str_ws + " -t 100" + " > " + log_name)
                        elif Method=="HybridNew":
                            f.write("combine -M HybridNew --frequentist --testStat LHC "+str_ws+" -H ProfileLikelihood --fork "+CPU+" -t 1"+ " > " + log_name)
                    else:print "wrong!"
                    f.write("\n")
                    f.close()
print "create script done!"
