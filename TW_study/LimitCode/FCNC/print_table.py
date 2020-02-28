import math
import ROOT
limt_dict={}
limt_dict["Cug_ee"      ]=[-0.432 , 0.432 ,-0.632 , 0.632 ]
limt_dict["Cug_emu"     ]=[-0.389 , 0.389 ,-0.561 , 0.561 ]
limt_dict["Cug_mumu"    ]=[-0.396 , 0.396 ,-0.570 , 0.570 ]
limt_dict["Cug_combined"]=[-0.313 , 0.313 ,-0.445 , 0.445 ]
limt_dict["Ccg_ee"      ]=[-0.488 , 0.488 ,-0.715 , 0.715 ]
limt_dict["Ccg_emu"     ]=[-0.438 , 0.438 ,-0.632 , 0.632 ]
limt_dict["Ccg_mumu"    ]=[-0.455 , 0.455 ,-0.652 , 0.652 ]
limt_dict["Ccg_combined"]=[-0.356 , 0.356 ,-0.509 , 0.509 ]
'''
exp:Cug  _ee                     | best: 0.000 | 1sigma:-0.432 to 0.432 | 2sigma:-0.632 to 0.632|
exp:Cug  _emu                    | best: 0.000 | 1sigma:-0.389 to 0.389 | 2sigma:-0.561 to 0.561|
exp:Cug  _mumu                   | best: 0.000 | 1sigma:-0.396 to 0.396 | 2sigma:-0.570 to 0.570|
exp:Cug  _combined               | best: 0.000 | 1sigma:-0.313 to 0.313 | 2sigma:-0.445 to 0.445|
exp:Ccg  _ee                     | best: 0.000 | 1sigma:-0.488 to 0.488 | 2sigma:-0.715 to 0.715|
exp:Ccg  _emu                    | best: 0.000 | 1sigma:-0.438 to 0.438 | 2sigma:-0.632 to 0.632|
exp:Ccg  _mumu                   | best: 0.000 | 1sigma:-0.455 to 0.455 | 2sigma:-0.652 to 0.652|
exp:Ccg  _combined               | best: 0.000 | 1sigma:-0.356 to 0.356 | 2sigma:-0.509 to 0.509|
obs:Cug  _ee                     | best: -0.025| 1sigma:-0.334 to 0.334 | 2sigma:-0.549 to 0.549|
obs:Cug  _emu                    | best: -0.025| 1sigma:-0.250 to 0.250 | 2sigma:-0.433 to 0.433|
obs:Cug  _mumu                   | best: -0.025| 1sigma:-0.249 to 0.249 | 2sigma:-0.431 to 0.431|
obs:Cug  _combined               | best: -0.025| 1sigma:-0.187 to 0.187 | 2sigma:-0.330 to 0.330|
obs:Ccg  _ee                     | best: -0.025| 1sigma:-0.368 to 0.368 | 2sigma:-0.607 to 0.607|
obs:Ccg  _emu                    | best: -0.025| 1sigma:-0.266 to 0.266 | 2sigma:-0.467 to 0.467|
obs:Ccg  _mumu                   | best: -0.025| 1sigma:-0.283 to 0.283 | 2sigma:-0.490 to 0.490|
obs:Ccg  _combined               | best: -0.025| 1sigma:-0.202 to 0.202 | 2sigma:-0.362 to 0.362|
'''
#limt_dict["Cug_ee"      ]=[-0.304,0.304,-0.511,0.511]
#limt_dict["Cug_emu"     ]=[-0.257,0.257,-0.448,0.448]
#limt_dict["Cug_mumu"    ]=[-0.284,0.284,-0.476,0.476]
#limt_dict["Cug_combined"]=[-0.234,0.234,-0.390,0.390]
#limt_dict["Ccg_ee"      ]=[-0.321,0.321,-0.553,0.553]
#limt_dict["Ccg_emu"     ]=[-0.259,0.259,-0.464,0.464]
#limt_dict["Ccg_mumu"    ]=[-0.304,0.304,-0.523,0.523]
#limt_dict["Ccg_combined"]=[-0.239,0.239,-0.415,0.415]
#exp:Cug  _ee                     | -0.442,0.442,-0.648,0.648|
#exp:Cug  _emu                    | -0.398,0.398,-0.574,0.574|
#exp:Cug  _mumu                   | -0.401,0.401,-0.580,0.580|
#exp:Cug  _combined               | -0.319,0.319,-0.452,0.452|
#exp:Ccg  _ee                     | -0.501,0.501,-0.734,0.734|
#exp:Ccg  _emu                    | -0.447,0.447,-0.645,0.645|
#exp:Ccg  _mumu                   | -0.461,0.461,-0.662,0.662|
#exp:Ccg  _combined               | -0.363,0.363,-0.517,0.517|
#obs:Cug  _ee                     | -0.304,0.304,-0.511,0.511|
#obs:Cug  _emu                    | -0.257,0.257,-0.448,0.448|
#obs:Cug  _mumu                   | -0.284,0.284,-0.476,0.476|
#obs:Cug  _combined               | -0.234,0.234,-0.390,0.390|
#obs:Ccg  _ee                     | -0.321,0.321,-0.553,0.553|
#obs:Ccg  _emu                    | -0.259,0.259,-0.464,0.464|
#obs:Ccg  _mumu                   | -0.304,0.304,-0.523,0.523|
#obs:Ccg  _combined               | -0.239,0.239,-0.415,0.415|



