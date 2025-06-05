# dbs search --query='find file, file.numevents where run=172998 and site=caf.cern.ch and dataset=/MinimumBias/Run2011A-PromptReco-v6/RECO' > bla.txt
# Lumi
#das_client.py --limit=0 --query='file dataset=/AlCaLumiPixels/Run2015C-LumiPixels-v1/RAW run=254319' # YES
#das_client.py --limit=0 --query='file dataset=/AlCaLumiPixels/Run2015D-LumiPixels-PromptReco-v4/ALCARECO run=260490' 

# 2016
#das_client.py --limit=0 --query='file dataset=/ExpressPhysics/Run2016E-Express-v2/FEVT run=277148' # 
# 2017 
#/cvmfs/cms.cern.ch/common/das_client  --limit=0 --query='file dataset=/ZeroBias/Run2017C-PromptReco-v3/RECO run=300742' 
#/cvmfs/cms.cern.ch/common/das_client  --limit=0 --query='file dataset=/ExpressPhysics/Run2017F-Express-v1/FEVT run=305282' 
#/cvmfs/cms.cern.ch/common/dasgoclient  --limit=0 --query='file dataset=/ZeroBias/Run2017F-*/RECO'  # works


#dasgoclient -query='dataset dataset=/*/Run2018*/RAW site=T2_CH_CERN'  # all RAW at CERN
#dasgoclient -query='file dataset=/ZeroBias/Run2018E-v1/RAW site=T2_CH_CERN'  # all RAW at CERN
#dasgoclient -query='file dataset=/HIMinimumBias0/HIRun2018A-v1/RAW run=327560'  # RAW HI

# 2021 cosmics, express 
#dasgoclient -query='file dataset=/ExpressCosmics/Commissioning2021-Express-v1/FEVT run=347272'
#dasgoclient -query='file dataset=/ExpressPhysics/Commissioning2021-Express-v1/FEVT run=346450'
 # ZB
#dasgoclient -query='file dataset=/ZeroBias/Commissioning2021-v1/RAW run=346396'  
# 2022
#dasgoclient -query='file dataset=/ExpressPhysics/Commissioning2022-Express-v1/FEVT run=352165'
#dasgoclient -query='file dataset=/ExpressCosmics/Run2022A-Express-v1/FEVT run=352417'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2022B-Express-v1/FEVT run=355100'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2022C-Express-v1/FEVT run=357101'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2022D-Express-v2/FEVT run=357895'
#dasgoclient -query='file dataset=/ExpressCosmics/Run2022D-Express-v3/FEVT run=358831'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2022E-Express-v1/FEVT run=359291'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2022G-Express-v1/FEVT run=362614'
# 2023
#dasgoclient -query='file dataset=/ExpressCosmics/Commissioning2023-Express-v1/FEVT run=364174'
#dasgoclient -query='file dataset=/ExpressCosmics/Commissioning2023-Express-v2/FEVT run=365300'
#dasgoclient -query='file dataset=/ExpressCosmics/Run2023A-Express-v1/FEVT run=365936'
#dasgoclient -query='file dataset=/ExpressCosmics/Run2023A-Express-v2/FEVT run=366002'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2023A-Express-v1/FEVT run=365775'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2023B-Express-v1/FEVT run=366449'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2023C-Express-v1/FEVT run=367127'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2023C-Express-v2/FEVT run=367836'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2023C-Express-v4/FEVT run=367883'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2023D-Express-v1/FEVT run=370093'
#dasgoclient -query='file dataset=/ExpressCosmics/Run2023D-Express-v2/FEVT run=371692'
#dasgoclient -query='file dataset=/ExpressCosmics/Run2023E-Express-v1/FEVT run=372439'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2023E-Express-v1/FEVT run=373061'
#dasgoclient -query='file dataset=/HIExpressPhysics/HIRun2023A-Express-v1/FEVT run=374289'
#dasgoclient -query='file dataset=/HIExpressPhysics/HIRun2023A-Express-v2/FEVT run=375513'
# 24
#dasgoclient -query='file dataset=/ExpressCosmics/Commissioning2024-Express-v1/FEVT run=376826' 
#dasgoclient -query='file dataset=/ExpressPhysics/Run2024A-Express-v1/FEVT run=378239' 
#dasgoclient -query='file dataset=/ExpressPhysics/Run2024B-Express-v1/FEVT run=378985' 
#dasgoclient -query='file dataset=/ExpressPhysics/Run2024C-Express-v1/FEVT run=379470' 
#dasgoclient -query='file dataset=/ExpressPhysics/Run2024D-Express-v1/FEVT run=380384' 
#dasgoclient -query='file dataset=/ExpressPhysics/Run2024E-Express-v1/FEVT run=381543' 
#dasgoclient -query='file dataset=/ExpressPhysics/Run2024F-Express-v1/FEVT run=382878' 
#dasgoclient -query='file dataset=/ExpressPhysics/Run2024G-Express-v1/FEVT run=383996' 
#dasgoclient -query='file dataset=/ExpressPhysics/Run2024H-Express-v1/FEVT run=386319' 
#dasgoclient -query='file dataset=/ExpressPhysics/Run2024I-Express-v1/FEVT run=386509' 
#dasgoclient -query='file dataset=/HIExpressPhysics/HIRun2024A-Express-v1/FEVT run=388056' 
#dasgoclient -query='file dataset=/ExpressCosmics/HIRun2024A-Express-v1/FEVT run=388089' 
#dasgoclient -query='file dataset=/HIExpressPhysics/HIRun2024B-Express-v2/FEVT run=388769' 
# 25 
#dasgoclient -query='file dataset=/ExpressCosmics/Commissioning2025-Express-v1/FEVT run=389356'  
#dasgoclient -query='file dataset=/ExpressCosmics/Commissioning2025-Express-v2/FEVT run=389832'  
#dasgoclient -query='file dataset=/ExpressPhysics/Run2025A-Express-v1/FEVT run=390960'  
dasgoclient -query='file dataset=/ExpressPhysics/Run2025B-Express-v1/FEVT run=391910'  
