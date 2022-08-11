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

"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/103/00000/080ee2c6-2c26-47e5-805e-4bb61722a5ff.root",
"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/103/00000/14299b91-09fb-4d0c-9d1f-045eb4864880.root",
"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/103/00000/49f317f7-b01c-4ad9-8484-14fbfd53d048.root",
"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/103/00000/810c7bf5-27f3-451b-ab45-d78e79dbf796.root",
"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/103/00000/9541989a-d892-4c35-9bc0-dbe9ab53fb8d.root",
"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/103/00000/8cb271b5-f4d2-41e4-93da-7d5e6a1de7c1.root",
"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/103/00000/4169ab43-0678-4ed8-8cdb-bcb185a07110.root",
"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/103/00000/806a8218-2b1c-44d5-9cfe-2d458e05c057.root",
"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/103/00000/983438bf-a11b-42bc-be6e-f1c6e6db24f5.root",
"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/103/00000/575695f4-07d9-446d-bb6f-8cf55c78af9e.root",


#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/100/00000/e385159a-3c90-4dfc-bbb0-16a6e3196b5b.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/100/00000/8125dc00-244f-4029-8d0e-9eefcb576f3c.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/100/00000/455249d4-33cc-4abc-aead-744d45b2e8e3.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/100/00000/e33d0902-a370-4da6-99ee-153d58478878.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/100/00000/01815849-c210-4c3b-93b7-a96d29a5f9f1.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/100/00000/e168a475-9195-40a4-b537-666a26eb38eb.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/100/00000/82891125-f581-40f8-8491-d9803bdffcd7.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/100/00000/4d881c73-f7d8-48e1-995b-d333b05ed2fa.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/100/00000/7695dbef-7c3d-4914-b8c3-beb257bce90e.root",
#"/store/express/Run2022B/ExpressPhysics/FEVT/Express-v1/000/355/100/00000/66562b8a-350e-491f-822f-5451db5b4433.root",

#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/058/00000/14d4e373-d23b-4515-92f8-015843ba1c04.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/058/00000/3f46f088-8628-426c-b13c-7809fdb46a76.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/058/00000/91b1ce23-3966-42d3-86bf-44a55551b19b.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/058/00000/3fb959a5-78a9-42f4-b120-a6b7d94a37cd.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/058/00000/233a10a6-bcc2-49a6-94f0-48dafc349c12.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/058/00000/ae02de4a-1130-4101-b4f7-1db7af63edcc.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/058/00000/d84823d7-d538-46e5-9363-0490bc34ecdb.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/058/00000/e813b465-e5e4-43a1-a96b-031f308ae6a4.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/058/00000/3c963ec4-d156-4230-bbd7-2a35bbfc11a9.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/355/058/00000/325f53dc-fae6-46f5-b721-6a1d71f5ef7b.root",

#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/097/00000/92a7cc8f-d37a-4716-9fa7-a1268d7244c1.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/097/00000/45e24472-64b6-48e9-a200-d369714bdba9.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/097/00000/5ddceb3e-14c6-4009-bd5a-7da35990e8ca.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/097/00000/a9fc57fc-d7dd-48c1-9f14-7e4deb361037.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/097/00000/98f97522-ae6f-40c3-9bb9-679d38aeff2e.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/097/00000/4046bd11-43c4-4aef-91d8-a949726b3456.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/097/00000/98ff33ae-356a-43d9-98b0-6eb408f9ba30.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/097/00000/69a018e8-2796-48e3-a386-dd47a81cfb20.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/097/00000/2ebf93ac-6895-48c7-a540-5baa25be5923.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/097/00000/77a7eb18-9dae-48de-8285-29cd58225798.root",

#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/dd0286ac-9305-4ac1-b849-e835b56b2def.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/8da8bd23-b41a-44be-9eb5-374f562f7a0e.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/66f189f5-0def-4b14-ab5d-ab5b5c131d16.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/c375f7d1-8785-450a-b2d2-968c16ddeeb6.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/1b7bfea3-e324-425d-afb2-cb5f45cef07d.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/c6017e3c-85c2-4d50-80e3-15f06d8d4e92.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/465cc24a-8342-4b81-ad36-745c5094ae13.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/2911525b-0308-463a-bab3-9878055185c9.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/fdb7fa3b-ca17-46b7-86e3-96b07e5dd288.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/087/00000/29b33f51-92cd-4058-ae1e-4ff00fea68ba.root",

