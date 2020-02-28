#include <map>
#include <TString.h>
#include <TH1.h>
#include <TH1D.h>
#include <math.h>
#include <TMath.h>
#include <iostream>
#include <fstream>
#include <string>  
using namespace std;  
////////////// For ttbar channel R value //////////#
const double CMS_R[3]={1.014,0.003,0.032};
const double D0_R[2]={0.9,0.04};
const double CDF_R_1[2]={0.87,0.07};
const double CDF_R_2[2]={0.94,0.09};
////////////# For ttbar channel top width //////////
const double G_F=1.16637e-5;
const double MT=172.5;
const double MW=80.385;
const double aphi_s=0.118;
const double pi = 3.1415926535897;
const double top_width_scale=G_F*pow(MT,3)*pow((1-pow(MW/MT,2)),2)*(1+2*pow(MW/MT,2))*(1-((2*aphi_s)/(3*pi))*((2*pi*pi/3)-(5/2)))/(8*pi*sqrt(2));
const double ATLAS_W[3]={1.76,0.33,0.68};
const double CDF_W[2]={2.575,1.475};//(1.1+4.05)/2, 4.05-(1.1+4.05)/2
const double D0_W[2]={2.35,2.05  };//(0.3+4.4)/2, 4.4-(0.3+4.4)/2
////////////# For TW cross section //////////
const double ATLAS_TW_7[3]={16.8,2.9,4.9};
const double ATLAS_TW_8[4]={23.0,1.3,3.2,1.1};
const double ATLAS_TW_13[4]={94,10,22,2};
const double CMS_TW_7[2]={16,4};
const double CMS_TW_8[2]={23.4,5.4};
/////////# For t-channel inclusive XS and Rt //////////
const double ATLAS_7_Rt[2]={2.04,0.18}; 
const double ATLAS_8_Rt[2]={1.72,0.09}; 
const double ATLAS_8_t_fid[2]={9.78*0.324,0.57*0.324}; 
const double ATLAS_8_tbar_fid[2]={5.77*0.324,0.45*0.324}; 
const double ATLAS_13_t   [4]={156,5,27,3}; 
const double ATLAS_13_tbar[4]={91,4,18,2}; 
const double ATLAS_13_Rt[3]={1.72,0.09,0.18}; 
const double CMS_7_ttbar[2]={67.2,6.1};
const double CMS_8_t[3]={53.8,1.5,4.4};
const double CMS_8_tbar[3]={27.6,1.3,3.7};
const double CMS_8_Rt[3]={1.95,0.10,0.19};
const double CMS_13_t   [2]={154,22}; 
const double CMS_13_tbar[2]={85,16}; 
const double CMS_13_Rt[3]={1.81,0.18,0.15}; 
const double D0_ttbar[2]={2.9,0.59}; 
//#################### expected #####################
////////////// For ttbar channel R value //////////#
const double exp_CMS_R[3]={1.0,0.003,0.032};//8TeV
const double exp_D0_R[2]   ={1,0.04};
const double exp_CDF_R_1[2]={1,0.07};
const double exp_CDF_R_2[2]={1,0.09};
////////////# For ttbar channel top width //////////
const double exp_ATLAS_W[3]={top_width_scale,0.33,0.68};//8TeV
const double exp_CDF_W[2]  ={top_width_scale,1.475};//
const double exp_D0_W[2]   ={top_width_scale,2.05};//
////////////# For TW cross section //////////
const double exp_ATLAS_TW_8[4] ={1.26*8.87*2       ,1.3,3.2,1.1};//8TeV
const double exp_CMS_TW_8[2]   ={1.26*8.87*2       ,5.4};        //8TeV
const double exp_ATLAS_TW_7[3] ={1.26*6.26*2,2.9   ,4.9};
const double exp_ATLAS_TW_13[4]={1.28*28.02*2      ,10,22,2};
const double exp_CMS_TW_7[2]   ={1.26*6.26*2       ,4};
/////////# For t-channel XS //////////
const double exp_CMS_8_t[3]   ={56.3     ,1.5,4.4};//8TeV
const double exp_CMS_8_tbar[3]={30.7     ,1.3,3.7};//8TeV
const double exp_ATLAS_8_t_fid[2]   ={0.06 *56.3,0.57*0.324}; 
const double exp_ATLAS_8_tbar_fid[2]={0.061*30.7,0.45*0.324}; 
const double exp_ATLAS_13_t   [4]={136.5 ,5,27,3}; 
const double exp_ATLAS_13_tbar[4]={82.1  ,4,18,2}; 
const double exp_CMS_7_ttbar[2]  ={66.5  ,6.1};
const double exp_CMS_13_t   [2]  ={136.5 ,22}; 
const double exp_CMS_13_tbar[2]  ={82.1  ,16}; 
/////////#  Rt //////////
const double exp_ATLAS_8_Rt[2] ={56.3/30.7,0.09    };//8TeV 
const double exp_CMS_8_Rt[3]   ={56.3/30.7,0.1,0.19};//8TeV
const double exp_ATLAS_7_Rt[2] ={43.7/22.8,0.18}; 
const double exp_ATLAS_13_Rt[3]={136.5/82.1,0.09,0.18}; 
const double exp_CMS_13_Rt[3]  ={136.5/82.1,0.18,0.15}; 
const double exp_D0_ttbar[2]   ={2.1,0.59}; 

