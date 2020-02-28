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

#ifile = "exp_Cphiq.sh.o32885932"
#ifile = "obs_Cphiq.sh.o32885926"
#ifile = "exp_Ctw.sh.o32885934"
#ifile = "exp_Ctg.sh.o32885931"
#ifile = "exp_Cg.sh.o32885924"
#ifile = "obs_Cg.sh.o32885930"
#ifile = "exp_Ccg.sh.o32885925"
#ifile = "obs_Ccg.sh.o32885929"
ifile = "obs_Cug.sh.o32885928"
f_in = open(ifile,"r")
lines = f_in.readlines()
for i in range(0,len(lines)):
    #if "Parameter :   Best-fit" not in lines[i]:continue
    if "Parameter" in lines[i] and "Best-fit" in lines[i]:
        out = lines[i+1].split(":")[0]
        print out