#exp:Cug  _ee                     [-0.43,0.43,-0.63,0.63]
#exp:Cug  _emu                    [-0.37,0.37,-0.53,0.53]
#exp:Cug  _mumu                   [-0.40,0.40,-0.57,0.57]
#exp:Cug  _combined               [-0.32,0.32,-0.45,0.45]
#exp:Ccg  _ee                     [-0.49,0.49,-0.70,0.70]
#exp:Ccg  _emu                    [-0.41,0.41,-0.59,0.59]
#exp:Ccg  _mumu                   [-0.46,0.46,-0.66,0.66]
#exp:Ccg  _combined               [-0.36,0.36,-0.52,0.52]
#
#obs:Cug  _ee                     [-0.24,0.24,-0.43,0.43]
#obs:Cug  _emu                    [-0.25,0.25,-0.41,0.41]
#obs:Cug  _mumu                   [-0.24,0.24,-0.44,0.44]
#obs:Cug  _combined               [-0.18,0.18,-0.32,0.32]
#obs:Ccg  _ee                     [-0.26,0.26,-0.48,0.48]
#obs:Ccg  _emu                    [-0.27,0.27,-0.45,0.45]
#obs:Ccg  _mumu                   [-0.27,0.27,-0.48,0.48]
#obs:Ccg  _combined               [-0.19,0.19,-0.35,0.35]


#limt_dict["Cug_ee"                ]=[-0.48,0.48,-0.69,0.69]
#limt_dict["Cug_emu"               ]=[-0.34,0.34,-0.49,0.49]
#limt_dict["Cug_emu_1j1t"          ]=[-0.48,0.48,-0.71,0.71]
#limt_dict["Cug_emu_1j1t_2j1t_2j2t"]=[-0.40,0.40,-0.59,0.59]
#limt_dict["Cug_mumu"              ]=[-0.39,0.39,-0.56,0.56]
#limt_dict["Cug_combined"          ]=[-0.28,0.28,-0.41,0.41]
#limt_dict["Ccg_ee"                ]=[-0.54,0.54,-0.78,0.78]
#limt_dict["Ccg_emu"               ]=[-0.38,0.38,-0.55,0.55]
#limt_dict["Ccg_emu_1j1t"          ]=[-0.54,0.54,-0.80,0.80]
#limt_dict["Ccg_emu_1j1t_2j1t_2j2t"]=[-0.45,0.45,-0.67,0.67]
#limt_dict["Ccg_mumu"              ]=[-0.44,0.44,-0.64,0.64]
#limt_dict["Ccg_combined"          ]=[-0.33,0.33,-0.46,0.46]

#Sigma_Cug=68
#Sigma_Ccg=18

Br=0.324

Sigma_Cug=16.7*Br*Br
Sigma_Ccg=4.57*Br*Br

k_factor=1.27

#Factor=math.pow(172.5,5.0)/(6*3.14159*1e12*1.33)
Factor=float(0.033/1.33)

for Coup in ["Cug","Ccg"]:
    for chan in ["ee","emu","mumu","combined"]:
        for region in ["","_1j1t","_1j1t_2j1t_2j2t"]:
            str_key=Coup+"_"+chan+region
            if str_key not in limt_dict:continue
            print " ++++++++++Channel %s%s +++++++"%(str(chan),str(region))
            print "$\sigma$(pp$\\rightarrow$tW)$\\times$B(W$\\rightarrow \ell\\nu$)$^2$",
            print "& {[}0,%.2f{]} pb & {[}0,%.2f{]} pb \\\\"%(float(limt_dict[str_key][0]*limt_dict[str_key][0]),float(limt_dict[str_key][2]*limt_dict[str_key][2]))
            print "$%s$"%(str(Coup)),
            scale=1
            if Coup=="Cug":scale=math.sqrt(Sigma_Cug*k_factor)
            elif Coup=="Ccg":scale=math.sqrt(Sigma_Ccg*k_factor)
            print "& {[}%.2f,%.2f{]} & {[}%.2f,%.2f{]} \\\\"%(float(limt_dict[str_key][0]/scale),float(limt_dict[str_key][1]/scale),float(limt_dict[str_key][2]/scale),float(limt_dict[str_key][3]/scale))
            if Coup=="Cug":
                print "B(t $\\rightarrow$ ug)",
                #B_scale=100*2*4.292/(22.9*100)
                #print "& {[}0,%.3f\\%%{]} & {[}0,%.3f\\%%{]} \\\\"%(float(limt_dict[str_key][0]*limt_dict[str_key][0]*B_scale),float(limt_dict[str_key][2]*limt_dict[str_key][2]*B_scale))
                print "& {[}0,%.5f\\%%{]} & {[}0,%.5f\\%%{]} \\\\"%(float(100*limt_dict[str_key][0]*limt_dict[str_key][0]*Factor/(k_factor*Sigma_Cug)),float(100*limt_dict[str_key][2]*limt_dict[str_key][2]*Factor/(k_factor*Sigma_Cug)))
                 
    
            elif Coup=="Ccg":
                print "B(t $\\rightarrow$ cg)",
                #B_scale=100*2*4.292/(6.06*100)
                #print "& {[}0,%.3f\\%%{]} & {[}0,%.3f\\%%{]} \\\\"%(float(limt_dict[str_key][0]*limt_dict[str_key][0]*B_scale),float(limt_dict[str_key][2]*limt_dict[str_key][2]*B_scale))
                print "& {[}0,%.5f\\%%{]} & {[}0,%.5f\\%%{]} \\\\"%(float(100*limt_dict[str_key][0]*limt_dict[str_key][0]*Factor/(k_factor*Sigma_Ccg)),float(100*limt_dict[str_key][2]*limt_dict[str_key][2]*Factor/(k_factor*Sigma_Ccg)))