map<int, map<int,double>> matrix(){
map<int, map<int,double>> Correlation_matrix;
map<int, double> map1 ;
map<int, double> map2 ;
map<int, double> map3 ;
map<int, double> map4 ;
map<int, double> map5 ;
map<int, double> map6 ;
map<int, double> map7 ;
map<int, double> map8 ;
map<int, double> map9 ;
map<int, double> map10;
map<int, double> map11;
map<int, double> map12;
map<int, double> map13;
map<int, double> map14;
map<int, double> map15;
map<int, double> map16;
map<int, double> map17;
map<int, double> map18;
map<int, double> map19;
map<int, double> map20;
map<int, double> map21;
map<int, double> map22;
map<int, double> map23;
map<int, double> map24;
map<int, double> map25;
map<int, double> map26;
map<int, double> map27;
map<int, double> map28;
map<int, double> map29;
map<int, double> map30;
map<int, double> map31;
map<int, double> map32;
map<int, double> map33;
map<int, double> map34;
map<int, double> map35;
map<int, double> map36;
map<int, double> map37;
map<int, double> map38;
map<int, double> map39;
map<int, double> map40;
map<int, double> map41;
map<int, double> map42;
map<int, double> map43;
map<int, double> map44;
map<int, double> map45;
map<int, double> map46;
map<int, double> map47;
map<int, double> map48;
map<int, double> map49;
map<int, double> map50;
map<int, double> map51;
map<int, double> map52;
map<int, double> map53;
map<int, double> map54;
map<int, double> map55;
map<int, double> map56;
map<int, double> map57;
map<int, double> map58;
map<int, double> map59;
map<int, double> map60;
map<int, double> map61;
map<int, double> map62;
map<int, double> map63;
map<int, double> map64;
map<int, double> map65;
map<int, double> map66;
map<int, double> map67;
map<int, double> map68;
map<int, double> map69;
//Stat_correlation_matrix["1"]={"1":1    ,"2":-0.36,"3":0.04 ,"4":0.01 ,"5":0    ,"6":-0.01,"7":0    }
map1.insert(map<int, double> :: value_type(1, 1.00));
map1.insert(map<int, double> :: value_type(2,-0.36));
map1.insert(map<int, double> :: value_type(3, 0.04));
map1.insert(map<int, double> :: value_type(4, 0.01));
map1.insert(map<int, double> :: value_type(5, 0.00));
map1.insert(map<int, double> :: value_type(6,-0.01));
map1.insert(map<int, double> :: value_type(7,-0.00));
//Stat_correlation_matrix["2"]={"1":-0.36,"2":1    ,"3":-0.3 ,"4":0.03 ,"5":0.02 ,"6":0.02 ,"7":-0.01}
map2.insert(map<int, double> :: value_type(1,-0.36));
map2.insert(map<int, double> :: value_type(2, 1.00));
map2.insert(map<int, double> :: value_type(3,-0.30));
map2.insert(map<int, double> :: value_type(4, 0.03));
map2.insert(map<int, double> :: value_type(5, 0.02));
map2.insert(map<int, double> :: value_type(6, 0.02));
map2.insert(map<int, double> :: value_type(7,-0.01));
////////////////////// 8TeV top pt //////////////////////////////////////////////////////////////////////#
//Stat_correlation_matrix["3"]={"1":0.04 ,"2":-0.3 ,"3":1    ,"4":-0.27,"5":0.02 ,"6":0    ,"7":-0.01}
map3.insert(map<int, double> :: value_type(1, 0.04));
map3.insert(map<int, double> :: value_type(2,-0.30));
map3.insert(map<int, double> :: value_type(3, 1.00));
map3.insert(map<int, double> :: value_type(4,-0.27));
map3.insert(map<int, double> :: value_type(5, 0.02));
map3.insert(map<int, double> :: value_type(6, 0.00));
map3.insert(map<int, double> :: value_type(7,-0.01));
//Stat_correlation_matrix["4"]={"1":0.01 ,"2":0.03 ,"3":-0.27,"4":1    ,"5":-0.23,"6":0    ,"7":0.01 }
map4.insert(map<int, double> :: value_type(1, 0.01));
map4.insert(map<int, double> :: value_type(2, 0.03));
map4.insert(map<int, double> :: value_type(3,-0.27));
map4.insert(map<int, double> :: value_type(4, 1.00));
map4.insert(map<int, double> :: value_type(5,-0.23));
map4.insert(map<int, double> :: value_type(6, 0.00));
map4.insert(map<int, double> :: value_type(7, 0.01));
//Stat_correlation_matrix["5"]={"1":0    ,"2":0.02 ,"3":0.02 ,"4":-0.23,"5":1    ,"6":-0.17,"7":0.02 }
map5.insert(map<int, double> :: value_type(1, 0.00));
map5.insert(map<int, double> :: value_type(2, 0.02));
map5.insert(map<int, double> :: value_type(3, 0.02));
map5.insert(map<int, double> :: value_type(4,-0.23));
map5.insert(map<int, double> :: value_type(5, 1.00));
map5.insert(map<int, double> :: value_type(6,-0.17));
map5.insert(map<int, double> :: value_type(7, 0.02));
//Stat_correlation_matrix["6"]={"1":-0.01,"2":0.02 ,"3":0    ,"4":0    ,"5":-0.17,"6":1    ,"7":-0.2 }
map6.insert(map<int, double> :: value_type(1,-0.01));
map6.insert(map<int, double> :: value_type(2, 0.02));
map6.insert(map<int, double> :: value_type(3, 0.00));
map6.insert(map<int, double> :: value_type(4,-0.00));
map6.insert(map<int, double> :: value_type(5,-0.17));
map6.insert(map<int, double> :: value_type(6, 1.00));
map6.insert(map<int, double> :: value_type(7,-0.20));
//Stat_correlation_matrix["7"]={"1":0    ,"2":-0.01,"3":-0.01,"4":0.01 ,"5":0.02 ,"6":-0.20,"7":1    }
map7.insert(map<int, double> :: value_type(1,-0.00));
map7.insert(map<int, double> :: value_type(2,-0.01));
map7.insert(map<int, double> :: value_type(3,-0.01));
map7.insert(map<int, double> :: value_type(4, 0.01));
map7.insert(map<int, double> :: value_type(5, 0.02));
map7.insert(map<int, double> :: value_type(6,-0.20));
map7.insert(map<int, double> :: value_type(7, 1.00));
////////////////////// 8TeV top rap //////////////////////////////////////////////////////////////////////#
//Stat_correlation_matrix["8"]={"8":1     ,"9":-0.12,"10":0.01 ,"11":0.01 ,"12":0.01 ,"13":-0.01,"14":0    }
map8.insert(map<int, double> :: value_type(8 , 1.00));
map8.insert(map<int, double> :: value_type(9 ,-0.12));
map8.insert(map<int, double> :: value_type(10, 0.01));
map8.insert(map<int, double> :: value_type(11, 0.01));
map8.insert(map<int, double> :: value_type(12, 0.01));
map8.insert(map<int, double> :: value_type(13,-0.01));
map8.insert(map<int, double> :: value_type(14, 0.00));
//Stat_correlation_matrix["9"]={"8":-0.12 ,"9":1    ,"10":-0.13,"11":0    ,"12":-0.02,"13":0    ,"14":0    }
map9.insert(map<int, double> :: value_type(8 ,-0.12));
map9.insert(map<int, double> :: value_type(9 , 1.00));
map9.insert(map<int, double> :: value_type(10,-0.13));
map9.insert(map<int, double> :: value_type(11, 0.00));
map9.insert(map<int, double> :: value_type(12,-0.02));
map9.insert(map<int, double> :: value_type(13, 0.00));
map9.insert(map<int, double> :: value_type(14, 0.00));
//Stat_correlation_matrix["10"]={"8":0.01 ,"9":-0.13,"10":1    ,"11":-0.12,"12":0.01 ,"13":0.02 ,"14":0    }
map10.insert(map<int, double> :: value_type(8 , 0.01));
map10.insert(map<int, double> :: value_type(9 ,-0.13));
map10.insert(map<int, double> :: value_type(10, 1.00));
map10.insert(map<int, double> :: value_type(11,-0.12));
map10.insert(map<int, double> :: value_type(12, 0.01));
map10.insert(map<int, double> :: value_type(13, 0.02));
map10.insert(map<int, double> :: value_type(14, 0.00));
//Stat_correlation_matrix["11"]={"8":0.01 ,"9":0    ,"10":-0.12,"11":1    ,"12":-0.07,"13":0    ,"14":0    }
map11.insert(map<int, double> :: value_type(8 , 0.01));
map11.insert(map<int, double> :: value_type(9 , 0.00));
map11.insert(map<int, double> :: value_type(10,-0.12));
map11.insert(map<int, double> :: value_type(11, 1.00));
map11.insert(map<int, double> :: value_type(12,-0.07));
map11.insert(map<int, double> :: value_type(13, 0.00));
map11.insert(map<int, double> :: value_type(14, 0.00));
//Stat_correlation_matrix["12"]={"8":0.01 ,"9":-0.02,"10":0.01 ,"11":-0.07,"12":1    ,"13":-0.07,"14":0.01 }
map12.insert(map<int, double> :: value_type(8 , 0.01));
map12.insert(map<int, double> :: value_type(9 ,-0.02));
map12.insert(map<int, double> :: value_type(10, 0.01));
map12.insert(map<int, double> :: value_type(11,-0.07));
map12.insert(map<int, double> :: value_type(12, 1.00));
map12.insert(map<int, double> :: value_type(13,-0.07));
map12.insert(map<int, double> :: value_type(14, 0.01));
//Stat_correlation_matrix["13"]={"8":-0.01,"9":0    ,"10":0.02 ,"11":0    ,"12":-0.07,"13":1    ,"14":-0.04}
map13.insert(map<int, double> :: value_type(8 ,-0.01));
map13.insert(map<int, double> :: value_type(9 ,-0.00));
map13.insert(map<int, double> :: value_type(10, 0.02));
map13.insert(map<int, double> :: value_type(11,-0.00));
map13.insert(map<int, double> :: value_type(12,-0.07));
map13.insert(map<int, double> :: value_type(13, 1.00));
map13.insert(map<int, double> :: value_type(14,-0.04));
//Stat_correlation_matrix["14"]={"8":0    ,"9":0    ,"10":0    ,"11":0    ,"12":0.01 ,"13":-0.04,"14":1    }
map14.insert(map<int, double> :: value_type(8 ,-0.00));
map14.insert(map<int, double> :: value_type(9 ,-0.00));
map14.insert(map<int, double> :: value_type(10, 0.00));
map14.insert(map<int, double> :: value_type(11,-0.00));
map14.insert(map<int, double> :: value_type(12, 0.01));
map14.insert(map<int, double> :: value_type(13,-0.04));
map14.insert(map<int, double> :: value_type(14, 1.00));
//////////////////////8TeV top jet pt //////////////////////////////////////////////////////////////////////#
//Stat_correlation_matrix["15"]={"15":1    ,"16":-0.37,"17":0.06    ,"18":0    ,"19":-0.01 ,"20":0.01  }
map15.insert(map<int, double> :: value_type(15, 1.00));
map15.insert(map<int, double> :: value_type(16,-0.37));
map15.insert(map<int, double> :: value_type(17, 0.06));
map15.insert(map<int, double> :: value_type(18,-0.00));
map15.insert(map<int, double> :: value_type(19,-0.01));
map15.insert(map<int, double> :: value_type(20, 0.01));
//Stat_correlation_matrix["16"]={"15":-0.37,"16":1    ,"17":-0.33   ,"18":0.05 ,"19":0.01  ,"20":0     }
map16.insert(map<int, double> :: value_type(15,-0.37));
map16.insert(map<int, double> :: value_type(16, 1.00));
map16.insert(map<int, double> :: value_type(17,-0.33));
map16.insert(map<int, double> :: value_type(18, 0.05));
map16.insert(map<int, double> :: value_type(19, 0.01));
map16.insert(map<int, double> :: value_type(20, 0.00));
//Stat_correlation_matrix["17"]={"15":0.06 ,"16":-0.33,"17":1       ,"18":-0.33,"19":0.04  ,"20":0     }
map17.insert(map<int, double> :: value_type(15, 0.06));
map17.insert(map<int, double> :: value_type(16,-0.33));
map17.insert(map<int, double> :: value_type(17, 1.00));
map17.insert(map<int, double> :: value_type(18,-0.33));
map17.insert(map<int, double> :: value_type(19, 0.04));
map17.insert(map<int, double> :: value_type(20, 0.00));
//Stat_correlation_matrix["18"]={"15":0    ,"16":0.05 ,"17":-0.33   ,"18":1    ,"19":-0.22 ,"20":0.03  }
map18.insert(map<int, double> :: value_type(15, 0.00));
map18.insert(map<int, double> :: value_type(16, 0.05));
map18.insert(map<int, double> :: value_type(17,-0.33));
map18.insert(map<int, double> :: value_type(18, 1.00));
map18.insert(map<int, double> :: value_type(19,-0.22));
map18.insert(map<int, double> :: value_type(20, 0.03));
//Stat_correlation_matrix["19"]={"15":-0.01,"16":0.01 ,"17":0.04    ,"18":-0.22,"19":1     ,"20":-0.14 }
map19.insert(map<int, double> :: value_type(15,-0.01));
map19.insert(map<int, double> :: value_type(16, 0.01));
map19.insert(map<int, double> :: value_type(17, 0.04));
map19.insert(map<int, double> :: value_type(18,-0.22));
map19.insert(map<int, double> :: value_type(19, 1.00));
map19.insert(map<int, double> :: value_type(20,-0.14));
//Stat_correlation_matrix["20"]={"15":0.01 ,"16":0    ,"17":0       ,"18":0.03 ,"19":-0.14 ,"20":1     }
map20.insert(map<int, double> :: value_type(15, 0.01));
map20.insert(map<int, double> :: value_type(16, 0.00));
map20.insert(map<int, double> :: value_type(17, 0.00));
map20.insert(map<int, double> :: value_type(18, 0.03));
map20.insert(map<int, double> :: value_type(19,-0.14));
map20.insert(map<int, double> :: value_type(20, 1.00));
//////////////////////8TeV top jet rap //////////////////////////////////////////////////////////////////////#
//Stat_correlation_matrix["21"]={"21":1     ,"22":-0.02  ,"23":0.01       ,"24":0     ,"25":-0.02 ,"26":0     }
map21.insert(map<int, double> :: value_type(21, 1.00));
map21.insert(map<int, double> :: value_type(22,-0.02));
map21.insert(map<int, double> :: value_type(23, 0.01));
map21.insert(map<int, double> :: value_type(24, 0.00));
map21.insert(map<int, double> :: value_type(25,-0.02));
map21.insert(map<int, double> :: value_type(26, 0.00));
//Stat_correlation_matrix["22"]={"21":-0.02 ,"22":1      ,"23":-0.01      ,"24":-0.01 ,"25":0.01  ,"26":0     }
map22.insert(map<int, double> :: value_type(21,-0.02));
map22.insert(map<int, double> :: value_type(22, 1.00));
map22.insert(map<int, double> :: value_type(23,-0.01));
map22.insert(map<int, double> :: value_type(24,-0.01));
map22.insert(map<int, double> :: value_type(25, 0.01));
map22.insert(map<int, double> :: value_type(26, 0.00));
//Stat_correlation_matrix["23"]={"21":0.01  ,"22":-0.01  ,"23":1          ,"24":-0.02 ,"25":0     ,"26":0.01  }
map23.insert(map<int, double> :: value_type(21, 0.01));
map23.insert(map<int, double> :: value_type(22,-0.01));
map23.insert(map<int, double> :: value_type(23, 1.00));
map23.insert(map<int, double> :: value_type(24,-0.02));
map23.insert(map<int, double> :: value_type(25, 0.00));
map23.insert(map<int, double> :: value_type(26, 0.01));
//Stat_correlation_matrix["24"]={"21":0     ,"22":-0.01  ,"23":-0.02      ,"24":1     ,"25":-0.02 ,"26":0     }
map24.insert(map<int, double> :: value_type(21, 0.00));
map24.insert(map<int, double> :: value_type(22,-0.01));
map24.insert(map<int, double> :: value_type(23,-0.02));
map24.insert(map<int, double> :: value_type(24, 1.00));
map24.insert(map<int, double> :: value_type(25,-0.02));
map24.insert(map<int, double> :: value_type(26, 0.00));
//Stat_correlation_matrix["25"]={"21":-0.02 ,"22":0.01   ,"23":0          ,"24":-0.02 ,"25":1     ,"26":-0.03 }
map25.insert(map<int, double> :: value_type(21,-0.02));
map25.insert(map<int, double> :: value_type(22, 0.01));
map25.insert(map<int, double> :: value_type(23, 0.00));
map25.insert(map<int, double> :: value_type(24,-0.02));
map25.insert(map<int, double> :: value_type(25, 1.00));
map25.insert(map<int, double> :: value_type(26,-0.03));
//Stat_correlation_matrix["26"]={"21":0     ,"22":0      ,"23":0.01       ,"24":0     ,"25":-0.03 ,"26":1     }
map26.insert(map<int, double> :: value_type(21,-0.00));
map26.insert(map<int, double> :: value_type(22, 0.00));
map26.insert(map<int, double> :: value_type(23, 0.01));
map26.insert(map<int, double> :: value_type(24,-0.00));
map26.insert(map<int, double> :: value_type(25,-0.03));
map26.insert(map<int, double> :: value_type(26, 1.00));
//////////////////////8TeV atop pt //////////////////////////////////////////////////////////////////////#
//Stat_correlation_matrix["27"]={"27":1     ,"28":-0.36  ,"29":0.05       ,"30":0     ,"31":0     ,"32":-0.01 }
map27.insert(map<int, double> :: value_type(27, 1.00));
map27.insert(map<int, double> :: value_type(28,-0.36));
map27.insert(map<int, double> :: value_type(29, 0.05));
map27.insert(map<int, double> :: value_type(30,-0.00));
map27.insert(map<int, double> :: value_type(31,-0.00));
map27.insert(map<int, double> :: value_type(32, 0.01));
//Stat_correlation_matrix["28"]={"27":-0.36 ,"28":1      ,"29":-0.31      ,"30":0.05  ,"31":0     ,"32":0     }
map28.insert(map<int, double> :: value_type(27,-0.36));
map28.insert(map<int, double> :: value_type(28, 1.00));
map28.insert(map<int, double> :: value_type(29,-0.31));
map28.insert(map<int, double> :: value_type(30, 0.05));
map28.insert(map<int, double> :: value_type(31,-0.00));
map28.insert(map<int, double> :: value_type(32, 0.00));
//Stat_correlation_matrix["29"]={"27":0.05  ,"28":-0.31  ,"29":1          ,"30":-0.26 ,"31":0.02  ,"32":0.02  }
map29.insert(map<int, double> :: value_type(27, 0.05));
map29.insert(map<int, double> :: value_type(28,-0.31));
map29.insert(map<int, double> :: value_type(29, 1.00));
map29.insert(map<int, double> :: value_type(30,-0.26));
map29.insert(map<int, double> :: value_type(31, 0.02));
map29.insert(map<int, double> :: value_type(32, 0.02));
//Stat_correlation_matrix["30"]={"27":0     ,"28":0.05   ,"29":-0.26      ,"30":1     ,"31":-0.23 ,"32":0.01  }
map30.insert(map<int, double> :: value_type(27, 0.00));
map30.insert(map<int, double> :: value_type(28, 0.05));
map30.insert(map<int, double> :: value_type(29,-0.26));
map30.insert(map<int, double> :: value_type(30, 1.00));
map30.insert(map<int, double> :: value_type(31,-0.23));
map30.insert(map<int, double> :: value_type(32, 0.01));
//Stat_correlation_matrix["31"]={"27":0     ,"28":0      ,"29":0.02       ,"30":-0.23 ,"31":1     ,"32":-0.15 }
map31.insert(map<int, double> :: value_type(27, 0.00));
map31.insert(map<int, double> :: value_type(28, 0.00));
map31.insert(map<int, double> :: value_type(29, 0.02));
map31.insert(map<int, double> :: value_type(30,-0.23));
map31.insert(map<int, double> :: value_type(31, 1.00));
map31.insert(map<int, double> :: value_type(32,-0.15));
//Stat_correlation_matrix["32"]={"27":-0.01 ,"28":0      ,"29":0.02       ,"30":0.01  ,"31":-0.15 ,"32":1     }
map32.insert(map<int, double> :: value_type(27,-0.01));
map32.insert(map<int, double> :: value_type(28, 0.00));
map32.insert(map<int, double> :: value_type(29, 0.02));
map32.insert(map<int, double> :: value_type(30, 0.01));
map32.insert(map<int, double> :: value_type(31,-0.15));
map32.insert(map<int, double> :: value_type(32, 1.00));
//////////////////////8TeV atop rap //////////////////////////////////////////////////////////////////////#
//Stat_correlation_matrix["33"]={"33":1     ,"34":-0.13,"35":0.02 ,"36":0     ,"37":0.01 ,"38":0     ,"39":-0.01    }
map33.insert(map<int, double> :: value_type(33, 1.00));
map33.insert(map<int, double> :: value_type(34,-0.13));
map33.insert(map<int, double> :: value_type(35, 0.02));
map33.insert(map<int, double> :: value_type(36, 0.00));
map33.insert(map<int, double> :: value_type(37, 0.01));
map33.insert(map<int, double> :: value_type(38, 0.00));
map33.insert(map<int, double> :: value_type(39,-0.01));
//Stat_correlation_matrix["34"]={"33":-0.13 ,"34":1    ,"35":-0.11,"36":0     ,"37":0    ,"38":-0.01 ,"39":0        }
map34.insert(map<int, double> :: value_type(33,-0.13));
map34.insert(map<int, double> :: value_type(34, 1.00));
map34.insert(map<int, double> :: value_type(35,-0.11));
map34.insert(map<int, double> :: value_type(36, 0.00));
map34.insert(map<int, double> :: value_type(37, 0.00));
map34.insert(map<int, double> :: value_type(38,-0.01));
map34.insert(map<int, double> :: value_type(39,-0.00));
//Stat_correlation_matrix["35"]={"33":0.02  ,"34":-0.11,"35":1.00 ,"36":-0.11 ,"37":0    ,"38":-0.01 ,"39":-0.01    }
map35.insert(map<int, double> :: value_type(33, 0.02));
map35.insert(map<int, double> :: value_type(34,-0.11));
map35.insert(map<int, double> :: value_type(35, 1.00));
map35.insert(map<int, double> :: value_type(36,-0.11));
map35.insert(map<int, double> :: value_type(37, 0.00));
map35.insert(map<int, double> :: value_type(38,-0.01));
map35.insert(map<int, double> :: value_type(39,-0.01));
//Stat_correlation_matrix["36"]={"33":0.00  ,"34":0.00 ,"35":-0.11,"36":1.00  ,"37":-0.09,"38":0.00  ,"39":-0.01    }
map36.insert(map<int, double> :: value_type(33, 0.00));
map36.insert(map<int, double> :: value_type(34,-0.00));
map36.insert(map<int, double> :: value_type(35,-0.11));
map36.insert(map<int, double> :: value_type(36, 1.00));
map36.insert(map<int, double> :: value_type(37,-0.09));
map36.insert(map<int, double> :: value_type(38,-0.00));
map36.insert(map<int, double> :: value_type(39,-0.01));
//Stat_correlation_matrix["37"]={"33":0.01  ,"34":0.00 ,"35":0.00 ,"36":-0.09 ,"37":1.00 ,"38":-0.06 ,"39": 0.01    }
map37.insert(map<int, double> :: value_type(33, 0.01));
map37.insert(map<int, double> :: value_type(34,-0.00));
map37.insert(map<int, double> :: value_type(35,-0.00));
map37.insert(map<int, double> :: value_type(36,-0.09));
map37.insert(map<int, double> :: value_type(37, 1.00));
map37.insert(map<int, double> :: value_type(38,-0.06));
map37.insert(map<int, double> :: value_type(39, 0.01));
//Stat_correlation_matrix["38"]={"33":0.00  ,"34":-0.01,"35":-0.01,"36": 0.00 ,"37":-0.06,"38":1.00  ,"39":-0.04    }
map38.insert(map<int, double> :: value_type(33, 0.00));
map38.insert(map<int, double> :: value_type(34,-0.01));
map38.insert(map<int, double> :: value_type(35,-0.01));
map38.insert(map<int, double> :: value_type(36,-0.00));
map38.insert(map<int, double> :: value_type(37,-0.06));
map38.insert(map<int, double> :: value_type(38, 1.00));
map38.insert(map<int, double> :: value_type(39, 0.04));
//Stat_correlation_matrix["39"]={"33":-0.01 ,"34":0.00 ,"35":-0.01,"36":-0.01 ,"37":0.01 ,"38":-0.04 ,"39":1.00     }
map39.insert(map<int, double> :: value_type(33,-0.01));
map39.insert(map<int, double> :: value_type(34,-0.00));
map39.insert(map<int, double> :: value_type(35,-0.01));
map39.insert(map<int, double> :: value_type(36,-0.01));
map39.insert(map<int, double> :: value_type(37, 0.01));
map39.insert(map<int, double> :: value_type(38,-0.04));
map39.insert(map<int, double> :: value_type(39, 1.00));
//////////////////////8TeV atop jet pt //////////////////////////////////////////////////////////////////////#
//Stat_correlation_matrix["40"]={"40": 1.00,"41":-0.36,"42": 0.06,"43": 0.00,"44": 0.01,"45": 0.00 }
map40.insert(map<int, double> :: value_type(40, 1.00));
map40.insert(map<int, double> :: value_type(41,-0.36));
map40.insert(map<int, double> :: value_type(42, 0.06));
map40.insert(map<int, double> :: value_type(43,-0.00));
map40.insert(map<int, double> :: value_type(44, 0.01));
map40.insert(map<int, double> :: value_type(45,-0.00));
//Stat_correlation_matrix["41"]={"40":-0.36,"41": 1.00,"42":-0.36,"43": 0.05,"44": 0.02,"45": 0.00 }
map41.insert(map<int, double> :: value_type(40,-0.36));
map41.insert(map<int, double> :: value_type(41, 1.00));
map41.insert(map<int, double> :: value_type(42,-0.36));
map41.insert(map<int, double> :: value_type(43, 0.05));
map41.insert(map<int, double> :: value_type(44, 0.02));
map41.insert(map<int, double> :: value_type(45,-0.00));
//Stat_correlation_matrix["42"]={"40": 0.06,"41":-0.36,"42": 1.00,"43":-0.34,"44": 0.04,"45": 0.01 }
map42.insert(map<int, double> :: value_type(40, 0.06));
map42.insert(map<int, double> :: value_type(41,-0.36));
map42.insert(map<int, double> :: value_type(42, 1.00));
map42.insert(map<int, double> :: value_type(43,-0.34));
map42.insert(map<int, double> :: value_type(44, 0.04));
map42.insert(map<int, double> :: value_type(45, 0.01));
//Stat_correlation_matrix["43"]={"40": 0.00,"41": 0.05,"42":-0.34,"43": 1.00,"44":-0.22,"45": 0.01 }
map43.insert(map<int, double> :: value_type(40, 0.00));
map43.insert(map<int, double> :: value_type(41, 0.05));
map43.insert(map<int, double> :: value_type(42,-0.34));
map43.insert(map<int, double> :: value_type(43, 1.00));
map43.insert(map<int, double> :: value_type(44,-0.22));
map43.insert(map<int, double> :: value_type(45, 0.01));
//Stat_correlation_matrix["44"]={"40": 0.01,"41": 0.02,"42": 0.04,"43":-0.22,"44": 1.00,"45":-0.11 }
map44.insert(map<int, double> :: value_type(40, 0.01));
map44.insert(map<int, double> :: value_type(41, 0.02));
map44.insert(map<int, double> :: value_type(42, 0.04));
map44.insert(map<int, double> :: value_type(43,-0.22));
map44.insert(map<int, double> :: value_type(44, 1.00));
map44.insert(map<int, double> :: value_type(45,-0.11));
//Stat_correlation_matrix["45"]={"40": 0.00,"41": 0.00,"42": 0.01,"43": 0.01,"44":-0.11,"45": 1.00 }
map45.insert(map<int, double> :: value_type(40, 0.00));
map45.insert(map<int, double> :: value_type(41, 0.00));
map45.insert(map<int, double> :: value_type(42, 0.01));
map45.insert(map<int, double> :: value_type(43, 0.01));
map45.insert(map<int, double> :: value_type(44,-0.11));
map45.insert(map<int, double> :: value_type(45, 1.00));
//////////////////////8TeV atop jet rap  //////////////////////////////////////////////////////////////////////#
//Stat_correlation_matrix["46"]={"46": 1.00,"47":-0.02,"48": 0.00,"49": 0.01,"50": 0.00,"51": 0.00 }
map46.insert(map<int, double> :: value_type(46, 1.00));
map46.insert(map<int, double> :: value_type(47,-0.02));
map46.insert(map<int, double> :: value_type(48, 0.00));
map46.insert(map<int, double> :: value_type(49, 0.01));
map46.insert(map<int, double> :: value_type(50, 0.00));
map46.insert(map<int, double> :: value_type(51, 0.00));
//Stat_correlation_matrix["47"]={"46":-0.02,"47": 1.00,"48":-0.03,"49": 0.00,"50":-0.01,"51":-0.01 }
map47.insert(map<int, double> :: value_type(46,-0.02));
map47.insert(map<int, double> :: value_type(47, 1.00));
map47.insert(map<int, double> :: value_type(48,-0.03));
map47.insert(map<int, double> :: value_type(49, 0.00));
map47.insert(map<int, double> :: value_type(50,-0.01));
map47.insert(map<int, double> :: value_type(51,-0.01));
//Stat_correlation_matrix["48"]={"46":-0.00,"47":-0.03,"48": 1.00,"49":-0.02,"50":-0.00,"51": 0.01 }
map48.insert(map<int, double> :: value_type(46,-0.00));
map48.insert(map<int, double> :: value_type(47,-0.03));
map48.insert(map<int, double> :: value_type(48, 1.00));
map48.insert(map<int, double> :: value_type(49,-0.02));
map48.insert(map<int, double> :: value_type(50,-0.00));
map48.insert(map<int, double> :: value_type(51, 0.01));
//Stat_correlation_matrix["49"]={"46": 0.01,"47":-0.00,"48":-0.02,"49": 1.00,"50":-0.02,"51": 0.01 }
map49.insert(map<int, double> :: value_type(46, 0.01));
map49.insert(map<int, double> :: value_type(47,-0.00));
map49.insert(map<int, double> :: value_type(48,-0.02));
map49.insert(map<int, double> :: value_type(49, 1.00));
map49.insert(map<int, double> :: value_type(50,-0.02));
map49.insert(map<int, double> :: value_type(51, 0.01));
//Stat_correlation_matrix["50"]={"46": 0.00,"47":-0.01,"48":-0.00,"49":-0.02,"50": 1.00,"51":-0.03 }
map50.insert(map<int, double> :: value_type(46, 0.00));
map50.insert(map<int, double> :: value_type(47,-0.01));
map50.insert(map<int, double> :: value_type(48,-0.00));
map50.insert(map<int, double> :: value_type(49,-0.02));
map50.insert(map<int, double> :: value_type(50, 1.00));
map50.insert(map<int, double> :: value_type(51,-0.03));
//Stat_correlation_matrix["51"]={"46": 0.00,"47":-0.01,"48": 0.01,"49": 0.01,"50":-0.03,"51": 1.00 }
map51.insert(map<int, double> :: value_type(46, 0.00));
map51.insert(map<int, double> :: value_type(47,-0.01));
map51.insert(map<int, double> :: value_type(48, 0.01));
map51.insert(map<int, double> :: value_type(49, 0.01));
map51.insert(map<int, double> :: value_type(50,-0.03));
map51.insert(map<int, double> :: value_type(51, 1.00));
////////////////////// 7TeV top pt //////////////////////////////////////////////////////////////////////#
//Stat_correlation_matrix["52"]={"52": 1.00,"53": 0.48,"54": 0.49,"55": 0.43,"56": 0.35 }
map52.insert(map<int, double> :: value_type(52, 1.00));
map52.insert(map<int, double> :: value_type(53, 0.48));
map52.insert(map<int, double> :: value_type(54, 0.49));
map52.insert(map<int, double> :: value_type(55, 0.43));
map52.insert(map<int, double> :: value_type(56, 0.35));
//Stat_correlation_matrix["53"]={"52": 0.48,"53": 1.00,"54": 0.51,"55": 0.43,"56": 0.37 }
map53.insert(map<int, double> :: value_type(52, 0.48));
map53.insert(map<int, double> :: value_type(53, 1.00));
map53.insert(map<int, double> :: value_type(54, 0.51));
map53.insert(map<int, double> :: value_type(55, 0.43));
map53.insert(map<int, double> :: value_type(56, 0.37));
//Stat_correlation_matrix["54"]={"52": 0.49,"53": 0.51,"54": 1.00,"55": 0.34,"56": 0.31 }
map54.insert(map<int, double> :: value_type(52, 0.49));
map54.insert(map<int, double> :: value_type(53, 0.51));
map54.insert(map<int, double> :: value_type(54, 1.00));
map54.insert(map<int, double> :: value_type(55, 0.34));
map54.insert(map<int, double> :: value_type(56, 0.31));
//Stat_correlation_matrix["55"]={"52": 0.43,"53": 0.43,"54": 0.34,"55": 1.00,"56": 0.14 }
map55.insert(map<int, double> :: value_type(52, 0.43));
map55.insert(map<int, double> :: value_type(53, 0.43));
map55.insert(map<int, double> :: value_type(54, 0.34));
map55.insert(map<int, double> :: value_type(55, 1.00));
map55.insert(map<int, double> :: value_type(56, 0.14));
//Stat_correlation_matrix["56"]={"52": 0.35,"53": 0.37,"54": 0.31,"55": 0.14,"56": 1.00 }
map56.insert(map<int, double> :: value_type(52, 0.35));
map56.insert(map<int, double> :: value_type(53, 0.37));
map56.insert(map<int, double> :: value_type(54, 0.31));
map56.insert(map<int, double> :: value_type(55, 0.14));
map56.insert(map<int, double> :: value_type(56, 1.00));
////////////////////// 7TeV top rap //////////////////////////////////////////////////////////////////////#
//Stat_correlation_matrix["57"]={"57": 1.00,"58":-0.12,"59":-0.14,"60":-0.02 }
map57.insert(map<int, double> :: value_type(57, 1.00));
map57.insert(map<int, double> :: value_type(58,-0.12));
map57.insert(map<int, double> :: value_type(59,-0.14));
map57.insert(map<int, double> :: value_type(60,-0.02));
//Stat_correlation_matrix["58"]={"57":-0.12,"58": 1.00,"59":-0.19,"60":-0.09 }
map58.insert(map<int, double> :: value_type(57,-0.12));
map58.insert(map<int, double> :: value_type(58, 1.00));
map58.insert(map<int, double> :: value_type(59,-0.19));
map58.insert(map<int, double> :: value_type(60,-0.09));
//Stat_correlation_matrix["59"]={"57":-0.14,"58":-0.19,"59": 1.00,"60":-0.18 }
map59.insert(map<int, double> :: value_type(57,-0.14));
map59.insert(map<int, double> :: value_type(58,-0.19));
map59.insert(map<int, double> :: value_type(59, 1.00));
map59.insert(map<int, double> :: value_type(60,-0.18));
//Stat_correlation_matrix["60"]={"57":-0.02,"58":-0.09,"59":-0.18,"60": 1.00 }
map60.insert(map<int, double> :: value_type(57,-0.02));
map60.insert(map<int, double> :: value_type(58,-0.09));
map60.insert(map<int, double> :: value_type(59,-0.18));
map60.insert(map<int, double> :: value_type(60, 1.00));
////////////////////// 7TeV atop pt //////////////////////////////////////////////////////////////////////#
//Stat_correlation_matrix["61"]={"61": 1.00,"62": 0.34,"63": 0.26,"64": 0.13,"65": 0.13 }
map61.insert(map<int, double> :: value_type(61, 1.00));
map61.insert(map<int, double> :: value_type(62, 0.34));
map61.insert(map<int, double> :: value_type(63, 0.26));
map61.insert(map<int, double> :: value_type(64, 0.13));
map61.insert(map<int, double> :: value_type(65, 0.13));
//Stat_correlation_matrix["62"]={"61": 0.34,"62": 1.00,"63": 0.32,"64": 0.03,"65": 0.15 }
map62.insert(map<int, double> :: value_type(61, 0.34));
map62.insert(map<int, double> :: value_type(62, 1.00));
map62.insert(map<int, double> :: value_type(63, 0.32));
map62.insert(map<int, double> :: value_type(64, 0.03));
map62.insert(map<int, double> :: value_type(65, 0.15));
//Stat_correlation_matrix["63"]={"61": 0.26,"62": 0.32,"63": 1.00,"64": 0.09,"65": 0.05 }
map63.insert(map<int, double> :: value_type(61, 0.26));
map63.insert(map<int, double> :: value_type(62, 0.32));
map63.insert(map<int, double> :: value_type(63, 1.00));
map63.insert(map<int, double> :: value_type(64, 0.09));
map63.insert(map<int, double> :: value_type(65, 0.05));
//Stat_correlation_matrix["64"]={"61": 0.13,"62": 0.03,"63": 0.09,"64": 1.00,"65":-0.06 }
map64.insert(map<int, double> :: value_type(61, 0.13));
map64.insert(map<int, double> :: value_type(62, 0.03));
map64.insert(map<int, double> :: value_type(63, 0.09));
map64.insert(map<int, double> :: value_type(64, 1.00));
map64.insert(map<int, double> :: value_type(65,-0.06));
//Stat_correlation_matrix["65"]={"61": 0.13,"62": 0.15,"63": 0.05,"64":-0.06,"65": 1.00 }
map65.insert(map<int, double> :: value_type(61, 0.13));
map65.insert(map<int, double> :: value_type(62, 0.15));
map65.insert(map<int, double> :: value_type(63, 0.05));
map65.insert(map<int, double> :: value_type(64,-0.06));
map65.insert(map<int, double> :: value_type(65, 1.00));
////////////////////// 7TeV atop rap //////////////////////////////////////////////////////////////////////#
//Stat_correlation_matrix["66"]={"66": 1.00,"67":-0.05,"68":-0.17,"69": 0.11 }
map66.insert(map<int, double> :: value_type(66, 1.00));
map66.insert(map<int, double> :: value_type(67,-0.05));
map66.insert(map<int, double> :: value_type(68,-0.17));
map66.insert(map<int, double> :: value_type(69, 0.11));
//Stat_correlation_matrix["67"]={"66":-0.05,"67": 1.00,"68":-0.01,"69":-0.06 }
map67.insert(map<int, double> :: value_type(66,-0.05));
map67.insert(map<int, double> :: value_type(67, 1.00));
map67.insert(map<int, double> :: value_type(68,-0.01));
map67.insert(map<int, double> :: value_type(69,-0.06));
//Stat_correlation_matrix["68"]={"66":-0.17,"67":-0.01,"68": 1.00,"69":-0.23 }
map68.insert(map<int, double> :: value_type(66,-0.17));
map68.insert(map<int, double> :: value_type(67,-0.01));
map68.insert(map<int, double> :: value_type(68, 1.00));
map68.insert(map<int, double> :: value_type(69,-0.23));
//Stat_correlation_matrix["69"]={"66": 0.11,"67":-0.06,"68":-0.23,"69": 1.00 }
map69.insert(map<int, double> :: value_type(66, 0.11));
map69.insert(map<int, double> :: value_type(67,-0.06));
map69.insert(map<int, double> :: value_type(68,-0.23));
map69.insert(map<int, double> :: value_type(69, 1.00));


Correlation_matrix.insert(map<int, map<int,double>> :: value_type(1 ,map1  ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(2 ,map2  ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(3 ,map3  ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(4 ,map4  ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(5 ,map5  ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(6 ,map6  ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(7 ,map7  ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(8 ,map8  ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(9 ,map9  ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(10,map10 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(11,map11 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(12,map12 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(13,map13 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(14,map14 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(15,map15 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(16,map16 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(17,map17 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(18,map18 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(19,map19 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(20,map20 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(21,map21 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(22,map22 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(23,map23 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(24,map24 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(25,map25 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(26,map26 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(27,map27 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(28,map28 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(29,map29 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(30,map30 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(31,map31 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(32,map32 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(33,map33 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(34,map34 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(35,map35 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(36,map36 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(37,map37 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(38,map38 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(39,map39 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(40,map40 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(41,map41 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(42,map42 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(43,map43 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(44,map44 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(45,map45 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(46,map46 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(47,map47 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(48,map48 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(49,map49 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(50,map50 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(51,map51 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(52,map52 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(53,map53 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(54,map54 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(55,map55 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(56,map56 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(57,map57 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(58,map58 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(59,map59 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(60,map60 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(61,map61 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(62,map62 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(63,map63 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(64,map64 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(65,map65 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(66,map66 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(67,map67 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(68,map68 ));
Correlation_matrix.insert(map<int, map<int,double>> :: value_type(69,map69 ));
return Correlation_matrix;
}
pair <double,double> mod_limit(double vtb, double vts, double vtd, TString icat, int bin_min, int bin_max, TH1D hist_Vtb, TH1D hist_Vts, TH1D hist_Vtd, TH1D hist_Vtb_sys_uncert, TH1D hist_Vts_sys_uncert, TH1D hist_Vtd_sys_uncert, TH1D hist_data, int ndof, TString type, double lumi, bool do_Fix_R, double Fixed_R){
//double mod_limit(double vtb, double vts, double vtd, TString icat, int bin_min, int bin_max, TH1D hist_Vtb, TH1D hist_Vts, TH1D hist_Vtd, TH1D hist_Vtb_sys_uncert, TH1D hist_Vts_sys_uncert, TH1D hist_Vtd_sys_uncert, TH1D hist_data, int ndof, TString type, float* &tmp_chi2){
double chi2=0;
//chi2=49.577232;//from obs 8TeV differential
double R_val=vtb*vtb/(vtb*vtb+vts*vts+vtd*vtd);
//R_val=CMS_R[0];////////////////////////////////////////////////////// just for check
if(do_Fix_R)R_val=Fixed_R;////////////////////////////////////////////////////// just for check
double exp_i        ;
double err_mc_stat_i;
double err_sys_i    ;
double err_i        ;
double exp_j        ;
double err_mc_stat_j;
double err_sys_j    ;
double err_j        ;
map<int, map<int,double>> Correlation_matrix= matrix();
double top_width=(vtb*vtb+vts*vts+vtd*vtd)*top_width_scale;
double TW_7 =1.26*(6.26*2*vtb*vtb+12.19*2*vts*vts+(84+22.56)*vtd*vtd);
double TW_8 =1.26*(8.87*2*vtb*vtb+16.88*2*vts*vts+(109.08+31)*vtd*vtd);
double TW_13=1.28*(28.02*2*vtb*vtb+50.56*2*vts*vts+(265.8+89)*vtd*vtd);
double ST_t_7   =43.7*vtb*vtb +104.2*vts*vts+329.2*vtd*vtd ;
double ST_tbar_7=22.8*vtb*vtb +52.2 *vts*vts+84.4 *vtd*vtd ;
double Rt_7=ST_t_7/ST_tbar_7 ;
double ST_t_8   =56.3*vtb*vtb+132.5*vts*vts+406.4*vtd*vtd ;
double ST_tbar_8=30.7*vtb*vtb+69.6 *vts*vts+109.0*vtd*vtd ;
double Rt_8=ST_t_8/ST_tbar_8 ;
double ST_t_13   =136.5*vtb*vtb+300.72*vts*vts+772.8*vtd*vtd ;
double ST_tbar_13=82.1 *vtb*vtb+177.1 *vts*vts+260.4*vtd*vtd  ;
double Rt_13=ST_t_13/ST_tbar_13 ;
double ST_ttbar_2=2.1*vtb*vtb+6.3 *vts*vts+24.3*vtd*vtd ;
double ST_t_8_fid   =0.06*56.3*vtb*vtb+0.074*132.5*vts*vts+0.069*406.4*vtd*vtd; 
double ST_tbar_8_fid=0.061*30.7*vtb*vtb+0.075*69.6*vts*vts+0.075*109.0*vtd*vtd; 
if (icat.Contains("Diff")){
for(int ibini=bin_min;ibini<=bin_max;ibini++)
{
exp_i        =R_val*(vtb*vtb*hist_Vtb.GetBinContent(ibini)+vts*vts*hist_Vts.GetBinContent(ibini)+vtd*vtd*hist_Vtd.GetBinContent(ibini));
err_mc_stat_i=R_val*sqrt(pow(vtb*vtb*hist_Vtb.GetBinError(ibini),2)+pow(vts*vts*hist_Vts.GetBinError(ibini),2)+pow(vtd*vtd*hist_Vtd.GetBinError(ibini),2));
err_sys_i    =R_val*sqrt(pow(hist_Vtb_sys_uncert.GetBinContent(ibini)*vtb*vtb*hist_Vtb.GetBinContent(ibini),2)+pow(hist_Vts_sys_uncert.GetBinContent(ibini)*vts*vts*hist_Vts.GetBinContent(ibini),2)+pow(hist_Vtd_sys_uncert.GetBinContent(ibini)*vtd*vtd*hist_Vtd.GetBinContent(ibini),2));
err_i        =sqrt(pow(hist_data.GetBinError(ibini),2)+pow(err_mc_stat_i,2)+pow(err_sys_i,2));
map<int, double> tmp_map=Correlation_matrix[ibini];
for (auto iter = tmp_map.begin(); iter != tmp_map.end(); iter++ ) { 
int ibinj=iter->first;
double corr=iter->second;
exp_j        =R_val*(vtb*vtb*hist_Vtb.GetBinContent(ibinj)+vts*vts*hist_Vts.GetBinContent(ibinj)+vtd*vtd*hist_Vtd.GetBinContent(ibinj));
err_mc_stat_j=R_val*sqrt(pow(vtb*vtb*hist_Vtb.GetBinError(ibinj),2)+pow(vts*vts*hist_Vts.GetBinError(ibinj),2)+pow(vtd*vtd*hist_Vtd.GetBinError(ibinj),2));
err_sys_j    =R_val*sqrt(pow(hist_Vtb_sys_uncert.GetBinContent(ibinj)*vtb*vtb*hist_Vtb.GetBinContent(ibinj),2)+pow(hist_Vts_sys_uncert.GetBinContent(ibinj)*vts*vts*hist_Vts.GetBinContent(ibinj),2)+pow(hist_Vtd_sys_uncert.GetBinContent(ibinj)*vtd*vtd*hist_Vtd.GetBinContent(ibinj),2));
err_j        =sqrt(pow(hist_data.GetBinError(ibinj),2)+pow(err_mc_stat_j,2)+pow(err_sys_j,2));
chi2=chi2+((exp_i-hist_data.GetBinContent(ibini))*corr*(exp_j-hist_data.GetBinContent(ibinj))/(err_i*err_j));
                                                                  }
}
//std::cout<<"diff chi2="<<chi2<<std::endl;
}
if(type.Contains("exp")){
if (icat.Contains("Inclusive")){
////////////////////////////// Add R info ////////////////////////////////////////////////
chi2=chi2+pow((exp_CMS_R[0]-R_val)/sqrt(exp_CMS_R[1]*exp_CMS_R[1]+exp_CMS_R[2]*exp_CMS_R[2]),2) ;//exp_CMS_R
//chi2=chi2+pow((exp_D0_R[0]-R_val)/exp_D0_R[1],2)                                    ;    //exp_D0_R
//chi2=chi2+pow((exp_CDF_R_1[0]-R_val)/exp_CDF_R_1[1],2)                              ;    //exp_CDF_R_1
//chi2=chi2+pow((exp_CDF_R_2[0]-R_val)/exp_CDF_R_2[1],2)                              ;    //exp_CDF_R_2
////////////////////////////// Add top width info ////////////////////////////////////////////////
chi2=chi2+pow((exp_ATLAS_W[0]-top_width)/sqrt(exp_ATLAS_W[1]*exp_ATLAS_W[1]+exp_ATLAS_W[2]*exp_ATLAS_W[2]),2) ; //exp_ATLAS_W
//chi2=chi2+pow((exp_CDF_W[0]-top_width)/exp_CDF_W[1],2) ; //exp_CDF_W
//chi2=chi2+pow((exp_D0_W[0] -top_width)/exp_D0_W[1] ,2) ;//exp_D0_W
////////////////////////////// Add TW XS info ////////////////////////////////////////////////
//chi2=chi2+pow((exp_ATLAS_TW_7[0]-TW_7*R_val)/sqrt(exp_ATLAS_TW_7[1]*exp_ATLAS_TW_7[1]+exp_ATLAS_TW_7[2]*exp_ATLAS_TW_7[2]),2);//exp_ATLAS_TW_7
chi2=chi2+pow((exp_ATLAS_TW_8[0]-TW_8*R_val)/sqrt(exp_ATLAS_TW_8[1]*exp_ATLAS_TW_8[1]+exp_ATLAS_TW_8[2]*exp_ATLAS_TW_8[2]+exp_ATLAS_TW_8[3]*exp_ATLAS_TW_8[3]),2);//exp_ATLAS_TW_8
chi2=chi2+pow((exp_ATLAS_TW_13[0]-TW_13*R_val)/sqrt(exp_ATLAS_TW_13[1]*exp_ATLAS_TW_13[1]+exp_ATLAS_TW_13[2]*exp_ATLAS_TW_13[2]+exp_ATLAS_TW_13[3]*exp_ATLAS_TW_13[3]),2);//exp_ATLAS_TW_13
chi2=chi2+pow((exp_CMS_TW_7[0]-TW_7*R_val)/exp_CMS_TW_7[1],2);//exp_CMS_TW_7
//chi2=chi2+pow((exp_CMS_TW_8[0]-TW_8*R_val)/exp_CMS_TW_8[1],2);//exp_CMS_TW_8
////////////////////////////// Add t-channel inclusive XS and Rt ////////////////////////////////////////////////
chi2=chi2+pow((exp_ATLAS_7_Rt[0]-Rt_7)/exp_ATLAS_7_Rt[1],2);//exp_ATLAS_7_Rt
chi2=chi2+pow((exp_ATLAS_8_Rt[0]-Rt_8)/exp_ATLAS_8_Rt[1],2);//exp_ATLAS_8_Rt
//chi2=chi2+pow((exp_ATLAS_13_t[0]-ST_t_13*R_val)/sqrt(exp_ATLAS_13_t[1]*exp_ATLAS_13_t[1]+exp_ATLAS_13_t[2]*exp_ATLAS_13_t[2]+exp_ATLAS_13_t[3]*exp_ATLAS_13_t[3]),2);//exp_ATLAS_13_t
//chi2=chi2+pow((exp_ATLAS_13_tbar[0]-ST_tbar_13*R_val)/sqrt(exp_ATLAS_13_tbar[1]*exp_ATLAS_13_tbar[1]+exp_ATLAS_13_tbar[2]*exp_ATLAS_13_tbar[2]+exp_ATLAS_13_tbar[3]*exp_ATLAS_13_tbar[3]),2);//exp_ATLAS_13_tbar
chi2=chi2+pow((exp_ATLAS_13_Rt[0]-Rt_13)/sqrt(exp_ATLAS_13_Rt[1]*exp_ATLAS_13_Rt[1]+exp_ATLAS_13_Rt[2]*exp_ATLAS_13_Rt[2]),2);//exp_ATLAS_13_Rt
chi2=chi2+pow((exp_CMS_7_ttbar[0]-(ST_t_7+ST_tbar_7)*R_val)/exp_CMS_7_ttbar[1],2);//exp_CMS_7_ttbar
//chi2=chi2+pow((exp_CMS_8_Rt[0]-Rt_8)/sqrt(exp_CMS_8_Rt[1]*exp_CMS_8_Rt[1]+exp_CMS_8_Rt[2]*exp_CMS_8_Rt[2]),2);//exp_CMS_8_Rt
chi2=chi2+pow((exp_CMS_8_t[0]-ST_t_8*R_val)/sqrt(exp_CMS_8_t[1]*exp_CMS_8_t[1]+exp_CMS_8_t[2]*exp_CMS_8_t[2]),2);//exp_CMS_8_t
chi2=chi2+pow((exp_CMS_8_tbar[0]-ST_tbar_8*R_val)/sqrt(exp_CMS_8_tbar[1]*exp_CMS_8_tbar[1]+exp_CMS_8_tbar[2]*exp_CMS_8_tbar[2]),2);//exp_CMS_8_tbar
chi2=chi2+pow((exp_CMS_13_t[0]-ST_t_13*R_val)/exp_CMS_13_t[1],2);//exp_CMS_13_t
chi2=chi2+pow((exp_CMS_13_tbar[0]-ST_tbar_13*R_val)/exp_CMS_13_tbar[1],2);//exp_CMS_13_tbar
//chi2=chi2+pow((exp_CMS_13_Rt[0]-Rt_13)/sqrt(exp_CMS_13_Rt[1]*exp_CMS_13_Rt[1]+exp_CMS_13_Rt[2]*exp_CMS_13_Rt[2]),2);//exp_CMS_13_Rt
chi2=chi2+pow((exp_D0_ttbar[0]-ST_ttbar_2*R_val)/exp_D0_ttbar[1],2);//exp_D0_ttbar
}
if(icat.Contains("8TeV") && icat.Contains("tW")){
chi2=chi2+pow((exp_ATLAS_TW_8[0]-TW_8*R_val)/sqrt(exp_ATLAS_TW_8[1]*exp_ATLAS_TW_8[1]+exp_ATLAS_TW_8[2]*exp_ATLAS_TW_8[2]+exp_ATLAS_TW_8[3]*exp_ATLAS_TW_8[3]),2);//ATLAS_TW_8
//chi2=chi2+pow((exp_CMS_TW_8[0]-TW_8*R_val)/exp_CMS_TW_8[1],2);//CMS_TW_8
}
if(icat.Contains("8TeV") && icat.Contains("ST")){
chi2=chi2+pow((exp_CMS_8_t[0]   -ST_t_8*R_val   )/sqrt(exp_CMS_8_t[1]   *exp_CMS_8_t[1]   +exp_CMS_8_t[2]   *exp_CMS_8_t[2])   ,2);//CMS_8_t
chi2=chi2+pow((exp_CMS_8_tbar[0]-ST_tbar_8*R_val)/sqrt(exp_CMS_8_tbar[1]*exp_CMS_8_tbar[1]+exp_CMS_8_tbar[2]*exp_CMS_8_tbar[2]),2);//CMS_8_tbar
}
if(icat.Contains("8TeV") && icat.Contains("st_fid")){
chi2=chi2+pow((exp_ATLAS_8_t_fid[0]      -ST_t_8_fid   *R_val   )/exp_ATLAS_8_t_fid[1]      ,2);//ATLAS_8_t_fid
chi2=chi2+pow((exp_ATLAS_8_tbar_fid[0]   -ST_tbar_8_fid*R_val   )/exp_ATLAS_8_tbar_fid[1]   ,2);//ATLAS_8_tbar_fid
}
if(icat.Contains("8TeV") && icat.Contains("Width")){
chi2=chi2+pow((exp_ATLAS_W[0]-top_width)/sqrt(exp_ATLAS_W[1]*exp_ATLAS_W[1]+exp_ATLAS_W[2]*exp_ATLAS_W[2]),2) ; //ATLAS_W
}
if(icat.Contains("Ratio")){
if     (icat.Contains("13TeV"))chi2=chi2+pow((exp_CMS_R[0]-R_val)/sqrt(exp_CMS_R[1]*exp_CMS_R[1]+exp_CMS_R[2]*exp_CMS_R[2]),2) ;
else if(icat.Contains("8TeV")) chi2=chi2+pow((exp_CMS_R[0]-R_val)/sqrt(exp_CMS_R[1]*exp_CMS_R[1]+exp_CMS_R[2]*exp_CMS_R[2]),2) ;//CMS_R
}
if(icat.Contains("8TeV") && icat.Contains("Rt")){
chi2=chi2+pow((exp_ATLAS_8_Rt[0]-Rt_8)/exp_ATLAS_8_Rt[1],2);//ATLAS_8_Rt
//chi2=chi2+pow((exp_CMS_8_Rt[0]  -Rt_8)/sqrt(exp_CMS_8_Rt[1]*exp_CMS_8_Rt[1]+exp_CMS_8_Rt[2]*exp_CMS_8_Rt[2]),2);//CMS_8_Rt
}
}
else{
if (icat.Contains("Inclusive")){
////////////////////////////// Add R info ////////////////////////////////////////////////
chi2=chi2+pow((CMS_R[0]-R_val)/sqrt(CMS_R[1]*CMS_R[1]+CMS_R[2]*CMS_R[2]),2) ;//CMS_R
//chi2=chi2+pow((D0_R[0]-R_val)/D0_R[1],2)                                    ;    //D0_R
//chi2=chi2+pow((CDF_R_1[0]-R_val)/CDF_R_1[1],2)                              ;    //CDF_R_1
//chi2=chi2+pow((CDF_R_2[0]-R_val)/CDF_R_2[1],2)                              ;    //CDF_R_2
//std::cout<<"R chi2="<<chi2<<std::endl;
////////////////////////////// Add top width info ////////////////////////////////////////////////
chi2=chi2+pow((ATLAS_W[0]-top_width)/sqrt(ATLAS_W[1]*ATLAS_W[1]+ATLAS_W[2]*ATLAS_W[2]),2) ; //ATLAS_W
chi2=chi2+pow((CDF_W[0]-top_width)/CDF_W[1],2) ; //CDF_W
chi2=chi2+pow((D0_W[0] -top_width)/D0_W[1] ,2) ;//D0_W
//std::cout<<"W chi2="<<chi2<<std::endl;
////////////////////////////// Add TW XS info ////////////////////////////////////////////////
chi2=chi2+pow((ATLAS_TW_7[0]-TW_7*R_val)/sqrt(ATLAS_TW_7[1]*ATLAS_TW_7[1]+ATLAS_TW_7[2]*ATLAS_TW_7[2]),2);//ATLAS_TW_7
chi2=chi2+pow((ATLAS_TW_8[0]-TW_8*R_val)/sqrt(ATLAS_TW_8[1]*ATLAS_TW_8[1]+ATLAS_TW_8[2]*ATLAS_TW_8[2]+ATLAS_TW_8[3]*ATLAS_TW_8[3]),2);//ATLAS_TW_8
chi2=chi2+pow((ATLAS_TW_13[0]-TW_13*R_val)/sqrt(ATLAS_TW_13[1]*ATLAS_TW_13[1]+ATLAS_TW_13[2]*ATLAS_TW_13[2]+ATLAS_TW_13[3]*ATLAS_TW_13[3]),2);//ATLAS_TW_13
chi2=chi2+pow((CMS_TW_7[0]-TW_7*R_val)/CMS_TW_7[1],2);//CMS_TW_7
chi2=chi2+pow((CMS_TW_8[0]-TW_8*R_val)/CMS_TW_8[1],2);//CMS_TW_8
//std::cout<<"tW chi2="<<chi2<<std::endl;
////////////////////////////// Add t-channel inclusive XS and Rt ////////////////////////////////////////////////
chi2=chi2+pow((ATLAS_7_Rt[0]-Rt_7*R_val)/ATLAS_7_Rt[1],2);//ATLAS_7_Rt
chi2=chi2+pow((ATLAS_8_Rt[0]-Rt_8*R_val)/ATLAS_8_Rt[1],2);//ATLAS_8_Rt
chi2=chi2+pow((ATLAS_13_t[0]-ST_t_13*R_val)/sqrt(ATLAS_13_t[1]*ATLAS_13_t[1]+ATLAS_13_t[2]*ATLAS_13_t[2]+ATLAS_13_t[3]*ATLAS_13_t[3]),2);//ATLAS_13_t
chi2=chi2+pow((ATLAS_13_tbar[0]-ST_tbar_13*R_val)/sqrt(ATLAS_13_tbar[1]*ATLAS_13_tbar[1]+ATLAS_13_tbar[2]*ATLAS_13_tbar[2]+ATLAS_13_tbar[3]*ATLAS_13_tbar[3]),2);//ATLAS_13_tbar
chi2=chi2+pow((ATLAS_13_Rt[0]-Rt_13)/sqrt(ATLAS_13_Rt[1]*ATLAS_13_Rt[1]+ATLAS_13_Rt[2]*ATLAS_13_Rt[2]),2);//ATLAS_13_Rt
chi2=chi2+pow((CMS_7_ttbar[0]-(ST_t_7+ST_tbar_7)*R_val)/CMS_7_ttbar[1],2);//CMS_7_ttbar
chi2=chi2+pow((CMS_8_Rt[0]-Rt_8)/sqrt(CMS_8_Rt[1]*CMS_8_Rt[1]+CMS_8_Rt[2]*CMS_8_Rt[2]),2);//CMS_8_Rt
chi2=chi2+pow((CMS_8_t[0]-ST_t_8*R_val)/sqrt(CMS_8_t[1]*CMS_8_t[1]+CMS_8_t[2]*CMS_8_t[2]),2);//CMS_8_t
chi2=chi2+pow((CMS_8_tbar[0]-ST_tbar_8*R_val)/sqrt(CMS_8_tbar[1]*CMS_8_tbar[1]+CMS_8_tbar[2]*CMS_8_tbar[2]),2);//CMS_8_tbar
chi2=chi2+pow((CMS_13_t[0]-ST_t_13*R_val)/CMS_13_t[1],2);//CMS_13_t
chi2=chi2+pow((CMS_13_tbar[0]-ST_tbar_13*R_val)/CMS_13_tbar[1],2);//CMS_13_tbar
chi2=chi2+pow((CMS_13_Rt[0]-Rt_13)/sqrt(CMS_13_Rt[1]*CMS_13_Rt[1]+CMS_13_Rt[2]*CMS_13_Rt[2]),2);//CMS_13_Rt
chi2=chi2+pow((D0_ttbar[0]-ST_ttbar_2*R_val)/D0_ttbar[1],2);//D0_ttbar
//std::cout<<"ST chi2="<<chi2<<std::endl;
}
if (icat.Contains("Ratio")){
chi2=chi2+pow((CMS_R[0]-R_val)/sqrt(CMS_R[1]*CMS_R[1]+CMS_R[2]*CMS_R[2]),2) ;//CMS_R
//std::cout<<"R chi2="<<chi2<<std::endl;
}
if(icat.Contains("8TeV") && icat.Contains("st_fid")){
chi2=chi2+pow((ATLAS_8_t_fid[0]    -ST_t_8_fid*R_val      )/ATLAS_8_t_fid[1]   ,2);//ATLAS_8_t_fid
chi2=chi2+pow((ATLAS_8_tbar_fid[0] -ST_tbar_8_fid*R_val   )/ATLAS_8_tbar_fid[1]   ,2);//ATLAS_8_tbar_fid
}
}
//////////////////////////////// Calculate Prob //////////////////////////////////////////////
//std::cout<<"prob="<<double(TMath::Prob( chi2,ndof))<<",chi2="<<chi2<<",ndof="<<ndof<<std::endl;
//tmp_chi2={chi2};
//return double(TMath::Prob( chi2,ndof));
pair <double,double> result(TMath::Prob(chi2,ndof),chi2); 
return result;
}
