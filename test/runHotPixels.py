#
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
process = cms.Process("d",eras.Run3)

import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
# accept if 'path_1' succeeds
process.hltfilter = hlt.hltHighLevel.clone(
# Min-Bias
#    HLTPaths = ['HLT_Physics_v*'],
#    HLTPaths = ['HLT_L1Tech_BSC_minBias_threshold1_v*'],
    HLTPaths = ['HLT_Random_*'],
#    HLTPaths = ['HLT_ZeroBias_*'],
# Commissioning:
#    HLTPaths = ['HLT_L1_Interbunch_BSC_v*'],
#    HLTPaths = ['HLT_L1_PreCollisions_v*'],
#    HLTPaths = ['HLT_BeamGas_BSC_v*'],
#    HLTPaths = ['HLT_BeamGas_HF_v*'],
# Alca
#    HLTPaths = ['AlCa_LumiPixels_Random_v*'],
#    HLTPaths = ['AlCa_LumiPixels_ZeroBias_v*'],
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
    fileName = cms.string('noise.root')
)

myfilelist = cms.untracked.vstring()
myfilelist.extend([
])

process.source = cms.Source("PoolSource",
# fileNames =  myfilelist )
    fileNames = cms.untracked.vstring( 
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/344/068/00000/11cf55ba-55c8-4e8e-b984-281c724fb881.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/344/266/00000/542038a5-47ac-4b1b-98d6-6a5e4baa9a82.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/344/420/00000/7e2f37ab-ef2b-4dd6-a017-3fda8d7c23df.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/344/632/00000/f0459c3f-f269-41c3-bb04-1dbe7548e659.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/344/677/00000/050086f9-4711-4987-a737-08ba1ec2ae40.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/344/679/00000/001494f3-5062-4f4a-92fa-1049f64d2a70.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/344/681/00000/0bdb3b49-44f5-4d19-9c96-2c4be8aad8e4.root",


    )
)

#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('205217:0-205217:323')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('324410:0-324410:168')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('324276:48-324276:9999')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('324075:0-324075:307')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('323829:0-323829:455')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('323481:38-323481:311')

process.d = cms.EDAnalyzer("FindHotPixelFromRaw", 

    Timing = cms.untracked.bool(False),
    IncludeErrors = cms.untracked.bool(True),
#    InputLabel = cms.untracked.string('source'),
#   In 2012, 2015, extension = _LHC                                
    InputLabel = cms.untracked.string('rawDataCollector'),
#   For PixelLumi stream                           
#    InputLabel = cms.untracked.string('hltFEDSelectorLumiPixels'),
#    InputLabel = cms.untracked.string('siPixelRawData'),
    CheckPixelOrder = cms.untracked.bool(False),
#   Fraction to define  noisy pixels 
    Fraction = cms.untracked.double(0.05),
    MAXFED = cms.untracked.int32(1293)  # bpix only 
    #MAXFED = cms.untracked.int32(1338)  # all  
)

#process.p = cms.Path(process.hltfilter*process.d)
process.p = cms.Path(process.d)

# process.ep = cms.EndPath(process.out)


