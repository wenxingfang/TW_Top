import sys
import os
if len(sys.argv)<2:
    print "please give user name"
    sys.exit(0)
print "creating job info for %s"%(sys.argv[1])
os.system("qstat -f > ./qstat_tmp.txt")
f=open("./qstat_tmp.txt","r")
lines=f.readlines()

f_out=open(sys.argv[1]+"_job_info.txt","w")
li=0
max_wide=0
for line in lines:
    li+=1
    if str(sys.argv[1]+"@") in line:
        jobs_ID  =lines[li-3]
        jobs_name=lines[li-2]
        if len(line) > max_wide:
            max_wide=len(line)
        if len(jobs_ID) > max_wide:
            max_wide=len(jobs_ID)
        if len(jobs_name) > max_wide:
            max_wide=len(jobs_name)

ID_str  ="Job ID".center(max_wide)
name_str="Job name".center(max_wide)
user_str="Job user".center(max_wide)
f_out.write(ID_str)
f_out.write(name_str)
f_out.write(user_str)
f_out.write("\n")

li=0

for line in lines:
    li+=1
    if str(sys.argv[1]+"@") in line:
        job_ID  =lines[li-3].split("Job Id:")[-1]
        job_name=lines[li-2].split("Job_Name =")[-1]
        job_user=line.split("Job_Owner =")[-1]
        w_ID=job_ID[:-1].center(max_wide)
        w_name=job_name[:-1].center(max_wide)
        w_user=job_user[:-1].center(max_wide)
        f_out.write(w_ID)
        f_out.write(w_name)
        f_out.write(w_user)
        f_out.write("\n")

f_out.close()
os.system("rm ./qstat_tmp.txt")
print "done !"
