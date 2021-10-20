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
    HLTPaths = ['HLT_ZeroBias_v*'],
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
"/store/express/Run2018D/ExpressPhysics/FEVT/Express-v1/000/325/159/00000/2EB3AEDA-747D-FB46-9583-BC1F1241CFE7.root",
])

process.source = cms.Source("PoolSource",
# fileNames =  myfilelist
    fileNames = cms.untracked.vstring(
                          
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/d76f76b4-2162-4e70-a967-a527b0b0184c.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/2ec08322-19c0-46e5-815d-6cd2b81f2d7b.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/be1e95ec-c502-46b6-86d4-655182f38980.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/3279f59f-6efe-4994-88dc-91217e7a9d6a.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/b7a4517e-1359-45d3-8aeb-cc6ebd57a679.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/1603df00-db5b-4f43-9318-f345342b12d9.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/82d6fb27-86bb-4acf-b03a-c34b4bbd5b3f.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/8e1219d8-2bd9-4a96-8f03-9af02a995a24.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/f71df157-bed0-41ff-858b-488bfcb6b6a0.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/294c1b20-f745-45f9-a981-10a795e004c5.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/6b3c1c8b-1007-4f2a-89b8-c26d879e894c.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/67383448-8b1d-4ebf-8f26-e6252e9a6101.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/59e457bb-96b4-4c9c-b4b6-f7c119fcc316.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/50379c2a-d81f-4dcf-adcf-c4801b27b9cf.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/fb5120bf-3acd-4503-a44b-a7f7927dade2.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/1805e979-b139-49ce-840c-068d5b28a70f.root",

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

#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('325159:1-325159:47')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('325159:1-325159:34')  # no collisions, no HV
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('325159:35-325159:46') # collisions no HV 
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('325159:47-325159:61') # nonstable lumi
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('325159:62-325159:999')

process.d = cms.EDAnalyzer("SiPixelRawDump", 
    Timing = cms.untracked.bool(False),
    IncludeErrors = cms.untracked.bool(True),
#   In 2015 data, label = rawDataCollector, extension = _LHC                                
    InputLabel = cms.untracked.string('rawDataCollector'),

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
                           selectedType = cms.untracked.int32(-1)
)

#process.p = cms.Path(process.hltfilter*process.d)
process.p = cms.Path(process.d)

# process.ep = cms.EndPath(process.out)


