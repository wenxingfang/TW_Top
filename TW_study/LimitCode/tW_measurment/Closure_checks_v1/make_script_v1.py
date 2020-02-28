import os
import shutil

check_nuisances =False
get_postfit=True

out_script_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks_v1/script/"
if os.path.exists(out_script_path):
        shutil.rmtree(out_script_path)
os.makedirs(out_script_path)
output_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks_v1/output/"

card_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/data_card_ttbar_DY/"

top_n=10

cat=[]
cat.append("exp")
cat.append("obs")

chans=[]
#chans.append("only_b")
chans.append("bplus_s")
cards={}
cards["ee_1jet_1bjet.root"]=['TT_normalisation','ISR_','JetEnergyScale_','ElectronIDIsoScaleFactor_','Luminosity']  
cards["ee_2jet_1bjet.root"]=['tw_DS_','ee_2jet_1bjet_DY_stat_bin6_','JetEnergyResolution_','FSR_','tw_MEscale_']  
cards["ee_2jet_2bjet.root"]=['FSR_','TT_normalisation','JetEnergyScale_','ElectronIDIsoScaleFactor_','BtagScaleFactor_bc_']  
cards["ee_card.root"]      =['JetEnergyResolution_','ISR_','BtagScaleFactor_bc_','ee_1jet_1bjet_DY_stat_bin6_','is1jet_1bjet_DY_normalisation_Norm']        
#cards["ee_emu_mumu_1j1t_card.root"]=['','','','','']  
cards["ee_emu_mumu_card.root"] =['BtagScaleFactor_bc_','FSR_','JetEnergyResolution_','is1jet_1bjet_DY_normalisation_Norm','ISR_']       
#cards["emu_11_21_22_card.root"]=['','','','','']      
#cards["emu_11_21_card.root"]=['','','','','']         
cards["emu_1jet_0bjet.root"]=['Othernormalisation_Norm','FSR_','emu_1jet_0bjet_DY_stat_bin5_','DY_PDF_','is1jet_0bjet_DY_normalisation_Norm']  
cards["emu_1jet_1bjet.root"]=['FSR_','ISR_','TT_normalisation','JetEnergyResolution_','is1jet_1bjet_DY_normalisation_Norm']  
cards["emu_2jet_1bjet.root"]=['ISR_','tw_DS_','JetEnergyResolution_','TT_Tune_','JetEnergyScale_']  
cards["emu_2jet_2bjet.root"]=['FSR_','TT_normalisation','BtagScaleFactor_bc_','Luminosity','JetEnergyScale_']  
cards["emu_card.root"]       =['FSR_','BtagScaleFactor_bc_','JetEnergyResolution_','is1jet_1bjet_DY_normalisation_Norm','tw_MEscale_']         
cards["mumu_1jet_1bjet.root"]=['is1jet_1bjet_DY_normalisation_Norm','TT_normalisation','JetEnergyScale_','Luminosity','ISR_']
cards["mumu_2jet_1bjet.root"]=['JetEnergyScale_','JetEnergyResolution_','tw_DS_','UnclusteredEn_','TT_CR_']
cards["mumu_2jet_2bjet.root"]=['FSR_','TT_normalisation','JetEnergyScale_','BtagScaleFactor_bc_','Luminosity']
cards["mumu_card.root"]      =['is1jet_1bjet_DY_normalisation_Norm','JetEnergyResolution_','BtagScaleFactor_bc_','mumu_2jet_1bjet_DY_stat_bin6_','FSR_']

for card in cards:
    for chan in chans:
        f_out=open("%s%s_%s.sh"%(out_script_path,card,chan),"w")
        if not os.path.exists(str(output_path+card+"//"+chan)):
            os.makedirs(str(output_path+card+"//"+chan))
        expectS="1"
        if chan =="only_b":
            expectS="0"
        elif chan =="bplus_s":
            expectS="1"
        dicti={"output":str(output_path+card+"//"+chan),"card":str(card_path+card),"card_name":str(card.split(".root")[0]+"_"+chan),"expectS":expectS,"python":"~/Limits/CMSSW_7_4_7/src/LimitCode/tW_measurment/Closure_checks_v1/diffNuisances_wx.py","top_n":str(top_n+1)}
        tmp0='''
cd %(output)s
eval `scramv1 runtime -sh`
combine -M MaxLikelihoodFit -d %(card)s -t -1 --expectSignal %(expectS)s
'''
        f_out.write(tmp0%(dicti))
        ############ for check_nuisances ###################### 
        if check_nuisances:
            tmp='''
python %(python)s -a mlfit.root -g plots.root -n %(card_name)s_sorted > %(card_name)s
'''
            f_out.write("\n"+tmp%(dicti))
            for ivar in cards[card]:
                f_out.write("\n"+"python %s -a mlfit.root -g plots.root -n %s --poi %s "%(dicti['python'],ivar,ivar))
        ############ for fit shape###################### 
        if get_postfit and chan =="bplus_s":
            f_out.write("\n"+"PostFitShapesFromWorkspace -o fit_shapes.root -f mlfit.root:fit_s --postfit --sampling --print -w %s > postfit.print"%(dicti['card']))
        f_out.close()
print "create script done!"

