import math
import datetime

import ROOT
import os
path_script="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/script/"
path_exec  ="/user/wenxing/ST_TW_channel/CMSSW_8_0_25/src/Phynomenological_study/Single_TOP/"

str_ma=""
str_Ma=""
do_margin=False
if do_margin:
    str_ma="_Ma"    
    str_Ma="-M"

do_fix_R=True

dicti={}
dicti["dchi2"]={}
#dicti["dchi2"]["obs"]=["Diff_8TeV","Diff_8TeV_Ratio","Diff_8TeV_7TeV_Inclusive"]
dicti["dchi2"]["obs"]=["Diff_8TeV_Ratio","Diff_8TeV_7TeV_Inclusive"]
#dicti["dchi2"]["obs"]=["8TeV_Ratio_st_fid"]
#dicti["dchi2"]["exp"]=["tW_8TeV","ST_8TeV","Width_8TeV","Ratio_8TeV","Rt_8TeV","Diff_8TeV","Diff_8TeV_Ratio","Diff_8TeV_7TeV_Inclusive","Diff_13TeV","Diff_13TeV_Ratio"]
#dicti["dchi2"]["exp"]=["tW_Ratio_8TeV","ST_Ratio_8TeV","Width_8TeV","Rt_8TeV","Diff_8TeV"]
#dicti["dchi2"]["exp"]=["Diff_13TeV_Ratio"]
#dicti["dchi2"]["exp"]=["8TeV_Ratio_st_fid"]
dicti["dchi2"]["exp"]=["Diff_8TeV_Ratio","Diff_8TeV_7TeV_Inclusive"]
#dicti["dchi2"]["exp"]=["Diff_8TeV_Ratio","Diff_8TeV_7TeV_Inclusive","Diff_13TeV_Ratio"]
#dicti["dchi2"]["obs"]=["Diff_8TeV","Diff_8TeV_Ratio","Diff_7TeV_Inclusive","Diff_8TeV_7TeV_Inclusive","Diff_8TeV_top_pt","Diff_8TeV_top_y","Diff_8TeV_top_jet_pt","Diff_8TeV_top_jet_y","Diff_8TeV_atop_pt","Diff_8TeV_atop_y","Diff_8TeV_atop_jet_pt","Diff_8TeV_atop_jet_y"]
for im in dicti:
    for it in dicti[im]:
        for ic in dicti[im][it]:
            if "13TeV" not in ic:
                if do_fix_R==False:
                    f = open(path_script+"script_"+im+"_"+it+"_"+ic+str_ma+".sh",'w')
                    f.write("cd /user/wenxing/ST_TW_channel/CMSSW_8_0_25/src")
                    f.write("\n")
                    f.write("eval `scramv1 runtime -sh`")
                    f.write("\n")
                    f.write("python "+path_exec+"fit_limit_deltachi2.py"+" -m "+'"'+im+'"'+" -e "+'"'+it+'"'+" -c "+'"'+ic+'"'+" "+str_Ma)
                    f.close()
                else:
                    #for iR in [0.95,0.99]:
                    #for iR in [0.95]:
                    #for iR in [0.99]:
                    for iR in [0.90]:
                        f = open(path_script+"script_"+im+"_"+it+"_"+ic+str_ma+"_R_"+str(iR)+".sh",'w')
                        f.write("cd /user/wenxing/ST_TW_channel/CMSSW_8_0_25/src")
                        f.write("\n")
                        f.write("eval `scramv1 runtime -sh`")
                        f.write("\n")
                        f.write("python "+path_exec+"fit_limit_deltachi2.py"+" -m "+'"'+im+'"'+" -e "+'"'+it+'"'+" -c "+'"'+ic+'"'+" "+str_Ma+ " -R "+str(iR))
                        f.write("\n")
                        f.write("python "+path_exec+"fit_limit_deltachi2_FixR1.py"+" -m "+'"'+im+'"'+" -e "+'"'+it+'"'+" -c "+'"'+ic+'"'+" "+str_Ma+ " -R "+str(iR))
                        f.write("\n")
                        f.write("python "+path_exec+"fit_limit_deltachi2_FixR2.py"+" -m "+'"'+im+'"'+" -e "+'"'+it+'"'+" -c "+'"'+ic+'"'+" "+str_Ma+ " -R "+str(iR))
                        f.close()
            else:
                #for iL in ["100fb","300fb","3000fb"]:
                for iL in ["300fb","3000fb"]:
                    f = open(path_script+"script_"+im+"_"+it+"_"+ic+str_ma+"_"+str(iL)+".sh",'w')
                    f.write("cd /user/wenxing/ST_TW_channel/CMSSW_8_0_25/src")
                    f.write("\n")
                    f.write("eval `scramv1 runtime -sh`")
                    f.write("\n")
                    f.write("python "+path_exec+"fit_limit_deltachi2.py"+" -m "+'"'+im+'"'+" -e "+'"'+it+'"'+" -c "+'"'+ic+'"'+" "+str_Ma+" -L "+'"'+iL+'"')
                    f.close()
