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

"/store/express/Run2022A/ExpressCosmics/FEVT/Express-v1/000/352/768/00000/c95e4ffd-e693-4579-ba5e-eade30de5265.root",
"/store/express/Run2022A/ExpressCosmics/FEVT/Express-v1/000/352/768/00000/8b150e56-8a33-4708-b557-2fc9104901a8.root",

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

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/964/00000/95c684da-2efa-4409-b784-c1e406255219.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/964/00000/db6b6b43-23b7-4578-b47e-ae28e68cf0fa.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/964/00000/c5bbac67-0cb1-4c7e-a4c1-72c819e1c0da.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/964/00000/c96aed8d-107f-454b-9783-d7c0ae3a771a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/964/00000/b9f51750-6ce5-4ec6-bd79-64879c88cbe0.root",
     
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/977/00000/c991f6ea-2ae9-47bb-8757-f81f7930818c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/977/00000/a47e2f54-f4af-4870-81f5-c02d92c172b0.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/977/00000/4e6cfac5-f16f-4a31-a573-a42094140854.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/977/00000/6e45fc75-a454-4942-81c3-b467312ac7a8.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/977/00000/cba19a1e-c084-472e-b166-fda5f60f2c77.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/772/00000/3dfba781-047a-4843-8685-6b010484439c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/772/00000/8d9f056b-511b-4055-862e-39832ad2f206.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/772/00000/9ffb4364-dcab-4f38-89e7-a6eeb99bfaa4.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/772/00000/9a3b6c70-3d8e-4d7b-9cb0-ef36c721f844.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/772/00000/62314d9f-9457-4517-9ff7-94e37565ead7.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/589/00000/2eb6fc16-353c-4d19-80fc-804ea9cee648.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/589/00000/c37e7364-bd2a-4bb2-a57f-d7e99d12b231.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/589/00000/430db2b4-c886-4bf2-87f2-d3a693e0d694.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/589/00000/a5378423-d8a9-491f-af6e-c8bb68e3c6a1.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/589/00000/ac6d2615-e293-41d7-902d-f06cb3eb7041.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/588/00001/cce2c568-de5b-4573-8796-f8390e014ae2.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/588/00001/74b44980-a057-4444-9aea-15888b855734.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/588/00001/25d205eb-1209-4e7f-a08a-acad2cdb4452.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/588/00001/dbce9cac-df7f-440c-8ae5-a4fdcfdd0310.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/588/00001/35e56fcc-f7fd-4fe6-904f-00bf16b55732.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/472/00000/fbf80f7b-7c67-41fd-8dd8-a1a25ea60735.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/471/00000/37f7296b-66af-4431-87d5-25508d3c902c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/471/00000/3b4e1203-ae9d-48ea-8d2f-fb472a0b6900.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/471/00000/3ab1434b-e44c-486d-82b6-ac0a64a5a1f7.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/471/00000/ed45cb82-c91c-443a-9f18-277f55dc0a10.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/470/00000/03b21398-abee-40ed-8a8b-331eb8c978b6.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/470/00000/96bb7f7e-19ab-47e3-9aa9-fa995943b8bd.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/470/00000/b5fc1eac-efec-4647-b790-6e0e45670356.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/470/00000/04f6ed83-8ff8-43bb-b9d5-fff7679ed37f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/470/00000/2b229b19-6a3e-457a-96a5-38278d735017.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/340/00000/980bb60b-2d01-473d-b6b7-e729844a44b3.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/340/00000/d7594847-de6a-4214-a7ab-19e7508bce7e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/340/00000/19bc5985-bd02-4dd4-aefa-d5650af73934.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/340/00000/a8bf1624-e62d-489a-8f7f-0b841ef7ba27.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/340/00000/6ed7f031-d4c1-493d-9aff-c5d93355348c.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/287/00000/a373b0a7-847e-4e08-a7da-49ac4e5804e5.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/287/00000/2184b4f6-43c3-4539-95c6-53c42dc6399a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/287/00000/c32893cf-3b1a-482e-a9e7-7579d6a0ba9e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/287/00000/ceb6e9b5-509f-4582-b204-060d599fdb24.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/287/00000/5e1e1927-58db-4589-9b44-a6dd3eb8f14c.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/264/00000/5a2c35a2-8efa-4611-aadf-a2d7049978b1.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/264/00000/7080d1d9-41bb-4066-a77c-31e63e9bd08e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/264/00000/4aa5901c-04d9-431a-92c3-5841544937b3.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/264/00000/6305fb69-51a4-4baf-8c43-17ef66b35390.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/264/00000/e8c18796-3f93-49ad-85b9-df7d7c4b8755.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/217/00000/460c8377-56ba-4773-9f48-a11e85679c0b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/217/00000/ab96f8b4-dbcb-49c0-9b46-308a2787580d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/217/00000/65489017-b55a-44e8-897a-f1bdb225debe.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/217/00001/8307ac89-0407-4d87-96dc-90f1331d5434.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/217/00000/ec3a5588-bbf5-428e-b3c8-fed9c95bc66d.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/207/00000/5c23a1b4-2375-49ff-9845-c02c10c5d4f6.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/207/00000/54e083a6-5bf5-4b48-8a96-e92ee717bd8d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/207/00000/12253259-2c78-4a0a-a486-da06c634cddf.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/207/00000/ba97826f-9164-4f53-b53a-4485f84676b4.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/207/00000/d9d06ad1-bf44-4bb9-9857-d1f36786d3e8.root",
# end run 
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/207/00000/f356e6c7-2cfc-4221-ad47-fba10cbb355d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/207/00000/3c9fbdaf-d065-4e0d-857e-94dacd285feb.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/207/00000/ff632059-5744-4422-a703-3052cd40259b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/207/00000/3bcad44b-ae4c-40f4-b58a-f8d82341bf35.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/207/00000/aaba9512-8998-4865-82da-0d3e00aa5c4b.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/168/00000/24812da7-e4ee-4fa5-bc0c-c462fb933deb.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/168/00000/454210c2-8e49-4af2-8fea-6b6d2ee7a7c5.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/168/00000/015fbe60-808d-4460-af2c-10623e824e14.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/168/00000/8d5b4b3c-8874-45ad-8b99-dbb614b0388a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/168/00000/bcca1513-e33d-409f-b2ba-a34874f1571b.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/045/00000/4ef580d8-b961-4e8d-9694-152a581631b5.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/045/00000/181fe2a1-170d-4e31-81a3-8eed94d37f5b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/045/00000/0287ed70-c005-4c05-97d3-98afc0fb5f8c.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/044/00000/fb1ad79e-84c3-48d7-9f64-96198ef6539a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/044/00000/ff39a4f5-bfa0-4197-af28-4f85e7c6bb6c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/044/00000/e807331c-4747-4e15-95d1-3a10d1d8e92c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/044/00000/4b9e98ee-ffca-4d84-8e18-994639206801.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/044/00000/59bd0336-0731-472d-ad27-760cc6467256.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/041/00000/90da4e40-4848-4534-8ba4-29f2d8681ac3.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/041/00000/251c3e71-5243-4a1d-aa89-9f3a561d8572.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/041/00000/b2a964fe-4832-4cd1-b7b8-5d90bba0960e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/041/00000/e8e2cd2d-3c21-4a46-abe8-0c146a6a6ba0.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/041/00000/f693ef01-8283-4046-9ff0-607966420412.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/034/00000/ff558ffa-52b2-4d28-85cd-ac8e600cbeb9.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/034/00000/715653ee-c8e6-4204-8f76-deaa94ea36c3.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/034/00000/5baa6bb7-967e-45b6-815f-64a60e6f2de6.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/034/00000/a3d403a6-0ef4-4cef-b0a7-e80fa4b80187.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/034/00000/3a9175d4-29bd-4768-844c-61448ad533b8.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/032/00000/83d235b7-98d3-49bb-9e5f-7d97ac3bc1f6.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/032/00000/db16ab3b-e5a1-46ac-b160-14920626c34d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/032/00000/f607ce53-218b-4149-836d-d942edb8d390.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/032/00000/bf55a747-4a67-482a-ad8a-1bb350696e2d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/032/00000/7c81a03d-c60c-4d72-8074-462f0423a417.root",


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

#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('325159:1-325159:47')
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


