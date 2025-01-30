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
# HI
#    HLTPaths = ['HLT_HIRandom*'],
#    HLTPaths = ['HLT_HIMinimumBiasHF1ANDZDC*'],
   
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
    input = cms.untracked.int32(10)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('raw.root')
)

myfilelist = cms.untracked.vstring()
myfilelist.extend([
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/63940444-f6e4-4e6d-b632-9c1bc12510e4.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/3547438c-e7eb-4bfe-878f-0297229d4980.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/b2b437d2-b237-489c-b3f3-eaaf0f5282fd.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/096ab2e8-244f-4cbd-9b1a-d1eaf6ee0b0a.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/75061dee-e7ed-4629-84e1-26aaa61c946c.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/97610552-166a-4baf-906f-a8a6749e3f28.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/261c17e3-05f6-4085-899f-87cb93d4fa88.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/909e4761-edbf-426e-8bda-1003f1970ccd.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/1052819e-b200-48ea-9d0b-0462d387097f.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/7efbd321-ec2f-4e96-94d9-e25e2df0363e.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/a226e181-7265-49b7-8f47-662c201f16c4.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/ec877fdb-e97d-4358-89d3-ff29f97f3473.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/23b32a5a-5f8f-400f-8220-bbe4fcbd4d4b.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/63d2b23b-f699-4db7-bc09-ab765d524232.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/037b6c46-77ef-4555-b3cf-b8d7a5f717d2.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/9f59813b-a4a0-4a2f-a62e-2805fe9f8697.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/fc1e71ba-6c82-401a-b032-da6bd375e6ad.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/e7080cd4-b94f-4ca2-83ef-55d9b9df8cf5.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/ea7413df-48f7-4a31-973e-825b9bff520d.root",
"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/814/00000/7d97fc4d-2e8b-48b0-9676-492fa20765ea.root",

])

process.source = cms.Source("PoolSource",
 fileNames =  myfilelist)

#    fileNames = cms.untracked.vstring(
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/885/00000/6a4a3afd-81cd-4095-b967-bab82d5ac6a0.root",

#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/b671246f-ffbd-4df7-80d8-101cee10a90f.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/1508252c-65ae-4e14-9e0d-20960858dc68.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/6d64f432-a659-4cea-b407-e331ab9d5825.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/94ee6cf0-29c3-4086-afae-64be3f96129f.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/cbeb3eef-8995-4659-b221-d2d9a34be8e3.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/62ab1f56-3d80-46c9-adb8-5ef8682fdcfc.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/c05e14f9-406d-4601-bc36-c411c4c693d0.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/0c27c3a3-671a-462f-833b-52f99c7996b0.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/654ca6e9-e888-41f8-894b-3ad027eea29b.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/19203c6f-27a5-4592-b483-59941f5b4cd1.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/1da067d3-ebe6-4525-a262-afb029d91179.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/8121618f-31b3-4867-82ec-afd5e4cda1c5.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/1d8afd03-d5f6-4e84-9514-f80613735edf.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/9cf94044-33d9-4aa0-b20d-ed3ca76bac14.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/3194fbcf-1d97-41c2-a339-93f1d1765ea7.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/ed1b2aed-82a0-4476-80ff-77b1bdcdfd9e.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/f28a6c40-b270-440b-97f2-893546265ba2.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/811/00000/bde7cf9e-0ce2-4aa9-9dc9-6a4067d1ea4c.root",


#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/945/00000/cdc9c96f-b722-4bc6-845c-c753e36c7bdc.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024I/ExpressPhysics/FEVT/Express-v2/000/386/951/00000/aa9b219d-2832-4f56-b274-2e46d656efc2.root",
#"root://eoscms.cern.ch//eos/cms/store/express/Run2024A/ExpressPhysics/FEVT/Express-v1/000/378/750/00000/bc4f70d1-e7ae-449c-8d1a-ee138b5ee7fa.root",
#   )
#)

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

#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('378750:41-378750:9999')
process.source.skipBadFiles = cms.untracked.bool( True )

process.d = cms.EDAnalyzer("SiPixelRawDump", 
    Timing = cms.untracked.bool(False),
    IncludeErrors = cms.untracked.bool(True),
#   In 2015 data, label = rawDataCollector, extension = _LHC        
    InputLabel = cms.untracked.string('rawDataCollector'), # for p-p
#    InputLabel = cms.untracked.string('rawDataRepacker'), # for HI
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
                           selectedEvent = cms.untracked.int64(0),
                           bpixOnly = cms.untracked.bool(False),
                           hitsCut = cms.untracked.int32(400), #hits in 1 roc
                           hitsCut2 = cms.untracked.int32(500), #hits per chan
)

process.p = cms.Path(process.hltfilter*process.d)
#process.p = cms.Path(process.d) # for cosmics  use no trigger 

# process.ep = cms.EndPath(process.out)


