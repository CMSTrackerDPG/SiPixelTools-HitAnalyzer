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
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/9847bf8f-bc3e-4ec6-b417-e598366387e3.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/9ce500ab-6f5b-4ef6-86cb-e8713dbd65cb.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/e613add6-ac51-421e-937b-ff5efaa70886.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/7fdaadbb-57e3-4c6b-84d7-164f5a07c0d8.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/5f0e5f09-f2ef-4fae-aecd-f1988295de0b.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/445c8c75-12c5-4480-9559-a81204ba8e35.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/72bd68bf-2990-4596-82c1-89b14fc54f83.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/4201e78f-e9b7-4659-a827-623b957e039e.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/276b756d-5002-48d2-a019-f18c8d2f47ef.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/61be6f77-cdca-4a72-b358-33af4163affc.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/2b09a04b-dd13-4a7f-b97f-87c3f4748b1e.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/35676619-c08c-4a5e-8579-bb78ab7fb8ad.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/f212df67-1805-4f98-87f2-07d515f6bca5.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/af2f1618-8b0b-4850-bdf6-75fe6f101092.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/679202ba-d60d-4a60-a04d-b98704dfa9a2.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/6043d4bc-50fa-4b9d-ab5b-2c1af15e711e.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/8fd384ec-7098-4881-bf25-14ccf16bb713.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/bfd0bedc-51cf-49be-a10f-9a2a0b15104d.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/0f1badf0-5cfb-4d82-9fe5-1ab8dbf10fd3.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/ede953f0-c2ea-49b9-bbee-5fcf3b46a103.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/d4541253-34de-4db7-bde0-ae213c402c0b.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/47d3ee0a-9152-40d1-93b4-b524a06aaf80.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/840aa751-05ac-4d4a-ac41-cfcd00954c80.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/3c09cfa2-70f0-4ee6-a27f-97f633d4db8b.root",
])

process.source = cms.Source("PoolSource",
fileNames =  myfilelist )

#    fileNames = cms.untracked.vstring( 

#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/9847bf8f-bc3e-4ec6-b417-e598366387e3.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/9ce500ab-6f5b-4ef6-86cb-e8713dbd65cb.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/e613add6-ac51-421e-937b-ff5efaa70886.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/7fdaadbb-57e3-4c6b-84d7-164f5a07c0d8.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/272/00000/5f0e5f09-f2ef-4fae-aecd-f1988295de0b.root",


#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/260/00000/a5d78084-ebac-481e-a053-d8678aafc8db.root",

#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/222/00000/3bf7f901-d269-45e0-888d-0de42606046b.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/222/00000/af6b19ba-9f94-4294-9551-88599bfd5a63.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/222/00000/3b3f7470-11b9-45d2-a402-9f480a2d2ab5.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/222/00000/47d0653b-f9a0-4959-83bd-0bc77b77c7af.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/222/00000/a02cee5e-7e7b-4f8a-bca9-10fb329fc306.root",

#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/152/00000/4f3871fd-c3a0-4090-9444-5ec565e00764.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/152/00000/64d3100d-fc7b-4a55-922b-7171dcd8a7aa.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/152/00000/af34c973-2096-4431-91ff-d5c9c8ca630a.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/152/00000/6426e6c9-6e29-4f62-a0e1-d4feb58a43ad.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/152/00000/bb3cf595-7800-46a3-a4e7-968a74a8656b.root",

#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/024/00000/5143421d-e7b6-4e9c-96b2-e7b98892b178.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/024/00000/83b8ea32-a7ca-4942-a9a1-d9bd2bb781c1.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/024/00000/34643fa5-d640-4117-b979-669ae1ba7909.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/024/00000/eccc7b6f-11b8-4418-b0bd-eaf9d921968e.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/347/024/00000/a2da446c-c202-4f07-b49d-afa62dc6aaff.root",

#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/979/00000/f63ea27e-cb73-4857-813f-71dd90567d6d.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/979/00000/12d30578-de18-4f75-9f46-f2b96594d637.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/979/00000/54236348-258e-4869-a979-1f0db44f2a97.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/979/00000/7995829c-92b7-4955-8859-60a49a779d86.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/979/00000/0ac0d282-92f6-4902-949e-4a3720a25ab9.root",

