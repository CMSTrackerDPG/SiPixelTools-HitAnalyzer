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

# 2018
# /store/mc/Run3Summer19DR/TTbar_14TeV_TuneCP5_Pythia8/GEN-SIM-DIGI-RAW/106X_mcRun3_2021_realistic_v3-v2/130000/F37978B0-7657-4845-B84A-918A4C91652E.root
#"/store/relval/CMSSW_10_6_1_patch3/RelValTTbar_13/GEN-SIM-RECO/PU25ns_106X_upgrade2018_realistic_v6-v1/20000/FF0A1ADF-8ECA-514A-A177-2723BCCABDE0.root",
#/cvmfs/cms.cern.ch/common/dasgoclient  --limit=0 --query='file dataset=/ExpressCosmics/Commissioning2018-Express-v1/FEVT run=313759'
 
# 2018 data 
#/cvmfs/cms.cern.ch/common/dasgoclient  --limit=0 --query='file dataset=/ExpressPhysics/Run2018D-Express-v1/FEVT run=325097'
#/cvmfs/cms.cern.ch/common/dasgoclient  --limit=0 --query='file dataset=/ExpressPhysics/Run2018E-Express-v1/FEVT run=325308'
#/cvmfs/cms.cern.ch/common/dasgoclient  --limit=0 --query='file dataset=/HIExpressPhysics/HIRun2018A-Express-v1/FEVT run=326384'

#dasgoclient -query='dataset dataset=/*/Run2018*/RAW site=T2_CH_CERN'  # all RAW at CERN
#dasgoclient -query='file dataset=/ZeroBias/Run2018E-v1/RAW site=T2_CH_CERN'  # all RAW at CERN
#dasgoclient -query='file dataset=/HIMinimumBias0/HIRun2018A-v1/RAW run=327560'  # RAW HI

# 2021 cosmics, express 
#dasgoclient -query='file dataset=/ExpressCosmics/Commissioning2021-Express-v1/FEVT run=347272'
#dasgoclient -query='file dataset=/ExpressPhysics/Commissioning2021-Express-v1/FEVT run=346450'
 # ZB
#dasgoclient -query='file dataset=/ZeroBias/Commissioning2021-v1/RAW run=346396'  
# 2022
#dasgoclient -query='file dataset=/ExpressCosmics/Commissioning2022-Express-v1/FEVT run=352040'
#dasgoclient -query='file dataset=/ExpressPhysics/Commissioning2022-Express-v1/FEVT run=352165'
#dasgoclient -query='file dataset=/ExpressCosmics/Run2022A-Express-v1/FEVT run=352417'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2022B-Express-v1/FEVT run=355100'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2022C-Express-v1/FEVT run=357101'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2022D-Express-v2/FEVT run=357895'
#dasgoclient -query='file dataset=/ExpressCosmics/Run2022D-Express-v3/FEVT run=358831'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2022E-Express-v1/FEVT run=359291'
#dasgoclient -query='file dataset=/ExpressPhysics/Run2022F-Express-v1/FEVT run=361045'
dasgoclient -query='file dataset=/ExpressPhysics/Run2022G-Express-v1/FEVT run=362614'
