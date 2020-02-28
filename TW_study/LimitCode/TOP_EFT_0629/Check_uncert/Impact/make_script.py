import os

if True:
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
            str3 = 'logsave -a log.txt combineTool.py -M Impacts -d %s -m 125 --setPhysicsModelParameterRanges r=%.1f,%.1f --robustFit 1 --minimizerTolerance=0.001 --doInitialFit %s'%(wk_path1,dict_r[ic][0], dict_r[ic][1], exp_obs)
            #str4 = 'logsave -a log.txt combineTool.py -M Impacts -d %s -m 125 --setPhysicsModelParameterRanges r=%.1f,%.1f --robustFit 1 --minimizerTolerance=0.01  --doFits  --parallel 8 %s'%(wk_path1,dict_r[ic][0], dict_r[ic][1], exp_obs)
            str4 = 'logsave -a log.txt combineTool.py -M Impacts -d %s -m 125 --setPhysicsModelParameterRanges r=%.1f,%.1f --robustFit 1 --minimizerTolerance=0.01  --doFits  %s'%(wk_path1,dict_r[ic][0], dict_r[ic][1], exp_obs)
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
                if cat in ifile and ic in ifile and ".sh.o" in ifile:
                    print ifile
                    f_in = open(ifile,"r")
                    f_out= open(cat+"_"+ic+".txt","w")
                    lines = f_in.readlines()
                    for line in lines:
                        if "combine" not in line:continue
                        f_out.write(line)
                    f_out.close()
                    f_in.close()
    print "done"
























