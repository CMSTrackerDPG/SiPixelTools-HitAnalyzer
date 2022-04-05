import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
process = cms.Process("MyRawToDigi",eras.Run3)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
# to use no All 
# 2016
#process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v3' # for 266277
#process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v8' # for 272
# AUTO conditions 
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_design', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2017', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data_express', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data_prompt', '')


import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
# accept if 'path_1' succeeds
process.hltfilter = hlt.hltHighLevel.clone(
# Min-Bias	
#    HLTPaths = ['HLT_Physics*'],
#    HLTPaths = ['HLT_Random*'],
#    HLTPaths = ['HLT_ZeroBias*'],
    HLTPaths = ['HLT_ZeroBias_v*'],
#    HLTPaths = ['HLT_L1SingleMuOpen_v*'],
#    HLTPaths = ['HLT_PAZeroBias*'],
#    HLTPaths = ['HLT_PARandom*'],
#    HLTPaths = ['HLT_PAMinBias*'],
# Commissioning:
#    HLTPaths = ['HLT_L1Tech5_BPTX_PlusOnly_v*'],
#    HLTPaths = ['HLT_L1Tech6_BPTX_MinusOnly_v*'],
#    HLTPaths = ['HLT_L1Tech7_NoBPTX_v*'],
#
#    HLTPaths = ['p*'],
#    HLTPaths = ['path_?'],
    andOr = True,  # False = and, True=or
    throw = False
    )


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100000))

process.source = cms.Source("PoolSource",
 # fileNames =  cms.untracked.vstring('file:rawdata.root')
 fileNames =  cms.untracked.vstring(

"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/05d4e531-3560-40bd-ba85-d18f4fa78981.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/22cbd905-6a6d-4632-888f-fe96c32ad40e.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/e936125e-53eb-4e71-bafe-c027cb550a1d.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/bc3801d1-c45f-4ff8-bb44-6d9915e7cdd5.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/704bfd06-68ac-4e4d-9be7-59ce0fef0cb9.root",

 )
)

#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('273725:83-273725:9999')

# Cabling
#  include "CalibTracker/Configuration/data/Tracker_FakeConditions.cff"
#process.load("CalibTracker.Configuration.SiPixel_FakeConditions_cff")
#process.load("CalibTracker.Configuration.SiPixelCabling.SiPixelCabling_SQLite_cff")
#process.GlobalTag.connect = "frontier://FrontierProd/CMS_COND_21X_GLOBALTAG"
#process.GlobalTag.globaltag = "CRAFT_V3P::All"
#process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')
#process.siPixelCabling.connect = 'sqlite_file:cabling.db'
#process.siPixelCabling.toGet = cms.VPSet(cms.PSet(
#    record = cms.string('SiPixelFedCablingMapRcd'),
#    tag = cms.string('SiPixelFedCablingMap_v14')
#))


process.load("EventFilter.SiPixelRawToDigi.SiPixelRawToDigi_cfi")
# for simultaions 
#process.siPixelDigis.cpu.InputLabel = 'siPixelRawData'
# for data
#process.siPixelDigis.cpu.InputLabel = 'source'
process.siPixelDigis.cpu.InputLabel = 'rawDataCollector'
process.siPixelDigis.cpu.IncludeErrors = True
process.siPixelDigis.cpu.UsePhase1 = True 

process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('siPixelDigis'),
    destinations = cms.untracked.vstring('r2d'),
#    r2d = cms.untracked.PSet( threshold = cms.untracked.string('DEBUG'))
#    r2d = cms.untracked.PSet( threshold = cms.untracked.string('INFO'))
#    r2d = cms.untracked.PSet( threshold = cms.untracked.string('WARNING'))
    r2d = cms.untracked.PSet( threshold = cms.untracked.string('ERROR'))
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName =  cms.untracked.string('file:digis.root'),
#    fileName =  cms.untracked.string(
#'file:/afs/cern.ch/work/d/dkotlins/public/data/digis/digi_zb_248025.root'),
#)
    outputCommands = cms.untracked.vstring("drop *","keep *_siPixelDigis_*_*")
)

process.a = cms.EDAnalyzer("PixDigisTest",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
# sim in V7
#    src = cms.InputTag("mix"),
# old default
    src = cms.InputTag("siPixelDigis"),
    Select1 = cms.untracked.int32(0),  # select the cut type, o no cut
    Select2 = cms.untracked.int32(0),  # select the cut value   
)

process.d = cms.EDAnalyzer("PixelFedErrorDumper", 
    Verbosity = cms.untracked.bool(False),
    InputLabel = cms.untracked.string('siPixelDigis'),
)

process.r = cms.EDAnalyzer("SiPixelRawDump", 
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
                           CheckPixelOrder = cms.untracked.bool(True),
# 0 - nothing, 1 - error , 2- data, 3-headers, 4-hex
                           Verbosity = cms.untracked.int32(0),
# threshold, print fed/channel num of errors if tot_errors > events * PrintThreshold, default 0,001 
    PrintThreshold = cms.untracked.double(0.001)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('digis_histo.root')
)

#
#process.p = cms.Path(process.r)
#process.p = cms.Path(process.siPixelDigis)
process.p = cms.Path(process.r*process.siPixelDigis*process.a)
#process.p = cms.Path(process.hltfilter*process.siPixelDigis*process.a)
#process.p = cms.Path(process.hltfilter*process.siPixelDigis*process.a*process.d)
# disable data write to disk 
#process.ep = cms.EndPath(process.out)
