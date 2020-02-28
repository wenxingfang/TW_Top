import os

WithOut_ws=True
path_workspace="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC_tug/ws/"
path_datacard="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC_tug/data_card_combined/"
path_script   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC_tug/script_0719_100Toy_fullsim/"
path_result   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC_tug/result_0719_100Toy_fullsim/"
#path_datacard="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC_tug/data_card_combined_noSignalStat/"
#path_script   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC_tug/script_0719_100Toy_fastsim_noSignalStat/"
#path_result   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC_tug/result_0719_100Toy_fastsim_noSignalStat/"

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


for ic in cat:
    for chan in channel:
        for sf in ["1.00", "0.05", "0.10", "0.15", "0.20", "0.25", "0.30","0.02","0.50"]:
            f = open(path_script+str(ic)+"_"+str(chan)+"_FCNC"+"_"+str(sf)+".sh",'w')
            f.write("cd /user/wenxing/Limits/CMSSW_7_4_7/src")
            f.write("\n")
            f.write("eval `scramv1 runtime -sh`")
            f.write("\n")
            str_ws=path_workspace+str(chan)+"_FCNC"+"_"+str(sf)+".root"
            if WithOut_ws:
                str_ws=path_datacard+str(chan)+"_FCNC"+"_"+str(sf)+".txt"
            
            log_name=str(ic)+"_"+str(chan)+"_FCNC"+"_"+str(sf)+".log"
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
