import os

#input_path ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_tug/"
#output_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tug/"
#input_path ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_tcg/"
#output_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tcg/"

#input_path ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_tcg_statonly/"
#output_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tcg_statonly/"
#input_path ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_tug_Ptll/"
#output_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tug_Ptll/"
#input_path ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_tug_NoTopPtReW/"
#output_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tug_NoTopPtReW/"
input_path ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_tcg_NoTopPtReW/"
output_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tcg_NoTopPtReW/"

if not os.path.exists(output_path):
    os.makedirs(output_path)

#ee_region=["ee_1jet_1bjet","ee_2jet_1bjet","ee_2jet_2bjet"]
#mumu_region=["mumu_1jet_1bjet","mumu_2jet_1bjet","mumu_2jet_2bjet"]
#emu_region=["emu_1jet_0bjet","emu_1jet_1bjet","emu_2jet_1bjet","emu_2jet_2bjet"]
#emu_region=["emu_1jet_1bjet"]
#emu_region=["emu_1jet_1bjet","emu_2jet_1bjet","emu_2jet_2bjet"]
ee_region=["ee_xjet_1bjet"]
mumu_region=["mumu_xjet_1bjet"]
emu_region=["emu_xjet_1bjet"]
ee_emu_mumu_region=[]
ee_emu_mumu_region.extend(ee_region)
ee_emu_mumu_region.extend(emu_region)
ee_emu_mumu_region.extend(mumu_region)


f_combine=open("make_combined_card.sh","w")
f_combine.write("cd "+input_path+"\n")
#for sf in ["1.00", "0.05", "0.10", "0.15", "0.20", "0.25", "0.30","0.02","0.50"]:
for sf in ["0.10"]:
    for chan in ["ee","emu","mumu","combined"]:
        command=""
        if chan == "emu":
            command="combineCards.py " 
            N=1
            for ir in emu_region:
                name="Name"+str(N)+"="+ir+"_FCNC"+"_"+str(sf)+".txt"
                N=N+1
                command=command+" "+name
            command=command+" > "+output_path+str(chan)+"_FCNC"+"_"+str(sf)+".txt"
        elif chan == "ee":
            command="combineCards.py " 
            N=1
            for ir in ee_region:
                name="Name"+str(N)+"="+ir+"_FCNC"+"_"+str(sf)+".txt"
                N=N+1
                command=command+" "+name
            command=command+" > "+output_path+str(chan)+"_FCNC"+"_"+str(sf)+".txt"
        elif chan == "mumu":
            command="combineCards.py " 
            N=1
            for ir in mumu_region:
                name="Name"+str(N)+"="+ir+"_FCNC"+"_"+str(sf)+".txt"
                N=N+1
                command=command+" "+name
            command=command+" > "+output_path+str(chan)+"_FCNC"+"_"+str(sf)+".txt"
        elif chan == "combined":
            command="combineCards.py " 
            N=1
            for ir in ee_emu_mumu_region:
                name="Name"+str(N)+"="+ir+"_FCNC"+"_"+str(sf)+".txt"
                N=N+1
                command=command+" "+name
            command=command+" > "+output_path+str(chan)+"_FCNC"+"_"+str(sf)+".txt"
        f_combine.write(command+"\n")
str_echo='echo '"'done!'"''
f_combine.write(str_echo+"\n")
print "make_combined_card.sh is created!!"
