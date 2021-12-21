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
])

process.source = cms.Source("PoolSource",
# fileNames =  myfilelist
    fileNames = cms.untracked.vstring(

"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/9847bf8f-bc3e-4ec6-b417-e598366387e3.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/e76118dc-a56e-494e-ad01-778dd2e6a542.root",


#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/260/00000/a5d78084-ebac-481e-a053-d8678aafc8db.root",

#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/222/00000/3bf7f901-d269-45e0-888d-0de42606046b.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/222/00000/2ca90bb0-5d5f-43d1-9d8b-355c2a2440b4.root",

#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/152/00000/4f3871fd-c3a0-4090-9444-5ec565e00764.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/152/00001/1b922864-0d08-4cf1-8fcf-e86591c22f6d.root",

#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/024/00000/5143421d-e7b6-4e9c-96b2-e7b98892b178.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/850/00000/e2291232-b5cb-4382-a8ea-1a5e0d791f9d.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/924/00000/fe6c7291-333d-4609-af9a-7948cb05df17.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/979/00000/f63ea27e-cb73-4857-813f-71dd90567d6d.root",


#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/777/00000/cfefd0f1-5d00-4d82-b27f-5efbf1eacaa8.root",

#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/05d4e531-3560-40bd-ba85-d18f4fa78981.root", 
                         
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/d76f76b4-2162-4e70-a967-a527b0b0184c.root",

#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/299/00000/043c9bc6-c62f-41a1-bb76-957481dc340d.root",

# "root://eoscms.cern.ch//eos/cms/tier0/store/express/Commissioning2021/StreamExpress/

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


