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

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/619/00000/07c6174f-3170-431f-b64b-45bdab4c6ff1.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/619/00000/709736eb-6e44-4b63-80bf-b707da61fbd0.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/619/00000/792912d3-a500-4b13-850a-1b773de0d6a2.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/619/00000/c334296a-852e-42ac-9749-ae55fe0e1925.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/619/00000/8d488133-0257-4195-b7dc-1641ade754ea.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/618/00000/72bf6139-5b50-4838-a82e-db375c35b6d6.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/618/00000/d0c66d46-9c3a-43fc-91cb-5c2de7cfc6c7.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/618/00000/1d0fa04b-8c90-4593-a956-3bb4bf4882b8.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/618/00000/bed1b9c8-4785-4a9c-a709-ad522735b270.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/618/00000/93ff6fd1-28e7-4067-80fe-ce723f844be6.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/617/00000/e64c6351-a12a-469a-8110-21eff6145eac.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/617/00000/8b4e335a-5929-443b-b784-b8e3cc08c83b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/617/00000/daa64f3d-1309-4ec7-85b1-194ebbd80273.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/617/00000/50e3df3d-afa7-472c-98c9-6425729e9c69.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/617/00000/ff1488b9-b40e-4470-b5e5-c55fcd600896.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/616/00000/3e69ac32-40d8-4b9e-b44b-c7e69c743b68.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/616/00000/e2684b23-2dfb-41be-bb14-9410cd2fb7bf.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/616/00000/bad0a186-0ee6-41d2-b527-154cc83022f5.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/616/00000/e8dd3ac6-e512-42d3-ba27-2e61d75146cc.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/616/00000/4463bd04-26b9-4290-b8ea-446917683e2b.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/612/00000/0afd3d03-0174-4bda-ab28-ab6a935fc5d6.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/612/00000/44d40234-e4f7-4ab7-825e-3cda50960d70.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/612/00000/c2d55cec-2923-4a97-8774-d6f42f082782.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/612/00000/964b14c8-f227-4312-b780-ebac513ff30e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/612/00000/c5e1dd0c-9478-4c1d-8640-ebfdb3208caf.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/564/00000/ed8424ba-95e9-45a4-bead-7fc80e38ed91.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/564/00000/3aeaad65-33b2-4e52-a6a7-6601c3bdaf84.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/564/00000/689bf769-4251-4c1e-8e29-7345e6d03a7f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/564/00000/6bbc6e79-1fc5-4754-9b53-6c8987ea4094.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/564/00000/ff283f3b-6c6a-47a1-a648-1551126bd934.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/561/00000/664e031c-6ba0-4e4f-819c-1ef5da983341.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/561/00000/35f0f7c0-9e21-4da0-9a55-7049524b350d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/561/00000/b2c3e1e8-0235-4d59-bbed-af0d80532ee0.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/561/00001/31593f07-3879-4c25-afa9-c85f1ca07570.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/561/00000/bb194604-95f0-4356-9fc7-b5821e826923.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/559/00000/1e9be05c-653e-4348-949b-23ff6196ff33.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/559/00000/5d76d09f-b871-48ea-ac55-eed3f1b1f7ae.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/559/00000/64992718-1b5f-4586-a040-b22e1fc33399.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/559/00000/7e7e1432-1dce-4235-b1b3-9836c2116b50.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/559/00000/f186839b-1875-4418-9e82-82f70b8f1095.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/492/00000/dd2f5b7c-83ff-4e72-9d27-110b41c1918c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/492/00000/fa72df70-0e9a-4244-8835-4802b3355a13.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/492/00000/447e28c6-c92f-4f52-88f5-2a4c39c831d2.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/492/00000/56297174-b9dd-41fb-905b-e4f8a9779c1d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/492/00000/0110cc4f-1751-4363-a023-87a6dec32d7c.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/491/00000/c6be438a-2ce1-40cf-9059-938e498664e8.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/491/00000/ae8a184f-5527-4498-bdfb-87a2a5dc2619.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/491/00000/b440ce91-e416-4fb6-8272-0c7f1987ba8e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/491/00000/7617f9d1-7957-4727-b9ef-d5bc74edb445.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/491/00000/dedce09f-027a-43ab-ba6a-62c30737a136.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/490/00000/d40d05f7-0333-4f9a-97a7-06c30088c531.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/490/00000/9dfb8e88-49d0-4ca6-bec1-2544de024585.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/490/00000/292ac001-76c5-43c5-a016-10cc96df1b15.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/490/00000/3b97c6dc-c605-4fea-98d0-af7182c6802d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/490/00000/e8e60daf-69fa-4798-9419-5a9fa6e6a301.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/464/00000/4a763e11-9f8f-4c99-95b2-48a698261d90.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/464/00000/fd594c23-d191-4cbd-948a-f71fa371102a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/464/00000/e6dc83b4-e0eb-4ac3-9ec2-1eb0bd2ae063.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/464/00000/0d00aae9-da92-4850-9cf6-99c54e7a64e5.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/464/00000/8f3e7140-27b3-4bb8-9591-c0abe3382d5e.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/463/00000/bfa3e367-4af4-4961-a1ff-f8dce9d143ac.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/463/00000/26d273bf-8f2e-4488-9686-55544cc9735b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/463/00000/4ea183c5-0dd9-4f46-a84c-b16d5688c6eb.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/463/00000/c323d617-91f2-4542-a879-c3606d07906b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/463/00000/adc4c270-07d5-4cc1-a4dc-0a95d92d193c.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/462/00000/5c990dde-5e7e-4fb8-afd7-605e6dd1f2e1.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/462/00000/210757d1-c5ba-45e6-b871-74e0bdc89891.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/462/00000/3e9f3dfd-f1d6-4946-ad80-56ffa348f77d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/462/00000/434ff64f-c3af-4772-94c6-c058cba3062b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/462/00000/8173792f-c332-42a3-b34d-01cd806a027d.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/361/00000/f4134006-81d9-4bfc-bb3b-311bfc1ae99c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/361/00000/74d3ad36-6317-4c16-a6d8-44d63f06078f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/361/00001/de7a4ee8-ed94-47f0-95e9-5635e9b17c54.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/361/00000/3c1f9caf-06f0-4a8a-a58d-8f833ba11340.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/361/00000/c37f027c-df4e-4255-bd13-2df843bd982b.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/174/00000/129fdf66-8dcb-4186-93eb-94e85280c21a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/174/00000/69cb21e7-5547-4ec6-8735-cd7cbdaf057e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/174/00000/4ca711b7-ac15-4959-a19b-5c87991e0070.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/174/00000/7b56333d-86f6-40ca-a2e8-12e52a3a54a1.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/174/00000/52cc4238-b4eb-45cb-a5eb-b70c279db924.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/166/00000/90d4bfae-d707-4fdf-b25f-62ea3ddc063c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/166/00000/205e4425-d0c3-4642-b025-15a69a2bcc78.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/166/00000/094021a7-5deb-478a-a9b8-2b252b6dc92f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/166/00000/7187c3f1-fa90-40f5-bd69-80eb17ca6ef5.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/166/00000/0ae9237c-30cb-45d7-8776-562d8e28fb72.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/156/00000/e94ff79b-eeaa-43d8-8172-9d7f8f05364a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/156/00000/05edc057-c36a-4585-b01d-0500d7069241.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/156/00000/f4fffcc9-f20a-4f85-92d8-408fd44ba42c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/156/00000/9811271c-6e2d-4f45-a048-3830ba801da2.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/156/00000/b4c98463-380d-499d-aa3a-6efb52897bed.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/142/00000/189ee84a-c144-46e6-b434-3e96abf900ef.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/142/00000/e81dc730-1df4-4a20-8c00-7084db4a8a1d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/142/00000/060c9100-0b7b-4479-a00b-a7b3aa5f36da.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/142/00000/7c156a19-2379-4cda-8709-1c452402d61f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/142/00000/bdacb78b-f882-448f-ba29-664afb9d78ad.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/107/00000/fb0380ec-d07c-423a-b5fd-593e9a394ef8.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/107/00000/3b57db12-5bba-485b-8580-14cec1bbb154.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/107/00000/7bd8645f-d491-4de1-aa94-1eb21917ca6f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/107/00000/1d1663c1-6948-4b1c-a46e-ef8f734c90a3.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/350/107/00000/e5b9d1f6-e6f6-4336-bf88-47ce74df9415.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/963/00000/adbe2c42-c33d-4074-b564-c5a4ec0147f9.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/963/00000/36a47be2-34ba-4b02-a92b-2d2c58ac89d2.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/963/00000/0e416363-795e-485f-9f4b-3c11e030358c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/963/00000/6942b81d-4dc0-44a1-aebf-78a342a8a8ac.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/963/00000/fa9bb03e-f2d7-4d71-997d-ce9a1fc94b6c.root",
# end
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/963/00000/a2cb0e32-ab67-45a1-b312-75b98ff3d757.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/963/00000/6be85939-0ad8-4e7b-b387-1fc146850137.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/963/00000/1eced49d-6ef1-45ae-9deb-eece5e01fbb9.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/963/00000/c63cc220-eedb-49cf-93f1-efb0ad4b037f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/963/00000/063fee1a-46bc-43aa-b66c-98f7154745e5.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/893/00000/46f5617f-956e-4ff1-b341-58088597432d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/893/00000/c801a0f7-b42d-4959-b2b1-3fd8266defdd.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/893/00000/87b6c86a-f220-4cff-9f4b-2bf899e6e489.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/893/00000/c789cee9-68e1-476f-8170-43333f54edd1.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/893/00000/786575b6-da44-4e30-b314-f2e0028f1b20.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/840/00000/f0999bfb-0a6b-4143-b602-acb3eafcbaa0.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/840/00000/57f4ae41-5f4d-4d2f-996d-a2aa0048b8fa.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/840/00000/ea364b37-2c1e-4bed-9098-bf616fa8a6f7.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/840/00000/99820201-8069-4474-8482-912b077b3100.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/840/00000/151dd7e3-42b8-4d03-b331-04b202a23e31.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/839/00001/7608cb6a-592a-441c-b3de-9ed341d5602e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/839/00001/9538a0d9-07dd-4be0-8e60-f07b387ec001.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/839/00001/82072343-55b7-4140-adc4-15c476e68d6b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/839/00002/aee96463-59c7-4cd2-9067-fd74c8cdea1d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/839/00002/2bfa4ad2-da8d-431d-812d-9cdc991a076c.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/838/00000/aeba6a13-61fc-4240-8459-b4f4418d52db.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/838/00000/5f5e02c5-58bb-4d86-9231-3687be011ad9.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/838/00000/5ac28abe-465b-4337-b928-28ef9ac7c719.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/838/00000/4df9d583-4a90-4862-a554-bc21ae39c844.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/838/00000/38f4e18b-994a-483e-92cd-0fc656c5de95.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/834/00000/8de1e336-3169-492a-bdd9-d9b1bda9ad0e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/834/00000/a29998b3-8a2e-44f3-b0d9-0e2dcebda9ad.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/834/00000/064b7d4f-786a-4c9b-8a2c-118f59194b28.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/834/00000/e9de7bcc-2d98-458e-894d-a0537b93db93.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/834/00000/27d63780-bd86-4569-b44c-ba54226d9577.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/833/00000/eaddd23e-983a-4885-8583-ff4daebc12d7.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/833/00000/af28a241-7be2-4eef-a6f6-38caf48e8fbe.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/833/00000/0cb64e26-154f-4980-bbe5-ee10642e1736.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/833/00000/19efd64a-2cbf-405f-9108-3e7714cba818.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/833/00000/e6a70c64-5b78-49c7-9958-6b091dd8bc03.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/758/00000/57462df1-58f3-4c50-814b-5190e0e3064d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/758/00000/9e1ff716-b74e-4908-a56f-53f90f0e2e23.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/758/00000/f7daaaeb-52bf-4327-b1a2-6c6b491fcc9b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/758/00000/6f388dd9-d9d9-4cf6-8e07-97515b4bf0f9.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/758/00000/fa238dc7-e2fd-4c82-9ce0-4c8ff7e8f2fb.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/757/00000/863e7401-5963-4db6-a1b3-5fedf6968c6d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/757/00000/7bb09340-840b-4e60-b227-c67e073f24f3.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/757/00000/0af0fed7-c418-499d-bd42-7d20afdeab33.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/757/00000/e0bbb350-6ffd-40e1-8105-3ca2e10540f2.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/757/00000/354e4053-0fab-48c0-8b0a-c7ebefd3e34d.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/756/00000/35a5370e-81fd-4db8-8631-dcf9a435ee85.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/756/00000/49c144fc-3c76-41ca-8aff-2694352a9208.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/756/00000/ec71cd3b-3fd9-4ab9-8ee3-54f691761700.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/756/00000/4137b358-e396-44ea-942f-a9e8f9bb2869.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/756/00000/3954fd77-f953-404d-bd8b-f8bc66d91b0f.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/753/00000/93b4e392-830b-4e2e-b81c-663decf551a6.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/753/00000/c394b9a7-35d1-47e5-8621-bceeb6a89d0d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/753/00000/4fde7a0d-3b1a-4fe0-bd38-6470a5cc8089.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/753/00000/304b46a1-f1f6-46e4-9dc0-0747a94422d2.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/753/00000/d5fcb4d4-7a4f-4ea3-b571-5a5d77e2eeef.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/703/00000/ac393d3f-2ab9-4e81-ab95-d1e63c0f97c0.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/703/00000/6d89d990-774d-4186-9050-9b439716268f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/703/00000/d72ebacb-0dce-4941-a2b8-76081e739c49.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/703/00000/24774c83-3e05-49b8-bd72-5eb42ed7470f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/703/00000/0a6bd412-41cf-4957-9be5-b30b1fa34745.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/701/00000/1339eb22-5387-4e9b-a591-2c02e5ca25a1.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/701/00000/cb20fd6e-df73-4da2-a7df-fb6f2dfe449b.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/701/00000/b21092e3-4265-4b93-9a84-26ab7b98d0c9.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/701/00000/415b55f8-9932-43ae-8ad8-6399478d697e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/701/00000/02a4a84c-ae0a-4e1a-9366-bf597c4638ae.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/614/00000/7884f13e-4019-48b3-ba28-5ecf855a4e8a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/614/00000/f6fe8ceb-a77b-4b0a-94f4-d4f88859cfd5.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/614/00000/efe0cef7-9a9b-4622-9629-90964a0b0bab.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/612/00000/7f146f18-3fee-4ed4-a4ef-c8a5b8940ab4.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/612/00000/e84bbcc5-de09-4009-b253-3be070356b16.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/612/00000/d57f861b-7c17-45e6-a106-affb593aaccd.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/612/00000/3eb31eef-36ab-4fbb-bba6-445c5a84c8c0.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/612/00000/fb6810db-3289-47b4-9c96-ff2d4f52a3a4.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/612/00000/749ae9c3-36aa-4299-bc59-dbff7c9370ed.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/612/00000/e105772e-a7c9-4d84-a7d0-730bf6c88b2c.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/611/00000/80c68590-d9c7-4ac0-a2c2-ab7fcd47477c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/611/00000/aea24a75-d9d5-4036-b5ab-61fbfcc4a304.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/611/00000/52baccb5-c215-49cb-9dda-bca1b789b7cb.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/611/00000/9ef53eb9-c284-4874-aefa-e6ef6bf35224.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/611/00000/3542b94e-2832-4df3-b07f-5ce5289fc80c.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/610/00000/484f7602-6e75-43f1-a0fc-67502dbada5a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/610/00000/a15b3810-7cd6-4169-87f5-691ffd362339.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/610/00000/a47dc97e-c7c9-4863-89f7-fec7bd1de612.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/610/00000/8384d755-ffec-408a-8287-3e55403573dd.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/610/00000/8785e57c-5044-477f-b022-69ed926c9c65.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/528/00000/af6ef298-c7b5-4571-9eef-e2d386134528.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/528/00000/b6156acb-d4ce-4c2f-b975-e58c838f9bef.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/528/00000/8b20041d-ce03-416d-8b02-0dced67affda.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/528/00000/f5af6081-c717-4812-bd14-0419c91e886e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/528/00000/0f663b90-3d11-425b-b669-e663f826231c.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/527/00000/6241b250-e66b-454c-8cb0-e060cb893826.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/527/00000/94a42a7b-6912-4cb6-8760-fbc78b588bfc.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/527/00000/069ceca1-914d-4295-a9ee-e829fd8468f4.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/527/00000/36b97461-17ca-4eb1-9bfd-1c7428b6a920.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/527/00000/f86abb1e-6b4a-4f5c-809e-86224f2c75ba.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/437/00000/40c790f6-5d91-4eee-9658-c54d2cc6c02a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/437/00000/cbfc9ead-c8f4-4a57-97a6-2a7fa8d69ba0.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/437/00000/00875e18-6788-44a3-b50c-d9060889e70a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/437/00001/037f3dd5-2931-4dab-bc9d-4bd7c9807a10.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/437/00001/e90b0f50-0050-4668-b042-eccfcc5abda7.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/436/00000/8023f2d4-72f6-4c79-b953-5aa697d8257e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/436/00000/0fe11344-6f5b-4e66-84b4-f39f51a59a65.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/436/00000/631e9544-a78e-46c7-bea5-604e001c1960.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/436/00000/8fbae49c-9023-48ee-b0bd-c6d385e5617f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/436/00000/abc4182d-6397-4ed1-a787-a57ef857fdfd.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/433/00000/c4cce2f3-e932-4d01-bdd5-b4378b5f89ae.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/433/00000/40124f55-9dd1-4b20-9f48-b8f4b83344f8.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/433/00000/13d097d6-fe05-4d4b-bc17-cafc88858d3f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/433/00000/e54e88a4-2186-4bf5-8e24-6bba9d540884.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/433/00000/76d19140-e4a2-47a5-93b2-a25caf170cdd.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/422/00000/95a6ddac-01f7-41e9-aba5-6b9811bccfe2.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/422/00000/f1797307-e3b9-44ed-aa22-a0f665062172.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/422/00000/f5cfe0d0-40ca-42ea-b423-ce90fd722fe8.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/422/00001/bda4ecc0-f539-479d-9a7c-2bf085c07c04.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/422/00001/7ef0e55b-0a39-45b4-a30a-5ab98accc3b0.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/348/00000/5f790bc7-2194-4bfe-b259-a295268ffb29.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/348/00000/d31307b7-2fa9-4306-b0fa-d1dcee76d16c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/348/00000/8d95a9db-7e5c-4da8-a37b-7f2b7db1ce5a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/348/00000/ed0bac6e-9c53-4e47-b0ff-6ca77c511ce2.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/348/00000/0c59a617-00ad-434a-8867-5c25edbab15b.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/346/00000/c749cad1-ddb4-46ac-8f5d-f4271016e8b3.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/346/00000/b2ddac06-311d-4478-befa-7be189cade44.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/346/00000/cfe7decd-f22e-4806-9301-e6ac0be23bcf.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/346/00000/2b804ee9-1732-472f-b703-4f52f2dd5459.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/346/00000/e3ef9003-e564-4d93-97cd-6521db34117c.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/263/00000/1fa6eecc-e13d-463d-84c3-832eab612c61.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/263/00000/8e79c1d5-eb8f-42f5-86b0-a1666f34caa4.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/263/00000/dc9c474f-a4f2-4e52-972f-15093a6cf23f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/263/00000/64510f2c-e7c3-4643-949f-fd96c4f6e6d6.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/263/00000/54736b10-969c-4781-a2dd-058510e5cedf.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/260/00000/1f48eaa8-d8fe-48ff-8759-3be0e81892af.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/260/00000/f0e1927a-5a38-4645-833d-db3d35d6effc.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/260/00000/b5f94763-ebae-4820-bcad-84c1d0f3a73c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/260/00000/fff04869-7899-4b75-9d57-cebfb6a40c2c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/260/00000/9b45c00b-823b-4792-88f2-046fe5cbc774.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/147/00000/756e03f5-251c-4e24-8181-13e1444bb257.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/147/00000/af3a91e2-7615-4830-bdd6-98e2fb745a23.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/147/00000/f89e83e6-920c-4426-807a-07391f42ee59.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/147/00000/5afba49e-ba7d-436d-a5db-18d20fbda54f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/147/00000/48c75d10-8592-4375-be8a-90446dd67763.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/146/00000/7eee3dac-6511-4e2d-9ebf-1685b2ffb864.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/146/00000/d744f1bd-902f-449f-a55e-520114cb7f22.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/146/00000/2ab67d7e-4775-4ebb-9443-d0187cdfbba3.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/146/00000/ed1db26c-4602-4383-aa38-7d0ad5c3b289.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/146/00000/dac48732-5f94-49e0-8fe0-65f8532d3354.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/145/00000/5138f98e-3b9c-4dbc-a676-79db8d4fd00a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/145/00000/73c2ff7e-6d16-400e-b9f4-9ad3bdd25e73.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/145/00000/8fcc9a5c-e81f-4bbc-8288-73c13214ecc9.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/145/00000/8f72fe4d-94f0-4c76-9fbd-21df791ea08d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/145/00000/9c6c4dd9-4814-463f-9eaf-175a05575b3b.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/088/00000/d01597be-e864-4e66-96fb-64279b389654.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/088/00000/938f4b8c-561c-4a0f-8fa1-7b9330011cb8.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/088/00000/de173cd3-d776-40f3-b668-694a68ebc7f7.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/088/00000/e662431c-dced-46e2-a246-61e2d5cc93e6.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/088/00000/b76af329-3fbd-463a-b6f2-cad8012928bf.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/084/00000/354162b0-77d1-4e4d-808e-528921d7944c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/084/00000/92825789-b6d6-4709-9dc9-5093c79b2cdb.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/084/00000/fabca92e-cea4-433f-911c-30b1e7ea3b4f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/084/00000/1e263078-1900-4a5f-9380-608efd74625f.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/084/00000/9cc00509-b9ac-47a7-8c32-4f730c8c26aa.root",

