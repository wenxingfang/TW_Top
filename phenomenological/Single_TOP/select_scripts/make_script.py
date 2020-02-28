import math
import datetime

import ROOT
import os
path_script="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/select_scripts/script/"
path_exc   ="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/select_scripts/"


is_parton_level=True####

uncertainty=[]
uncertainty.append("nominal")
##############  parton shower uncertainty ################
uncertainty.append("PS_Down")
uncertainty.append("PS_Up"  )
##############  PDF uncertainty ################
for ip in range(1010,1112):
    uncertainty.append("%s"%(str(ip)))    
##############  QCD uncertainty ################
for ip in ["1002","1003","1004","1005","1007","1009"]:
    uncertainty.append("%s"%(str(ip)))    


for uncer in uncertainty:
    f1 = open(path_script+"script_"+uncer+".py",'w') 
    f1.write("import os \n")
    f1.write("import ROOT \n")
    if is_parton_level:
        f1.write('ROOT.gSystem.Load("'+path_exc+'select_save_parton_C.so") \n')
        f1.write("ROOT.gROOT.ProcessLine('select_save_parton("+'"'+uncer+'"'+")') \n")
    else:
        f1.write('ROOT.gSystem.Load("'+path_exc+'select_save_PL_C.so") \n')
        f1.write("ROOT.gROOT.ProcessLine('select_save_PL("+'"'+uncer+'"'+")') \n")
    f1.write("print 'Done!'")
    f1.close()

    f2 = open(path_script+"script_"+uncer+".sh",'w') 
    f2.write("cd /user/wenxing/ST_TW_channel/CMSSW_8_0_25/src")
    f2.write("\n")
    f2.write("eval `scramv1 runtime -sh`")
    f2.write("\n")
    f2.write("python "+path_script+"script_"+uncer+".py")
    f2.close()
print "done"
