
#qdel 14483238 
#qdel 14483261 
#qdel 14483263 
#qdel 14483330 

qsub -q localgrid ./Job_split/split_1763.sh
qsub -q localgrid ./Job_split/split_0832.sh
qsub -q localgrid ./Job_split/split_0950.sh
qsub -q localgrid ./Job_split/split_1879.sh