#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/2499e0b2-8ec8-4c6e-8173-c2ab48510815.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/ef867575-a95e-4bb7-832a-1eec9904fffc.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/0e1b06f9-2393-49ee-9afc-ed1ca7b5ce4b.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/a73ced30-a5cc-4998-9d4d-b83faaac436d.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/6aa8ee92-5491-403f-96c0-069dc4a40d54.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/3c036ed4-94ba-4d69-a0dd-0445d6aa1842.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/8fae349e-a532-41a5-81c3-0d09313143a7.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/811b7829-a2a7-44d0-86df-db3cd7dc6ba1.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/cccf674a-7698-428f-a580-85b44f443f23.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/353/060/00000/c803395d-2c00-40d7-9d2d-db56428dedec.root",

#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/509/00000/31ddb814-16b9-48ca-9e83-088a37673872.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/509/00000/3a261264-741a-43bd-970f-6a1f2df7a567.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/509/00000/01cb99ff-207a-40e0-bc0d-879f9d33ca7c.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/509/00000/a5b146de-096e-4da2-a42e-ba6b06e61ae6.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/509/00000/f271c85b-02ff-478f-be94-95955b95a26f.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/509/00000/87e08162-108c-4b04-961a-d5e88e3afa78.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/509/00000/938a9cf3-328f-45fc-9a90-f27b747cca9b.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/509/00000/34a1c38a-08e3-4f66-af9f-d3a22140886e.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/509/00000/fa624358-4613-4034-8c82-0458f5155b7a.root",
#"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/509/00000/2709331e-0077-4dce-b48d-ec88643cf214.root",

