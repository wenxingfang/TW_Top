import os
import ROOT
import math



class out_object:
    def __init__(self, name, input_path, output_name,  real, method):
        self.name = name
        self.input_path = input_path
        self.output_name = output_name
        self.filenames = os.listdir(self.input_path)
        self.real=real
        self.method=method
    def print_info(self):
        f1 = open(self.output_name,'w')
        N=0
        dir_limit={}
        for ifile in  self.filenames:
            N=N+1
            if N%1000==0:
                print N
            file_name=self.input_path+ifile
            if ".log" not in file_name:continue
            str_key=ifile.split(".log")[0]
            dir_limit[str_key]=[]
            f2 = open(file_name,'r') 
            lines = f2.readlines()
            for li in lines:
                li=li.strip("\n")
                if "obs" in file_name:
                    if self.method=="Asymptotic":
                        if "Observed Limit"in li:
                            value=str(li.split("<")[-1])
                            value=value.strip(" ")
                            dir_limit[str_key].append(value)
                            break
                    elif self.method=="HybridNew":
                        if "Limit: CMS_TW_mu <" in li and "@ 95% CL" in li:
                            value=str(li.split("<")[-1])
                            value_1=value.split("+")[0]
                            value_1=value_1.strip(" ")
                            dir_limit[str_key].append(value_1)
                            break
                elif "exp" in file_name:
                    if "mean   expected limit" in li or "median expected limit" in li:
                        dir_limit[str_key].append(li.split("@")[0])
                    elif "68% expected band" in li or "95% expected band" in li:
                        dir_limit[str_key].append(li)
                          
            f2.close()
        
#        print dir_limit
        for ic in ["FCNC"]:
            for chan in ["ee","emu","mumu","combined"]:
                for sf in ["1.00", "0.02","0.05", "0.10", "0.15", "0.20", "0.25", "0.30","0.50"]:
                    for io in ["obs","exp"]:
                        ikey=str(io+"_"+chan+"_"+ic+"_"+sf)
                        if ikey in dir_limit:
                            if self.real==True:
                                if io=="obs" and len(dir_limit[ikey])!=0:
                                    real_c=float(dir_limit[ikey][0])*float(sf)*float(XS)
                                    dir_limit[ikey][0]=str(real_c)
                                elif io=="exp":
                                    for ie in dir_limit[ikey]:
                                        if "mean   expected limit" in ie:
                                            tmp_1=ie.split("<")[-1]       
                                            tmp_2=tmp_1.split("+")[0]
                                            tmp_3=tmp_2.strip(" ")
                                            val=float(tmp_3)*float(sf)*float(XS)
                                            dir_limit[ikey][dir_limit[ikey].index(ie)]="mean   expected limit: < %s"%(str(val))
                                        elif "median expected limit" in ie:
                                            tmp_1=ie.split("<")[-1]
                                            tmp_2=tmp_1.strip(" ")
                                            val=float(tmp_2)*float(sf)*float(XS) 
                                            dir_limit[ikey][dir_limit[ikey].index(ie)]="median expected limit: < %s"%(str(val))
                                        elif "68% expected band" in ie or "95% expected band" in ie:
                                            tmp_1=ie.split(":")[-1]
                                            tmp_2=tmp_1.split("< r <")[0].strip(" ")  
                                            tmp_3=tmp_1.split("< r <")[-1].strip(" ")  
                                            val_1=float(tmp_2)*float(sf)*float(XS) 
                                            val_2=float(tmp_3)*float(sf)*float(XS) 
                                            dir_limit[ikey][dir_limit[ikey].index(ie)]=("68% expected band: "+str(val_1)+"-"+str(val_2)) if "68%" in ie else ("95% expected band: "+str(val_1)+"-"+str(val_2))
                            f1.write(ikey+":"+str(dir_limit[ikey]))
                            f1.write('\n')
        f1.close()
 
#method="HybridNew"
method="Asymptotic"

XS=10

date="_20170720"
transfer_to_real=True
str_real=""
if transfer_to_real:
    str_real="_real"
obj_list=[]
obj_list.append(out_object(str_real,"./result_0719_100Toy_fullsim/"             ,"tug_FullSim_"+str_real+date+"_"+method+"_100Toy.txt", transfer_to_real , method))
obj_list.append(out_object(str_real,"./result_0719_100Toy_fastsim_noSignalStat/","tug_FastSim_"+str_real+date+"_"+method+"_100Toy.txt", transfer_to_real , method))


for i in obj_list:
    i.print_info()
    print "%s is done"%(i.output_name)
