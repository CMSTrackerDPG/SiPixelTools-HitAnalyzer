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

"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/7a95071a-a0f1-4ecf-b3bc-5bf2bdecd588.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/655d1133-df1e-4a53-b2f9-36f9cd611650.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/c357f0e3-8949-4eed-8b0d-b6e8944d1c6d.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/cd61eea9-8a03-468e-a351-490d6c84294b.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/22b4a307-b1a1-43bf-83bb-1cd7f98a093f.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/5a31e66c-a5d9-42a0-bf5c-b7b14c255f58.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/03bcaf51-82bc-41d5-95ed-715a57a2643e.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/36c97fae-b7e7-4329-b509-07df501e5da2.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/edf65712-1a0f-4320-83b1-59050eeb3ef5.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/13579ca8-e265-48a8-bf85-8b47ddf85a67.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/bfba2161-698f-4bf3-bfbb-1ae258d52c73.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/7956a136-c2ac-411c-817d-b4e20219568b.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/0f0ab7d6-721d-409e-b69a-3ea76c08503c.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/6a0ee4d4-c039-4694-b3e7-7853239a6e93.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/878f0bc0-0845-4a92-8dcf-7fa6424750b5.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/84cb565a-c2a8-4288-a452-89eda1067ad5.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/9d472f52-2fc7-4ea9-8e9d-206f11468502.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/c01c8fae-e641-4a1e-a202-896f7aa6d3bf.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/0bb8c8d0-1585-4e6f-9098-feb3e1562519.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/12db9eca-f748-42ba-9a30-bcd7174b7dd4.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/fcf84d5f-c079-4eb9-a75d-5e69bad90863.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/23efb59a-324c-4a59-97d7-20417bcf2df5.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/56226cce-de9b-47e5-af90-5a8cb7149b93.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/90b2ed76-fada-40bc-a456-3214c342d7a2.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/de0b2bb3-15c1-4d7d-ad34-659be9089231.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/f037e72b-6d8e-4002-b032-44d6ea6c89b4.root",
"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/810/00000/1eed3bbc-688b-4659-be28-e038367c4c41.root",



#"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/563/00000/f6adcf9f-9d24-4e6e-986c-9b7f454d49b4.root",
#"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/563/00000/f5e14417-075b-495c-ae9f-25fe11c7dcb3.root",
#"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/563/00000/ffcc4028-6732-48fe-911c-ac8c65206f35.root",
#"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/563/00000/a94a85a6-bcd9-453f-b963-99a3a970aa65.root",
#"/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/356/563/00000/565d9277-6616-4e74-a915-fd0b1ba3148d.root",

#"/store/express/Run2022B/ExpressCosmics/FEVT/Express-v1/000/355/555/00000/b7c848d8-edcf-4c13-b609-db0b0cf6384b.root",
#"/store/express/Run2022B/ExpressCosmics/FEVT/Express-v1/000/355/555/00000/af1ddf64-b8c6-4535-b9f0-fe343db73fcc.root",
#"/store/express/Run2022B/ExpressCosmics/FEVT/Express-v1/000/355/555/00000/e1a10777-b857-4cde-970d-089049df5426.root",
#"/store/express/Run2022B/ExpressCosmics/FEVT/Express-v1/000/355/555/00000/be9b535f-1e4b-490a-b5b8-bcdcf79c839c.root",
#"/store/express/Run2022B/ExpressCosmics/FEVT/Express-v1/000/355/555/00000/06ac2516-a694-4685-b63d-28842a4153a3.root",

#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/381/00000/7e9331c8-ae86-43a6-be18-05c83046e1bc.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/381/00000/ca341087-3c22-4bd5-be25-71bf306c99c0.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/381/00000/9416b0f1-76fb-4015-bbd7-2bb9a552b2de.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/381/00000/564244ee-b6d9-4298-9904-c15cdcdd88ac.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/381/00000/94dc6ace-f294-4781-87ab-f4f371e0a764.root",

#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/208/00000/189ea7e2-6515-498a-a562-d8902ded3294.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/208/00000/deada9b3-33b5-4752-a965-fc990c15e278.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/208/00000/f4a171c3-63ff-4d2d-8b58-fd91a327aab4.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/208/00000/8ce26356-1dc4-4fdb-9188-66b03df28232.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/208/00000/ba89d899-4a11-4be2-9e6f-06c5866a0be8.root",

#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/207/00000/beb46d70-a0d4-4c8f-a1eb-7b8e51139df6.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/207/00000/34f79386-6dcc-4d42-887b-d9f6a5f28b72.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/207/00000/5124fbd0-687f-4ec0-be1e-04c9c311a338.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/207/00000/156e5248-a00a-43df-8ebc-fe70301219b2.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/207/00000/cad6131e-f79d-4e0a-9901-50f093cb0f1f.root",

#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/206/00000/f3609fb7-0627-4f16-ba04-f77e686749ca.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/206/00000/566f0f14-e9d6-4b40-8dc3-2e426e93ae1a.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/206/00000/eb6b4de9-e3ce-458e-bda5-07b5e664c9dd.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/206/00000/d0f4ac11-c782-448b-87b6-efc4e71940a0.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/206/00000/94d39973-b35d-40b0-b4a8-02db30754bb3.root",

