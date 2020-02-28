import os
path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/"
input_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card/"

channels=["ee","emu","mumu","ee_emu_mumu"]
dicti={}
dicti["ntoy"]=1
is_expect=True
for chan in channels:
    if not os.path.exists(path+str(chan)):
        os.makedirs(path+str(chan))
    f_out=open(path+str(chan)+"/script.sh","w")
    dicti["input_root"]=str(input_path)+str(chan)+"_card.root"
    template=''' '''
    if is_expect:
        template='''
combineTool.py -M Impacts -d %(input_root)s -m 125 --robustFit 1 --doInitialFit -t -%(ntoy)s --expectSignal=1
combineTool.py -M Impacts -d %(input_root)s -m 125 --robustFit 1 --doFits -t -%(ntoy)s --expectSignal=1
combineTool.py -M Impacts -d %(input_root)s -m 125 -t -%(ntoy)s --expectSignal=1 -o impacts.json
plotImpacts.py -i impacts.json -o impacts
'''
    f_out.write(template%dicti)
print "done!"
