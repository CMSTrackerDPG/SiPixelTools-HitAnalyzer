#
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
process = cms.Process("d",eras.Run3)

import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
# accept if 'path_1' succeeds
process.hltfilter = hlt.hltHighLevel.clone(
# Min-Bias
#    HLTPaths = ['HLT_Physics_v*'],  # not in ZB stream
#    HLTPaths = ['DST_Physics_v*'], useless 
#    HLTPaths = ['HLT_Random_v*'],
#    HLTPaths = ['HLT_ZeroBias_v*'],
#    HLTPaths = ['HLT_L1Tech54_ZeroBias*'],
# Commissioning:
#    HLTPaths = ['HLT_L1_Interbunch_BSC_v*'],
#    HLTPaths = ['HLT_L1_PreCollisions_v1'],
#    HLTPaths = ['HLT_BeamGas_BSC_v*'],
#    HLTPaths = ['HLT_BeamGas_HF_v*'],
# LumiPixels
#    HLTPaths = ['AlCa_LumiPixels_Random_v*'],
#    HLTPaths = ['AlCa_LumiPixels_ZeroBias_v*'],
#    HLTPaths = ['AlCa_LumiPixels_v*'],
# HI
#    HLTPaths = ['HLT_HIRandom*'],
    HLTPaths = ['HLT_HIMinimumBiasHF1ANDZDC*'],
   
# examples
#    HLTPaths = ['p*'],
#    HLTPaths = ['path_?'],
    andOr = True,  # False = and, True=or
    throw = False
    )

# process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('dumper'),
    destinations = cms.untracked.vstring('cout'),
#    destinations = cms.untracked.vstring("log","cout"),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING')
    )
#    log = cms.untracked.PSet(
#        threshold = cms.untracked.string('DEBUG')
#    )
)
#process.MessageLogger.cerr.FwkReport.reportEvery = 1
#process.MessageLogger.cerr.threshold = 'Debug'

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('raw.root')
)

myfilelist = cms.untracked.vstring()
myfilelist.extend([
])

process.source = cms.Source("PoolSource",
# fileNames =  myfilelist)
    fileNames = cms.untracked.vstring(

"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/0e9daa80-f3ac-4e1e-9ddf-ec0c29441dab.root",
"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/f238c278-cb51-4a87-99f2-ff7ad1d3a587.root",
"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/761c0b2f-c86f-4dc1-9a93-0f5822819521.root",
"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/3c53c2e1-b354-4c6f-b4c7-e0b14b0f8260.root",
"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/7f47999a-e8ac-43a9-aa6e-c6b265a12a91.root",
"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/c26cb958-7fa3-4e33-a1ab-e930612a5b45.root",
"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/1ef69fa5-3a84-41ef-b4cc-a6a380946b8f.root",
"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/6bb36cf3-0d09-464c-b80f-ea29b832ca06.root",
"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/f7c74548-28bb-4104-a417-806fe27b972c.root",
"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/9ff71d51-8ea7-480a-a9b1-22d73da97b00.root",

#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v2/000/374/810/00000/da1c27b7-ff6a-43a0-b708-3c4039bac111.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v2/000/374/810/00000/0b51694c-0263-46e9-9d1d-1b690da3c0cd.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v2/000/374/810/00000/2b117ecc-5511-4851-b3d1-a492aa62d8e0.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v2/000/374/810/00000/eea7c671-bfb8-4169-98a1-32ece1655f0d.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v2/000/374/810/00000/294719e5-50d2-4881-a784-f25a70e18847.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v2/000/374/810/00000/24130d18-5a03-4117-934f-60548e49e047.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v2/000/374/810/00000/64bd4019-2e95-46be-9bb2-88b4bf6ef8bd.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v2/000/374/810/00000/9421d7e5-9bb0-4f0d-aa3d-f795b3f1a4c7.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v2/000/374/810/00000/172d5ebe-414b-4b05-902d-df07342f225e.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v2/000/374/810/00000/51b62508-bbdb-42e7-a432-1172be95a179.root",

#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/354/00000/c2cb56ee-a125-45ef-b6c5-612d6ea3ad7d.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/354/00000/02a578b4-d2c9-4085-a407-14857851d848.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/354/00000/0bf45c49-7e4f-47c2-b502-4dd5548453f0.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/354/00000/f687c060-4f75-4967-994b-bd45df436999.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/354/00000/d7b044b9-92b9-4249-9bc5-c906dadd1dff.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/354/00000/9b6dfaba-7b2e-4f07-b882-91c7c1007543.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/354/00000/6466e905-86b2-43cb-92b6-077fce905e7b.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/354/00000/0a1085df-5659-445d-a42d-880dde15e78a.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/354/00000/d1abb169-ad31-444f-a5b2-614c473aa8cd.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/354/00000/48a18d4c-9b4d-44ad-9497-4dfeb5fd8a89.root",

#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/289/00000/2c7613fb-60e2-4a13-a0e5-fc86eacbf397.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/289/00000/5bfe58cb-b867-4cfc-8021-b7c19547849e.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/289/00000/d4156f41-c0ae-405b-b493-ee73c410438b.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/289/00000/9de4ea8a-0a1d-4633-9ea6-9b54c63f595b.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/289/00000/e0ebec7f-2023-4d9e-8407-904780eae41f.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/289/00000/f4ec65e7-9878-47b0-9388-99da94e983f4.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/289/00000/c072264f-7c44-4ff2-8f52-2fe72ec6724c.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/289/00000/c9b24fe9-49c5-469c-a36b-141fdf2f487c.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/289/00000/b6c3381a-b928-40d8-8adb-1f20d376d8c5.root",
##"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/289/00000/88819b55-87d2-4192-a3a3-da701ceb286d.root",

#"/store/express/Run2023E/ExpressPhysics/FEVT/Express-v1/000/373/061/00000/1364522d-7428-48ac-af45-ce36bafcc3ad.root",
#"/store/express/Run2023E/ExpressPhysics/FEVT/Express-v1/000/373/061/00000/7630847a-a966-4380-bf84-5c521f870f50.root",
#"/store/express/Run2023E/ExpressPhysics/FEVT/Express-v1/000/373/061/00000/210ad411-84e8-4b0d-a9ed-3167ff709c13.root",
#"/store/express/Run2023E/ExpressPhysics/FEVT/Express-v1/000/373/061/00000/2e8f2119-4ed2-4fd0-916e-e24876689724.root",
#"/store/express/Run2023E/ExpressPhysics/FEVT/Express-v1/000/373/061/00000/4a7e6e62-d262-43e5-b58c-004864edfadb.root",
#"/store/express/Run2023E/ExpressPhysics/FEVT/Express-v1/000/373/061/00000/a5c1128f-b115-4881-b2c7-33e23f91b307.root",
#"/store/express/Run2023E/ExpressPhysics/FEVT/Express-v1/000/373/061/00000/f680a3d3-24e6-45d4-b294-ad98ebd4b637.root",
#"/store/express/Run2023E/ExpressPhysics/FEVT/Express-v1/000/373/061/00000/bfa5e631-4c68-4a12-8bc9-d4490c94a5b5.root",
#"/store/express/Run2023E/ExpressPhysics/FEVT/Express-v1/000/373/061/00000/4d2728ba-27da-4ed0-ad8a-e3d9c9b92561.root",
#"/store/express/Run2023E/ExpressPhysics/FEVT/Express-v1/000/373/061/00000/d58689aa-0cfd-41dd-a3eb-80f305fff495.root",

   )
)

