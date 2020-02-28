import numpy as np
f=file("tmp.txt","r")
li=f.readlines()
num=[]
N_effective=0
N_weighted =0
for i in li:
    a=i.strip("\n")
    num.append(float(a))
    N_weighted +=float(a)
    N_effective = N_effective+1 if float(a) >0 else N_effective-1
#    print a
#print num
print np.mean(num)
print "N effective : %f"%(N_effective)
print "N weighted  : %f"%(N_weighted)
