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

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/955/00000/9e19d04e-141c-449a-823f-dc49c8172d17.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/955/00000/825cf2ae-73fc-4e06-ae7b-4382f7d805a4.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/955/00000/5fe90350-7152-4046-8b29-e276724cb5c0.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/955/00000/b48d3eed-179c-498c-ad09-028990935f94.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/955/00000/a471e6ff-18f7-4d92-beb8-6f9138f6c42e.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/929/00000/d79b6368-6fd5-48ea-80af-f78e238a6fb5.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/929/00000/c60a8d6d-1911-4a4f-9bb5-130d910bd56e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/929/00000/03f25888-82f1-4145-b1dc-16903f1e8a75.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/929/00000/6773f215-5205-4fb0-ac92-92bd782290ea.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/929/00000/654b5e99-9030-4629-92cf-92a00a32c2ed.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/908/00000/d2c70f4f-0a21-4b9d-ba25-f2336b7cbc02.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/908/00001/63f242c1-b5bf-47d8-95e3-8d119bd9b9af.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/908/00001/0a2ab488-0dbf-45a0-a65e-7df2aadc9767.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/908/00000/c4f38d71-3a84-465e-9459-adc29cbc2741.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/908/00000/3d5cb7f5-871d-4eaf-967b-c111e66160c5.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/905/00000/64e4075a-433c-43d0-a2df-5501491e97d9.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/905/00000/b2ed640c-89e8-4753-b985-ad8424799089.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/905/00000/e67ced3f-4d31-491a-b928-61163f8f8e13.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/905/00000/d578f957-755e-420b-a43f-3c21399e9eac.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/905/00000/aa764b46-d548-46d8-a52c-70d1c87b026d.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/901/00000/22d603a8-c974-41db-9f7f-0ebaa9722000.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/901/00000/adf700bc-bae8-489e-9328-2608e7603616.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/901/00000/e7d6b64d-4485-4129-a8f2-0655e3317339.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/901/00000/6c2dfcdf-cac1-46c5-91e6-b94d414e496e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/901/00000/b8d64a60-05a2-46d6-8901-8284d3aedb21.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/838/00000/fd3f2919-0462-4d2e-a3dd-d472fa444268.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/838/00001/b362b944-42d1-4f95-9c8e-7aa6c32b3002.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/838/00000/85f68c6a-39bf-4d16-9264-449585927907.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/838/00000/9c417c17-50d7-49e1-afc8-423881c14c5b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/838/00000/532c4f63-94e5-45bf-9b6e-cf6f7abb1aef.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/776/00000/efe9c6c5-3ce6-4ae0-a380-c0cc4d614ed2.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/776/00000/4257f678-6cfe-4cc5-b22c-bd56be130b5f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/776/00000/ffeb3752-03c3-4b24-ae87-fdb33bcf3d49.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/776/00000/2005f905-8444-4544-bf41-ec5480eece32.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/776/00000/b6fa089f-d28b-40ca-86d0-0c04cac8a19c.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/773/00000/6df868b1-40da-46b5-9dcb-e95f29ecb70b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/773/00000/8be45a0f-32b4-4f5f-8ccb-0f93c0d07f97.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/773/00000/d98b2c1c-9b17-4cc0-8135-8b83bdef8bd2.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/773/00001/2b5e73a2-e3c2-4c5b-96e2-d5ac76e08587.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/773/00002/5c11ed01-cb3c-4836-bf8a-c3511326be98.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/683/00000/b6bc6d55-45f1-41ec-9eca-24e0eeae1141.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/683/00000/26015d21-7d7e-4160-baa2-a59f6fbcad98.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/683/00001/d19cf1e2-8c6f-48aa-922d-be14cea53dbb.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/683/00000/a8fbac99-f705-41e2-803e-682c2dad2cef.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/683/00000/e7ae582c-093d-431f-9989-6f74c6baba83.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/594/00001/f2e8aa9c-7697-46ca-beae-4537b9b74e56.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/594/00000/cbe22ab2-7a67-4cfa-9f29-916fcd46d539.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/594/00000/003643a6-5f01-403d-9516-f7fdac938ede.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/594/00000/73086fda-8575-4918-9ddf-ab73930b0081.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/594/00000/6eddeb0e-901e-4410-a137-51d78047f654.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/590/00000/bed3ebdd-9ce5-48df-a268-fde9cf9c3934.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/590/00000/6fcba8d1-48b3-442c-bdc6-c37877166a35.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/590/00000/07df9310-89b0-4349-989f-32eda58b6a62.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/590/00000/5f1ffe99-c6c0-4ae0-8bdb-a23e4e794dba.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/590/00000/a8b0682a-c234-40e2-8ddf-b4babb3c65eb.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/587/00000/5df56468-23f0-4705-83f8-e57d3abd335d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/587/00000/d7efa2e9-0aef-4fdf-abad-702fe50253f4.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/587/00000/ad866783-8e02-48c7-84e1-54d466a7ef3f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/587/00000/215ed796-b044-4c50-a30a-6e93d14bae1b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/587/00000/11ff9e7a-fb13-4968-a138-f9437e9bfd9a.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/490/00000/7389e84f-9850-4363-82bb-9ec7bdf4aa0d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/490/00000/7a020620-f4e7-4be1-82f8-6953bfbce6b1.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/490/00000/720e04d4-73c5-49d5-9a74-b82d8fcac8dd.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/490/00000/91ba1945-bf30-486b-9dd4-4b68a065b287.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/490/00000/37ab4217-2a08-4dcb-9df6-a4b8a9c8fff0.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/482/00000/a90c8478-9208-47ed-885d-c50a973e1d15.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/482/00000/fd4ebb97-3b7f-4553-ab19-6125820fe10e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/482/00000/854be282-4e6a-4a09-812c-d7a99fd6bc5e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/482/00000/4d75c179-21fb-411f-b44a-5e5d513c3cad.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/482/00000/2332776b-9054-4df0-a924-e772b867e397.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/410/00000/77cf5def-8b96-4c63-90d9-2f5716565634.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/410/00000/bff2529d-1f2f-41f4-96c2-93d10e2952f4.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/410/00000/ee1ba976-c4ef-40fe-a599-28fcb989222c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/410/00000/e4f84747-5435-41c5-9a0b-1715bd7d0793.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/410/00000/2ce30aa2-fc7a-44c9-8fbe-bec2bb2dfd20.root",
 
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/409/00000/b225b012-7fcb-4d2a-9bfd-f7c9ef5101f0.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/409/00000/f19ea422-171d-45d4-b184-1c79b88689ef.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/409/00000/5d5d7a64-eff1-4561-8b84-d54579148fa0.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/409/00000/b03f71ca-ca9b-415f-ac0d-c02b6eec8ffe.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/409/00000/d0177c10-ac03-4ea9-932d-097e441e2657.root",
# last 5 runs 
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/409/00000/7cb6ebd2-85ac-487d-8eef-743038df0582.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/409/00000/2e13d471-6560-4a34-80ea-a1ac392e5212.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/409/00000/75701adf-bb09-4e7b-ae4d-46d300aa4b63.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/409/00000/6290e9f5-64ea-4774-9441-18404c8494cb.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/409/00000/73d3284d-f26e-4a00-85e8-800424196fae.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/396/00000/5f84e142-a620-4dd0-a26b-213662fafcff.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/396/00000/479e2daa-9cf1-4f97-8f35-e2fdccb2a92b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/396/00000/466b4345-613b-4785-b304-96d601fc799b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/396/00000/d8c25598-1ca5-49db-af93-bcd4b105d35a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/396/00000/6e51aac1-be14-4b54-91a0-b9d201478204.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/403/00000/8ada7aae-be51-46e3-9dc0-4119b78d2e8d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/403/00000/c95059be-946a-4dea-8735-8a306233013f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/403/00000/25e7c084-b2e1-4721-9ec7-245f131cdaf7.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/403/00000/667c7674-32ba-41f6-9bef-4e1291ffa3e1.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/403/00000/e7c78cd6-d45d-4901-aaec-2099e7f1929e.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/273/00001/396bb564-060e-4e2a-a14f-3affaeeb7798.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/273/00000/859ad3c1-09b6-4376-89cd-a6e807d83d99.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/273/00000/81ce27cf-c361-483b-890c-bc66cbc793bd.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/273/00000/72c596e0-9546-4961-997f-81a3da55247b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/273/00000/03760c18-fc59-4bbe-8947-21ebb9cb404e.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/245/00000/ab454f91-6728-46f6-8626-4aea9a9bd775.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/245/00000/1f7b3d93-b00e-44e7-b9ca-a2dbce285142.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/245/00000/70606ca4-6749-459e-a74b-2f338896ca40.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/245/00000/81e73ece-d262-4149-8419-3ed501beedba.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/245/00000/8ec91ed5-6992-4110-a08d-11a498ccdbf9.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/202/00000/39ef7c14-cf5c-4729-8e6d-b9f3afe8df29.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/202/00000/c611c9bf-04d0-4140-a935-67106b68fd59.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/202/00000/c4452457-b7d6-467f-a777-3ff1ca2a35a7.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/202/00000/ad08c874-b5ef-46da-9d32-91ba8c194053.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/202/00000/0f8bbb13-f9eb-4cdd-ad91-792c800f0826.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/153/00000/d2e32152-a3c0-4d2e-82fd-fe36e6f4e331.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/153/00000/ba5a9a65-b0bd-4cd3-8f97-8a60d5d1ebac.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/153/00000/ece54694-e503-44b2-bad3-e728f7033849.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/153/00000/f115bc06-5241-4e01-ac3f-0d69b2460115.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/153/00000/2182d902-971a-44cf-9839-21606c44da6b.root",

"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/05d4e531-3560-40bd-ba85-d18f4fa78981.root",
"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/22cbd905-6a6d-4632-888f-fe96c32ad40e.root",
"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/e936125e-53eb-4e71-bafe-c027cb550a1d.root",
"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/bc3801d1-c45f-4ff8-bb44-6d9915e7cdd5.root",
"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/704bfd06-68ac-4e4d-9be7-59ce0fef0cb9.root",

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
                           selectedType = cms.untracked.int32(-1)
)

#process.p = cms.Path(process.hltfilter*process.d)
process.p = cms.Path(process.d)

# process.ep = cms.EndPath(process.out)


