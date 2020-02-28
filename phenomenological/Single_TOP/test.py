import ROOT
import numpy



list_x=[1.0,2.0,3.0,4.0,4.0,3.0,2.0,1.0]
list_y=[1.1,2.2,3.3,4.4,3.6,2.7,1.8,0.9]

exp_x=numpy.array(list_x)
exp_y=numpy.array(list_y)
print exp_x
print exp_y
GraphErr2Sig=ROOT.TGraph(len(exp_x),exp_x,exp_y)
#GraphErr2Sig=ROOT.TGraphAsymmErrors(len(exp_x),exp_x,exp_y)
GraphErr2Sig.SetFillColor(ROOT.kYellow+1)
GraphErr2Sig.SetMarkerStyle(8)

cCL=ROOT.TCanvas("cCL", "cCL",0,0,700,500)
cCL.cd()
DummyGraph=ROOT.TH2D("DummyGraph","",1,0,10,1,0,10)
DummyGraph.Draw()
GraphErr2Sig.Draw("pl")
#GraphErr2Sig.Draw("F")
cCL.Print("./test.png","png")
