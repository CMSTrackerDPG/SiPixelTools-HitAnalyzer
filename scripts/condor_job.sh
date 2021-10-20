#!/bin/bash
echo $home

source /afs/cern.ch/cms/LCG/LCG-2/UI/cms_ui_env.sh

cd /afs/cern.ch/user/d/dkotlins/public/CMSSW/CMSSW_12_0_1/src

SCRAM_ARCH=slc7_amd64_gcc900; export SCRAM_ARCH

source /afs/cern.ch/project/gd/apps/cms/cmsset_default.sh  

# /cvmfs/cms.cern.ch/cmsset_default.sh

# must be run frm the release area
eval `scram runtime -sh`

cd SiPixelTools/HitAnalyzer/scripts

#cmsRun runRawToClus_344681.py
cmsRun runRawToClus_345829.py
#cmsRun runRawToTracks_344420.py
#cmsRun runRawToTracks_344632.py
#cmsRun runRawToTracks_344677.py
#cmsRun runRawToTracks_344679.py
#cmsRun runRawToTracks_344681.py
#cmsRun runRawToTracks_345603.py

