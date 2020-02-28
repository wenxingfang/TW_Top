import os

do_search=True

#data_card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tug/"
#output_path   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/script_create_ws/"
#ws_path       ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tug_20180625/"
#data_card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tcg/"
#output_path   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/script_create_ws/"
#ws_path       ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_20180625/"

#data_card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tcg_statonly/"
#output_path   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/script_create_ws/"
#ws_path       ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_20180323_statonly/"
#data_card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tug_Ptll/"
#output_path   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/script_create_ws/"
#ws_path       ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tug_20180418_Ptll/"
#data_card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tug_NoTopPtReW/"
#output_path   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/script_create_ws/"
#ws_path       ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tug_20190608_NoTopPtReW/"
data_card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_combined_tcg_NoTopPtReW/"
output_path   ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/script_create_ws/"
ws_path       ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_20190608_NoTopPtReW/"

if not os.path.exists(output_path):
    os.makedirs(output_path)
if not os.path.exists(ws_path):
    os.makedirs(ws_path)


filenames = os.listdir(data_card_path)
for fname in filenames:
    ncard=data_card_path+str(fname)
    ws_name=ws_path+str(fname).split(".txt")[0]+".root"
    f1 = open(output_path+"cws_"+str(fname).split(".txt")[0]+".sh",'w')
    f1.write("cd /user/wenxing/Limits/CMSSW_7_4_7/src/")
    f1.write("\n")
    f1.write("eval `scramv1 runtime -sh`")
    f1.write("\n")
    if do_search:
        f1.write("text2workspace.py %s -o %s -P TOP_EFT_Models_search:Model_FCNC \n"%(ncard,ws_name))
    else:
        f1.write("text2workspace.py %s -o %s  \n"%(ncard,ws_name))
    f1.write('echo "done!"')
    f1.close()
print "done "
