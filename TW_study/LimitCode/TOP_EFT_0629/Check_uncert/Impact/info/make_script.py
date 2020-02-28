import os

if False:
    dict_r = {}
    dict_r['Cg']    = [-1, 1]
    dict_r['Ctg']   = [-0.5, 0.5]
    dict_r['Ctw']   = [-2, 7]
    dict_r['Cphiq'] = [-4, 2]
    dict_r['Cug']   = [-2, 2]
    dict_r['Ccg']   = [-2, 2]
    
    for cat in ['obs','exp']:
        for ic in ['Cg', 'Ctg', 'Ctw', 'Cphiq', 'Cug', 'Ccg']:
            str1 = 'cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/Impact/%s/%s'%(cat, ic)
            str2 = 'eval `scramv1 runtime -sh`'
            wk_path = '/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/'
            icname = 'higgsCombine%s.MultiDimFit.mH120.root'%(ic)
            wk_path1= wk_path + icname
            exp_obs = '-t -1 --expectSignal=0' if cat == 'exp' else ' '
            str5 = 'combineTool.py -M Impacts -d %s -m 125 -o impacts.json %s'%(wk_path1, exp_obs)
            str6 = 'plotImpacts.py -i impacts.json -o impacts_%s_%s'%(cat, ic)
            script_path = './scripts/'
            script_name = '%s_%s.sh'%(cat, ic)
            f = open(script_path+script_name,'w')
            f.write(str1+'\n')
            f.write(str2+'\n')
            f.write(str3+'\n')
            f.write(str4+'\n')
            f.write(str5+'\n')
            f.write(str6+'\n')
            f.close()
    print 'done!'
        
if False:
    files=os.listdir("./")
    for cat in ['obs','exp']:
        for ic in ['Cg', 'Ctg', 'Ctw', 'Cphiq', 'Cug', 'Ccg']:
            for ifile in files:
                #if cat in ifile and ic in ifile and ".sh.o" in ifile:
                if cat in ifile and ic in ifile and "log" in ifile:
                    print ifile
                    f_in = open(ifile,"r")
                    f_out= open(cat+"_"+ic+".txt","w")
                    lines = f_in.readlines()
                    for line in lines:
                        if "combine" not in line:continue
                        line_out = line.split(">>")[-1]
                        f_out.write(line_out)
                    f_out.close()
                    f_in.close()
    print "done"


if True:

    dict_r = {}
    dict_r['Cg']    = [-1, 1]
    dict_r['Ctg']   = [-0.5, 0.5]
    dict_r['Ctw']   = [-2, 7]
    #dict_r['Cphiq'] = [-4, 2]
    dict_r['Cphiq'] = [-4, 0]
    dict_r['Cug']   = [-2, 2]
    dict_r['Ccg']   = [-2, 2]

    Resub={}
    Resub['obs']={}
    Resub['exp']={}
    Resub['obs']['Cg']=[]
    Resub['obs']['Ctg']=[]
    Resub['obs']['Ctw']=[]
    Resub['obs']['Ctw'].append('ee_2jet_1bjet_other_stat_bin3_')
    Resub['obs']['Ctw'].append('emu_1jet_0bjet_TW_stat_bin1_')
    Resub['obs']['Ctw'].append('emu_2jet_1bjet_other_stat_bin5_')



    Resub['obs']['Cphiq']=[]
    Resub['obs']['Cphiq'].append('ee_2jet_1bjet_TW_stat_bin2_')
    Resub['obs']['Cphiq'].append('ee_2jet_1bjet_other_stat_bin1_')
    Resub['obs']['Cphiq'].append('ee_2jet_2bjet_TW_stat_bin1_')
    Resub['obs']['Cphiq'].append('emu_2jet_1bjet_TW_stat_bin5_')
    Resub['obs']['Cphiq'].append('emu_2jet_1bjet_other_stat_bin5_')
    Resub['obs']['Cphiq'].append('mumu_2jet_1bjet_other_stat_bin3_')
    Resub['obs']['Cphiq'].append('mumu_2jet_2bjet_TW_stat_bin1_')



    Resub['obs']['Cug']  =[]
    Resub['obs']['Ccg']  =[]
    Resub['exp']['Cg']   =[]
    Resub['exp']['Ctg']  =[]
    Resub['exp']['Ctw']  =[]
    Resub['exp']['Cphiq']=[]
    Resub['exp']['Cug']  =[]
    Resub['exp']['Ccg']  =[]
  
    for cat in Resub:
        for ic in Resub[cat]:
            if len(Resub[cat][ic])==0: continue
            f_out = open('script_resub/%s_%s_resub.sh'%(cat,ic),'w')
            str1 = 'cd /user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/Impact/%s/%s'%(cat, ic)
            str2 = 'eval `scramv1 runtime -sh`'
            wk_path = '/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/TOP_EFT_0629/Check_uncert/print_uncertinties/workspace/'
            icname = 'higgsCombine%s.MultiDimFit.mH120.root'%(ic)
            wk_path1= wk_path + icname
            exp_obs = '-t -1 --expectSignal=0' if cat == 'exp' else ' '
            f_out.write(str1+'\n')
            f_out.write(str2+'\n')
            for sys in Resub[cat][ic]:
                str3='logsave -a log_resub.txt combine -M MultiDimFit -n _paramFit_Test_%s --algo impact --redefineSignalPOIs r -P %s --floatOtherPOIs 1 --saveInactivePOI 1 --setPhysicsModelParameterRanges r=%.1f,%.1f --robustFit 1 --minimizerTolerance=0.001 %s -m 125 -d %s'%(sys,sys,dict_r[ic][0], dict_r[ic][1], exp_obs, wk_path1)
                f_out.write(str3+'\n')
            f_out.close()
    print 'done'

