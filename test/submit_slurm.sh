#!/bin/bash
# 
######SBATCH -p wn
######SBATCH --time 10:00:00 # 4h not enough for digis
######SBATCH -w t3wn60
######SBATCH --job-name=job-name
######SBATCH --account=t3
#SBATCH -e cn-test.err 
#SBATCH -o cn-test.out  # replace default slurm-SLURM_JOB_ID.out

echo HOME: $HOME 
echo USER: $USER 
echo SLURM_JOB_ID: $SLURM_JOB_ID
echo HOSTNAME: $HOSTNAME
echo PWD: $PWD

MYPWD=$PWD
echo $MYPWD

export X509_USER_PROXY=/t3home/kotlinski/.x509up_u1373
# export X509_USER_PROXY=/tmp/x509up_u1373  # does not work, copy from this to myhome 

echo JOB_ID: $SLURM_JOB_ID 
echo $X509_USER_PROXY

# each worker node has local /scratch space to be used during job run
mkdir -p /scratch/$USER/${SLURM_JOB_ID}
sleep 10
#
cd /scratch/$USER/${SLURM_JOB_ID}
cp $MYPWD/translation.dat ./translation.dat
#cmsRun $MYPWD/SimsToClus.py
#cmsRun $MYPWD/SimsToRec.py
#cmsRun $MYPWD/RawToRec.py
#cmsRun $MYPWD/gen_sim.py
#cmsRun $MYPWD/digitize.py
#cmsRun $MYPWD/reco.py

#cmsRun $MYPWD/runRawDumper.py
#cmsRun $MYPWD/runRawDumper_368546_rnd.py
#cmsRun $MYPWD/runRawDumper_379613.py
#cmsRun $MYPWD/runRawDumper_379765.py
#cmsRun $MYPWD/runRawDumper_380001.py
#
#cmsRun $MYPWD/runHotPixels_378113.py
#cmsRun $MYPWD/runHotPixels.py
#
#cmsRun $MYPWD/PixClusterAndTrack_367413.py
#cmsRun $MYPWD/PixClusterAndTrack_369596.py
#cmsRun $MYPWD/PixClusterAndTrack_369927.py
#cmsRun $MYPWD/PixClusterAndTrack_369956.py
#cmsRun $MYPWD/PixClusterAndTrack_370093.py
#cmsRun $MYPWD/PixClusterAndTrack_370093_tree.py
#cmsRun $MYPWD/PixClusterAndTrack_370129.py
#cmsRun $MYPWD/PixClusterAndTrack_370169.py
#
#cmsRun $MYPWD/PixClusterAndTrack_370093_1mod.py
#cmsRun $MYPWD/PixClusterAndTrack_370129_1mod.py
#
#cmsRun $MYPWD/PixClusterAndTrack_373608.py   
#cmsRun $MYPWD/test.py   
# 2024
#cmsRun $MYPWD/PixClusterAndTrack_376826.py   
#cmsRun $MYPWD/PixClusterAndTrack_377298.py   
#cmsRun $MYPWD/PixClusterAndTrack_377676.py   
#cmsRun $MYPWD/PixClusterAndTrack_377778.py   
#cmsRun $MYPWD/PixClusterAndTrack_378239.py   
#cmsRun $MYPWD/PixClusterAndTrack_378750.py   
#cmsRun $MYPWD/PixClusterAndTrack_378985.py   
#cmsRun $MYPWD/PixClusterAndTrack_379028.py   
#cmsRun $MYPWD/PixClusterAndTrack_379058.py   
#cmsRun $MYPWD/PixClusterAndTrack_379060.py   
#cmsRun $MYPWD/PixClusterAndTrack_379252.py   
#cmsRun $MYPWD/PixClusterAndTrack_379350.py   
#cmsRun $MYPWD/PixClusterAndTrack_379417.py   
#cmsRun $MYPWD/PixClusterAndTrack_379470.py   
#cmsRun $MYPWD/PixClusterAndTrack_379613.py   
#cmsRun $MYPWD/PixClusterAndTrack_379765.py   
#cmsRun $MYPWD/PixClusterAndTrack_380001.py   
#cmsRun $MYPWD/PixClusterAndTrack_380049.py   
#cmsRun $MYPWD/PixClusterAndTrack_380126.py   
#cmsRun $MYPWD/PixClusterAndTrack_380384.py   
#cmsRun $MYPWD/PixClusterAndTrack_380624.py   
#cmsRun $MYPWD/PixClusterAndTrack_381190.py   
#cmsRun $MYPWD/PixClusterAndTrack_381543.py   
#cmsRun $MYPWD/PixClusterAndTrack_382580.py   
#cmsRun $MYPWD/PixClusterAndTrack_382594.py   
#cmsRun $MYPWD/PixClusterAndTrack_382878.py   
cmsRun $MYPWD/PixClusterAndTrack_383034.py   
 
pwd
ls 
cd $MYPWD
pwd
ls /scratch/$USER/${SLURM_JOB_ID}
#cp /scratch/$USER/${SLURM_JOB_ID}/noise.root $MYPWD/.
#cp /scratch/$USER/${SLURM_JOB_ID}/simtorec.root $MYPWD/.
#cp /scratch/$USER/${SLURM_JOB_ID}/rawtoreco.root $MYPWD/.
#cp /scratch/$USER/${SLURM_JOB_ID}/raw.root $MYPWD/raw.root
#cp /scratch/$USER/${SLURM_JOB_ID}/clus_ana_cosmics.root $MYPWD/.
cp /scratch/$USER/${SLURM_JOB_ID}/clus_ana.root $MYPWD/.

# xrdcp -d 1 -f s.root root://t3se01.psi.ch:1094//store/user/kotlinski/MC/test/s.root  # is OK,
# xrdcp      -f s.root root://t3dcachedb.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/kotlinski/MC/test/. # OK
# xrdcp -f /scratch/$USER/${SLURM_JOB_ID}/s.root root://t3dcachedb.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/kotlinski/MC/test/s.root   # OK
#xrdcp -f /scratch/$USER/${SLURM_JOB_ID}/s.root root://t3se01.psi.ch:1094//store/user/kotlinski/MC/mu_pt100/simhits/simHits2_eta0p1.root # OK
#xrdcp -f /scratch/$USER/${SLURM_JOB_ID}/d.root root://t3se01.psi.ch:1094//store/user/kotlinski/MC11/mu_pt100/raw/raw1.root # OK
#xrdcp -f /scratch/$USER/${SLURM_JOB_ID}/r.root root://t3se01.psi.ch:1094//store/user/kotlinski/MC11/mu_pt100/reco/reco1.root # OK

#  rmdir  /scratch/$USER/${SLURM_JOB_ID}
rm -rf  /scratch/$USER/${SLURM_JOB_ID}
date


