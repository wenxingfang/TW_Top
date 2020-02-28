import os

if False:
    files=os.listdir("./")
    #for cat in ['obs','exp']:
    for cat in ['obs']:
        #for ic in ['Cg', 'Ctg', 'Ctw', 'Cphiq', 'Cug', 'Ccg']:
        for ic in ['Cphiq']:
            print "%s_%s"%(cat,ic)
            for ifile in files:
                if cat in ifile and ic in ifile and "log" in ifile:
                        f_in = open(ifile,"r")
                        lines = f_in.readlines()
                        print type(lines)
                        for i in range(0,len(lines)):
                        #for line in lines:
                            if "NOT converge" not in lines[i]:continue
                        #    print line
                        #    idx = lines.index(line)
                        #    print idx
                            out = lines[i+2].split(":")[0]
                            print out

#ifile = "obs_Ctw_resub.sh.o32916067"
ifile = "obs_Cphiq_resub.sh.o32916566"
f_in = open(ifile,"r")
lines = f_in.readlines()
for i in range(0,len(lines)):
    if "NOT converge" not in lines[i]:continue
    out = lines[i+2].split(":")[0]
    print out