#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/924/00000/fe6c7291-333d-4609-af9a-7948cb05df17.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/924/00000/380572a6-24c2-4396-9a7c-671e2cd3f662.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/924/00000/774461bf-370f-443c-ac0e-1eedd2774d9c.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/924/00000/d404cf93-bf4c-422d-a8d7-47c88fe8aa34.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/924/00000/388faeb4-1351-4fb5-891b-4c2a16b147a7.root",

#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/777/00000/cfefd0f1-5d00-4d82-b27f-5efbf1eacaa8.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/777/00000/5fcdc0ab-67ee-47bb-a854-dd47ffacbde2.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/777/00000/f6977636-18bc-421f-9f69-fde17ba7adba.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/777/00000/cb33d727-e31f-49f8-91a2-0016cff8c337.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/346/777/00000/6c5fbd48-5a1f-40a3-bca8-ed1fdcd57608.root",

#"/store/data/Commissioning2021/ZeroBias/RAW/v1/000/346/512/00000/0fb9b53a-ead7-45b2-8f8c-c15332c16d12.root",
#"/store/data/Commissioning2021/ZeroBias/RAW/v1/000/346/512/00000/99bb2b4d-0701-45a8-b7d1-036f0ca17d5a.root",
#"/store/data/Commissioning2021/ZeroBias/RAW/v1/000/346/512/00000/76c83cce-2f11-43b3-99ec-cacf72dfb343.root",
#"/store/data/Commissioning2021/ZeroBias/RAW/v1/000/346/512/00000/bdf5b83f-0ed4-4e51-be43-6e81049304c1.root",
#"/store/data/Commissioning2021/ZeroBias/RAW/v1/000/346/512/00000/f44121c2-8c19-4c88-a1bd-f080b82f7d07.root",

#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/512/00000/05d4e531-3560-40bd-ba85-d18f4fa78981.root",

#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/450/00000/dec81202-ec6d-4611-8417-97a965611150.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/450/00000/6bb53ee7-8038-4f2e-8442-e2f7465ed7e5.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/450/00000/cf85744d-1aaa-46df-9ea8-cd1cb7e1b651.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/450/00000/fa317fa3-514c-4a8b-a1cb-530d69f87171.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/450/00000/342620e5-2d04-4c04-a0d9-604931d0e6eb.root",

#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/396/00000/471bcde2-88ee-4b13-8e5d-a8fed92b4d80.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/396/00000/6194f392-c4d5-4a21-ac67-701a014cea21.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/396/00000/c23afa3b-9ab4-4081-b85e-6c1c2b797d19.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/396/00000/a73c4b81-94ed-4805-baaf-edfc90065b22.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/396/00000/b7e82ae6-4b3d-44d8-8e6f-b9af7867b1ed.root",

#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/389/00000/91d3a1fd-f293-467e-8aa2-8ee9b5450440.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/389/00000/7efee44d-28af-4499-b793-5d412948b2ff.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/389/00000/e93865e5-78f7-479e-958b-112f246c8604.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/389/00000/f54cefb2-0901-4a33-9bc0-1ebc9e9c478b.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/389/00000/932d8c0f-87d3-4d11-b563-41886245a405.root",

#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/236/00000/1e926627-4553-4b96-bf6b-51bb2587f01a.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/236/00000/62476398-24db-4869-8288-17982f19c909.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/236/00000/0757eddf-0c0a-462b-88fe-c62dbe588e32.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/236/00000/9f4edfe6-1cec-4407-b50c-5be900384a39.root",
#"/store/express/Commissioning2021/ExpressPhysics/FEVT/Express-v1/000/346/236/00000/84356223-f54b-4716-b0e4-7a6011ca76dc.root",

#    )
#)

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
    MAXFED = cms.untracked.int32(1293)  # bpix only 
    #MAXFED = cms.untracked.int32(1338)  # all  
)

#process.p = cms.Path(process.hltfilter*process.d)
process.p = cms.Path(process.d)

# process.ep = cms.EndPath(process.out)


