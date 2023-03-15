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

"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v2/000/364/727/00000/361da06d-a912-4e7d-9374-e80517d6a8f0.root",
"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v2/000/364/727/00000/48e7364e-caec-44ee-8edd-a886bad847cc.root",
"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v2/000/364/727/00000/8bf4d193-bc8d-4532-94eb-c97cf7fdea0f.root",
"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v2/000/364/727/00000/21f1e628-cfd7-4648-819c-18047ee245d9.root",
"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v2/000/364/727/00000/040fef78-8509-4ea2-bbec-4f353902b771.root",
"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v2/000/364/727/00000/e2e3bc2b-8fb5-4e5f-867f-c9d7e1c5a3d8.root",
"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v2/000/364/727/00000/86414aa0-dba1-44ea-ac8e-d4563f55a751.root",
"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v2/000/364/727/00000/369c6c3b-88c1-431a-bbd7-883209697082.root",
"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v2/000/364/727/00000/fd59dfa7-72f1-40da-b2c6-5d69a53a2472.root",
"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v2/000/364/727/00000/0afa7325-e453-4df6-a45a-df27f39321c5.root",

#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/612/00000/fa99d014-228b-456e-9420-4f27b073e43f.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/612/00000/0344b8a1-f1dc-4705-a336-4cd069b124e2.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/612/00000/92a82c2d-439c-42f5-9b46-025571c67097.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/612/00000/158cb316-ff61-4196-951f-bd3173adc653.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/612/00000/7bb2ec6c-5008-44a7-b48c-f9df2fda3a51.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/612/00000/940afef2-95bf-4bff-9bbb-f1139437c33f.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/612/00000/e973a4e3-30e7-4958-8651-c948925d2f14.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/612/00000/53df35f5-40ff-459b-bb29-d515c6fe46d5.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/612/00000/38d6b15e-ef0f-433c-b711-7bad65a464e3.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/612/00000/5b3418f5-37a0-4644-b41e-723e8046d564.root",

#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/531/00000/92eb21d7-a543-4c6c-b3ca-cda2adc0adbd.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/531/00000/f969220e-b513-4168-852a-df40e9c628f2.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/531/00000/1cfa8e12-850f-4e88-884d-0f1bcb493bc2.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/531/00000/ecb1d268-3c82-401a-b56b-90f42a59a362.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/531/00000/480536fa-ee50-448c-a88e-9bd9b2776769.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/531/00000/651dbcab-9fa3-4d01-9709-8bd1742afd7d.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/531/00000/34b85b7c-6c96-4c3a-b04c-57244189d044.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/531/00000/ac46a05f-df98-4818-aa15-a800d06e3b37.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/531/00000/a41a3b55-9939-4dc1-9a1e-432a82416f8f.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/531/00000/a23ed62e-76ba-423c-b5f3-22405d87699b.root",

#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/520/00000/53ae16b6-4654-4b98-a631-e442dfc78393.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/520/00000/95ff53d1-5b65-4fa9-920c-15c59aa16486.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/520/00000/69aec864-0006-4971-b7ce-80aab81ed384.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/520/00000/89d362ba-1ec9-43fe-a83b-df98f9732b32.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/520/00000/23f64a2a-211d-4179-a340-1d6ad55bf811.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/520/00000/ef9c6296-c452-4c26-993b-4986f31b7e76.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/520/00000/cf484f6e-af7e-4bb9-a770-6b5c253e9443.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/520/00000/93dc110c-53ba-4892-b21e-92c73c9d9052.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/520/00000/2ac72d44-b1fb-4aff-8620-f14ae1d825d4.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/520/00000/a70bb986-f766-44a6-82d6-807ac6a4e55f.root",

