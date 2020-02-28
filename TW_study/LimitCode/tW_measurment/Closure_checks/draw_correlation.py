import os
import ROOT
ROOT.gROOT.SetBatch(ROOT.kTRUE)
input_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks/output/"

chans=[]
chans.append("only_b")
chans.append("bplus_s")

for cat in os.listdir(input_path):
    for chan in chans:
        nuisances=[]
        for filename in os.listdir(input_path+cat+"/"+chan):
            if ".txt" not in filename: continue
            if "_clean" in filename: continue
            if "_sorted" in filename:
               # print "for "+str(input_path+cat+"/"+chan+"/"+filename)
                tmp=open(input_path+cat+"/"+chan+"/"+filename,"r")
                lines=tmp.readlines()
                file_out=open(input_path+cat+"/"+chan+"/"+cat+"_clean.txt","w")
                for line in lines:
                    line1=line.replace("\n","")
                    sp_line=line1.split(":")
                    if chan=="only_b":
                        file_out.write("\n"+sp_line[0]+sp_line[1]+sp_line[3])
                    elif chan=="bplus_s":
                        file_out.write("\n"+sp_line[0]+sp_line[2]+sp_line[3])
                file_out.close()
                tmp.close()
            else:
                nuisances.append(filename.split(".txt")[0])
        so_nuisances=sorted(nuisances)
        h_corr=ROOT.TH2F("%s_%s"%(cat,chan),"%s(%s)"%(cat.split(".root")[0],chan.replace("plus_","+")),len(so_nuisances),0,len(so_nuisances),len(so_nuisances),0,len(so_nuisances))
        h_corr.SetStats(ROOT.kFALSE)
        h_corr.GetXaxis().SetLabelSize(0.03)
        h_corr.GetXaxis().SetLabelFont(62)
        h_corr.GetYaxis().SetLabelSize(0.03)
        h_corr.GetYaxis().SetLabelFont(62)
        for binx in range(1,h_corr.GetXaxis().GetNbins()+1):
            h_corr.GetXaxis().SetBinLabel(binx,so_nuisances[binx-1])
            tmp=open(input_path+cat+"/"+chan+"/"+so_nuisances[binx-1]+".txt","r")
            lines=tmp.readlines()
            for biny in range(1,h_corr.GetYaxis().GetNbins()+1):
                h_corr.GetYaxis().SetBinLabel(biny,so_nuisances[biny-1])
                for line in lines:
                    if so_nuisances[biny-1]==line.split(":")[0].strip(" "):
                        corr_value=float(line.split(":")[-1])
                        h_corr.SetBinContent(binx,biny,corr_value)
            tmp.close()
        #canvas=ROOT.TCanvas("%s_%s"%(cat,chan),"%s_%s"%(cat,chan),800,800)
        canvas=ROOT.TCanvas("%s_%s"%(cat,chan),"",800,800)
        canvas.cd()
        canvas.SetTopMargin(0.1)
        canvas.SetBottomMargin(0.33)
        canvas.SetLeftMargin(0.33)
        canvas.SetRightMargin(0.13)
        #h_corr.Draw("COLZ")
        h_corr.LabelsDeflate("X")
        h_corr.LabelsDeflate("Y")
        h_corr.LabelsOption("v")
        h_corr.Draw("COLZ TEXT")
        canvas.SaveAs(input_path+cat+"/"+chan+"/"+cat.split(".root")[0]+"_"+chan+"_correlation.png")
print "done!"
               
            
