#
# Last update: new version for python
#
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
process = cms.Process("cluTest",eras.Run3)
                   
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
# process.load("Configuration.StandardSequences.Services_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
# to use no All 
# 2017
#process.GlobalTag.globaltag = '90X_dataRun2_Express_v4' # 
#process.GlobalTag.globaltag = '92X_dataRun2_Express_v2' # 
#process.GlobalTag.globaltag = '92X_dataRun2_Express_v4' # for 926
#process.GlobalTag.globaltag = '92X_dataRun2_Express_v7' # for 927,9
#process.GlobalTag.globaltag = '94X_dataRun2_ReReco_EOY17_v2' # for 2017 rereco

# 2018
#process.GlobalTag.globaltag = '100X_dataRun2_Express_v2' # 
#process.GlobalTag.globaltag = '101X_dataRun2_Express_v8' # 

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
#    HLTPaths = ['HLT_Random*'],
    HLTPaths = ['HLT_ZeroBias*'],  # includes _part* and others 
#    HLTPaths = ['HLT_ZeroBias_v*'],
#    HLTPaths = ['HLT_ZeroBias_part*'],  # empty
#    HLTPaths = ['HLT_ZeroBias_FirstCollisionInTrain_*'], # empty
#    HLTPaths = ['HLT_ZeroBias_LastCollisionInTrain_*'],  # empty
#    HLTPaths = ['HLT_ZeroBias_FirstBXAfterTrain_*'], # empty
#    HLTPaths = ['HLT_ZeroBias_IsolatedBunches_*'], # ok
#    HLTPaths = ['HLT_ZeroBias_FirstCollisionAfterAbortGap_*'], # ok
#    HLTPaths = ['HLT_ZeroBias_BeamSpot_*'],
#    HLTPaths = ['HLT_L1SingleMuOpen_v*'],
#    HLTPaths = ['HLT_PAZeroBias*'],
#    HLTPaths = ['HLT_PARandom*'],
#    HLTPaths = ['HLT_PAMinBias*'],
# Commissioning:
#    HLTPaths = ['HLT_L1ETT_ZeroBias_*'],
#    HLTPaths = ['HLT_L1ETT_ZeroBias_part*'],
#    HLTPaths = ['HLT_L1ETT_ZeroBias_v*'],
#    HLTPaths = ['HLT_PixelClusters_*'],
#
#    HLTPaths = ['p*'],
#    HLTPaths = ['path_?'],
    andOr = True,  # False = and, True=or
    throw = False
    )

process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('siPixelClusters'),
#    destinations = cms.untracked.vstring('cout'),
    destinations = cms.untracked.vstring("log","cout"),
    log = cms.untracked.PSet(
        threshold = cms.untracked.string('ERROR')
#        threshold = cms.untracked.string('DEBUG')
    ),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('ERROR')
    )
)


# ----------------------------------------------------------------------

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

myfilelist = cms.untracked.vstring()
myfilelist.extend([
])

process.source = cms.Source("PoolSource",
                             fileNames =  myfilelist )

#  fileNames = cms.untracked.vstring(  

#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/236/00000/1e926627-4553-4b96-bf6b-51bb2587f01a.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/236/00000/62476398-24db-4869-8288-17982f19c909.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/236/00000/0757eddf-0c0a-462b-88fe-c62dbe588e32.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/236/00000/9f4edfe6-1cec-4407-b50c-5be900384a39.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/236/00000/84356223-f54b-4716-b0e4-7a6011ca76dc.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/236/00000/07a0f8c9-7ee3-40a8-ae2b-9c1e7f145f32.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/236/00000/7a970327-ebc7-4987-88bf-7ca184c08d71.root",

#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/247/00000/953d941c-dd4f-4779-8045-07f5076ac5b2.root",