#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/508/00000/321b5ff3-37b4-45ae-86fb-ef1f234eb60d.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/508/00000/9c877d7d-7162-4863-9dae-7b5f05eb93ae.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/508/00000/1ae9708c-3e80-421a-9a3b-e896dee02122.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/508/00000/e02d2c30-8c5e-466c-81c6-ec196375b208.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/508/00000/b2204fc7-c969-4b61-b24e-10ec552b83d8.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/508/00000/e42b933d-cfbc-45c5-9e42-4cf2f71183ab.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/508/00000/3db61994-5c11-4a0a-a230-1008c564e9c3.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/508/00000/82b9bac1-e8e0-4a41-94ec-6d043e3a0762.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/508/00000/e897f011-877b-4669-bd8e-a7d24ebc2cfe.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/508/00000/35a30882-81ff-4ad6-9197-6aa68ea677d2.root",

#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/441/00000/d6ee58a1-ee0b-42cc-9920-eab11bd947ec.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/441/00000/f57b32ba-fb6d-4592-9e6d-c8150d70a687.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/441/00000/0dd1b6fe-eb6a-4233-a73f-525109db72b3.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/441/00000/0ce6900c-77ce-4a1f-a3f6-dc4590c53a80.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/441/00000/84604bbf-cc94-4218-bb3a-de0a804bb864.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/441/00000/6e00c6b8-cd0a-4652-978a-8646782eafe7.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/441/00000/d08501b4-9787-4d3c-bd69-bc4ceea6e524.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/441/00000/3474d0c5-f02f-44bc-a787-d5a7da0130ee.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/441/00000/84d92422-7cfb-4517-91d2-acebc7c51df3.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/441/00000/a6e4f58c-35ef-4829-97a7-d6f5c80fbcfc.root",

#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/376/00000/6dd49386-aac0-4d52-8081-4165c3f593b1.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/376/00000/369c7bd8-f026-40da-9210-7699074ff077.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/376/00000/05cb7237-0839-4eb5-8dab-3dd1da1378e3.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/376/00000/6d482aef-75b6-4723-9041-2c4215e7d11f.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/376/00000/d8b23bd9-45df-43fe-aa2f-e6a762e3e17f.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/376/00000/53d96da6-f8e1-4e0c-b17e-2d830a4c64f2.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/376/00000/c606c2d1-0345-4787-9a54-30f2aca36328.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/376/00000/ffec57fb-5923-4403-a4dc-04e04280ce9f.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/376/00000/21281535-0d3a-4ce9-afc4-9bddfbeb9b6d.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/376/00000/5ec7f19d-8a05-4def-9b7a-7d851b58e8e8.root",

#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/338/00000/c1517ca0-ce63-4e6f-8968-6cd0badc4d8c.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/338/00000/b835dff6-a94d-49aa-9c65-6bbc3c836499.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/338/00000/35131613-79e0-4c04-8640-3e7c751ae0ff.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/338/00000/4eff50f7-26fd-4271-8a71-4af7bb61f005.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/338/00000/3cf6d0cc-ee38-4da4-b80e-73410444020d.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/338/00000/0df1573a-cc95-4367-a5e4-1f26ffaa0545.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/338/00000/7e758c46-3931-4ff5-9989-a6eb7b449f5c.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/338/00000/4f888f6f-0e85-4578-92e3-a76ae6e19cb4.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/338/00000/7f0ea8b1-9177-4e2d-b2fc-68c9e9e28efc.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/338/00000/da7a9aca-ca0b-44c8-9eda-10c81b108e6f.root",

#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/238/00000/ec208391-fa11-491d-bbe7-28a9e0ead3f2.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/238/00000/e66f3337-f5e1-490c-9db3-c13290cfb0ed.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/238/00000/77618a51-5ea2-40ca-8d3c-b93006b7b72b.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/238/00000/32429b0d-8515-4786-9c14-a159e554ad0a.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/238/00000/26beb97a-f9d8-425d-8b68-0421c084bd69.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/238/00000/07b78f81-8683-4182-8a39-50b46cfa99a9.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/238/00000/5385b645-1f9d-4440-af35-22011be94c3d.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/238/00000/70c9278c-d61d-4c99-8339-c8f00ce7c00f.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/238/00000/83981aa0-f361-4cae-9c73-1e8a6c22952e.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/238/00000/7f035842-be04-4cbe-a8df-5a46ef7759ad.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/238/00000/95a005ef-3d65-4074-be90-fe496f2dc36c.root",

