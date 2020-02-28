import os
class card_object:
    def __init__(self,name,channel,Dict, out_name):
        self.name=name
        self.channel =channel
        self.template=''''''
        self.Dict=Dict
        self.out_name=out_name
    def make_template(self):
        if "xjet_1bjet" in self.name:
            if self.channel=="emu":
                self.template='''
max    1     number of categories
jmax   5     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-----------------------------------------------------------------------------------------------------------
bin                                            %(cname)s          %(cname)s         %(cname)s         %(cname)s          %(cname)s            %(cname)s
process                                         0                    1                 2                   3                     4                   5
process                                         FCNCSignal          TW                   TT               DY                  other                 jets
rate                                           %(n_FCNCSignal)s    %(n_TW)s            %(n_TT)s         %(n_DY)s            %(n_other)s           %(n_jets)s
---------------------------------------------------------------------------------------------------- -----------------------------------------------
%(c_reg)s_FCNCSignal_stat_bin1_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin2_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin3_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin4_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin5_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin6_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin7_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin8_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin9_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin10_   shape        1                  -                     -                -                   -                    -
%(c_reg)s_TW_stat_bin1_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin2_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin3_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin4_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin5_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin6_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin7_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin8_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin9_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin10_           shape        -                  1                     -                -                   -                    -
%(c_reg)s_TT_stat_bin1_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin2_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin3_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin4_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin5_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin6_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin7_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin8_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin9_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin10_           shape        -                  -                     1                -                   -                    -
%(c_reg)s_DY_stat_bin1_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin2_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin3_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin4_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin5_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin6_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin7_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin8_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin9_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin10_           shape        -                  -                     -                1                   -                    -
%(c_reg)s_other_stat_bin1_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin2_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin3_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin4_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin5_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin6_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin7_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin8_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin9_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin10_        shape        -                  -                     -                -                   1                    -
'''
            elif self.channel=="ee":
                self.template='''
max    1     number of categories
jmax   5     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-----------------------------------------------------------------------------------------------------------
bin                                            %(cname)s          %(cname)s         %(cname)s         %(cname)s          %(cname)s            %(cname)s
process                                         0                    1                 2                   3                     4                   5
process                                         FCNCSignal          TW                   TT               DY                  other                 jets
rate                                           %(n_FCNCSignal)s    %(n_TW)s            %(n_TT)s         %(n_DY)s            %(n_other)s           %(n_jets)s
---------------------------------------------------------------------------------------------------- -----------------------------------------------
%(c_reg)s_FCNCSignal_stat_bin1_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin2_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin3_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin4_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin5_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin6_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin7_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin8_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin9_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin10_   shape        1                  -                     -                -                   -                    -
%(c_reg)s_TW_stat_bin1_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin2_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin3_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin4_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin5_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin6_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin7_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin8_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin9_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin10_           shape        -                  1                     -                -                   -                    -
%(c_reg)s_TT_stat_bin1_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin2_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin3_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin4_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin5_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin6_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin7_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin8_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin9_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin10_           shape        -                  -                     1                -                   -                    -
%(c_reg)s_DY_stat_bin1_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin2_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin3_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin4_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin5_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin6_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin7_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin8_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin9_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin10_           shape        -                  -                     -                1                   -                    -
%(c_reg)s_other_stat_bin1_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin2_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin3_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin4_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin5_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin6_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin7_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin8_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin9_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin10_        shape        -                  -                     -                -                   1                    -
'''
            elif self.channel=="mumu":
                self.template='''
max    1     number of categories
jmax   5     number of samples minus one
kmax    *     number of nuisance parameters
-------------------------------------------------------------------------------------------------------------
shapes * * %(input_root)s.root $PROCESS $PROCESS_$SYSTEMATIC
-------------------------------------------------------------------------------------------------------------
bin                                            %(cname)s
observation                                    %(n_observation)s
-----------------------------------------------------------------------------------------------------------
bin                                            %(cname)s          %(cname)s         %(cname)s         %(cname)s          %(cname)s            %(cname)s
process                                         0                    1                 2                   3                     4                   5
process                                         FCNCSignal          TW                   TT               DY                  other                 jets
rate                                           %(n_FCNCSignal)s    %(n_TW)s            %(n_TT)s         %(n_DY)s            %(n_other)s           %(n_jets)s
---------------------------------------------------------------------------------------------------- -----------------------------------------------
%(c_reg)s_FCNCSignal_stat_bin1_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin2_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin3_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin4_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin5_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin6_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin7_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin8_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin9_    shape        1                  -                     -                -                   -                    -
%(c_reg)s_FCNCSignal_stat_bin10_   shape        1                  -                     -                -                   -                    -
%(c_reg)s_TW_stat_bin1_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin2_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin3_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin4_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin5_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin6_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin7_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin8_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin9_            shape        -                  1                     -                -                   -                    -
%(c_reg)s_TW_stat_bin10_           shape        -                  1                     -                -                   -                    -
%(c_reg)s_TT_stat_bin1_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin2_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin3_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin4_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin5_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin6_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin7_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin8_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin9_            shape        -                  -                     1                -                   -                    -
%(c_reg)s_TT_stat_bin10_           shape        -                  -                     1                -                   -                    -
%(c_reg)s_DY_stat_bin1_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin2_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin3_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin4_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin5_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin6_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin7_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin8_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin9_            shape        -                  -                     -                1                   -                    -
%(c_reg)s_DY_stat_bin10_           shape        -                  -                     -                1                   -                    -
%(c_reg)s_other_stat_bin1_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin2_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin3_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin4_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin5_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin6_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin7_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin8_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin9_         shape        -                  -                     -                -                   1                    -
%(c_reg)s_other_stat_bin10_        shape        -                  -                     -                -                   1                    -
'''

    def writeCard(self):
        text_file = open("%s.txt" % (self.out_name), "w")
        text_file.write(self.template % (self.Dict))
        text_file.close()
        print "write card: %s"%(self.out_name)