#end of run
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/084/00000/0c4640c5-ced9-4503-a9c6-6c8c3175793c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/084/00000/476b616a-e50b-432a-b8e0-0c2f75249260.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/084/00000/827337c6-5203-430d-9d74-fc365ac2a5e1.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/084/00000/3e7aae84-258a-4b46-a736-42cbddf373db.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/084/00000/03f4b4a1-c3a7-4f45-8e29-294bbc60bac6.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/081/00000/cccbcb3d-7225-42b7-a377-a9f9aba33e3e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/081/00000/2ccacdcb-298a-4b5e-b361-5a2a2512355a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/081/00000/e8d4c0e6-8791-4f6f-9c2e-40cd5b15117a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/081/00000/7360cf15-32ee-48b6-b968-1775d13a5c8d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/081/00000/6e53f3ca-f631-4400-9147-a15c08ee3c02.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/079/00000/1e11458d-d703-44c1-9dc9-efc4c327a9aa.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/079/00000/a8c115bd-ca3b-48fe-8fa4-51bf0e3abbe3.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/079/00000/9b1d946f-e61a-45e4-9883-190214961e62.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/079/00000/ce033f5b-e710-4057-ad58-be935ac6ddd9.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/079/00000/6ed3a23a-5f28-495c-8aeb-e0ceb626a825.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/078/00000/c417642b-d84d-459f-80c3-fdb88f043d44.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/078/00000/8b5d7561-bc3c-43f1-8afe-1f9c296d955d.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/078/00000/2370e4aa-85c0-435c-ae7d-3ded46ca2938.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/078/00000/a05cdd88-7568-4684-9bd6-ca3426f741a9.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/078/00000/16074c5c-c76d-42a6-9f26-0b20616d30ca.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/073/00000/79819494-31f7-4c32-b880-ce720b1cf734.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/073/00000/138bbe2c-5afc-421d-af10-3c7ef8bb75ba.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/073/00000/16606d41-0e80-4610-b180-e99c9fd4f940.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/073/00000/8fe25d54-daaa-4887-8015-6ff22b3be9d9.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/073/00000/82eb05a0-580b-4a0c-a348-b520ccb33fe1.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/071/00000/2a556dd9-b4af-4919-b3f2-e1745f45e473.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/071/00000/b6971205-be9d-4f2f-9bc2-94a597b2b399.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/071/00000/3fa11a5d-1f24-44a0-8c2d-7bc4b7a7c056.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/071/00000/3cec5dd4-4fa4-4a70-9a5d-47a3d9bf1a8c.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/071/00000/8e9c50e4-aced-4a6b-bb35-edc3a0a3523e.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/016/00000/825675cc-ea6f-425a-934f-c84705e02c1e.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/016/00000/c1247c34-1b24-4a7b-b6d6-b1a9877f94e4.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/016/00000/0843e5f7-3c38-431d-b25a-cb4cd66dd8b8.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/016/00000/405e5077-4f84-47af-9319-d71762f7eb59.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/016/00000/3584f372-9513-4d6f-beb8-e484e1a598e5.root",

#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/007/00000/ea25c5b8-733b-4b7c-a896-dac11286cd23.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/007/00000/821d5af2-db65-4a17-8d45-86c19e070d72.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/007/00000/5a56f7ba-5854-4043-ba62-d9c90f39220a.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/007/00000/dafad32c-a009-4845-985b-82d9450a0caa.root",
#"/store/express/Commissioning2022/ExpressCosmics/FEVT/Express-v1/000/349/007/00000/d144811f-ce55-43a9-aab9-ac714cbd4321.root",

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

#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/05d4e531-3560-40bd-ba85-d18f4fa78981.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/22cbd905-6a6d-4632-888f-fe96c32ad40e.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/e936125e-53eb-4e71-bafe-c027cb550a1d.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/bc3801d1-c45f-4ff8-bb44-6d9915e7cdd5.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/704bfd06-68ac-4e4d-9be7-59ce0fef0cb9.root",

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


