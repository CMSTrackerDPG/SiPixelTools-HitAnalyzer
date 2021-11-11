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
# fileNames =  myfilelist )
    fileNames = cms.untracked.vstring( 
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/603/00000/9959aae3-2b99-4e5e-8f9a-c1ea7079cf48.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/683/00000/154e9bac-ded0-47c8-94b6-d580ca5e50cb.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/755/00000/c182b2c3-4b2a-4e1b-b692-abc17459d7eb.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/758/00000/6b96fce8-75d5-4405-943d-634c0afc181b.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/823/00000/382e5d92-761c-479d-a911-5dd05903accf.root",

"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/828/00000/93fcca5c-4746-4d6e-9738-6415f8446139.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/828/00000/ef5e1259-88cd-45eb-923b-a9b9884bdfb4.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/828/00000/e1cbba3d-2fbe-4bb1-bd1e-72afc2387009.root",
"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/828/00000/58e350fa-cb48-4440-8a65-039823d2864c.root",

#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/829/00000/1bde50d4-edc8-4f9c-b257-3011e88f5bb5.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/829/00000/263667e4-5458-41f7-bb2b-f7baf9788199.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/829/00000/a655ebaf-688d-49dc-8676-3d92cbc114b4.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/829/00000/efc41ce1-50db-4084-a42d-0df9fc5f3a57.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/829/00003/1e6c11c9-317c-4bef-9bb1-85637708d2af.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/829/00003/95a72402-a936-4c85-8891-8aef24a15b6d.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/829/00003/e24c2851-31de-4a31-8d51-1a1141108613.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/829/00003/21a02b74-0802-4950-98c9-0e0729837820.root",

#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/d76f76b4-2162-4e70-a967-a527b0b0184c.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/2ec08322-19c0-46e5-815d-6cd2b81f2d7b.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/be1e95ec-c502-46b6-86d4-655182f38980.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/830/00000/3279f59f-6efe-4994-88dc-91217e7a9d6a.root",

#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/876/00000/a84a9412-d920-41f6-bf29-cb47ec319ad0.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/876/00000/7ded5f7f-71ae-417d-b350-fd36a14533b4.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/876/00000/87f9e506-03fd-4424-9388-1eb86f5f5ff8.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/345/876/00000/f5bc216f-15b5-4259-8f13-07c93dd07229.root",


#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/344/068/00000/11cf55ba-55c8-4e8e-b984-281c724fb881.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/344/266/00000/542038a5-47ac-4b1b-98d6-6a5e4baa9a82.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/344/420/00000/7e2f37ab-ef2b-4dd6-a017-3fda8d7c23df.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/344/632/00000/f0459c3f-f269-41c3-bb04-1dbe7548e659.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/344/677/00000/050086f9-4711-4987-a737-08ba1ec2ae40.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/344/679/00000/001494f3-5062-4f4a-92fa-1049f64d2a70.root",
#"/store/express/Commissioning2021/ExpressCosmics/FEVT/Express-v1/000/344/681/00000/0bdb3b49-44f5-4d19-9c96-2c4be8aad8e4.root",

    )
)

#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('205217:0-205217:323')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('324410:0-324410:168')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('324276:48-324276:9999')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('324075:0-324075:307')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('323829:0-323829:455')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('323481:38-323481:311')

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


