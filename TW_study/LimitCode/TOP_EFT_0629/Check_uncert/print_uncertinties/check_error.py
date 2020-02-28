import os

path="./log"

for iname in os.listdir(path):
    with open(path+str("/")+iname,"r") as f:
        lines=f.readlines()
        for line in lines:
            if "Minos error" in line:
            #if "Error" in line or "error" in line or "Not" in line or "not" in line or "NOT" in line:
                print "bin=%s :line %d: %s"%(iname.split(".sh")[0],lines.index(line),str(line))
                break
print "done"
