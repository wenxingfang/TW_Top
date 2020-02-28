combineTool.py -M Impacts -d  data_card/ee_card.root -m 125 --robustFit 1 --doInitialFit -t -1 --expectSignal=1
combineTool.py -M Impacts -d  data_card/ee_card.root -m 125 --robustFit 1 --doFits       -t -1 --expectSignal=1
combineTool.py -M Impacts -d  data_card/ee_card.root -m 125 -t -1 --expectSignal=1              -o impacts.json
plotImpacts.py -i impacts.json -o impacts
