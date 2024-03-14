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

"root://eoscms.cern.ch//eos/cms/store/express/Commissioning2024/ExpressCosmics/FEVT/Express-v1/000/376/826/00000/f6f7484f-ff8c-4a19-b407-8cd6875dfccd.root",
"root://eoscms.cern.ch//eos/cms/store/express/Commissioning2024/ExpressCosmics/FEVT/Express-v1/000/376/826/00000/c03d9316-8844-4d71-9acd-4a601f16b8e0.root",
"root://eoscms.cern.ch//eos/cms/store/express/Commissioning2024/ExpressCosmics/FEVT/Express-v1/000/376/826/00000/51146cdf-2957-48a0-8fb4-50b1119dfe8e.root",
"root://eoscms.cern.ch//eos/cms/store/express/Commissioning2024/ExpressCosmics/FEVT/Express-v1/000/376/826/00000/1bd604f8-6c6f-40c5-a842-2825b7ea706b.root",
"root://eoscms.cern.ch//eos/cms/store/express/Commissioning2024/ExpressCosmics/FEVT/Express-v1/000/376/826/00000/7e8daa17-6dec-439a-a83f-b068d7965bd7.root",
"root://eoscms.cern.ch//eos/cms/store/express/Commissioning2024/ExpressCosmics/FEVT/Express-v1/000/376/826/00000/0e10a07b-e8c1-46fe-b726-d1e3034970e6.root",
"root://eoscms.cern.ch//eos/cms/store/express/Commissioning2024/ExpressCosmics/FEVT/Express-v1/000/376/826/00000/d7168a7e-12ad-455d-bd88-c264d89caf59.root",
"root://eoscms.cern.ch//eos/cms/store/express/Commissioning2024/ExpressCosmics/FEVT/Express-v1/000/376/826/00000/8ef16e3e-f8a8-480e-b383-5097ae87a238.root",
"root://eoscms.cern.ch//eos/cms/store/express/Commissioning2024/ExpressCosmics/FEVT/Express-v1/000/376/826/00000/f6293bf5-4a8a-497a-8ebb-a5b3435ebe54.root",
"root://eoscms.cern.ch//eos/cms/store/express/Commissioning2024/ExpressCosmics/FEVT/Express-v1/000/376/826/00000/161384c8-828e-4390-97b2-0cf8f8d3086d.root",

#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/0e9daa80-f3ac-4e1e-9ddf-ec0c29441dab.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/f238c278-cb51-4a87-99f2-ff7ad1d3a587.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/761c0b2f-c86f-4dc1-9a93-0f5822819521.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/3c53c2e1-b354-4c6f-b4c7-e0b14b0f8260.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/7f47999a-e8ac-43a9-aa6e-c6b265a12a91.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/c26cb958-7fa3-4e33-a1ab-e930612a5b45.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/1ef69fa5-3a84-41ef-b4cc-a6a380946b8f.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/6bb36cf3-0d09-464c-b80f-ea29b832ca06.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/f7c74548-28bb-4104-a417-806fe27b972c.root",
#"root://eoscms.cern.ch//eos/cms/store/express/HIRun2023A/HIExpressPhysics/FEVT/Express-v1/000/374/778/00000/9ff71d51-8ea7-480a-a9b1-22d73da97b00.root",

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


