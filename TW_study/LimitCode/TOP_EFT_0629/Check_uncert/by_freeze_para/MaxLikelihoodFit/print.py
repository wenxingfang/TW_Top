import os
import math

for cat in ['obs']:
#for cat in ['obs','exp']:
    for ic in ['Cg','Ctg','Ctw','Cphiq','Cug','Ccg']:
    #for ic in ['Cphiq']:
        print "########## %s %s ################"%(cat,ic)
        files=os.listdir('./%s/%s'%(cat,ic))
        tmp_dict={}
        for ifile in files:
            if '.log' not in ifile:continue
            f=open('./%s/%s/%s'%(cat,ic,ifile),'r')
            lines=f.readlines()
            hasError = 0
            hasBest =0
            for line in lines:
                if 'SysError' in line: continue
                if ('Error' in line) or ('ERROR' in line) or ('error' in line) or ('NOT' in line) or ('Not' in line) or ('not' in line) or ('fail' in line) or ('Fail' in line):hasError=1
                if ('Best' in line) and ('fit' in line):
                    str1=line.split(':')[-1]
                    str2=str1.split('(')[0]
                    mean=str2.split('  ')[0]
                    CI  =str2.split('  ')[1]
                    low=CI.split('/')[0]
                    up =CI.split('/')[1]
                    value_CI=float(up)-float(low)
                    bestfit= '%-50s:%-10d:%-20s,%-20s,%-20s'%(ifile,hasError,mean,low,up)
                    tmp_dict[bestfit]=value_CI
                    hasBest=1
                    #print '%-50s:%d:%-20s,%-20s,%-20s'%(ifile,hasError,mean,low,up)
            if hasBest == 0:
                tmp_dict[ifile]=999
        total=999.0
        for i in tmp_dict:
            if 'Total' in i:
                total=tmp_dict[i]
                break              
        Max=0
        if False:
            for i in tmp_dict:
                if tmp_dict[i]!=999 and tmp_dict[i]>Max:Max=tmp_dict[i]
            total=Max    

        tmp=sorted(tmp_dict.items(), key=lambda item:item[1])
        print '%-50s:%-10s:%-20s,%-20s,%-20s,%-20s'%("sys",'status','mean','down','up','CI')
        for it in tmp:
            #print it,
            print "%s,%-20s,"%(it[0],str(it[1])),
            if 'Freeze' not in it[0]:
                if total >= it[1]:
                    print "%-20s%%"%(str(100*math.sqrt(math.pow(total,2)-math.pow(it[1],2))/total))
                    #print "%-20s%%"%(str(100*(total-it[1])/total))
                else:
                    print "%-20s%%"%(str("0"))
            else:
                print "%-20s%%"%(str(100*it[1]/total))
        print "#######################"
#Best fit r: -0.155843  -0.569426/+0.568985  (68% CL)
