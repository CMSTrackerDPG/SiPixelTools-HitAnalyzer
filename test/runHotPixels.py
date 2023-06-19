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
"/store/express/Run2023C/ExpressCosmics/FEVT/Express-v4/000/368/293/00000/929ee0a1-e8c7-4c65-b7db-787ebd839515.root",
"/store/express/Run2023C/ExpressCosmics/FEVT/Express-v4/000/368/293/00000/7c46f122-f6d3-4723-8907-a12a77fe707e.root",
"/store/express/Run2023C/ExpressCosmics/FEVT/Express-v4/000/368/293/00000/6c3101e2-eea0-44ad-be0d-58c44c7ef2cf.root",
"/store/express/Run2023C/ExpressCosmics/FEVT/Express-v4/000/368/293/00000/82bbbf67-4134-4b37-a738-e62a0a02a8af.root",
"/store/express/Run2023C/ExpressCosmics/FEVT/Express-v4/000/368/293/00000/2bddcc37-92f3-4eb4-bc86-2244515b3370.root",
"/store/express/Run2023C/ExpressCosmics/FEVT/Express-v4/000/368/293/00000/bfe0c3b3-94ed-42ea-84c7-4cd97a4fc8ff.root",
"/store/express/Run2023C/ExpressCosmics/FEVT/Express-v4/000/368/293/00000/2e5390df-70e5-4152-8abf-820505654a02.root",
"/store/express/Run2023C/ExpressCosmics/FEVT/Express-v4/000/368/293/00000/41621a46-5d90-4d1d-873d-cb5917b89e58.root",
"/store/express/Run2023C/ExpressCosmics/FEVT/Express-v4/000/368/293/00000/348dae33-9fb9-411f-a262-046efd269f1d.root",
"/store/express/Run2023C/ExpressCosmics/FEVT/Express-v4/000/368/293/00000/f9b85e44-6533-4b62-95c7-eb1546f23583.root",

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
                           Fraction = cms.untracked.double(0.001),
#                           Fraction = cms.untracked.double(0.001),
    MAXFED = cms.untracked.int32(1293)  # bpix only 
    #MAXFED = cms.untracked.int32(1338)  # all  
)

#process.p = cms.Path(process.hltfilter*process.d)
process.p = cms.Path(process.d)

# process.ep = cms.EndPath(process.out)


