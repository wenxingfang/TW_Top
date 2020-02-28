import math
G_F=1.16637e-5
MT=172.5
MW=80.385
aphi_s=0.118
value=G_F*math.pow(MT,3)*math.pow((1-math.pow(MW/MT,2)),2)*(1+2*math.pow(MW/MT,2))*(1-((2*aphi_s)/(3*math.pi))*((2*math.pi*math.pi/3)-(5/2)))/(8*math.pi*math.sqrt(2))
print value

