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
"root://eoscms.cern.ch//eos/cms/store/express/Run2024A/ExpressPhysics/FEVT/Express-v1/000/378/750/00000/bc4f70d1-e7ae-449c-8d1a-ee138b5ee7fa.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024A/ExpressPhysics/FEVT/Express-v1/000/378/750/00000/47c936ac-22d4-4f6a-88fc-ed99c9d4bf5b.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024A/ExpressPhysics/FEVT/Express-v1/000/378/750/00000/4c664f11-2bff-4dc8-8afe-9db42351ff40.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024A/ExpressPhysics/FEVT/Express-v1/000/378/750/00000/a534bec3-e2e0-4442-b0f8-bd56349292be.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024A/ExpressPhysics/FEVT/Express-v1/000/378/750/00000/207f4510-7cf0-4581-b708-50ece66a70d6.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024A/ExpressPhysics/FEVT/Express-v1/000/378/750/00000/ad2f61ed-6ab7-426f-862c-71f6a7cdf4d0.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024A/ExpressPhysics/FEVT/Express-v1/000/378/750/00000/1d81b905-c38d-4170-b17e-f45bf0b32323.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024A/ExpressPhysics/FEVT/Express-v1/000/378/750/00000/2ac43a41-682b-44ec-a15c-10ae8ab46209.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024A/ExpressPhysics/FEVT/Express-v1/000/378/750/00000/bc072f37-d77a-48d8-851c-67eaff65d810.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024A/ExpressPhysics/FEVT/Express-v1/000/378/750/00000/64a00bbc-95c4-4dbe-b2ba-b85216768e6d.root",

    )
)

process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('378750:41-378750:9999')
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
                           Fraction = cms.untracked.double(0.1),
#                           Fraction = cms.untracked.double(0.001),
    MAXFED = cms.untracked.int32(1293)  # bpix only 
    #MAXFED = cms.untracked.int32(1338)  # all  
)

process.p = cms.Path(process.hltfilter*process.d)
#process.p = cms.Path(process.d)

# process.ep = cms.EndPath(process.out)


