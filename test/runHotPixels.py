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



"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/078/00000/c417642b-d84d-459f-80c3-fdb88f043d44.root",
"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/078/00000/8b5d7561-bc3c-43f1-8afe-1f9c296d955d.root",
"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/078/00000/2370e4aa-85c0-435c-ae7d-3ded46ca2938.root",
"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/078/00000/a05cdd88-7568-4684-9bd6-ca3426f741a9.root",
"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/078/00000/16074c5c-c76d-42a6-9f26-0b20616d30ca.root",
"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/078/00000/393cfcea-35b0-4f3c-83c9-7fad92841aa2.root",
"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/078/00000/5d71fa86-e2f0-463a-af2b-bdbdc7523ff6.root",
"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/078/00000/519ad2dc-24c2-412a-b753-ef751c3f2cad.root",
"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/078/00000/f583278d-8ff0-4245-8de7-6ed10dade87e.root",
"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/078/00000/56d660c9-207b-4bcb-9615-4f7d45578442.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/073/00000/79819494-31f7-4c32-b880-ce720b1cf734.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/073/00000/138bbe2c-5afc-421d-af10-3c7ef8bb75ba.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/073/00000/16606d41-0e80-4610-b180-e99c9fd4f940.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/073/00000/8fe25d54-daaa-4887-8015-6ff22b3be9d9.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/073/00000/82eb05a0-580b-4a0c-a348-b520ccb33fe1.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/073/00000/978252ce-b4a1-4049-a4e6-23ba10b6d74c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/073/00000/41f7d13f-6433-4e49-bc49-8fb93626e4de.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/073/00000/95af464d-b040-487e-bf46-3f9235f7c82f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/073/00000/b8e92f6e-a4f4-4a84-9c3a-497b38d4fecd.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/073/00000/34770910-bb7a-4f47-8007-9de105d88292.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/071/00000/2a556dd9-b4af-4919-b3f2-e1745f45e473.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/071/00000/b6971205-be9d-4f2f-9bc2-94a597b2b399.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/071/00000/3fa11a5d-1f24-44a0-8c2d-7bc4b7a7c056.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/071/00000/3cec5dd4-4fa4-4a70-9a5d-47a3d9bf1a8c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/071/00000/8e9c50e4-aced-4a6b-bb35-edc3a0a3523e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/071/00000/630f297f-6e4d-43cd-b926-9bb5f8e075a9.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/071/00000/bbad9467-d9e1-4f6a-ba91-9c42fdd55031.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/071/00000/4824b18b-bfe0-4200-8ec2-ed3e2707f226.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/071/00000/567a3c3f-6007-4b8b-8988-ceb8e309f18f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/071/00000/af63f26a-d3f1-4e02-891b-28ff168e238d.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/016/00000/825675cc-ea6f-425a-934f-c84705e02c1e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/016/00000/c1247c34-1b24-4a7b-b6d6-b1a9877f94e4.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/016/00000/0843e5f7-3c38-431d-b25a-cb4cd66dd8b8.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/016/00000/405e5077-4f84-47af-9319-d71762f7eb59.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/016/00000/3584f372-9513-4d6f-beb8-e484e1a598e5.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/016/00000/5d41cdd1-eab6-44a4-8da1-089188448f05.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/016/00000/d2c099ed-b324-4e2f-b934-fc5d680b381a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/016/00000/5c791fa8-aeca-4911-91fc-f66a1c298243.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/016/00000/51dda97f-379a-4675-a344-ab80e920cd3b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/016/00000/8d5809fb-411e-417a-96d4-f5b499e46dd5.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/007/00000/ea25c5b8-733b-4b7c-a896-dac11286cd23.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/007/00000/821d5af2-db65-4a17-8d45-86c19e070d72.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/007/00000/5a56f7ba-5854-4043-ba62-d9c90f39220a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/007/00000/dafad32c-a009-4845-985b-82d9450a0caa.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/007/00000/d144811f-ce55-43a9-aab9-ac714cbd4321.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/007/00000/8aec739a-48cd-4822-ac75-236fbe276aef.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/007/00000/4df80660-a15c-4b39-9b25-148773349280.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/007/00000/6c54922e-c0d9-4185-90dd-a64ea51fc8d1.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/007/00000/efaccfdb-2e67-4504-840b-6ddf270473b4.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/007/00000/208057f6-46ca-4aa0-b172-246a12efedc3.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/955/00000/9e19d04e-141c-449a-823f-dc49c8172d17.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/955/00000/825cf2ae-73fc-4e06-ae7b-4382f7d805a4.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/955/00000/5fe90350-7152-4046-8b29-e276724cb5c0.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/955/00000/b48d3eed-179c-498c-ad09-028990935f94.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/955/00000/a471e6ff-18f7-4d92-beb8-6f9138f6c42e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/955/00000/e6594dd6-5b35-4d13-93c2-2be9360aa567.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/955/00000/e74f65ca-172b-443c-be52-8ac5c91526b5.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/955/00000/ba3df4fb-f66d-4225-88ab-7b496c479096.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/955/00000/ab451761-88d9-4ab3-8fc7-12ee84eee671.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/955/00000/0b866d06-6f89-4bb6-a053-16c7ab74df06.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/929/00000/d79b6368-6fd5-48ea-80af-f78e238a6fb5.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/929/00000/c60a8d6d-1911-4a4f-9bb5-130d910bd56e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/929/00000/03f25888-82f1-4145-b1dc-16903f1e8a75.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/929/00000/6773f215-5205-4fb0-ac92-92bd782290ea.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/929/00000/654b5e99-9030-4629-92cf-92a00a32c2ed.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/929/00000/73691e36-9912-44e0-94ce-a8794fd8b220.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/929/00000/92e1e3e3-a11a-477b-97bc-8028a92a7850.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/929/00000/e508cf05-3e83-4441-8d6c-35fd53d1d990.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/929/00000/d76695d6-44c6-4412-af38-1a862ba8be40.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/929/00000/f096f8d2-8b9a-4097-b963-9c1ebe8af269.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/908/00000/d2c70f4f-0a21-4b9d-ba25-f2336b7cbc02.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/908/00001/63f242c1-b5bf-47d8-95e3-8d119bd9b9af.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/908/00001/0a2ab488-0dbf-45a0-a65e-7df2aadc9767.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/908/00000/c4f38d71-3a84-465e-9459-adc29cbc2741.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/908/00000/3d5cb7f5-871d-4eaf-967b-c111e66160c5.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/908/00000/ffbaddc4-55f2-4a93-83e7-8d8c61bb27a5.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/908/00000/45544699-f358-4b08-b1f4-d0d7fbaed834.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/908/00000/f91763da-5157-452b-8a20-c632682e5296.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/908/00000/10135600-96b0-4ef6-ad68-289af4481f46.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/908/00000/7b932121-ab92-4759-a2aa-9e52e92cd7ad.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/905/00000/64e4075a-433c-43d0-a2df-5501491e97d9.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/905/00000/b2ed640c-89e8-4753-b985-ad8424799089.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/905/00000/e67ced3f-4d31-491a-b928-61163f8f8e13.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/905/00000/d578f957-755e-420b-a43f-3c21399e9eac.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/905/00000/aa764b46-d548-46d8-a52c-70d1c87b026d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/905/00000/d6e68ef7-bdf5-4afc-b603-e228ffd069cb.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/905/00000/d8b1f403-1ca6-4f5f-9c2c-7a11ee9784af.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/905/00000/ec469c99-1f13-42ec-a270-8ee84d88a177.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/905/00000/15038475-8f78-42c3-b2f7-982afbc5b88b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/905/00000/59fbc761-f581-4d54-b4ea-ebcd2126564d.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/901/00000/22d603a8-c974-41db-9f7f-0ebaa9722000.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/901/00000/adf700bc-bae8-489e-9328-2608e7603616.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/901/00000/e7d6b64d-4485-4129-a8f2-0655e3317339.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/901/00000/6c2dfcdf-cac1-46c5-91e6-b94d414e496e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/901/00000/b8d64a60-05a2-46d6-8901-8284d3aedb21.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/901/00000/67792e28-700d-41d3-954e-d17eae5febd1.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/901/00000/daee7f38-fb06-43ba-b4e4-702137094c79.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/901/00000/626a2959-6a41-438c-a14f-22176f61a32e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/901/00000/bfa48493-a425-4873-90e6-db34797f064c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/901/00000/5e29167c-e156-4b34-9dce-116be513260a.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/840/00000/dccfafc5-70aa-48bd-9e7c-e660669f7493.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/840/00000/aa2bd31e-9551-42ad-924a-a941cc53f7f8.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/840/00000/72082a3d-75d8-4209-b8b7-e86edeeb44ed.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/840/00000/d6b6d3a0-0d4c-4bd1-8674-313312224fc4.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/840/00000/332261f8-1d58-426e-9d81-4d2dd0562e11.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/840/00000/3c543b6f-995f-46be-b8fc-8665ceeb9808.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/840/00000/c6dbf2e0-aaa0-4c79-9f0c-428e0891118d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/840/00000/4240f603-60f1-44a1-9911-befd88b0d028.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/840/00000/036e3372-cf51-4f41-bbf8-2a49f54b6270.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/840/00000/70ff3a11-2550-41f3-8b5a-998a1ec77205.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/839/00000/5147455b-8608-40f5-a7d8-b9cb45b462bc.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/839/00000/4b520aa3-2d57-4b2c-80ca-44ab6b5d21cb.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/839/00000/c77c87df-c856-4929-b5cc-4690367fcd74.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/839/00000/46489ca7-5be3-4eb9-9be9-5b0d84a11d87.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/839/00000/fd812384-a57d-4699-bfff-ace6a0999bc0.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/839/00000/9c79f6fd-a9a9-4d9d-bc40-10e378716ef4.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/839/00000/0425010e-0da0-49e5-acee-2602d0250a93.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/839/00000/0e9620af-4b19-4c4d-bc2f-3de82ab1a304.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/839/00000/c6e5d765-095e-4215-92fa-b3b83191cf69.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/839/00000/a728e73d-2f35-4d91-bb51-53d7bc54102b.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/838/00000/fd3f2919-0462-4d2e-a3dd-d472fa444268.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/838/00001/b362b944-42d1-4f95-9c8e-7aa6c32b3002.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/838/00000/85f68c6a-39bf-4d16-9264-449585927907.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/838/00000/9c417c17-50d7-49e1-afc8-423881c14c5b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/838/00000/532c4f63-94e5-45bf-9b6e-cf6f7abb1aef.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/838/00000/3292221a-fe91-4eed-8131-9f4ba804137e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/838/00000/48621e13-6abf-4ab8-a05c-ed2cc2b60409.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/838/00000/9dd69746-b9ad-4819-b8cc-6bfdaa1155b8.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/838/00000/6bf7b6c0-a6f0-46ad-b7e4-c2a9ae403749.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/838/00000/4f914e87-3d1e-470a-baaa-c54e0a023d5d.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/777/00000/12a60db1-af76-4272-b499-acf6359dba42.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/777/00000/0fdf47d3-5cd4-47c9-996f-09a791401b3c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/777/00000/97ba5ae9-d64f-4ac5-9701-f3bbc23de018.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/777/00000/ae5ee91d-f75d-465f-845c-529a248d15e3.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/777/00000/ae612f92-73e4-430b-ba1f-0a76fb05de63.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/777/00000/2bef8a68-38d6-45af-b3b8-93b49d5ca201.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/777/00000/7a111edf-362e-49b9-995d-0327ef5574d9.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/777/00000/a6a07ec0-4f74-49a5-a9ed-4bada1d2ee46.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/777/00000/7492c331-9d2d-459e-bf5a-0c5cc9ab832f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/777/00000/b3e9f846-b7db-4eaa-80b2-d969b2a600f9.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/776/00000/efe9c6c5-3ce6-4ae0-a380-c0cc4d614ed2.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/776/00000/4257f678-6cfe-4cc5-b22c-bd56be130b5f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/776/00000/ffeb3752-03c3-4b24-ae87-fdb33bcf3d49.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/776/00000/2005f905-8444-4544-bf41-ec5480eece32.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/776/00000/b6fa089f-d28b-40ca-86d0-0c04cac8a19c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/776/00000/5fcefeeb-fe0a-479c-8f54-956c86650618.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/776/00000/d8d3aafb-3c5c-4e87-9911-7cadc2aef7d2.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/776/00000/70bd9250-1046-435c-8746-d63d01de663e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/776/00000/0091faa2-cac3-4f75-8257-76b9ff9dd95f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/776/00000/645a4dac-943a-4a4f-8552-28db2ad12f91.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/773/00000/6df868b1-40da-46b5-9dcb-e95f29ecb70b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/773/00000/8be45a0f-32b4-4f5f-8ccb-0f93c0d07f97.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/773/00000/d98b2c1c-9b17-4cc0-8135-8b83bdef8bd2.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/773/00001/2b5e73a2-e3c2-4c5b-96e2-d5ac76e08587.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/773/00002/5c11ed01-cb3c-4836-bf8a-c3511326be98.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/773/00000/13feb01b-b812-40e7-94e3-6d3a3fc8a986.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/773/00000/4d6bc987-73fe-4cba-9b8e-f434f96b48dd.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/773/00000/975a5ef1-7e97-4f8f-84bc-84c6156a15a4.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/773/00000/f6751558-e4b9-4e40-81b2-7b030d72de87.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/773/00000/58ccbee3-4662-4b1a-802a-7bdfcbc862a8.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/683/00000/b6bc6d55-45f1-41ec-9eca-24e0eeae1141.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/683/00000/26015d21-7d7e-4160-baa2-a59f6fbcad98.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/683/00001/d19cf1e2-8c6f-48aa-922d-be14cea53dbb.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/683/00000/a8fbac99-f705-41e2-803e-682c2dad2cef.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/683/00000/e7ae582c-093d-431f-9989-6f74c6baba83.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/683/00000/1be7119a-5497-43c6-ab16-6be47821b58a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/683/00000/fca29cee-445e-48ce-aca7-8776ebacd3ed.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/683/00000/1e0d3840-11c7-4d28-82cf-4e5bf757ae38.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/683/00000/30a49a49-0a96-4f1b-a0e5-bbaa4ad30b4b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/683/00000/79e9f83d-82ce-4ee6-933a-bad21b781ea8.root",

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

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/492/00000/85f6c0fc-5c8d-40f1-a6c4-993c5ba233d8.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/492/00000/17deaad6-0c9e-45e9-862d-95165acddb20.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/492/00000/aa7617f3-bd49-4d61-b842-8ded01e3500b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/492/00000/2dfa2c54-61fd-4ff4-a0d1-74c54b55f8a6.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/348/492/00000/1670e079-df4d-40fa-8e33-0df0a300cf98.root",

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
#                           Fraction = cms.untracked.double(0.001),
                           Fraction = cms.untracked.double(0.0001),
    MAXFED = cms.untracked.int32(1293)  # bpix only 
    #MAXFED = cms.untracked.int32(1338)  # all  
)

#process.p = cms.Path(process.hltfilter*process.d)
process.p = cms.Path(process.d)

# process.ep = cms.EndPath(process.out)


