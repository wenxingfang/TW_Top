import os

#os.system("cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/impact/ee/obs/")
#os.system("nohup bash script_obs.sh &")
#os.system("cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/impact/ee/exp/")
#os.system("nohup bash script_exp.sh &")

os.system("cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/impact/emu/obs/")
os.system("nohup bash script_obs.sh &")
os.system("cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/impact/emu/exp/")
os.system("nohup bash script_exp.sh &")

os.system("cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/impact/mumu/obs/")
os.system("nohup bash script_obs.sh &")
os.system("cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/impact/mumu/exp/")
os.system("nohup bash script_exp.sh &")

os.system("cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/impact/combined/obs/")
os.system("nohup bash script_obs.sh &")
os.system("cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/impact/combined/exp/")
os.system("nohup bash script_exp.sh &")
print "done!"

