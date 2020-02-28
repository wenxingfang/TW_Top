import os
import shutil


out_script_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/impact/script/"
if os.path.exists(out_script_path):
        shutil.rmtree(out_script_path)
os.makedirs(out_script_path)
output_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/impact/output/"

card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/"

chans=[]
chans.append("exp")
chans.append("obs")
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
cards.append("ee_emu_card.root")       
cards.append("ee_mumu_card.root")       
cards.append("emu_mumu_card.root")       

for card in cards:
    for chan in chans:
        f_out=open("%s%s_%s.sh"%(out_script_path,card,chan),"w")
        if not os.path.exists(str(output_path+card+"//"+chan)):
            os.makedirs(str(output_path+card+"//"+chan))
        dicti={"output":str(output_path+card+"//"+chan),"card":str(card_path+card),"card_name":str(card.split(".root")[0]+"_"+chan)}
        if chan =="obs":
            tmp1='''
cd %(output)s
eval `scramv1 runtime -sh`
logsave -a log.txt combineTool.py -M Impacts -d %(card)s -m 125 --rMax 3 --robustFit 1 --minimizerTolerance=0.001 --doInitialFit
logsave -a log.txt combineTool.py -M Impacts -d %(card)s -m 125 --rMax 3 --robustFit 1 --minimizerTolerance=0.01  --doFits     --parallel 8 
logsave -a log.txt combineTool.py -M Impacts -d %(card)s -m 125  -o impacts.json
logsave -a log.txt plotImpacts.py -i impacts.json -o impacts_%(card_name)s
'''
            f_out.write(tmp1%(dicti))
            
        elif chan =="exp":
            tmp1='''
cd %(output)s
eval `scramv1 runtime -sh`
logsave -a log.txt combineTool.py -M Impacts -d %(card)s -m 125 --rMax 3 --robustFit 1 --minimizerTolerance=0.001 --doInitialFit             -t -1 --expectSignal=1 
logsave -a log.txt combineTool.py -M Impacts -d %(card)s -m 125 --rMax 3 --robustFit 1 --minimizerTolerance=0.01  --doFits     --parallel 8  -t -1 --expectSignal=1 
logsave -a log.txt combineTool.py -M Impacts -d %(card)s -m 125  -o impacts.json             -t -1 --expectSignal=1
logsave -a log.txt plotImpacts.py -i impacts.json -o impacts_%(card_name)s
'''
            f_out.write(tmp1%(dicti))
        f_out.close()
print "create script done!"



