import os

path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/GOD/output/"
filenames = os.listdir(path)

for chan in ["ee","emu","mumu","combined"]:
    for coup in ["Ctg","Ctw","Cphiq","Cg","Cug","Ccg"]:
        for cat in ["obs","exp"]:
            for filename in filenames:
                nfile = path +  filename
                if chan in filename and coup in filename and cat in filename:
                    god="null" 
                    File=open(nfile,"r")
                    lines=File.readlines()
                    if cat == "obs":
                        for line in lines:
                            if "Best fit test statistic:" in line:
                                tmp=line.split(":")[-1]
                                god=tmp.strip("\n")
                                break
                    else:
                        for line in lines:
                            if "median expected limit: r <" in line:
                                tmp=line.split("<")[-1]
                                god=tmp.split("@")[0]
                                break
                             
                    File.close()   
                    out_dir ={"ee":"ee","emu":"em","mumu":"mm","combined":"co"}
                    #print "|%s_%s_%s:%s|"%(out_dir[chan],coup,cat,god),
                    print "|%s_%s_%s:%.2f|"%(out_dir[chan],coup,cat,float(god)),
    print "\n",