#"/store/express/Commissioning2022/ExpressPhysics/FEVT/Express-v1/000/352/165/00000/179d95e5-51ad-4735-a226-f9191c64d5eb.root",
#"/store/express/Commissioning2022/ExpressPhysics/FEVT/Express-v1/000/352/165/00000/3ae149e9-0722-4d92-8b55-b549a6e98a14.root",
#"/store/express/Commissioning2022/ExpressPhysics/FEVT/Express-v1/000/352/165/00000/3e69a3a0-3538-4661-9aaf-d9fcaea25af3.root",
#"/store/express/Commissioning2022/ExpressPhysics/FEVT/Express-v1/000/352/165/00000/eab43e93-325f-4c64-b696-02211e7f1d26.root",
#"/store/express/Commissioning2022/ExpressPhysics/FEVT/Express-v1/000/352/165/00000/04b79903-8cd3-41b3-8b68-e91c4e2aa3cd.root",
#"/store/express/Commissioning2022/ExpressPhysics/FEVT/Express-v1/000/352/165/00000/f11d1245-4312-40bb-88df-440c1cb1d3b4.root",
#"/store/express/Commissioning2022/ExpressPhysics/FEVT/Express-v1/000/352/165/00000/0970c02d-9903-4015-a91a-79fc76f0c9e6.root",
#"/store/express/Commissioning2022/ExpressPhysics/FEVT/Express-v1/000/352/165/00000/79baada8-0cb5-4779-9818-91cac722c6fa.root",
#"/store/express/Commissioning2022/ExpressPhysics/FEVT/Express-v1/000/352/165/00000/01acf25a-ae2f-4f58-a428-256d49be0fb2.root",
#"/store/express/Commissioning2022/ExpressPhysics/FEVT/Express-v1/000/352/165/00000/970c006d-951b-4ca3-b1fe-f2e962ce02bf.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/040/00000/6172dc95-e149-412e-815a-0d0e4fa31343.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/040/00000/262b3d7e-78c3-4f16-a9f6-069a5638bfdd.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/040/00000/d78d5b79-4e8e-404f-9348-dbcb77f8d394.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/040/00000/231ad787-7e50-4787-88f5-09cd9b996d82.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/040/00000/a2ceaccc-1a9e-404c-ada6-e0506e3fbf8f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/040/00000/37ad7d8b-e92e-4c98-977f-ff621d570936.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/040/00000/b79c02f1-30cb-4909-b513-3362f4283481.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/040/00000/008720b9-21bb-4fa0-bb0c-1c986e4678df.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/040/00000/2f67b683-e550-4de5-9851-549563800603.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/352/040/00000/365b6563-b8a6-4947-b773-4038b40aaa19.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/589/00000/2eb6fc16-353c-4d19-80fc-804ea9cee648.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/589/00000/c37e7364-bd2a-4bb2-a57f-d7e99d12b231.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/589/00000/430db2b4-c886-4bf2-87f2-d3a693e0d694.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/589/00000/a5378423-d8a9-491f-af6e-c8bb68e3c6a1.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/589/00000/ac6d2615-e293-41d7-902d-f06cb3eb7041.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/589/00000/d1001165-2e34-4dda-833c-8cae32cb89ea.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/589/00000/1c5ba245-8aa4-4468-82cd-8c801da75978.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/589/00000/8bdde6e3-5421-474e-b7a8-1798ff12b3b2.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/589/00000/31b0385f-817e-4e4f-97cc-a36151a6c48b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/589/00000/b2f18246-7be2-4156-a929-f0484b7bbdf4.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/588/00001/cce2c568-de5b-4573-8796-f8390e014ae2.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/588/00001/74b44980-a057-4444-9aea-15888b855734.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/588/00001/25d205eb-1209-4e7f-a08a-acad2cdb4452.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/588/00001/dbce9cac-df7f-440c-8ae5-a4fdcfdd0310.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/588/00001/35e56fcc-f7fd-4fe6-904f-00bf16b55732.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/588/00001/802a78f5-77bb-4914-bb7b-7795ab78dc6b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/588/00001/fed23720-061e-4655-8938-91f16c9e61ea.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/588/00001/5ba302c6-c906-41e0-a483-2ebfbca1fcda.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/588/00001/bae30278-d745-4e97-b5db-1c5cfad6db29.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/588/00001/721191aa-6a0c-4b5c-9160-2f102f5f8ae1.root",


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
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/470/00000/28c49121-efaf-4568-9ec9-e55b553be5f6.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/470/00000/a73c8d97-aac3-4a43-b2f8-ec4e28a4ab85.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/470/00000/fa8ffe5f-99e7-4265-a4c6-ee712bb74d77.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/470/00000/a130c96c-f382-4dad-a3b7-71075b628344.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/470/00000/5b3dd19f-c073-4a49-a128-12e616e61304.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/340/00000/25a03828-34ed-4c1a-b8b7-7d85be2206d0.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/340/00000/980bb60b-2d01-473d-b6b7-e729844a44b3.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/340/00000/d7594847-de6a-4214-a7ab-19e7508bce7e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/340/00000/19bc5985-bd02-4dd4-aefa-d5650af73934.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/340/00000/6426fe74-eb79-430d-8f1f-e1e50294c88a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/340/00000/a8bf1624-e62d-489a-8f7f-0b841ef7ba27.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/340/00000/6ed7f031-d4c1-493d-9aff-c5d93355348c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/340/00000/e576a10b-46ee-46b4-a3a0-91832766d398.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/340/00000/154a74c2-6adc-47f7-a67e-fbea16daf931.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/340/00000/6597543c-ccb3-4e8d-8cff-bea93444ff47.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/287/00000/a373b0a7-847e-4e08-a7da-49ac4e5804e5.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/287/00000/2184b4f6-43c3-4539-95c6-53c42dc6399a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/287/00000/c32893cf-3b1a-482e-a9e7-7579d6a0ba9e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/287/00000/ceb6e9b5-509f-4582-b204-060d599fdb24.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/287/00000/5e1e1927-58db-4589-9b44-a6dd3eb8f14c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/287/00000/b20aafc4-4d81-43a4-8e63-1867a7705251.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/287/00000/807ec6ed-b320-44bb-aa14-813da53bb7fe.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/287/00000/e8b3675a-0893-4570-9472-35a2cf567010.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/287/00000/0b89db77-4c8a-46db-b57a-d3bdda9535fb.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/287/00000/70abe9cb-8b42-4750-bb0b-1f2f871e3f9e.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/264/00000/5a2c35a2-8efa-4611-aadf-a2d7049978b1.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/264/00000/7080d1d9-41bb-4066-a77c-31e63e9bd08e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/264/00000/4aa5901c-04d9-431a-92c3-5841544937b3.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/264/00000/6305fb69-51a4-4baf-8c43-17ef66b35390.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/264/00000/e8c18796-3f93-49ad-85b9-df7d7c4b8755.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/264/00000/6af6c7b5-14ce-4893-aeef-09a0494055ad.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/264/00000/f8ee94b6-5bd0-4e4d-a96b-89188a483c5c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/264/00000/53ec8849-075e-46cd-896b-75c1176f4742.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/264/00000/e903211d-4c19-4aa9-a296-bf915e428eec.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/264/00000/27f64804-5c30-45ef-9c3e-900d14480a8d.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/217/00000/460c8377-56ba-4773-9f48-a11e85679c0b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/217/00000/ab96f8b4-dbcb-49c0-9b46-308a2787580d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/217/00000/65489017-b55a-44e8-897a-f1bdb225debe.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/217/00001/8307ac89-0407-4d87-96dc-90f1331d5434.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/217/00000/ec3a5588-bbf5-428e-b3c8-fed9c95bc66d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/217/00000/bfaa91aa-a9ec-47f9-ab8b-2ead1348f73f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/217/00000/8bdd0e93-1a00-4c8e-9924-890292def6f0.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/217/00000/bed26d64-5a75-41fd-83f5-4d24763ae0cc.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/217/00000/fdd0e8e1-33e9-41bc-9505-4e8a0384a623.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/217/00000/79f40d80-4345-4ff7-b924-3ca9d30e64cc.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/168/00000/24812da7-e4ee-4fa5-bc0c-c462fb933deb.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/168/00000/454210c2-8e49-4af2-8fea-6b6d2ee7a7c5.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/168/00000/015fbe60-808d-4460-af2c-10623e824e14.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/168/00000/8d5b4b3c-8874-45ad-8b99-dbb614b0388a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/168/00000/bcca1513-e33d-409f-b2ba-a34874f1571b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/168/00000/b69a95d8-37e4-4285-aac2-df174df9416c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/168/00000/1ec6d2cd-6d17-4495-a311-b476ff49b96a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/168/00000/297a3a41-0569-459b-b1bd-792a3c611c58.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/168/00000/e7dae393-415a-4b08-892b-8d0ac6a45d3a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/168/00000/cb24a892-dc9c-4860-abb4-8e38c57695e7.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/034/00000/ff558ffa-52b2-4d28-85cd-ac8e600cbeb9.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/034/00000/715653ee-c8e6-4204-8f76-deaa94ea36c3.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/034/00000/5baa6bb7-967e-45b6-815f-64a60e6f2de6.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/034/00000/a3d403a6-0ef4-4cef-b0a7-e80fa4b80187.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/034/00000/3a9175d4-29bd-4768-844c-61448ad533b8.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/034/00000/f4062e7f-5cf3-41a9-8de2-4664991af3db.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/034/00000/28d4dac2-059c-4dda-88b8-50ed959ac47f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/034/00000/0a535fa3-98f6-4756-92a4-6ce7bf4911b3.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/034/00000/10bfecc7-b3e1-480c-a0d9-6aee61e25587.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/034/00000/0b2a522e-9dd7-4b94-ace7-6918c1b8da68.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/032/00000/83d235b7-98d3-49bb-9e5f-7d97ac3bc1f6.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/032/00000/db16ab3b-e5a1-46ac-b160-14920626c34d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/032/00000/f607ce53-218b-4149-836d-d942edb8d390.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/032/00000/bf55a747-4a67-482a-ad8a-1bb350696e2d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/032/00000/7c81a03d-c60c-4d72-8074-462f0423a417.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/032/00000/4151652c-780a-4efc-ad35-690fa39f7190.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/032/00000/4d776769-1fa8-450f-b692-f019916d6bdb.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/032/00000/0fcf83e9-4b25-428e-b8a6-9e595758a1b8.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/032/00000/7a66bb18-6be3-4546-8291-4f3576bb4139.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/351/032/00000/5108e8b9-38f1-4a73-b5d9-2be7bd81d700.root",


#"/store/data/Commissioning2021/ZeroBias/RAW/v1/000/346/512/00000/0fb9b53a-ead7-45b2-8f8c-c15332c16d12.root",
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
                           Fraction = cms.untracked.double(0.001),
#                           Fraction = cms.untracked.double(0.0001),
    MAXFED = cms.untracked.int32(1293)  # bpix only 
    #MAXFED = cms.untracked.int32(1338)  # all  
)

process.p = cms.Path(process.hltfilter*process.d)
#process.p = cms.Path(process.d)

# process.ep = cms.EndPath(process.out)


