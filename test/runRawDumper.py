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
    fileName = cms.string('raw.root')
)

myfilelist = cms.untracked.vstring()
myfilelist.extend([
])

process.source = cms.Source("PoolSource",
# fileNames =  myfilelist
    fileNames = cms.untracked.vstring(

#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/dd0286ac-9305-4ac1-b849-e835b56b2def.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/8da8bd23-b41a-44be-9eb5-374f562f7a0e.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/66f189f5-0def-4b14-ab5d-ab5b5c131d16.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/c375f7d1-8785-450a-b2d2-968c16ddeeb6.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/1b7bfea3-e324-425d-afb2-cb5f45cef07d.root",

"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/2499e0b2-8ec8-4c6e-8173-c2ab48510815.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/ef867575-a95e-4bb7-832a-1eec9904fffc.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/0e1b06f9-2393-49ee-9afc-ed1ca7b5ce4b.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/a73ced30-a5cc-4998-9d4d-b83faaac436d.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/6aa8ee92-5491-403f-96c0-069dc4a40d54.root",

#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/931/00000/e30ff91c-20fa-4bd6-a9ef-18308fab8a19.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/931/00000/b068d1a7-c6da-4675-8d2b-61eb59e565ec.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/931/00000/8f1ab562-4f7b-48a3-ae00-4b39359db128.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/931/00000/5591bd51-7ed7-4547-a114-203c5c5d6221.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/931/00000/5eb6fa68-cdbc-4396-826c-a2e5c6d6efe5.root",

#"/store/express/Run2022A/ExpressCosmics/FEVT/Express-v1/000/352/768/00000/c95e4ffd-e693-4579-ba5e-eade30de5265.root",
#"/store/express/Run2022A/ExpressCosmics/FEVT/Express-v1/000/352/768/00000/8b150e56-8a33-4708-b557-2fc9104901a8.root",

#"/store/express/Run2022A/ExpressCosmics/FEVT/Express-v1/000/352/584/00000/d1ad3538-78cb-4926-9755-01d95ffbf36b.root",
#"/store/express/Run2022A/ExpressCosmics/FEVT/Express-v1/000/352/584/00000/d73acade-bee2-46b5-a461-f53960624eed.root",

#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/568/00000/8083fdaf-a44e-4974-bd4e-c70cb4c43b58.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/568/00000/7ad4e867-fafc-4832-be24-4d662eb831fe.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/568/00000/c5a937d3-04c8-4ec5-9410-fd29e191dafe.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/568/00000/a711e343-1d9a-4ff1-a43a-9d9f60fee09b.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/568/00000/a9e31d10-95fb-47a7-907d-819c18287cd0.root",

#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/509/00000/31ddb814-16b9-48ca-9e83-088a37673872.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/509/00000/3a261264-741a-43bd-970f-6a1f2df7a567.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/509/00000/01cb99ff-207a-40e0-bc0d-879f9d33ca7c.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/509/00000/a5b146de-096e-4da2-a42e-ba6b06e61ae6.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/509/00000/f271c85b-02ff-478f-be94-95955b95a26f.root",

#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/425/00000/c8e01ece-6ea3-4696-8d53-070d51be7238.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/425/00000/1086c8cc-1a99-4580-a53b-645080fa15bd.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/425/00000/28102752-e8b5-4d67-8a9d-7b25e47a05f1.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/425/00000/e425d727-c615-495d-bdf1-8f967d71d4cd.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/425/00000/225903aa-1c48-461d-943f-70aa4a90caa3.root",

#"/store/express/Commissioning2022/ExpressPhysics/FEVT/Express-v1/000/352/165/00000/179d95e5-51ad-4735-a226-f9191c64d5eb.root",
#"/store/express/Commissioning2022/ExpressPhysics/FEVT/Express-v1/000/352/165/00000/3ae149e9-0722-4d92-8b55-b549a6e98a14.root",
#"/store/express/Commissioning2022/ExpressPhysics/FEVT/Express-v1/000/352/165/00000/3e69a3a0-3538-4661-9aaf-d9fcaea25af3.root",
#"/store/express/Commissioning2022/ExpressPhysics/FEVT/Express-v1/000/352/165/00000/eab43e93-325f-4c64-b696-02211e7f1d26.root",
#"/store/express/Commissioning2022/ExpressPhysics/FEVT/Express-v1/000/352/165/00000/04b79903-8cd3-41b3-8b68-e91c4e2aa3cd.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/040/00000/6172dc95-e149-412e-815a-0d0e4fa31343.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/040/00000/262b3d7e-78c3-4f16-a9f6-069a5638bfdd.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/040/00000/700a1eb2-848c-4f94-996a-d9b7446acff3.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/040/00000/63f4581b-0a9c-4816-820c-9a1b985dba4c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/040/00000/29669c0a-6638-46cf-86df-0f7732a34f02.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/037/00000/a8d8dc95-6212-44e6-beb2-50424417fa70.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/037/00000/ea1a6b2f-8321-404b-820e-c0e820dabe86.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/037/00000/0c26fb8b-5f38-45fa-9da5-3b0399d0aea5.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/037/00000/eea62842-e1b3-490c-8ef7-764a4ca87a0f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/037/00000/b1f46980-1ff0-47a8-a449-f0ca997b6a3c.root",

   )
)

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

#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('353060:1-353060:20')
process.source.skipBadFiles = cms.untracked.bool( True )

process.d = cms.EDAnalyzer("SiPixelRawDump", 
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

    CheckPixelOrder = cms.untracked.bool(False),
# 0 - nothing, 1 - error , 2- data, 3-headers, 4-hex
                           Verbosity = cms.untracked.int32(0),
# threshold, print fed/channel num of errors if tot_errors > events * PrintThreshold, default 0,001 
                           PrintThreshold = cms.untracked.double(0.001),
                           selectedFED = cms.untracked.int32(-1),
                           selectedChannel = cms.untracked.int32(-1),
                           selectedType = cms.untracked.int32(-1),
                           bpixOnly = cms.untracked.bool(False)
)

#process.p = cms.Path(process.hltfilter*process.d)
process.p = cms.Path(process.d)

# process.ep = cms.EndPath(process.out)