Do_tug=False
Do_tcg=True
input_path=""
output_path=""
info_name=""
if Do_tug: 
    input_path ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/input_file_tug/"
    output_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_tug_statonly/"
    info_name  ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/info_tug.txt"
elif Do_tcg: 
    input_path ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/input_file_tcg/"
    output_path="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/data_card_tcg_statonly/"
    info_name  ="/user/wenxing/Limits/CMSSW_7_4_7/src/LimitCode/FCNC/info_tcg.txt"
if not os.path.exists(output_path):
    os.makedirs(output_path)
Cards=[]
for chan in ["ee","emu","mumu"]:
    for region in ["xjet_1bjet"]:
        for sf in ["1.00", "0.05", "0.10", "0.15", "0.20", "0.25", "0.30","0.02","0.50"]:
            c_name=str(chan)+"_"+str(region)+"_FCNC"+"_"+str(sf)
            dir_tmp={}
            dir_tmp["cname"]=c_name
            dir_tmp["input_root"]=input_path+c_name
            dir_tmp["c_reg"]=str(chan)+"_"+str(region)
            dir_tmp["region"]="is"+str(region)
            f_info = open(info_name,'r')
            lines = f_info.readlines()
            for li in lines:
                li =li.strip('\n')
                if c_name in li:
                    if "data_obs" in li:
                        dir_tmp["n_observation"]=str(li.split(":")[-1])
                    elif "TW" in li :
                        dir_tmp["n_TW"]=str(li.split(":")[-1])
                    elif "TT" in li:
                        dir_tmp["n_TT"]=str(li.split(":")[-1])
                    elif "DY" in li:
                        dir_tmp["n_DY"]=str(li.split(":")[-1])
                    elif "other" in li:
                        dir_tmp["n_other"]=str(li.split(":")[-1])
                    elif "jets" in li:
                        dir_tmp["n_jets"]=str(li.split(":")[-1])
                    elif "FCNCSignal" in li:
                        dir_tmp["n_FCNCSignal"]=str(li.split(":")[-1])
            Cards.append(card_object(c_name,str(chan),dir_tmp, output_path+c_name))    
for icard in Cards:
    icard.make_template()
    icard.writeCard()