#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/205/00000/49efb5e2-ba09-4c8a-819b-389b298c9704.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/205/00000/65ab5073-f830-4e46-8039-7a8d227bdbe0.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/205/00000/dfeb5fff-426d-43da-bbb3-3ed078220d83.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/205/00000/718e3e1c-62fb-4a00-879d-d1156a9f0951.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/205/00000/dfd87a51-aa2b-4be1-b441-b57f1dcc385f.root",

#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/204/00000/1b01185a-6bff-4f4a-995e-259242e2cffe.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/204/00000/e40ee27f-7a2f-40bd-9b9c-32d6ec1e2351.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/204/00000/213fc4cd-c777-418d-a132-b8d2f83f667a.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/204/00000/23837ee7-93c5-4332-9f61-eb722469828a.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/204/00000/b85f3165-337d-4169-8151-d994704b66ba.root",

#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/133/00000/80bb21d0-a607-4d33-a1a9-d8bf6d47b7ea.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/133/00000/90505a0c-7e38-44ea-97da-f04b04da3e8c.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/133/00000/71909bb1-679b-4dfd-b2e6-80cfb1a65cb0.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/133/00000/4bdb3b9c-7766-43c1-9149-0cb2e08b4902.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/133/00000/2ebaa94e-381f-4ce6-907b-693f5ad0c65b.root",

#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/103/00000/080ee2c6-2c26-47e5-805e-4bb61722a5ff.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/103/00000/14299b91-09fb-4d0c-9d1f-045eb4864880.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/103/00000/49f317f7-b01c-4ad9-8484-14fbfd53d048.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/103/00000/810c7bf5-27f3-451b-ab45-d78e79dbf796.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/103/00000/9541989a-d892-4c35-9bc0-dbe9ab53fb8d.root",

#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/100/00000/e385159a-3c90-4dfc-bbb0-16a6e3196b5b.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/100/00000/8125dc00-244f-4029-8d0e-9eefcb576f3c.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/100/00000/455249d4-33cc-4abc-aead-744d45b2e8e3.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/100/00000/e33d0902-a370-4da6-99ee-153d58478878.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/100/00000/01815849-c210-4c3b-93b7-a96d29a5f9f1.root",

#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/058/00000/14d4e373-d23b-4515-92f8-015843ba1c04.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/058/00000/3f46f088-8628-426c-b13c-7809fdb46a76.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/058/00000/91b1ce23-3966-42d3-86bf-44a55551b19b.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/058/00000/3fb959a5-78a9-42f4-b120-a6b7d94a37cd.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/058/00000/233a10a6-bcc2-49a6-94f0-48dafc349c12.root",

#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/046/00000/9e9c5d55-fef5-4756-b784-9517a0b832c9.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/046/00000/0154be6f-8239-4cdd-82d3-c716843287ff.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/046/00000/12404eb1-ae05-41de-b0dc-0aae77c3196a.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/046/00000/dc494571-7249-4c07-9b34-d46e707a3d2e.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/046/00000/f9141467-0884-4066-943f-4d240a6b7cb6.root",

#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/706/00000/415e294b-b0eb-4895-a350-1eabb3a27960.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/706/00000/fb711f55-67e2-4d9c-b030-91679ded8edc.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/706/00000/fc97653f-8748-489f-9b1f-761354303d00.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/706/00000/0e7a502a-9bc9-4173-9347-4202a6708102.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/706/00000/428e2543-6cdc-4b76-971f-51163c2a1903.root",

#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/097/00000/92a7cc8f-d37a-4716-9fa7-a1268d7244c1.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/097/00000/45e24472-64b6-48e9-a200-d369714bdba9.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/097/00000/5ddceb3e-14c6-4009-bd5a-7da35990e8ca.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/097/00000/a9fc57fc-d7dd-48c1-9f14-7e4deb361037.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/097/00000/98f97522-ae6f-40c3-9bb9-679d38aeff2e.root",

#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/dd0286ac-9305-4ac1-b849-e835b56b2def.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/8da8bd23-b41a-44be-9eb5-374f562f7a0e.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/66f189f5-0def-4b14-ab5d-ab5b5c131d16.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/c375f7d1-8785-450a-b2d2-968c16ddeeb6.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/1b7bfea3-e324-425d-afb2-cb5f45cef07d.root",

#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/2499e0b2-8ec8-4c6e-8173-c2ab48510815.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/ef867575-a95e-4bb7-832a-1eec9904fffc.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/0e1b06f9-2393-49ee-9afc-ed1ca7b5ce4b.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/a73ced30-a5cc-4998-9d4d-b83faaac436d.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/6aa8ee92-5491-403f-96c0-069dc4a40d54.root",

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

process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('356810:1-356810:100')
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

process.p = cms.Path(process.hltfilter*process.d)
#process.p = cms.Path(process.d)

# process.ep = cms.EndPath(process.out)