#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/174/00000/5489aa57-76ed-40a9-9464-1fb509d80799.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/174/00000/b68c4534-7e03-437d-a7f0-060e1f447c0b.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/174/00000/3bdb921d-f5a4-4d1b-8a74-d19ac2ca3fc5.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/174/00000/1a5f71d4-88ef-497d-a87f-3519b9f93e9a.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/174/00000/b2c80309-3941-41f6-9d73-60f0409d076d.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/174/00000/1995c8ce-2eed-41a9-b117-a54d7b802835.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/174/00000/efedce5f-b247-4cca-8250-657f0f9b8919.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/174/00000/65e64bc4-390a-4c06-aa66-80511f550f61.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/174/00000/58ca21ae-0d08-4959-8f63-c6d873823fb2.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/174/00000/7c95cce2-746a-4688-906e-0b5f11d5a91d.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/174/00000/c898998d-c378-475a-a035-8b2fcf8609d8.root",

#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/158/00000/06983512-845c-4e3d-8c71-00e586d0d442.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/158/00000/196de583-8043-4691-a605-14bff75f254a.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/158/00000/f2a1bf9e-d8fb-42f1-987e-9026e0b81a0e.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/158/00000/e4fd6715-ab42-45fe-9fdb-d6db7124bbe9.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/158/00000/cc1cdbec-fa32-4dfe-aab3-5e4c165a04c1.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/158/00000/29542b46-8e6d-488d-a40c-624ede6eb726.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/158/00000/db1f3029-c0b0-4a77-bcdd-cea7fa7c21e6.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/158/00000/1650a376-b229-428f-a4eb-ac1fe712bc2c.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/158/00000/55642f1d-296e-4676-b565-4579d4a67517.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/158/00000/942bb801-bb5d-43e5-aa46-de878e9c7fc7.root",

#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/141/00000/b715cc03-407e-4d1f-8f3a-ccc2cd875555.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/141/00000/1afac341-765f-4ea1-bfbe-f801641eeb03.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/141/00000/5a357e47-b3df-4d0a-b310-2fe90a314b36.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/141/00000/850c51bf-ff60-40cd-9f89-8d686ac6f3b9.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/141/00000/5a6982df-4bf0-403e-ae8f-c74fd11938b0.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/141/00000/04addca6-8d47-4fc7-a67a-56fdfcba4e49.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/141/00000/210185fb-8e38-4079-abb9-83b0f82f0266.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/141/00000/a9549274-521d-44a6-a643-76f45ff4ca3f.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/141/00000/3db5f694-b537-4540-bf9b-056867c261aa.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/141/00000/e0af951e-7644-4d31-be41-15a5a2e0f061.root",

#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/053/00000/0c5dfb17-afe3-442e-b86d-308a3d809c3b.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/053/00000/2921d91b-3d4b-4333-bb44-2afcf91f3593.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/053/00000/06abc4b7-c271-4046-9d0b-59c26204a991.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/053/00000/8b7506db-7c8f-4cc0-bd3d-6f46f86fc30e.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/053/00000/c42516fd-8154-45bb-8cf8-f08a5e50fad9.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/053/00000/f9c7bd8c-c0a5-4147-9275-85e7ead27256.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/053/00000/1952fe05-9f40-40ca-9a37-c30434cff8ed.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/053/00000/133dd4ce-16f0-4256-b036-be5486c98586.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/053/00000/037d2e30-3b71-4b79-8128-43e58f4d1754.root",
#"/store/express/Commissioning2023/ExpressCosmics/FEVT/Express-v1/000/364/053/00000/3d8611b8-b0b5-474f-bd50-5998f9d39cd6.root",

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

process.p = cms.Path(process.hltfilter*process.d)
#process.p = cms.Path(process.d)

# process.ep = cms.EndPath(process.out)