# for dump files 
#process.source = cms.Source("PixelSLinkDataInputSource",
#    fedid = cms.untracked.int32(-1),
#    runNumber = cms.untracked.int32(-1),
#    #fileNames = cms.untracked.vstring('file:../phase1/PixelAlive_1293_1018.dmp')
#    fileNames = cms.untracked.vstring(
#     #'/store/group/dpg_tracker_pixel/comm_pixel/GainCalibrations/Phase1/Run_300/GainCalibration_1293_1015.dmp'
#     #'/store/group/dpg_tracker_pixel/comm_pixel/GainCalibrations/Phase1/Run_300/GainCalibration_1200_1015.dmp'
#     '/store/group/dpg_tracker_pixel/comm_pixel/GainCalibrations/Phase1/Run_300/GainCalibration_1300_300.dmp'
#    )
# )

process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('374778:38-374778:306')
process.source.skipBadFiles = cms.untracked.bool( True )

process.d = cms.EDAnalyzer("SiPixelRawDump", 
    Timing = cms.untracked.bool(False),
    IncludeErrors = cms.untracked.bool(True),
#   In 2015 data, label = rawDataCollector, extension = _LHC        
#    InputLabel = cms.untracked.string('rawDataCollector'), # for p-p
    InputLabel = cms.untracked.string('rawDataRepacker'), # for HI
# for MC
#    InputLabel = cms.untracked.string('siPixelRawData'),
#   For PixelLumi stream                           
#    InputLabel = cms.untracked.string('hltFEDSelectorLumiPixels'),

# for dump files 
#    InputLabel = cms.untracked.string('source'),
# old
#    InputLabel = cms.untracked.string('siPixelRawData'),
#    InputLabel = cms.untracked.string('source'),
#    InputLabel = cms.untracked.string("ALCARECOTkAlMinBias"), # does not work

    CheckPixelOrder = cms.untracked.bool(False),
# 0 - nothing, 1 - error , 2- data, 3-headers, 4-hex
                           Verbosity = cms.untracked.int32(0),
# threshold, print fed/channel num of errors if tot_errors > events * PrintThreshold, default 0,001 
                           PrintThreshold = cms.untracked.double(0.001),
                           selectedFED = cms.untracked.int32(-1),
                           selectedChannel = cms.untracked.int32(-1),
                           selectedType = cms.untracked.int32(-1),
                           bpixOnly = cms.untracked.bool(False),
                           hitsCut = cms.untracked.int32(400), #hits in 1 roc
                           hitsCut2 = cms.untracked.int32(500), #hits per chan
)

#process.p = cms.Path(process.hltfilter*process.d)
process.p = cms.Path(process.d) # for cosmics  use no trigger 

# process.ep = cms.EndPath(process.out)


