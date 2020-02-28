import numpy as np
f=file("tmp.txt","r")
li=f.readlines()
num=[]
for i in li:
    a=i.strip("\n")
    num.append(float(a))
#    print a
#print num
print np.mean(num)