#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/299/00000/88c9f30b-6c89-46aa-8e3d-35b7fb4f6d3e.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/299/00000/b88324ec-c65f-4319-8d85-eb33cc944238.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/299/00000/5bfb9364-0c76-4f84-b18f-6ad0049d63a6.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/299/00000/7ac16447-2bd8-4a26-8e2b-67a4b510d7d1.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/299/00000/c07210fd-8912-49e7-936a-2378d0289cc2.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/299/00000/5fdaa74b-049a-4920-a8aa-7bb94559a1f2.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/299/00000/cf2a8456-b3cb-4dfd-9b5e-507488e7307c.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/299/00000/fa57f067-9441-4b83-9344-d896caa24409.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/299/00000/cc63f67d-16a2-42fd-be0a-f1d46d8c16c5.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/299/00000/a0f7f300-992e-4e64-84a2-7357517b9d60.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/299/00000/043c9bc6-c62f-41a1-bb76-957481dc340d.root",

#  )   # end the list "by-hand"
#)

#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('124230:26-124230:9999','124030:2-124030:9999')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('325308:43-325308:9999')

process.source.skipBadFiles = cms.untracked.bool( True )

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
    Tracks = cms.InputTag("generalTracks"),
    # additional selections, e.g. select bx=1 -> (2,1)
    Select1 = cms.untracked.int32(0),  # select the cut type, 0 no cut
    Select2 = cms.untracked.int32(0),  # select the cut value   
)

process.d1 = cms.EDAnalyzer("PixClusterAna",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    #src = cms.InputTag("siPixelClustersForLumi"),   # from the lumi stream
    src = cms.InputTag("siPixelClusters"),
    #src = cms.InputTag("siPixelClustersPreSplitting"),
    #src = cms.InputTag("ALCARECOTkAlMinBias"), # ALCARECO
    Tracks = cms.InputTag("generalTracks"),
    # additional selections, e.g. select bx=1 -> (2,1)
    Select1 = cms.untracked.int32(103),  # select events with no pvs
    Select2 = cms.untracked.int32(0),  # select the cut value   
)
process.d2 = cms.EDAnalyzer("PixClusterAna",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    #src = cms.InputTag("siPixelClustersForLumi"),   # from the lumi stream
    src = cms.InputTag("siPixelClusters"),
    #src = cms.InputTag("siPixelClustersPreSplitting"),
    #src = cms.InputTag("ALCARECOTkAlMinBias"), # ALCARECO
    Tracks = cms.InputTag("generalTracks"),
    # additional selections, e.g. select bx=1 -> (2,1)
    Select1 = cms.untracked.int32(101),  # select events with no tracks
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
process.c1 = cms.EDAnalyzer("PixClustersWithTracks",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    src = cms.InputTag("generalTracks"),
# for cosmics 
#    src = cms.InputTag("ctfWithMaterialTracksP5"),
#     PrimaryVertexLabel = cms.untracked.InputTag("offlinePrimaryVertices"),
#     trajectoryInput = cms.string("TrackRefitterP5")
#     trajectoryInput = cms.string('cosmictrackfinderP5')
# additional selections
    Select1 = cms.untracked.int32(13),  # select the cut type, o no cut
    Select2 = cms.untracked.int32(1),  # select the cut value   
)
process.c2 = cms.EDAnalyzer("PixClustersWithTracks",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    src = cms.InputTag("generalTracks"),
# for cosmics 
#    src = cms.InputTag("ctfWithMaterialTracksP5"),
#     PrimaryVertexLabel = cms.untracked.InputTag("offlinePrimaryVertices"),
#     trajectoryInput = cms.string("TrackRefitterP5")
#     trajectoryInput = cms.string('cosmictrackfinderP5')
# additional selections
    Select1 = cms.untracked.int32(14),  # select the cut type, o no cut
    Select2 = cms.untracked.int32(1),  # select the cut value   
)


#process.p = cms.Path(process.hltfilter*process.d)
process.p = cms.Path(process.hltfilter*process.d*process.c)
#process.p = cms.Path(process.hltfilter*process.d*process.c*process.c1*process.c2)
#process.p = cms.Path(process.hltfilter*process.d*process.c*process.d1*process.d2)

#process.p = cms.Path(process.d*process.c) # for mc
#process.p = cms.Path(process.d) # 

