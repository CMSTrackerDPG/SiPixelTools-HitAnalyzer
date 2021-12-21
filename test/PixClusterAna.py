#
# Last update: new version for python
#
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
process = cms.Process("cluTest",eras.Run3)
                   
#process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
# process.load("Configuration.StandardSequences.Services_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
# AUTO conditions 
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_design', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2017', '')
# 2021
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data_express', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data_prompt', '')

import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
# accept if 'path_1' succeeds
process.hltfilter = hlt.hltHighLevel.clone(
# Min-Bias	
#    HLTPaths = ['HLT_Physics*'],
    HLTPaths = ['HLT_Random*'],
#    HLTPaths = ['HLT_ZeroBias*'],
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


process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('siPixelClusters'),
    destinations = cms.untracked.vstring('cout'),
#    destinations = cms.untracked.vstring("log","cout"),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('ERROR')
    )
#    log = cms.untracked.PSet(
#        threshold = cms.untracked.string('DEBUG')
#    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

myfilelist = cms.untracked.vstring()
myfilelist.extend([
])

process.source = cms.Source("PoolSource",
#fileNames =  myfilelist
  fileNames = cms.untracked.vstring(    

"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/389/00000/1494add5-e2a0-4539-9b9d-15e9a5ea54ea.root",

#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/22cbd905-6a6d-4632-888f-fe96c32ad40e.root",

#  'file:/afs/cern.ch/work/d/dkotlins/public/MC/mu_phase1/pt100/reco/reco1.root',
# "/store/data/Run2017C/AlCaLumiPixels/ALCARECO/LumiPixels-PromptReco-v1/000/299/593/00000/64845BDE-1471-E711-9D54-02163E01A6E1.root",

  )   # end the list "by-hand"
)

#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('124230:26-124230:9999','124030:2-124030:9999')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('296902:1-296902:25')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('274314:97-274314:9999')

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('clus_ana.root')
)

process.d = cms.EDAnalyzer("PixClusterAna",
                           Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    #src = cms.InputTag("siPixelClustersForLumi"),   # from the lumi stream
    src = cms.InputTag("siPixelClusters"),
    #src = cms.InputTag("siPixelClustersPreSplitting"),
    #src = cms.InputTag("ALCARECOTkAlMinBias"), # ALCARECO
    # additional selections, e.g. select bx=1 -> (2,1)
    Tracks = cms.InputTag("generalTracks"),
    Select1 = cms.untracked.int32(0),  # select the cut type, 0 no cut
    Select2 = cms.untracked.int32(0),  # select the cut value   
)

process.a = cms.EDAnalyzer("PixClusterTest",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    src = cms.InputTag("siPixelClusters"),
#    src = cms.InputTag("siPixelClustersPreSplitting"),
)

process.c = cms.EDAnalyzer("PixClustersWithTracks",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    src = cms.InputTag("generalTracks"),
# for cosmics 
#    src = cms.InputTag("ctfWithMaterialTracksP5"),
#     PrimaryVertexLabel = cms.untracked.InputTag("offlinePrimaryVertices"),
#     trajectoryInput = cms.string("TrackRefitterP5")
#     trajectoryInput = cms.string('cosmictrackfinderP5')
# additional selections
    Select1 = cms.untracked.int32(0),  # select the cut type, o no cut
    Select2 = cms.untracked.int32(0),  # select the cut value   
)


#process.p = cms.Path(process.hltfilter*process.a)
process.p = cms.Path(process.hltfilter*process.d)
#process.p = cms.Path(process.hltfilter*process.d*process.c)
#process.p = cms.Path(process.d) # for cosmics


