import os
import shutil


out_script_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/script/"
if os.path.exists(out_script_path):
        shutil.rmtree(out_script_path)
os.makedirs(out_script_path)
output_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/output/"

card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/"

top_n=10

chans=[]
chans.append("only_b")
chans.append("bplus_s")
cards=[]
cards.append("ee_1jet_1bjet.root")  
cards.append("ee_2jet_1bjet.root")  
cards.append("ee_2jet_2bjet.root")  
cards.append("ee_card.root")        
cards.append("ee_emu_mumu_1j1t_card.root")  
cards.append("ee_emu_mumu_card.root")       
cards.append("emu_11_21_22_card.root")      
cards.append("emu_11_21_card.root")         
cards.append("emu_1jet_0bjet.root")  
cards.append("emu_1jet_1bjet.root")  
cards.append("emu_2jet_1bjet.root")  
cards.append("emu_2jet_2bjet.root")  
cards.append("emu_card.root")         
cards.append("mumu_1jet_1bjet.root")
cards.append("mumu_2jet_1bjet.root")
cards.append("mumu_2jet_2bjet.root")
cards.append("mumu_card.root")

for card in cards:
    for chan in chans:
        f_out=open("%s%s_%s.sh"%(out_script_path,card,chan),"w")
        if not os.path.exists(str(output_path+card+"//"+chan)):
            os.makedirs(str(output_path+card+"//"+chan))
        expectS="1"
        if chan =="only_b":
            expectS="0"
        elif chan =="bplus_s":
            expectS="1"
        dicti={"output":str(output_path+card+"//"+chan),"card":str(card_path+card),"card_name":str(card.split(".root")[0]+"_"+chan),"expectS":expectS,"python":"~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/diffNuisances_wx.py","top_n":str(top_n+1)}
        tmp='''
cd %(output)s
eval `scramv1 runtime -sh`
combine -M MaxLikelihoodFit -d %(card)s -t -1 --expectSignal %(expectS)s
python %(python)s -a mlfit.root -g plots.root -n %(card_name)s_sorted > %(card_name)s
awk -F: 'NR>=2&&NR<=%(top_n)s{print $1 }' %(card_name)s_sorted.txt|xargs -I {} python %(python)s -a mlfit.root -g plots.root -n {} --poi {}
'''
        f_out.write(tmp%(dicti))
        f_out.close()
print "create script done!"



