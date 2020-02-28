import math
'''
############################# HybridNew ####################
obs_Cug     = 0.407997 /math.sqrt(16.7*0.324*0.324*1.27)
obs_Cug_err = 0.0378639/math.sqrt(16.7*0.324*0.324*1.27)
exp_Cug     = 0.440891 /math.sqrt(16.7*0.324*0.324*1.27)
exp_Cug_err = 0.0117268/math.sqrt(16.7*0.324*0.324*1.27)

obs_Ccg     = 0.475376 /math.sqrt(4.57*0.324*0.324*1.27)
obs_Ccg_err = 0.036248 /math.sqrt(4.57*0.324*0.324*1.27)
exp_Ccg     = 0.537908 /math.sqrt(4.57*0.324*0.324*1.27)
exp_Ccg_err = 0.0209768/math.sqrt(4.57*0.324*0.324*1.27)

print "obs Cug=%f +- %f"%(obs_Cug,obs_Cug_err)
print "exp Cug=%f +- %f"%(exp_Cug,exp_Cug_err)
print "obs Ccg=%f +- %f"%(obs_Ccg,obs_Ccg_err)
print "exp Ccg=%f +- %f"%(exp_Ccg,exp_Ccg_err)
'''
'''
############################# ProfileLikelihood  ####################
obs_Cug     = 0.330748 /math.sqrt(16.7*0.324*0.324*1.27)
exp_Cug     = 0.466487 /math.sqrt(16.7*0.324*0.324*1.27)

obs_Ccg     = 0.363208 /math.sqrt(4.57*0.324*0.324*1.27)
exp_Ccg     = 0.550083 /math.sqrt(4.57*0.324*0.324*1.27)

print "obs Cug=%f"%(obs_Cug)
print "exp Cug=%f"%(exp_Cug)
print "obs Ccg=%f"%(obs_Ccg)
print "exp Ccg=%f"%(exp_Ccg)
'''
'''
############################# Asymptotic  ####################
obs_Cug     = 0.3834 /math.sqrt(16.7*0.324*0.324*1.27)
exp_Cug     = 0.4484 /math.sqrt(16.7*0.324*0.324*1.27)

obs_Ccg     = 0.4306 /math.sqrt(4.57*0.324*0.324*1.27)
exp_Ccg     = 0.5109 /math.sqrt(4.57*0.324*0.324*1.27)

print "obs Cug=%f"%(obs_Cug)
print "exp Cug=%f"%(exp_Cug)
print "obs Ccg=%f"%(obs_Ccg)
print "exp Ccg=%f"%(exp_Ccg)
'''

############################# Using MaxLikelihoodFit to check the confident interval @ 68%  ####################
obs_Cug     = 0.187021 /math.sqrt(16.7*0.324*0.324*1.27)
exp_Cug     = 0.313038 /math.sqrt(16.7*0.324*0.324*1.27)

obs_Ccg     = 0.202537 /math.sqrt(4.57*0.324*0.324*1.27)
exp_Ccg     = 0.342583 /math.sqrt(4.57*0.324*0.324*1.27)

print "obs Cug=%f"%(obs_Cug)
print "exp Cug=%f"%(exp_Cug)
print "obs Ccg=%f"%(obs_Ccg)
print "exp Ccg=%f"%(exp_Ccg)


