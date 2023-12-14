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
# to use no All 
# 2018

# 2017
#process.GlobalTag.globaltag = '90X_dataRun2_Express_v4' # 
#process.GlobalTag.globaltag = '92X_dataRun2_Express_v2' # 
#process.GlobalTag.globaltag = '92X_dataRun2_Express_v4' # for 926
#process.GlobalTag.globaltag = '92X_dataRun2_Express_v7' # for 927,929
# 2018
#process.GlobalTag.globaltag = '100X_dataRun2_Express_v2' # 
#process.GlobalTag.globaltag = '101X_dataRun2_Express_v8' 
# 2021
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data_express', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data_prompt', '')
# 2016
#process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v3' # for 266277
#process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v9' # >=8010
#process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v10' # >=8014
#process.GlobalTag.globaltag = '80X_dataRun2_Express_v10' # >8010
#process.GlobalTag.globaltag = '80X_dataRun2_Express_v12' # >8014
# AUTO conditions 
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_data', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_design', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2017', '')


import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
# accept if 'path_1' succeeds
process.hltfilter = hlt.hltHighLevel.clone(
# Min-Bias	
#    HLTPaths = ['HLT_Physics*'],
    HLTPaths = ['HLT_Random*'],
#    HLTPaths = ['HLT_ZeroBias*'],
#    HLTPaths = ['HLT_ZeroBias_part*'],  # empty
#    HLTPaths = ['HLT_ZeroBias_FirstCollisionInTrain_*'], # empty
#    HLTPaths = ['HLT_ZeroBias_LastCollisionInTrain_*'],  # empty
#    HLTPaths = ['HLT_ZeroBias_FirstBXAfterTrain_*'], # empty
#    HLTPaths = ['HLT_ZeroBias_IsolatedBunches_*'], # empty
#    HLTPaths = ['HLT_ZeroBias_FirstCollisionAfterAbortGap_*'],
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
    input = cms.untracked.int32(-1)
)

myfilelist = cms.untracked.vstring()
myfilelist.extend([
])

process.source = cms.Source("PoolSource",
 fileNames =  myfilelist )
#  fileNames = cms.untracked.vstring(    
#"file:/eos/cms/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/344/681/00000/dfa10a80-f3ed-4ee3-9669-91bce823270e.root",


#"/store/express/Run2018D/ExpressCosmics/FEVT/Express-v1/000/325/088/00000/0189E695-D59D-3448-AD5B-AE4E5FCF2D1B.root",

#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/344/068/00000/ffc30ac2-6e3b-42e1-b6d9-74973a9cf961.root",

#  )   # end the list "by-hand"
#)

#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('124230:26-124230:9999','124030:2-124030:9999')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('325088:0-325088:9')

process.source.skipBadFiles = cms.untracked.bool( True )

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('clus_ana_cosmics.root')
)

process.d = cms.EDAnalyzer("PixClusterAna",
    Verbosity = cms.untracked.bool(False),
    Normalise = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    #src = cms.InputTag("siPixelClustersForLumi"),   # from the lumi stream
    src = cms.InputTag("siPixelClusters"),
    #src = cms.InputTag("siPixelClustersPreSplitting"),
    #src = cms.InputTag("ALCARECOTkAlMinBias"), # ALCARECO
    Tracks = cms.InputTag("ctfWithMaterialTracksP5"),
    # additional selections, e.g. select bx=1 -> (2,1)
    Select1 = cms.untracked.int32(0),  # select the cut type, 0 no cut
    Select2 = cms.untracked.int32(0),  # select the cut value   
)


process.clutest = cms.EDAnalyzer("PixClusterTest",
    Verbosity = cms.untracked.bool(True),
    phase1 = cms.untracked.bool(True),
    src = cms.InputTag("siPixelClusters"),
#    src = cms.InputTag("siPixelClustersPreSplitting"),
)

process.c = cms.EDAnalyzer("PixClustersWithTracks",
    Verbosity = cms.untracked.bool(False),
    Normalise = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
# for collisions 
#    src = cms.InputTag("generalTracks"),
# for cosmics 
    src = cms.InputTag("ctfWithMaterialTracksP5"),
#     PrimaryVertexLabel = cms.untracked.InputTag("offlinePrimaryVertices"),
#     trajectoryInput = cms.string("TrackRefitterP5")
#     trajectoryInput = cms.string('cosmictrackfinderP5')
# additional selections
    Select1 = cms.untracked.int32(0),  # select the cut type, o no cut
    Select2 = cms.untracked.int32(0),  # select the cut value   
)
process.c_cosm = cms.EDAnalyzer("PixClustersWithTracks",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    Normalise = cms.untracked.bool(False),
#    src = cms.InputTag("generalTracks"),
# for cosmics 
    src = cms.InputTag("ctfWithMaterialTracksP5"),
     PrimaryVertexLabel = cms.untracked.InputTag("offlinePrimaryVertices"),
#     trajectoryInput = cms.string("TrackRefitterP5"),
     trajectoryInput = cms.string('cosmictrackfinderP5'),
# additional selections
     Select1 = cms.untracked.int32(17),  # no high quality cut
#    Select2 = cms.untracked.int32(1),  # select the cut value   
)


#process.p = cms.Path(process.hltfilter*process.c)
#process.p = cms.Path(process.hltfilter*process.d)
#process.p = cms.Path(process.hltfilter*process.d*process.c)
#process.p = cms.Path(process.hltfilter*process.d*process.c*process.c1*process.c2)
#process.p = cms.Path(process.d*process.c)  # for mc 
process.p = cms.Path(process.d*process.c_cosm) # for cosmics


