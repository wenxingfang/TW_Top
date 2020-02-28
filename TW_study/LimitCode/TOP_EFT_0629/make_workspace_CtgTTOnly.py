import os

do_direct_search=True ## be true

#data_card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/data_card_combined/"
#output_path   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/script_create_ws/"
#ws_path       ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901_emu_11_21_22/"
#data_card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/data_card_1bin_combined/"
#output_path   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/script_create_ws/"
#ws_path       ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901_Cg_emu_11_21_22/"

#data_card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/data_card_combined_statonly/"
#output_path   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/script_create_ws/"
#ws_path       ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180323_statonly/"
#data_card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/data_card_1bin_combined_statonly/"
#output_path   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/script_create_ws/"
#ws_path       ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180323_1bin_statonly/"
#data_card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/data_card_Ptll_combined/"
#output_path   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/script_create_ws/"
#ws_path       ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180418_Ptll/"
#data_card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/data_card_combined_NoTopPtReW/"
#output_path   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/script_create_ws/"
#ws_path       ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20190608_NoTopPtReW/"
#data_card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/data_card_1bin_combined_NoTopPtReW/"
#output_path   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/script_create_ws/"
#ws_path       ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20190608_Cg_NoTopPtReW/"
data_card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/data_card_CtgTTOnly_combined/"
output_path   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/script_create_ws/"
ws_path       ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20190817_Ctg_TTOnly/"

if not os.path.exists(output_path):
    os.makedirs(output_path)
if not os.path.exists(ws_path):
    os.makedirs(ws_path)


filenames = os.listdir(data_card_path)
for fname in filenames:
    ncard=data_card_path+str(fname)
    ws_name=ws_path+str(fname).split(".txt")[0]+".root"
    f1 = open(output_path+"cws_"+str(fname).split(".txt")[0]+".sh",'w')
    f1.write("cd /user/wenxing/Limits/CMSSW_7_4_7/src")
    f1.write("\n")
    f1.write("eval `scramv1 runtime -sh`")
    f1.write("\n")
    model_name_1=fname.split(".txt")[0]
    model_name=model_name_1.replace(".","p")
    if do_direct_search==False:
        if "Ctg" in fname:
            model_name="TWTT_"+model_name
        elif "Cg" in fname or "Cphig" in fname:
            model_name="TT_"+model_name
        else:
            model_name="TW_"+model_name
        f1.write("text2workspace.py %s -o %s -P TOP_EFT_Models:%s \n"%(ncard,ws_name,model_name))
    else:
        model_name=""
        if "Ctg" in fname:
            model_name="Model_CtgTTOnly"
        elif "Ctw" in fname:
            model_name="Model_Ctw"
        elif "Cphiq" in fname:
            model_name="Model_Cphiq"
        elif "Cphig" in fname:
            model_name="Model_Cphig"
        elif "Cg" in fname:
            model_name="Model_Cg"
        f1.write("text2workspace.py %s -o %s -P TOP_EFT_Models_search_NLO:%s \n"%(ncard,ws_name,model_name))###for final
        #f1.write("text2workspace.py %s -o %s -P TOP_EFT_Models_search_NLO:%s_up \n"%(ncard,ws_name.replace(".root","_up.root"),model_name))###for final, scale up
        #f1.write("text2workspace.py %s -o %s -P TOP_EFT_Models_search_NLO:%s_down \n"%(ncard,ws_name.replace(".root","_down.root"),model_name))###for final, scale down
    f1.write('echo "done!"')
    f1.close()
print "done "
