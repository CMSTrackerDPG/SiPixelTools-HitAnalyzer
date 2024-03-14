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
#fileNames =  myfilelist )

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

    )
)

#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('323481:38-323481:311')
process.source.skipBadFiles = cms.untracked.bool( True )

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
                           Fraction = cms.untracked.double(0.01),
#                           Fraction = cms.untracked.double(0.001),
    MAXFED = cms.untracked.int32(1293)  # bpix only 
    #MAXFED = cms.untracked.int32(1338)  # all  
)

#process.p = cms.Path(process.hltfilter*process.d)
process.p = cms.Path(process.d)

# process.ep = cms.EndPath(process.out)


