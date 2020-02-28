import numpy as np


f_out = open("all_scripts.txt","w")

dir_EFT ='/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901'
dir_Cg  ='/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/ws_20180901_Cg'
dir_Cug ='/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tug_20180625'
dir_Ccg ='/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/ws_search_tcg_20180625'

Fast_Limit={}## value from ProfileLikelihood 
Fast_Limit['exp']={'Cg':0.76,'Cphiq':1.6 ,'Ctw':6.7,'Ctg':0.28,'Cug':0.44,'Ccg':0.62}
Fast_Limit['obs']={'Cg':1.00,'Cphiq':0.63,'Ctw':5.7,'Ctg':0.17,'Cug':0.33,'Ccg':0.36}


for cat in ['obs','exp']:
    str_exp=""
    if cat =='exp':str_exp='--expectedFromGrid 0.5'
    for channel in ['combined']:
        for ic in ['Cg','Cphiq','Ctw','Ctg','Cug','Ccg']:
            ic1 = ic
            dum = '1.00'
            if ic in ['Cphiq','Ctw','Ctg']:
                str_dir = dir_EFT
            elif ic in ['Cg']:
                str_dir = dir_Cg
            elif ic in ['Cug']:
                str_dir = dir_Cug
                ic1 = 'FCNC'
                dum = '0.10'
            elif ic in ['Ccg']:
                str_dir = dir_Ccg
                ic1 = 'FCNC'
                dum = '0.10'
            for ipoint in np.linspace(0.5*Fast_Limit[cat][ic],2*Fast_Limit[cat][ic],10):
                f_out.write('combine -M HybridNew --frequentist --testStat LHC %s/%s_%s_%s.root -H ProfileLikelihood --saveHybridResult --singlePoint %.2f --saveToys -s -1 --clsAcc 0  -n %s_%s_%s_r_%.2f %s\n'%(str_dir,channel,ic1,dum,float(ipoint),cat,channel,ic,float(ipoint),str_exp))
f_out.close()
print "done for creating script"
#combine -M HybridNew --frequentist --testStat LHC ../../ws_20180901/combined_Ctg_1.00.root -H ProfileLikelihood --saveHybridResult --singlePoint 0.22 --saveToys -s -1 --clsAcc 0 --expectedFromGrid 0.5 -n exp_combined_Ctg
