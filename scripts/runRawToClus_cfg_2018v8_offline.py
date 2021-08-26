##### Created July 11, 2021
##### Author: Lars Olivier Sebastian Noehte
##### lars.noehteATcern.ch
##### copied from runRawToClus_cfg.py
##### Warning #################################
## This config was tested with CMSSW_11_2_0 and 
## CMSSW_11_3_0. It does not run with 11_2_0.
###############################################


import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
process = cms.Process("MyRawToClus",eras.Run2_2018)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.StandardSequences.Services_cff")
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")

# clusterizer 
process.load("RecoLocalTracker.Configuration.RecoLocalTracker_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

from Configuration.AlCa.GlobalTag import GlobalTag

# AUTO conditions 
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
# accept if 'path_1' succeeds
process.hltfilter = hlt.hltHighLevel.clone(
# Min-Bias	
    HLTPaths = ['HLT_ZeroBias_v*'],  # simple democratic ZB
    andOr = True,  # False = and, True=or
    throw = False
    )

##### set the number of analyzed events #####
## set to -1 to run over all events ##
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000))


process.source = cms.Source("PoolSource",
    fileNames =  cms.untracked.vstring(
	"file:/afs/cern.ch/work/l/lnoehte/public/8C070B38-338E-E811-A4D1-FA163E781D28.root",
    )
)


process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('SiPixelClusterizer'),
    destinations = cms.untracked.vstring('cout'),
    cout = cms.untracked.PSet(
       threshold = cms.untracked.string('ERROR')
    )
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName =  cms.untracked.string('file:clus.root'),
    outputCommands = cms.untracked.vstring("drop *","keep *_*_*_MyRawToClus"), # 12.4MB per 100 events
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    splitLevel = cms.untracked.int32(0),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RECO')
    )
)

# pixel local reco (RecHits) needs the GenError object,
# not yet in GT, add here:
# DB stuff 
process.DBReaderFrontier = cms.ESSource("PoolDBESSource",
 DBParameters = cms.PSet(
     messageLevel = cms.untracked.int32(0),
     authenticationPath = cms.untracked.string('')
 ),
 toGet = cms.VPSet(
   cms.PSet(
   record = cms.string('SiPixelGainCalibrationOfflineRcd'),
    tag = cms.string('SiPixelGainCalibration_2018_v8') 
    ),
   ),
  connect = cms.string('sqlite_file:/afs/cern.ch/user/d/dkotlins/WORK/DB/Gains/SiPixelGainCalibration_2018_v9_offline.db')
 connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS')
) # end process
process.myprefer = cms.ESPrefer("PoolDBESSource","DBReaderFrontier")

# for Raw2digi for data
process.siPixelDigis.cpu.InputLabel = 'rawDataCollector'  # normal p-p
process.siPixelDigis.cpu.IncludeErrors = True
process.siPixelDigis.cpu.Timing = False 
process.siPixelDigis.cpu.UsePhase1 = True

# modify clusterie parameters
process.siPixelClustersPreSplitting.cpu.VCaltoElectronGain = 47  # default
process.siPixelClustersPreSplitting.cpu.VCaltoElectronOffset = -60
process.siPixelClustersPreSplitting.cpu.VCaltoElectronGain_L1 = 50  # default
process.siPixelClustersPreSplitting.cpu.VCaltoElectronOffset_L1 = -670

# To select full granularity gain calibration 
# process.siPixelClustersPreSplitting.payloadType = cms.string('Full')

process.a = cms.EDAnalyzer("PixDigisTest",
                           Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
# old default
    src = cms.InputTag("siPixelDigis"),
)


process.d = cms.EDAnalyzer("PixClusterAna",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    src = cms.InputTag("siPixelClustersPreSplitting"),
    Tracks = cms.InputTag(""), # ni tracks, only local reco
    Select1 = cms.untracked.int32(0),  # cut  
    Select2 = cms.untracked.int32(0),  # value     
)
process.d_cosm = cms.EDAnalyzer("PixClusterAna",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    src = cms.InputTag("siPixelClustersPreSplitting"),
    Tracks = cms.InputTag(""),
    Select1 = cms.untracked.int32(0),  # cut  
    Select2 = cms.untracked.int32(0),  # value     
)
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('digis_clus_2018v8_offline.root')
)

# for random cosmics 
#process.p = cms.Path(process.hltfilter*process.siPixelDigis*process.pixeltrackerlocalreco*process.a*process.d_cosm)

# for HI
process.p = cms.Path(process.siPixelDigis*process.pixeltrackerlocalreco*process.a*process.d)

# suppress output file or not
#process.ep = cms.EndPath(process.out)
